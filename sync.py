import asyncio

import time

def blocking_function():
    print("Starting a blocking operation...")
    time.sleep(10)  # Simulate a long-running I/O operation
    print("Blocking operation finished.")
    return "Result from blocking operation"

print("Before calling blocking function")
result = blocking_function()
result2 = blocking_function()
print(f"After calling blocking function: {result}")
print(f"After calling blocking function: {result2}")
print("This line runs only after blocking function completes.")