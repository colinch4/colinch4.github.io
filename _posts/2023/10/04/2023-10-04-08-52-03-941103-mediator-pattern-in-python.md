---
layout: post
title: "Mediator pattern in Python"
description: " "
date: 2023-10-04
tags: [softwareengineering, designpatterns]
comments: true
share: true
---

In software engineering, the Mediator pattern is a behavioral design pattern that allows loose coupling between components by using a mediator object to handle communication between them. This pattern promotes the principle of "separation of concerns" and helps in reducing the direct dependencies between the components. In this blog post, we will explore the Mediator pattern and see how it can be implemented in Python.

## What is the Mediator Pattern?

The Mediator pattern defines an object known as the mediator, which encapsulates the communication logic between multiple objects, also known as colleagues. Rather than having direct communication between colleagues, they communicate only through the mediator. The mediator acts as a central hub, facilitating communication and coordination between the colleagues.

## Use Cases of Mediator Pattern

The Mediator pattern can be useful in various scenarios, such as:

1. When a system is made up of multiple components with complex interactions.
2. When adding new components or changing existing ones should have minimal impact on the others.
3. When a system needs to be easily maintainable, extensible, and flexible.

## Implementation of Mediator Pattern in Python

Let's consider a scenario where we have a chat application with multiple users. Each user can send and receive chat messages from other users. Instead of directly connecting and communicating with other users, the communication will be facilitated through a chat mediator.

```python
# Creating the Mediator class
class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_message(message)

# Creating the User class
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")

# Usage
mediator = ChatMediator()

user1 = User("User 1", mediator)
user2 = User("User 2", mediator)
user3 = User("User 3", mediator)

mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)

user1.send_message("Hello World!")
```

In the above implementation, we have a `ChatMediator` class that maintains a list of users and provides methods to add users and send messages. The `User` class represents a user in the chat application and has methods to send and receive messages. Users communicate by calling the `send_message` method of the mediator, which then relays the message to all other users except the sender.

## Benefits of Using the Mediator Pattern

1. **Decoupling**: The Mediator pattern helps in decoupling components by promoting indirect communication through a mediator object. This reduces dependencies and makes the system more flexible.
2. **Scalability**: Adding new components or changing existing ones becomes easier as the communication logic is centralized in the mediator. The mediator can handle complex interactions between components, allowing the system to scale.
3. **Maintainability**: With the Mediator pattern, the communication logic is concentrated in one place, making it easier to maintain and modify. Changes in one component have minimal impact on other components.

## Conclusion

The Mediator pattern is a powerful design pattern that enables loose coupling and effective communication between components. By encapsulating communication logic, it promotes modularity, scalability, and maintainability in software systems. In Python, the Mediator pattern can be implemented using classes and method calls, as shown in the example. Consider using this pattern in scenarios where you need to manage complex interactions between components while keeping them loosely coupled.

#softwareengineering #designpatterns