---
layout: post
title: "Futures pattern in Python"
description: " "
date: 2023-10-04
tags: [introduction, using]
comments: true
share: true
---

In concurrent programming, the **Futures pattern** is a design pattern that allows for asynchronous execution of tasks and retrieval of their results. It is particularly useful when dealing with long-running or blocking operations, as it allows other tasks to continue executing while waiting for the results.

Python provides a built-in module called `concurrent.futures` that implements the Futures pattern and makes it easy to write concurrent code. In this blog post, we'll explore how to use the Futures pattern in Python using the `concurrent.futures` module.

## Table of Contents

- [Introduction to Futures Pattern](#introduction-to-futures-pattern)
- [Using the `concurrent.futures` Module](#using-the-concurrentfutures-module)
- [Creating and Submitting Futures](#creating-and-submitting-futures)
- [Retrieving Results from Futures](#retrieving-results-from-futures)
- [Exception Handling with Futures](#exception-handling-with-futures)
- [Conclusion](#conclusion)

## Introduction to Futures Pattern

The Futures pattern allows you to encapsulate a computation that may or may not have completed yet. It provides a way to access the result of the computation at a later time, without blocking the main thread.

A *future* is an object that represents the result of an asynchronous computation. It can be in one of three states:

- **Running**: The computation is currently in progress.
- **Completed**: The computation has finished successfully.
- **Cancelled**: The computation was cancelled before completion.

Using futures allows you to perform multiple computations concurrently and retrieve their results when they are available, improving the efficiency of your code.

## Using the `concurrent.futures` Module

Python's `concurrent.futures` module provides two classes for working with futures: `ThreadPoolExecutor` and `ProcessPoolExecutor`. The `ThreadPoolExecutor` utilizes multiple threads for concurrent execution, while the `ProcessPoolExecutor` uses multiple processes.

To start using the `concurrent.futures` module, you need to import it like this:

```python
import concurrent.futures
```

## Creating and Submitting Futures

To create and submit a future for execution, you first need to create a `ThreadPoolExecutor` or `ProcessPoolExecutor` object. Then, you can use the `submit()` method to submit a callable object (a function or a method) for execution.

Here's an example that demonstrates how to create and submit a future using `ThreadPoolExecutor`:

```python
import concurrent.futures

def calculate_square(n):
    return n ** 2

# Create a ThreadPoolExecutor with 2 worker threads
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# Submit the calculate_square function with argument 5 for execution
future = executor.submit(calculate_square, 5)
```

In the above example, `calculate_square` is submitted as a future for execution with a argument of 5.

## Retrieving Results from Futures

Once you have submitted a future for execution, you can retrieve its result using the `result()` method. This method blocks until the future has completed and returns the result.

```python
# Get the result from the future
result = future.result()
print(result)  # Output: 25
```

The `result()` method will block until the future has completed, so if the computation is still running, the program will wait until it finishes.

You can also specify a timeout parameter when calling `result()`, which will raise a `concurrent.futures.TimeoutError` if the future doesn't complete within the given timeout period.

## Exception Handling with Futures

When working with futures, it's important to handle any exceptions that might have occurred during the computation.

To handle exceptions, you can use the `exception()` method of the future. This method returns the exception that occurred during the computation, or `None` if the future completed successfully.

```python
import concurrent.futures

def calculate_square(n):
    if n < 0:
        raise ValueError("Invalid number.")
    return n ** 2

executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
future = executor.submit(calculate_square, -5)

try:
    result = future.result()
except Exception as e:
    print(f"An exception occurred: {e}")
```

In the above example, if the submitted computation raises a `ValueError`, we handle it by printing the exception message.

## Conclusion

The Futures pattern is a powerful tool to incorporate asynchronous and concurrent behavior into your Python programs. With the `concurrent.futures` module, Python provides an easy-to-use API for working with futures and executing tasks concurrently.

By using the Futures pattern, you can improve the performance and responsiveness of your Python code, especially when dealing with long-running or blocking operations.

So, the next time you have a task that can be executed asynchronously, consider using the Futures pattern in Python to make your code more efficient and responsive.

## #PythonProgramming #ConcurrentProgramming