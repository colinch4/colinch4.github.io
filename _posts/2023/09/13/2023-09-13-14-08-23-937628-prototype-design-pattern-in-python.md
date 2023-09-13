---
layout: post
title: "Prototype design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The Prototype design pattern is a creational design pattern that allows us to create new objects based on existing objects. It avoids the need to create subclasses of an object when we want to create variations of it. Instead, it provides a way to clone an existing object and modify it as required.

## When to use the Prototype design pattern?

The Prototype design pattern is useful in scenarios where:

1. The creation of a new object is expensive or complex.
2. Object creation is required at runtime, based on varying specifications.
3. A class hierarchy is difficult to maintain or adds unnecessary complexity.

## Implementation of Prototype design pattern

To implement the Prototype design pattern in Python, we need to define a base prototype class that contains a method for cloning itself. This method will be overridden in the concrete classes to provide a customized cloning mechanism.

Let's consider an example of a `Product` class that represents a generic product. We'll create a prototype class `ProductPrototype` that implements the cloning mechanism. Lastly, we'll create concrete product classes `Book` and `Pen`, which are cloned from the `ProductPrototype`.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def clone(self):
        pass

class ProductPrototype(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def clone(self):
        return ProductPrototype(self.name, self.price)

class Book(ProductPrototype):
    def __init__(self, name, price, genre):
        super().__init__(name, price)
        self.genre = genre
    
    def clone(self):
        return Book(self.name, self.price, self.genre)
        
class Pen(ProductPrototype):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
    
    def clone(self):
        return Pen(self.name, self.price, self.color)
```

In the above code, the `Product` class serves as the base prototype class. The `ProductPrototype` class is a concrete prototype class that implements the cloning mechanism by overriding the `clone` method. It creates a new object of the same class, copying the attributes from the original object. The `Book` and `Pen` classes inherit from the `ProductPrototype` and provide their own implementations of the `clone` method.

## Client code

Now, let's create a `Client` class that demonstrates the usage of the Prototype design pattern.

```python
class Client:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def clone_products(self):
        cloned_products = []
        for product in self.products:
            cloned_products.append(product.clone())

        return cloned_products


# Usage
client = Client()
book = Book("Harry Potter", 10.99, "Fantasy")
pen = Pen("Gel Pen", 2.99, "Red")

client.add_product(book)
client.add_product(pen)

cloned_products = client.clone_products()

# Verify clones
for cloned_product in cloned_products:
    print(cloned_product.name)
```

In the above code, the `Client` class maintains a list of `Product` objects and provides methods to add products and clone them. The `clone_products` method loops through the list of products and calls the `clone` method on each product, creating a new cloned product. Finally, we can verify the cloned products by printing their names.

## Benefits of using the Prototype design pattern

- Reduced subclassing: The Prototype pattern allows us to avoid creating subclasses for every possible variation of an object, reducing the number of classes in the system.
- Flexibility: It provides a flexible way to create new objects at runtime, based on varying specifications. It allows for easy configuration of complex objects.
- Performance improvement: The Prototype pattern avoids expensive object creation operations by cloning existing objects.

## Conclusion

The Prototype design pattern in Python provides a mechanism to create new objects by cloning existing ones. It helps in reducing subclassing, improves flexibility, and enhances performance by avoiding expensive object creation operations. By using this pattern, we can achieve better manageability and maintainability in our codebase.