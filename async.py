import asyncio

async def non_blocking_function():
    print("Starting a non-blocking operation...")
    await asyncio.sleep(10)  # Simulate a long-running I/O operation, non-blocking
    print("Non-blocking operation finished.")
    return "Result from non-blocking operation"

async def main():
    print("Before calling non-blocking function")
    # This schedules non_blocking_function to run but doesn't wait for it immediately
    task = asyncio.create_task(non_blocking_function())
    task2 = asyncio.create_task(non_blocking_function())
    print("This line runs immediately after scheduling the non-blocking function.")
    result = await task  # Now, we wait for the non-blocking function to complete
    result2 = await task2
    # print(f"After non-blocking function completes: {result}")
    # print(f"After non-blocking function completes: {result2}")
    print("This line runs after non-blocking function completes.")

if __name__ == "__main__":
    asyncio.run(main())