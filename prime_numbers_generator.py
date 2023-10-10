import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Using the prime_numbers_generator
primes = prime_numbers_generator()

for _ in range(50):
    print(next(primes))