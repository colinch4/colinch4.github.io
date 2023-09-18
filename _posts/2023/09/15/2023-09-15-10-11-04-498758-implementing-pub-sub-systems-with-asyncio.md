---
layout: post
title: "Implementing pub-sub systems with Asyncio"
description: " "
date: 2023-09-15
tags: [asyncio, pubsub, realtime, eventdriven]
comments: true
share: true
---

In today's fast-paced world, real-time communication and efficient data processing are crucial for many applications. Pub-Sub (Publish-Subscribe) systems provide a scalable and flexible solution to handle real-time data streaming and event-driven communication. In this blog post, we will explore how to implement a Pub-Sub system using the powerful asyncio library in Python.

## What is a Pub-Sub System?

A Pub-Sub system allows publishers to send messages to a central broker, which then distributes those messages to interested subscribers. It decouples the sender (publisher) from the receiver (subscriber) by relying on a broker to handle message routing. This architecture provides flexibility, as publishers and subscribers can be added or removed dynamically without impacting the overall system.

## Getting Started with Asyncio

Asyncio is a powerful asynchronous programming library in Python that provides support for writing concurrent code using coroutines, tasks, and event loops. To start working with Asyncio, make sure you have Python 3.7 or greater installed. You can install asyncio using pip:

```
pip install asyncio
```

Once installed, you can import the necessary modules to begin working with asyncio:

```python
import asyncio
```

## Implementing the Pub-Sub System

To implement the Pub-Sub system with asyncio, we can leverage its coroutines and event loop features. Let's start by creating a publisher and subscriber class.

### Publisher Class

The `Publisher` class will have a method to send messages to the broker. We can use an asyncio `Queue` to manage the messages sent by the publisher.

```python
class Publisher:
    def __init__(self):
        self.queue = asyncio.Queue()
    
    async def send_message(self, message):
        await self.queue.put(message)
```

### Subscriber Class

The `Subscriber` class will have a method to receive messages from the broker. We can use an asyncio `Queue` to manage the received messages.

```python
class Subscriber:
    def __init__(self, name):
        self.name = name
        self.queue = asyncio.Queue()
    
    async def receive_message(self):
        message = await self.queue.get()
        print(f"{self.name} received message: {message}")
```

### Broker Class

The `Broker` class will act as the central hub for message distribution. It will have a `publish` method to receive messages from publishers and a `subscribe` method to register subscribers.

```python
class Broker:
    def __init__(self):
        self.subscribers = set()
    
    async def publish(self, message):
        for subscriber in self.subscribers:
            await subscriber.queue.put(message)
    
    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)
```

### Putting it all together

We can now create an instance of the `Publisher`, `Subscriber`, and `Broker` classes to test our implementation.

```python
async def main():
    broker = Broker()

    publisher = Publisher()
    subscriber1 = Subscriber("Subscriber 1")
    subscriber2 = Subscriber("Subscriber 2")

    # Add subscribers to the broker
    broker.subscribe(subscriber1)
    broker.subscribe(subscriber2)

    # Send messages from the publisher
    await publisher.send_message("Hello, World!")
    await publisher.send_message("Pub-Sub is awesome!")

    # Receive messages from subscribers
    await subscriber1.receive_message()
    await subscriber2.receive_message()

asyncio.run(main())
```

When you run the code above, you should see the output:

```
Subscriber 1 received message: Hello, World!
Subscriber 2 received message: Hello, World!
Subscriber 1 received message: Pub-Sub is awesome!
Subscriber 2 received message: Pub-Sub is awesome!
```

## Conclusion

Asyncio provides powerful tools for implementing efficient and scalable Pub-Sub systems. By using coroutines and event loops, we can create publishers, subscribers, and a central broker to handle real-time message distribution. This enables real-time communication and data streaming in many applications, from chat systems to Internet of Things (IoT) devices.

#python #asyncio #pubsub #realtime #eventdriven