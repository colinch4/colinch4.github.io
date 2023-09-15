---
layout: post
title: "Basics of multi-threading in Python"
description: " "
date: 2023-09-15
tags: [Python, Threading]
comments: true
share: true
---

Multi-threading is a technique that allows multiple threads to execute concurrently within a single process. Python provides built-in support for multi-threading with the `threading` module. In this article, we'll cover the basics of multi-threading in Python and how it can be used to improve the performance of your programs.

## The `threading` module

The `threading` module in Python provides a high-level interface for creating and managing threads. It allows you to spawn new threads, control their execution, and synchronize them when necessary.

To get started, you need to import the `threading` module:

```python
import threading
```

## Creating and starting a thread

To create a new thread, you need to define a function that will be executed by the thread. This function is often referred to as the "target" function. You can then create an instance of the `Thread` class and pass the target function as an argument. Finally, you can start the thread by calling the `start()` method.

Here's an example that creates and starts a simple thread:

```python
import threading

def target_function():
    print("This is a target function executed by a thread.")

# Create a Thread instance
thread = threading.Thread(target=target_function)

# Start the thread
thread.start()
```

The output of this code will be:

```
This is a target function executed by a thread.
```

## Joining threads

In some cases, you may need to wait for a thread to complete its execution before continuing with the rest of your program. You can achieve this using the `join()` method, which blocks the execution of the main thread until the target thread has finished.

Here's an example that demonstrates how to join a thread:

```python
import threading
import time

def target_function():
    time.sleep(2)
    print("Finished executing target function.")

# Create a Thread instance
thread = threading.Thread(target=target_function)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Main thread continues after joining the thread.")
```

The output of this code will be:

```
Finished executing target function.
Main thread continues after joining the thread.
```

## Thread synchronization

When multiple threads access shared resources concurrently, thread synchronization is necessary to ensure thread safety and avoid issues like race conditions. Python provides several synchronization primitives, such as locks, semaphores, and condition variables, to help you achieve synchronization.

One commonly used synchronization primitive is the `Lock` class, which allows only a single thread to acquire the lock at a time, ensuring exclusive access to the shared resource.

Here's an example that demonstrates how to use a `Lock` to synchronize access to a shared variable:

```python
import threading

shared_variable = 0
lock = threading.Lock()

def increment_variable():
    global shared_variable

    with lock:
        shared_variable += 1

def decrement_variable():
    global shared_variable

    with lock:
        shared_variable -= 1

# Create two Thread instances
thread1 = threading.Thread(target=increment_variable)
thread2 = threading.Thread(target=decrement_variable)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Shared variable:", shared_variable)
```

The output of this code will depend on the order in which the threads acquire the lock. However, it will always be a consistent result.

## Conclusion

Multi-threading in Python can be a powerful tool to improve the performance of your programs by executing tasks concurrently. The `threading` module provides a convenient interface for creating and managing threads. Remember to properly synchronize your threads when accessing shared resources to avoid issues like race conditions.

#Python #Threading