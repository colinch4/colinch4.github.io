---
layout: post
title: "Basics of multi-processing in Python"
description: " "
date: 2023-09-15
tags: [python, multiprocessing]
comments: true
share: true
---

Python offers several options for implementing multi-processing to leverage the power of multiple CPU cores and enhance the performance of your applications. In this blog post, we will explore the basics of multi-processing in Python and how to get started with it.

## What is Multi-processing?

Multi-processing is a technique where a program executes multiple processes in parallel, each running independently and utilizing a separate CPU core. It allows for efficient usage of system resources and can significantly speed up the execution of CPU-intensive tasks.

## The `multiprocessing` Module

In Python, the `multiprocessing` module provides a high-level interface for implementing multi-processing. It allows you to create processes, communicate between them, and synchronize their execution.

To use the `multiprocessing` module, you first need to import it:

```python
import multiprocessing
```

### Creating Processes

The basic unit of multi-processing in Python is a process. You can create a new process by instantiating the `Process` class from the `multiprocessing` module. Here's an example:

```python
import multiprocessing

def worker():
    print("Worker process")

if __name__ == '__main__':
    process = multiprocessing.Process(target=worker)
    process.start()
```

In the above example, we define a `worker` function that will be executed by the new process. The `multiprocessing.Process` class is used to create a new process with the `target` argument set to the `worker` function. Finally, we start the process by calling the `start()` method.

### Inter-process Communication

Inter-process communication (IPC) allows processes to exchange data and synchronize their execution. Python's `multiprocessing` module provides several mechanisms for IPC, such as pipes, queues, and shared memory.

Let's look at an example of using a `Queue` for communication between two processes:

```python
import multiprocessing

def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f"Produced: {i}")

def consumer(queue):
    while not queue.empty():
        item = queue.get()
        print(f"Consumed: {item}")

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=producer, args=(queue,))
    process2 = multiprocessing.Process(target=consumer, args=(queue,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
```

In this example, we define a `producer` and a `consumer` function. The `producer` function puts items into a queue, and the `consumer` function consumes items from the queue. We create a `Queue` object and pass it as an argument to both processes. Finally, we start the processes and use the `join()` method to wait for them to complete.

### Process Pool

Python's `multiprocessing` module also provides a `Pool` class for managing a pool of worker processes. The `Pool` class simplifies the process management by abstracting away the creation and synchronization of processes.

Here's an example of using a process pool:

```python
import multiprocessing

def worker(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(worker, [1, 2, 3, 4, 5])
        print(results)
```

In this example, we define a `worker` function that multiplies a number by itself. We create a `Pool` object with 4 processes and use the `map()` method to apply the `worker` function to a list of numbers. The `map()` method returns the results of the function calls.

## Conclusion

Multi-processing in Python allows you to take advantage of multiple CPU cores and improve the performance of your applications. The `multiprocessing` module provides a straightforward interface for creating processes, communicating between them, and managing worker pools. By utilizing multi-processing techniques, you can tackle computationally intensive tasks more efficiently.

#python #multiprocessing