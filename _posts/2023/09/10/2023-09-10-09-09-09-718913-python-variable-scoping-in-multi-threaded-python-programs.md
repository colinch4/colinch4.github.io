---
layout: post
title: "[Python] Variable scoping in multi-threaded Python programs"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Introduction
Multi-threading is a powerful mechanism in Python that allows multiple threads to run concurrently within the same program. However, when using multiple threads, it is important to understand how variable scoping works to avoid unexpected behavior and bugs.

In this blog post, we will explore variable scoping in multi-threaded Python programs and discuss how to ensure proper variable access and synchronization between threads.

## Global Variables
In Python, variables declared outside of any function or class are considered global variables. These variables have global scope, meaning they can be accessed and modified from anywhere within the program, including different threads.

```
counter = 0

def increment_counter():
    global counter
    counter += 1

t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Counter value: {counter}")
```

In the above example, we define a global variable `counter` and two threads, `t1` and `t2`, that both call the `increment_counter` function which increments the value of `counter` by 1. By using the `global` keyword, we ensure that the `counter` variable is accessed and modified globally by both threads.

## Local Variables
Local variables, on the other hand, are declared within a function or method and are only accessible within that specific scope. Each thread has its own stack and local variables, which ensures thread-safety when accessing and modifying these variables.

```
import threading

def print_name(name):
    for _ in range(5):
        print(f"Hello, {name}!")

t1 = threading.Thread(target=print_name, args=("Alice",))
t2 = threading.Thread(target=print_name, args=("Bob",))

t1.start()
t2.start()

t1.join()
t2.join()
```

In this example, we define a `print_name` function that takes a `name` parameter and prints a greeting message using that name. We create two threads, `t1` and `t2`, each calling the `print_name` function with a different name.

Since the `name` parameter is local to the `print_name` function, each thread will have its own copy of the `name` variable, ensuring that the messages are printed correctly without interference from other threads.

## Thread-local Variables
In some cases, you may need to share data between threads but still want each thread to have its own separate copy of the data. Thread-local variables can be used to achieve this.

```
thread_data = threading.local()

def set_thread_name(name):
    thread_data.name = name

def print_thread_name():
    print(f"Thread name: {thread_data.name}")

t1 = threading.Thread(target=set_thread_name, args=("Alice",))
t2 = threading.Thread(target=set_thread_name, args=("Bob",))
t3 = threading.Thread(target=print_thread_name)
t4 = threading.Thread(target=print_thread_name)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
```

In this example, we use the `threading.local()` class to create a thread-local object called `thread_data`. We then define two functions, `set_thread_name` and `print_thread_name`, which respectively set the thread's name in `thread_data` and print the thread's name from `thread_data`.

By using thread-local variables, each thread can have its own separate copy of the `name` variable, and any modifications to `thread_data.name` will not affect other threads.

## Conclusion
Understanding variable scoping is crucial when working with multi-threaded Python programs. By properly defining the scope of variables, we can ensure correct and synchronized access to shared data across threads.

In this blog post, we have explored global variables, local variables, and thread-local variables in multi-threaded Python programs. By using the right variable scoping techniques, you can write robust and thread-safe code.

Happy coding!