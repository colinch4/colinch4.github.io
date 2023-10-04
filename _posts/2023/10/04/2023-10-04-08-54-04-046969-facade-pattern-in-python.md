---
layout: post
title: "Facade pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The Facade pattern is a software design pattern that provides a simplified interface to a complex system of classes, libraries, or APIs. It promotes loose coupling between the client code and the subsystems by providing a unified high-level interface.

## When to Use the Facade Pattern

Use the Facade pattern when:

1. You want to provide a simple interface to a complex system or set of classes.
2. You want to decouple the client code from the subsystems or dependencies.

## Implementation

To demonstrate the Facade pattern, let's consider a simple example of an online shopping system with various subsystems such as Inventory, Payment, and Shipping.

### Step 1: Create the Subsystem Classes

First, we need to create the subsystem classes that will handle specific functionalities of the system.

```python
# inventory.py

class Inventory:
    def check_stock(self, product_id):
        # Check stock availability for product
        pass

    def update_stock(self, product_id, quantity):
        # Update the stock quantity for a product
        pass

# payment.py

class Payment:
    def process_payment(self, amount):
        # Process payment for the given amount
        pass

# shipping.py

class Shipping:
    def ship_product(self, product_id, address):
        # Ship the product to the given address
        pass
```

### Step 2: Create the Facade Class

Next, we create a Facade class that provides a simplified interface to access the subsystems. It encapsulates the complexities and dependencies of the subsystems behind a single interface.

```python
# facade.py

from inventory import Inventory
from payment import Payment
from shipping import Shipping

class OnlineStoreFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def purchase_product(self, product_id, quantity, address):
        if self.inventory.check_stock(product_id) >= quantity:
            self.inventory.update_stock(product_id, -quantity)
            self.payment.process_payment(quantity * self.get_product_price(product_id))
            self.shipping.ship_product(product_id, address)
            print("Purchase successful!")
        else:
            print("Product out of stock.")

    def get_product_price(self, product_id):
        # Query database or external API to get product price
        pass
```

### Step 3: Usage

To use the Facade class, simply create an instance of `OnlineStoreFacade` and call the `purchase_product` method.

```python
# main.py

from facade import OnlineStoreFacade

def main():
    facade = OnlineStoreFacade()
    facade.purchase_product(product_id=1, quantity=2, address="123 Main Street")

if __name__ == "__main__":
    main()
```

## Benefits of Using the Facade Pattern

- **Simplified interface:** The Facade pattern provides a simplified interface that hides the complexities of the subsystems. This makes it easier for clients to interact with the system.
- **Decoupling:** The Facade pattern promotes loose coupling between the client code and the subsystems. Changes in the subsystems don't impact the client code as long as the interface remains the same.
- **Encapsulation:** The Facade class encapsulates the details and dependencies of the subsystems, providing a clear separation of concerns.

## Conclusion

The Facade pattern is a powerful tool for simplifying the interaction with complex systems. By providing a unified interface, it reduces the complexity and improves the maintainability of the codebase. Consider using the Facade pattern when you have complex subsystems that can benefit from a simplified interface.