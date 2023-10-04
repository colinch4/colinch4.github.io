---
layout: post
title: "Adapter pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible classes, making them compatible and enabling them to collaborate.

## How it works

The Adapter pattern involves creating an adapter class that implements the target interface and wraps an instance of an incompatible class. It then translates the calls from the target interface into calls to the wrapped object's interface.

## Example

Let's say we have a `LegacyPrinter` class that provides a method called `print`, which takes a string as input and prints it. We also have a `ModernPrinter` class that has a method called `print_text`, which takes a string and prints it.

We want to use the `ModernPrinter` class in our existing codebase, but it expects a different method name. We can use the Adapter pattern to create an adapter class that wraps an instance of the `ModernPrinter` class and provides a `print` method that the existing codebase expects.

```python
class LegacyPrinter:
    def print(self, text):
        print(f"Legacy Printer: {text}")


class ModernPrinter:
    def print_text(self, text):
        print(f"Modern Printer: {text}")


class PrinterAdapter:
    def __init__(self, printer):
        self.printer = printer

    def print(self, text):
        self.printer.print_text(text)


legacy_printer = LegacyPrinter()
modern_printer = ModernPrinter()

adapter = PrinterAdapter(modern_printer)

adapter.print("Hello World")
```

In the example above, the `PrinterAdapter` class wraps an instance of the `ModernPrinter` class and provides a `print` method. This allows us to use the `ModernPrinter` in our existing codebase by creating an adapter between the two incompatible interfaces.

## Benefits of using the Adapter pattern

1. **Code reusability**: The adapter allows us to reuse existing code that is incompatible with the desired interface.
2. **Simplifies integration**: It simplifies the integration of new components into existing codebases by providing an interface to communicate between incompatible classes.
3. **Maintainability**: The adapter pattern improves the maintainability of code by decoupling the client code from the incompatible classes.

## Conclusion

The Adapter pattern is a useful design pattern to handle the incompatibility between different interfaces. It provides a way to make incompatible classes work together, enabling code reusability, simplifying integration, and improving maintainability.

By leveraging the adapter pattern, developers can easily incorporate new functionalities or components into existing codebases without needing to modify the existing code.