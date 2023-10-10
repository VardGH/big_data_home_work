import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution = end_time - start_time
        print(f"{func.__name__} took {execution:.5f} seconds to run.")
        return result

    return wrapper

# Usage
@timing_decorator
def example_function():
    time.sleep(2)
    print("...")

# Calling the decorated function
example_function()
