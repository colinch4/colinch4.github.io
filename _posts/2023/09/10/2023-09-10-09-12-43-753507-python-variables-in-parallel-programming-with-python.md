---
layout: post
title: "[Python] Variables in parallel programming with Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Parallel programming allows us to distribute and execute tasks concurrently, improving the performance of our applications. In Python, we can achieve parallelism using libraries such as `multiprocessing` and `threading`. When working with parallel programming, it is important to understand how variables are handled in a concurrent environment.

## Shared and Local Variables

In parallel programming, we often encounter situations where multiple threads or processes need access to the same variables. These variables can be broadly categorized as **shared** and **local** variables.

- **Shared variables** are accessible by multiple threads or processes. When a shared variable is modified by one thread, the changes are visible to other threads. However, accessing and modifying shared variables concurrently can lead to **race conditions** and **data inconsistencies**.

- **Local variables** are independent for each thread or process. Each thread or process has its own copy of local variables, so modifications made to local variables in one thread do not affect the values in other threads.

Understanding the distinction between shared and local variables is crucial for writing correct and efficient parallel code.

## Thread-Local Variables

In Python's `threading` module, we can create thread-local variables using the `threading.local()` class. Each thread that accesses a thread-local variable has its own unique copy of the variable.

Let's see an example to understand how thread-local variables work:

```python
import threading

def print_counter(thread_name):
    local_counter = thread_local.counter
    for _ in range(5):
        local_counter += 1
        print(f"{thread_name}: Counter value = {local_counter}")
        thread_local.counter = local_counter

# Create a thread-local variable
thread_local = threading.local()

# Create two threads
thread1 = threading.Thread(target=print_counter, args=("Thread 1",))
thread2 = threading.Thread(target=print_counter, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()
```

In the code above, we create a thread-local variable `thread_local.counter` using `threading.local()`. Each thread has its own `counter` variable. The `print_counter` function modifies and prints its respective thread's counter variable. As a result, each thread maintains its separate counter, and the changes made by one thread do not affect the other.

## Multiprocess Variables

In Python's `multiprocessing` module, we can use shared variables to communicate between processes. The module provides various mechanisms such as `multiprocessing.Value` and `multiprocessing.Array` to create shared variables with lock synchronization.

Here's an example that demonstrates the usage of `multiprocessing.Value` to create shared variables:

```python
import multiprocessing

def increment_counter(counter):
    for _ in range(5):
        with counter.get_lock():
            counter.value += 1
            print(f"Counter value = {counter.value}")

if __name__ == "__main__":
    # Create a shared counter variable
    counter = multiprocessing.Value("i", 0)

    # Create two processes
    process1 = multiprocessing.Process(target=increment_counter, args=(counter,))
    process2 = multiprocessing.Process(target=increment_counter, args=(counter,))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to complete
    process1.join()
    process2.join()
```

In the code above, we create a shared counter variable `counter` using `multiprocessing.Value`. The `increment_counter` function increments the counter in a thread-safe manner by acquiring a lock using the `get_lock()` method. As a result, the changes made by one process are visible to the other process, and we get the correct counter value.

## Conclusion

Understanding how variables are handled in parallel programming is essential to write efficient and bug-free code. Python provides us with tools like thread-local variables and shared variables to handle data in parallel environments. By utilizing these tools effectively, we can harness the power of parallel programming to enhance the performance of our Python applications.