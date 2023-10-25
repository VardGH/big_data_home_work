from bs4 import BeautifulSoup # is used for web scraping and extracting data from HTML.
from collections import defaultdict # is a dictionary subclass that provides a default value for a nonexistent key.
import requests # requests is used for making HTTP requests.
import urllib3 # is used to disable SSL warnings.
import json # is used for working with JSON data.

# This line disable SSL warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://quotes.toscrape.com/page/'

def quotes_count(num_pages):
    tag_count = defaultdict(int)
    for page in range(1, num_pages + 1):
        response = requests.get(url + str(page) + '/', verify=False)
        if response.status_code == 200: # The request was successful.
            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup.find_all(class_='tag')
            for tag in tags:
                tag_name = tag.get_text()
                tag_count[tag_name] += 1
        else:
            print("[Error] Exited with status code:", response.status_code)

    return tag_count

# This function takes a dictionary of tag counts and saves it to a JSON
def save_to_json(tag_counts):
    with open('tag_counts.json', 'w') as json_file:
        json.dump(tag_counts, json_file, indent=4)

def main():
    num_pages = int(input("Number of pages to scrape: "))
    tag_counts = quotes_count(num_pages)

    sorted_tag_counts = dict(sorted(tag_counts.items(), key=lambda item: item[1], reverse=True))

    for tag, count in sorted_tag_counts.items():
        print(f"{tag}: {count}")

    save_to_json(sorted_tag_counts)
    print("Saved to 'tag_counts.json'.")

if __name__ == "__main__":
    main()
