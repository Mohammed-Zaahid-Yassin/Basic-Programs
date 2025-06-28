import time
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {self.func.__name__}: {end_time - start_time:.4f} seconds")
        return result

@Timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Example usage
result = example_function(1000000)
print("Result:", result)
