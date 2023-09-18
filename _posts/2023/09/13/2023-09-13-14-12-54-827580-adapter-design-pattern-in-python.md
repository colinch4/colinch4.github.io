---
layout: post
title: "Adapter design pattern in Python"
description: " "
date: 2023-09-13
tags: [AdapterPattern]
comments: true
share: true
---

The Adapter design pattern is a structural pattern that allows incompatible interfaces to work together by wrapping one interface with another, acting as a bridge between them. It is useful when we want to reuse an existing class but its interface does not match the requirements of our system.

## When to Use the Adapter Design Pattern?
- When you have an existing class that you want to reuse, but its interface is incompatible with the rest of the codebase.
- When you want to provide a unified interface to different classes with similar functionalities.

## Example Scenario

Let's say we have an existing `LegacyPrinter` class that prints data in a specific format using deprecated methods. However, our new codebase requires the use of a `ModernPrinter` class that has a different interface. We can use the Adapter design pattern to make the `LegacyPrinter` compatible with our new codebase without modifying its existing code.

## Implementation

We'll start by creating our `LegacyPrinter` class:

```python
class LegacyPrinter:
    def __init__(self, data):
        self._data = data

    def print_data(self):
        print("Printing data: {}".format(self._data))

    # Additional methods specific to the LegacyPrinter class
```

Next, we'll create our `ModernPrinter` class with the required interface:

```python
class ModernPrinter:
    def __init__(self, data):
        self.data = data

    def print(self):
        print("Printing: {}".format(self.data))

    # Additional methods specific to the ModernPrinter class
```

Now, we can create our adapter class, `LegacyPrinterAdapter`, which wraps the `LegacyPrinter` object and provides the required interface:

```python
class LegacyPrinterAdapter:
    def __init__(self, data):
        self.legacy_printer = LegacyPrinter(data)

    def print(self):
        self.legacy_printer.print_data()

    # Additional methods specific to the adapter class
```

Finally, we can use the adapter in our codebase to print data using the `ModernPrinter` interface with the help of the `LegacyPrinterAdapter`:

```python
data = "Hello, world!"
modern_printer = ModernPrinter(data)
modern_printer.print()

legacy_printer_data = "Hello from the past!"
legacy_printer_adapter = LegacyPrinterAdapter(legacy_printer_data)
legacy_printer_adapter.print()
```

## Final Thoughts

The Adapter design pattern is a powerful tool when it comes to integrating incompatible interfaces. It allows us to reuse existing code without modifying it, saving time and effort. By understanding this pattern, you can make your code more modular, flexible, and maintainable.

#Python #AdapterPattern