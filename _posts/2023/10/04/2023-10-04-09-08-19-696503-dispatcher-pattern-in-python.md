---
layout: post
title: "Dispatcher pattern in Python"
description: " "
date: 2023-10-04
tags: [introduction, implementing]
comments: true
share: true
---

The Dispatcher pattern is a design pattern that allows decoupling between the sender of a request and its receivers. It is commonly used in event-driven systems, where multiple objects need to be notified when a certain event occurs. In this blog post, we will explore how to implement the Dispatcher pattern in Python.

## Table of Contents
- [Introduction to the Dispatcher Pattern](#introduction-to-the-dispatcher-pattern)
- [Implementing the Dispatcher Pattern in Python](#implementing-the-dispatcher-pattern-in-python)
- [Benefits of Using the Dispatcher Pattern](#benefits-of-using-the-dispatcher-pattern)
- [Conclusion](#conclusion)

## Introduction to the Dispatcher Pattern

The dispatcher pattern follows the publisher-subscriber model, where the publisher (dispatcher) broadcasts events to all the subscribers (receivers) that have registered themselves to receive those events. The dispatcher acts as a central hub, enabling loose coupling between the sender and its receivers.

## Implementing the Dispatcher Pattern in Python

Let's start by defining the `Dispatcher` class:

```python
class Dispatcher:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.subscribers:
            self.subscribers[event].remove(callback)

    def dispatch(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)
```

The `Dispatcher` class has three main methods:

- `subscribe(event, callback)`: This method registers a callback function to be called when the specified event occurs.
- `unsubscribe(event, callback)`: This method removes a callback function from the subscribers list for the specified event.
- `dispatch(event, data=None)`: This method triggers all the registered callbacks for the specified event, passing an optional data parameter.

Let's see an example of how to use the `Dispatcher` class:

```python
# Create a dispatcher instance
dispatcher = Dispatcher()

# Define event handlers
def handler1(data):
    print("Handler 1:", data)

def handler2(data):
    print("Handler 2:", data)

# Subscribe event handlers
dispatcher.subscribe("event1", handler1)
dispatcher.subscribe("event2", handler2)

# Dispatch events
dispatcher.dispatch("event1", "Hello")
dispatcher.dispatch("event2", "World")

# Unsubscribe event handler
dispatcher.unsubscribe("event1", handler1)

# Dispatch event after unsubscribe
dispatcher.dispatch("event1", "This won't be printed")
```

In this example, two event handlers (`handler1` and `handler2`) are registered to the dispatcher for different events. The `dispatch` method is then called to trigger the respective event handlers with the specified data.

## Benefits of Using the Dispatcher Pattern

The Dispatcher pattern offers several benefits:

- **Loose coupling**: The dispatcher acts as an intermediary between the sender and receivers, enabling them to operate independently. The sender does not need to have direct knowledge of the receivers.
- **Easy extensibility**: Adding new subscribers (receivers) or removing existing ones can be done dynamically.
- **Decentralized control**: The control flow is decentralized with the dispatcher being responsible for managing the event dispatching.

## Conclusion

The Dispatcher pattern provides an efficient way to implement event-driven systems and decouple the sender and its receivers. By using the Dispatcher pattern, you can achieve loosely-coupled components and easy extensibility in your Python projects.

Remember to [follow us on Twitter](https://twitter.com/yourcompany) for more tech tips and updates! #Python #DispatcherPattern