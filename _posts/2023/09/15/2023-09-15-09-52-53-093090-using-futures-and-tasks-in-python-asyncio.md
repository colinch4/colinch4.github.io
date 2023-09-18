---
layout: post
title: "Using Futures and Tasks in Python Asyncio"
description: " "
date: 2023-09-15
tags: [asyncio]
comments: true
share: true
---

Python's `asyncio` library provides a powerful way to write asynchronous programs. One of its key features is the ability to work with concurrent tasks using futures and tasks. In this blog post, we will explore how to use futures and tasks in `asyncio` to make your code more efficient and responsive.

## Futures

A future represents a result that is not yet available. It is a placeholder object that allows you to work with the result of a computation that might not be finished yet. When you create a future, it starts in a pending state. You can await a future to get the result of the computation.

```python
import asyncio

async def compute_result():
    await asyncio.sleep(5)
    return 42

async def main():
    future = asyncio.ensure_future(compute_result())
    result = await future
    print(result)

asyncio.run(main())
```

In the code snippet above, we define a coroutine `compute_result()` that simulates a long-running computation using `asyncio.sleep(5)`. We create a future using `asyncio.ensure_future()` and await it to get the result. Finally, we print the result once it becomes available.

## Tasks

A task is a subclass of a future and is used to wrap a coroutine in order to schedule its execution. It allows you to manage the execution of coroutines concurrently. Tasks are created using `asyncio.create_task()`.

```python
import asyncio

async def compute_result():
    await asyncio.sleep(5)
    return 42

async def main():
    task = asyncio.create_task(compute_result())
    result = await task
    print(result)

asyncio.run(main())
```

In the above code, we create a task using `asyncio.create_task()` and await it to get the result. Tasks allow you to schedule multiple coroutines concurrently and manage their execution.

## Cancelling Tasks

You can cancel tasks using the `task.cancel()` method. When a task is cancelled, it raises a `CancelledError` exception inside the coroutine. You can handle this exception to perform any necessary cleanup or react appropriately to the cancellation.

```python
import asyncio

async def compute_result():
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Computation cancelled!")

async def main():
    task = asyncio.create_task(compute_result())
    await asyncio.sleep(2)
    task.cancel()

asyncio.run(main())
```

In the code above, we cancel the task after waiting for 2 seconds using `task.cancel()`. The `compute_result()` coroutine catches the `CancelledError` exception and prints a message to indicate that the computation has been cancelled.

## Conclusion

Futures and tasks are powerful tools in `asyncio` for managing concurrent computations in Python. They allow you to write efficient and responsive asynchronous code. By understanding how to work with futures and tasks, you can harness the full potential of `asyncio` and build high-performance applications.

#python #asyncio