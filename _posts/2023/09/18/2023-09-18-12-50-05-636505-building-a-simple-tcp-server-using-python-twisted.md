---
layout: post
title: "Building a simple TCP server using Python Twisted"
description: " "
date: 2023-09-18
tags: [python, twisted]
comments: true
share: true
---

In this tutorial, we will learn how to create a simple TCP server using **Python Twisted**. Twisted is an event-driven networking engine that provides support for various protocols, including TCP, UDP, and SSL.

## Prerequisites
To follow along with this tutorial, make sure you have the following installed:
- Python (version 3.x recommended)
- Twisted library (`pip install twisted`)

## Creating the TCP Server
First, let's import the required modules:

```python
from twisted.internet import reactor, protocol
```

Next, we define our custom protocol class that inherits from `protocol.Protocol`:

```python
class MyProtocol(protocol.Protocol):
    def connectionMade(self):
        print("Client connected!")

    def dataReceived(self, data):
        print("Received:", data)
```

In this example, we override the `connectionMade` method to print a message when a client connects, and the `dataReceived` method to print the received data.

Now, we create a factory class that inherits from `protocol.Factory` and associates our custom protocol with it:

```python
class MyFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return MyProtocol()
```

We override the `buildProtocol` method to return an instance of our custom protocol whenever a new client connects.

Finally, we start the server by calling `reactor.listenTCP` with the desired port number:

```python
if __name__ == "__main__":
    factory = MyFactory()
    reactor.listenTCP(1234, factory)
    print("Server started!")

    reactor.run()
```

In this example, the server listens on port **1234**. You can change the port number according to your needs.

## Running the TCP Server
Save the above code in a **.py** file and run it. You should see the message "Server started!" printed to the console, indicating that the server has started successfully.

You can now open a TCP client and connect to the server using the specified port. Once connected, any data you send will be displayed in the console.

## Conclusion
In this tutorial, we learned how to build a simple TCP server using Python Twisted. Twisted provides a powerful and flexible framework for developing network applications, making it easy to handle various protocols and scale your server when needed.

#python #twisted