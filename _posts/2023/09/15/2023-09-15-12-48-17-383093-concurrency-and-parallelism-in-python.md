---
layout: post
title: "Concurrency and parallelism in Python"
description: " "
date: 2023-09-15
tags: [Python, Concurrency]
comments: true
share: true
---

In Python, both concurrency and parallelism are techniques used to improve the performance of code execution. While they are related concepts, there are some key differences between them.

## Concurrency

Concurrency is the ability of a program to execute multiple tasks simultaneously. It allows for overlapping execution of tasks, so it appears as if they are executed simultaneously. However, under the hood, the execution is typically interleaved and non-deterministic.

Python provides several ways to handle concurrency. One of the most commonly used approaches is the *threading* module which allows you to create and manage multiple threads within a single program. Threads are lightweight and can be used to divide the execution of tasks among multiple CPU cores or to handle I/O-bound operations efficiently.

```python
import threading

def task1():
    # code for task1

def task2():
    # code for task2

if __name__ == "__main__":
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
```

It's important to note that due to the Global Interpreter Lock (GIL) in CPython, Python threads cannot fully utilize multiple CPU cores for compute-bound tasks.

Another approach to achieve concurrency in Python is by using asynchronous programming with the `asyncio` module. This allows you to write concurrent code using coroutines and event loops. With `asyncio`, you can handle I/O-bound tasks efficiently without blocking the execution of other tasks.

```python
import asyncio

async def task1():
    # code for task1

async def task2():
    # code for task2

async def main():
    await asyncio.gather(task1(), task2())

if __name__ == "__main__":
    asyncio.run(main())
```

## Parallelism

Parallelism, on the other hand, is the execution of multiple tasks simultaneously by distributing them across multiple CPU cores. It is well-suited for compute-bound tasks that can be divided into independent subtasks.

Python provides the `multiprocessing` module for achieving parallelism. It allows you to create and manage separate processes, each with its own Python interpreter and memory space. The `multiprocessing.Pool` class provides a convenient interface to execute tasks in parallel using processes.

```python
import multiprocessing

def task1():
    # code for task1

def task2():
    # code for task2

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        pool.apply_async(task1)
        pool.apply_async(task2)
        pool.close()
        pool.join()
```

Unlike threads, the Python interpreter releases the Global Interpreter Lock (GIL) for each process, allowing them to utilize multiple CPU cores for compute-bound tasks.

## Conclusion

Concurrency and parallelism are both important techniques that can improve the performance of your Python programs. Concurrency allows for overlapping execution of tasks, making it suitable for handling I/O-bound operations efficiently. Parallelism, on the other hand, enables the execution of multiple tasks simultaneously by distributing them across multiple CPU cores, making it ideal for compute-bound tasks.

By understanding the differences between concurrency and parallelism, you can choose the appropriate technique for your specific use case and optimize the performance of your Python applications.

#Python #Concurrency #Parallelism