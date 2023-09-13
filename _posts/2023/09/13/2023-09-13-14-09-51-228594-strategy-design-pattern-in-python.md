---
layout: post
title: "Strategy design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The Strategy design pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable at runtime. It decouples the algorithms from the client code, making it easier to add, remove, or modify algorithms without affecting the clients.

## How does it work?

The key idea behind the Strategy design pattern is to define a set of algorithms that can be used interchangeably. Each algorithm is encapsulated in a separate class, and they all implement a common interface or base class.

The client code can then use any of the available algorithms by simply interacting with the common interface. This provides flexibility and extensibility, as new algorithms can be added without modifying the existing code.

## Example

Let's consider an example where we have a `PaymentProcessor` class that handles different payment methods. We want the payment method to be interchangeable, so we apply the Strategy design pattern to encapsulate the payment algorithms.

First, we define the strategy interface, `PaymentStrategy`, which declares a method `process_payment()`:

```python
class PaymentStrategy:
    def process_payment(self, amount):
        pass
```

Next, we implement concrete strategy classes for different payment methods. Let's say we have `CreditCardPaymentStrategy` and `PaypalPaymentStrategy`:

```python
class CreditCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} dollars")

class PaypalPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing Paypal payment of {amount} dollars")
```

Finally, we have our `PaymentProcessor` class that takes a payment strategy and uses it to process payments:

```python
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.process_payment(amount)
```

Now, let's use the implemented classes:

```python
cc_payment = CreditCardPaymentStrategy()
pp_payment = PaypalPaymentStrategy()

processor = PaymentProcessor(cc_payment)
processor.process_payment(100)

processor = PaymentProcessor(pp_payment)
processor.process_payment(50)
```

In this example, we create instances of the concrete strategy classes `CreditCardPaymentStrategy` and `PaypalPaymentStrategy`. We then pass them as arguments to the `PaymentProcessor` instance and call the `process_payment()` method. The output will be:

```
Processing credit card payment of 100 dollars
Processing Paypal payment of 50 dollars
```

## Conclusion

The Strategy design pattern is a powerful tool for encapsulating and controlling the behavior of different algorithms in your applications. It promotes code reusability, flexibility, and maintainability. By applying this pattern in Python, you can easily switch between different algorithms or add new ones without modifying the existing codebase.