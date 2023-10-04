---
layout: post
title: "Chain of Responsibility pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In software development, the **Chain of Responsibility** pattern is a behavioral design pattern that allows an object to pass a request along a chain of potential handlers until the request is handled or reaches the end of the chain.

## Why use Chain of Responsibility?

The Chain of Responsibility pattern provides a way to decouple the sender and receiver of a request. This can be useful when we want to give multiple objects an opportunity to handle a request without explicitly specifying a receiver. It promotes loose coupling and flexibility in handling requests.

## How does it work?

1. Define an abstract base class (or an interface) that represents a handler in the chain. This class should have a method for handling requests and a reference to the next handler in the chain.

2. Create concrete handler classes that inherit from the abstract base class. Each concrete handler should implement the handling logic and decide whether to handle the request or pass it to the next handler in the chain.

3. Instantiate the handlers and connect them in a chain by setting the next handler for each handler.

4. Pass a request to the first handler in the chain. The request will be passed along the chain until it's handled or reaches the end of the chain.

## Example

Let's demonstrate the Chain of Responsibility pattern with an example. Suppose we have a customer support system where customer requests are handled by different levels of support staff based on the complexity of the issue.

```python
class SupportHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, request):
        pass


class Level1Handler(SupportHandler):
    def handle_request(self, request):
        if request == "Level 1":
            print("Handled by Level 1 Support")
        elif self.next_handler:
            self.next_handler.handle_request(request)


class Level2Handler(SupportHandler):
    def handle_request(self, request):
        if request == "Level 2":
            print("Handled by Level 2 Support")
        elif self.next_handler:
            self.next_handler.handle_request(request)


class Level3Handler(SupportHandler):
    def handle_request(self, request):
        if request == "Level 3":
            print("Handled by Level 3 Support")
        else:
            print("No appropriate handler found")


# Setting up the chain
level1_handler = Level1Handler()
level2_handler = Level2Handler()
level3_handler = Level3Handler()

# Connecting the handlers
level1_handler.next_handler = level2_handler
level2_handler.next_handler = level3_handler

# Handling requests
level1_handler.handle_request("Level 2")  # Output: Handled by Level 2 Support
level1_handler.handle_request("Level 3")  # Output: Handled by Level 3 Support
level1_handler.handle_request("Level 4")  # Output: No appropriate handler found
```

In this example, we have three levels of support handlers (`Level1Handler`, `Level2Handler`, and `Level3Handler`). The `handle_request` method of each handler checks if it can handle the request, and if not, passes the request to the next handler in the chain. If no appropriate handler is found, it displays a message indicating that.

## Conclusion

The Chain of Responsibility pattern provides a flexible and decoupled way to handle requests by chaining multiple handlers. It promotes loose coupling, reusability, and extensibility in the code. By implementing the pattern, you can easily manage complex request handling scenarios in your Python applications.