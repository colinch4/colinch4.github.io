---
layout: post
title: "Composite design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The **Composite Design Pattern** is a structural design pattern that allows you to treat individual objects and compositions of objects in the same way. It allows you to create complex hierarchical structures by composing objects into tree-like structures.

## How does the Composite Design Pattern work?

The basic idea behind the Composite Design Pattern is to create a class hierarchy where both individual objects (leaf nodes) and composite objects (nodes that contain leaf nodes and/or other composite nodes) implement the same interface.

The key components of the Composite Design Pattern are as follows:

1. **Component**: This is the common interface implemented by all objects in the composite structure. It declares the operations that can be performed on both individual objects and composite objects.
2. **Leaf**: This represents the individual objects in the composite structure. It does not have any child objects.
3. **Composite**: This represents the composite objects in the composite structure. It can contain both leaf objects and other composite objects.

## Example Implementation in Python

Let's imagine we are building a file system hierarchy. We can use the Composite Design Pattern to represent directories and files as a composite structure. Here's an example implementation in Python:

```python
# Component
class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        raise NotImplementedError()

# Leaf
class File(FileSystemComponent):
    def show_info(self):
        print(f"File: {self.name}")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def show_info(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.show_info()

# Usage
root = Directory("Root")
root_file1 = File("file1.txt")
root_file2 = File("file2.txt")
subdirectory = Directory("Subdirectory")
subdirectory_file = File("subfile.txt")

root.add(root_file1)
root.add(root_file2)
root.add(subdirectory)
subdirectory.add(subdirectory_file)

root.show_info()
```

In this implementation, `FileSystemComponent` serves as the **Component** interface, `File` represents the **Leaf** objects, and `Directory` represents the **Composite** objects. We can add leaf objects and/or composite objects to the directory, and when we call `show_info()` on the root directory, it recursively prints information about all the objects in the composite structure.

## Advantages of using the Composite Design Pattern

- It allows you to treat individual objects and compositions of objects uniformly, simplifying the client code.
- It provides a flexible way to add new types of objects to the composite structure without affecting the existing code.
- It promotes code reusability and maintainability by separating the common operations from the specific ones.

## Final Thoughts

The Composite Design Pattern is a powerful pattern that allows you to create complex hierarchical structures by combining objects into a tree-like structure. By providing a common interface, it enables you to treat individual objects and composite objects uniformly. This pattern can be particularly useful in scenarios where you need to work with tree-like structures that can vary in complexity.