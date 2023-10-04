---
layout: post
title: "Active Object pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In concurrent programming, the Active Object pattern is a design pattern that decouples method invocation from method execution in order to achieve concurrency and reduce thread contention. The pattern allows multiple threads to interact with an object while asynchronously executing its methods.

## How it works

The Active Object pattern involves the following components:

1. **Proxy**: The proxy object serves as the interface between the client and the active object. It receives method calls from the client and enqueues them in a message queue.

2. **Scheduler**: The scheduler is responsible for dequeuing messages from the message queue and executing them on the active object. It ensures that only one method is executed at a time, thus avoiding thread contention.

3. **Active Object**: The active object is the object with which the client interacts. It maintains an internal state and executes methods in a sequential manner.

## Example Implementation

Let's consider a simple example of a `Printer` class that prints a message. We will implement the Active Object pattern to allow multiple clients to print messages concurrently.

```python
import threading
from queue import Queue

class Printer:
    def __init__(self):
        self.message_queue = Queue()

    def print_message(self, message):
        print(f"Printing: {message}")

    def _run(self):
        while True:
            message = self.message_queue.get()
            self.print_message(message)
            self.message_queue.task_done()

    def start(self):
        threading.Thread(target=self._run, daemon=True).start()

class PrinterProxy:
    def __init__(self):
        self.printer = Printer()

    def print_message(self, message):
        self.printer.message_queue.put(message)

# Client code
printer_proxy = PrinterProxy()
printer_proxy.print_message("Hello")
printer_proxy.print_message("World")
```

In the example above, we create a `Printer` class, which has an internal message queue. The `print_message` method enqueues the message in the queue. The private `_run` method continuously dequeues messages from the queue and prints them using the `print_message` method.

To interact with the `Printer` class, we create a `PrinterProxy` class. The `PrinterProxy` object receives the `print_message` method calls from the client and enqueues them in the `Printer` object's message queue.

## Conclusion

The Active Object pattern allows concurrent method execution while maintaining thread safety and reducing contention. By decoupling method invocation from execution, the pattern improves the scalability and performance of concurrent systems. In Python, we can implement the Active Object pattern using a combination of a message queue, a scheduler, and a proxy object.