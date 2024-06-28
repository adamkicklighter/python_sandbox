from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    This function returns the nth Fibonacci number using caching.
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Measure execution time for cached version
start_time_cached = time.time()
fib_numbers_cached = [fibonacci_cached(n) for n in range(35)]
end_time_cached = time.time()

print(f"Cached Fibonacci sequence: {fib_numbers_cached}")
print(f"Execution time with cache: {end_time_cached - start_time_cached} seconds")