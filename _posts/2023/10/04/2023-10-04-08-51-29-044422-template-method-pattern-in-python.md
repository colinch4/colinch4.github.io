---
layout: post
title: "Template method pattern in Python"
description: " "
date: 2023-10-04
tags: [designpatterns]
comments: true
share: true
---

In object-oriented programming, the Template Method pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class and allows its subclasses to provide implementation for certain steps of the algorithm. This pattern promotes code reusability and allows customization of specific parts of an algorithm without changing the overall structure.

## When to use the Template Method pattern?

The Template Method pattern is useful in scenarios where you want to define a common algorithm that follows a specific sequence of steps, but allows the subclasses to provide their own implementation for some of these steps. It is often used when you want to enforce a certain structure or sequence of operations, while providing flexibility for customization.

## Implementing the Template Method pattern

To illustrate the Template Method pattern, let's consider a simple example of a notification system. We want to create a base class that provides a template for sending notifications, but allows subclasses to define their own ways of sending the actual message.

```python
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    def send_notification(self, message):
        self.connect_to_service()
        self.authenticate()
        self.prepare_message(message)
        self.send_message()

    @abstractmethod
    def connect_to_service(self):
        pass

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def prepare_message(self, message):
        pass

    @abstractmethod
    def send_message(self):
        pass

class EmailNotification(NotificationSender):
    def connect_to_service(self):
        print("Connecting to email service...")

    def authenticate(self):
        print("Authenticating email account...")

    def prepare_message(self, message):
        print(f"Preparing email message: {message}")

    def send_message(self):
        print("Sending email...")

class SMSNotification(NotificationSender):
    def connect_to_service(self):
        print("Connecting to SMS service...")

    def authenticate(self):
        print("Authenticating SMS account...")

    def prepare_message(self, message):
        print(f"Preparing SMS message: {message}")

    def send_message(self):
        print("Sending SMS...")
```

In the above example, we have a base class `NotificationSender` that defines the template method `send_notification()`. The template method calls several abstract methods that need to be implemented by the subclasses. 

We then create two subclasses, `EmailNotification` and `SMSNotification`, which inherit from the `NotificationSender` class and provide their own implementations for the abstract methods.

## Using the Template Method pattern

Now, let's see how we can use the Template Method pattern to send notifications:

```python
email_notification = EmailNotification()
email_notification.send_notification("Hello from email")

sms_notification = SMSNotification()
sms_notification.send_notification("Hello from SMS")
```

When we run this code, we get the following output:

```
Connecting to email service...
Authenticating email account...
Preparing email message: Hello from email
Sending email...

Connecting to SMS service...
Authenticating SMS account...
Preparing SMS message: Hello from SMS
Sending SMS...
```

As you can see, the `send_notification()` method follows a common sequence of steps defined in the base class, but the implementation of each step is provided by the subclasses.

## Conclusion

The Template Method pattern provides a way to define a common structure or sequence of operations, while allowing subclasses to provide their own implementation for specific steps. It promotes code reusability and customization. By using this pattern, you can ensure that the overall algorithm remains the same while allowing flexibility in certain parts of the implementation.

#python #designpatterns