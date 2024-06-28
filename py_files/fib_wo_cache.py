import time

def fibonacci_no_cache(n):
    """
    This function returns the nth Fibonacci number without caching.
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n < 2:
        return n
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# Measure execution time for non-cached version
start_time_no_cache = time.time()
fib_numbers_no_cache = [fibonacci_no_cache(n) for n in range(35)]
end_time_no_cache = time.time()

print(f"Non-cached Fibonacci sequence: {fib_numbers_no_cache}")
print(f"Execution time without cache: {end_time_no_cache - start_time_no_cache} seconds")
