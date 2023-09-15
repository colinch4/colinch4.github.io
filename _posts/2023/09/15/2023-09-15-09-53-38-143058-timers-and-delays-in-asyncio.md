---
layout: post
title: "Timers and delays in Asyncio"
description: " "
date: 2023-09-15
tags: [Python, Asyncio]
comments: true
share: true
---

When working with asynchronous programming in Python, the `asyncio` library is a powerful tool for managing concurrency. One common requirement in such programming paradigms is the need for timers and delays. In this blog post, we will explore how to use timers and delays in `asyncio` to control the execution flow of our asynchronous code.

## Timers

Timers are useful when you need to schedule a function to run after a certain period of time. In `asyncio`, you can use the `asyncio.sleep()` function to create a timer. Let's take a look at a simple example:

```python
import asyncio

async def my_function():
    print("This is my function")
    
    await asyncio.sleep(2)  # Sleep for 2 seconds
    
    print("The timer has ended")

asyncio.run(my_function())
```

In the above example, we define an `async` function called `my_function()`. Inside this function, we print a message, then we use `asyncio.sleep(2)` to sleep for 2 seconds. After the sleep duration is over, the program continues and prints another message.

By using timers, we can introduce delays between different parts of our code, allowing us to control the execution flow in an asynchronous manner.

## Delays

Delays are similar to timers but are useful when you want to introduce a delay without blocking the execution of other concurrent tasks. `asyncio` provides the `asyncio.create_task()` function to handle delays. Here's a practical example:

```python
import asyncio

async def long_running_task():
    await asyncio.sleep(5)
    print("Long running task completed")

async def my_function():
    print("This is my function")
    
    task = asyncio.create_task(long_running_task())
    
    print("Task started, but my_function doesn't wait for it to complete")
    
    print("This is another statement")

asyncio.run(my_function())
```

In the above code, we define two `async` functions: `my_function` and `long_running_task`. When `my_function` is called, it creates a new task using `asyncio.create_task()`, which represents `long_running_task`. The key point here is that `my_function` does not wait for `long_running_task` to complete and continues executing other statements immediately.

By using delays, we can achieve better concurrency and avoid blocking the execution of other async tasks. Delays are particularly useful when dealing with long-running tasks that can be executed independently.

## Conclusion

In this blog post, we explored how to use timers and delays in `asyncio` to control the execution flow of asynchronous code. Timers allow us to schedule actions to happen after a certain period of time, while delays introduce pauses without blocking concurrent tasks. Understanding and effectively using timers and delays is crucial for writing efficient and responsive asynchronous code using `asyncio`.

#Python #Asyncio