---
layout: post
title: "[Python] Garbage collection of variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, **garbage collection** is the process of automatically freeing up the memory occupied by objects that are no longer in use. This process helps manage memory efficiently and ensure that resources are not wasted.

Python uses a **reference counting** mechanism as its primary garbage collection technique. It keeps track of the number of references to an object and when the reference count drops to zero, the object is considered garbage and its memory is reclaimed.

Let's look at some examples to understand how garbage collection works in Python.

## Example 1: Reference Counting

```python
# Example 1: Reference Counting

# Initialize two variables
x = 10
y = x

# Print the reference count of x and y
print(sys.getrefcount(x))
print(sys.getrefcount(y))

# Delete the reference to x
del x

# Print the reference count of y again
print(sys.getrefcount(y))
```

In the above example, we create two variables `x` and `y` and assign `x` to `y`. The `sys.getrefcount()` function is used to get the reference count of an object. As long as the reference count of an object is greater than zero, it means there are references to the object.

After deleting the reference to `x` with `del x`, we can see that the reference count of `y` remains the same, indicating that it still has a reference.

## Example 2: Circular Reference

```python
# Example 2: Circular Reference

# Create two objects with circular reference
a = [1, 2]
b = [a, 3]
a.append(b)

# Delete the reference to a and b
del a
del b
```

In this example, we create two objects `a` and `b` with a circular reference. `a` contains a reference to `b`, and `b` contains a reference back to `a`. As a result, even if we delete the references to `a` and `b`, their reference counts will not reach zero because they still reference each other.

Python's garbage collector can handle situations like these and detects circular references to release the memory occupied by such objects.

## Example 3: `gc` Module

Python provides the `gc` module for managing garbage collection explicitly. It allows you to control when and how garbage collection is performed.

```python
# Example 3: gc Module

import gc

# Disable automatic garbage collection
gc.disable()

# Enable automatic garbage collection
gc.enable()

# Collect garbage manually
gc.collect()
```

In this example, we import the `gc` module and use the `disable()`, `enable()`, and `collect()` methods to control garbage collection. Disabling garbage collection can be useful in scenarios where you want to manage memory manually or improve performance by avoiding frequent garbage collection cycles.

## Conclusion

Garbage collection in Python helps manage memory efficiently and ensures that unused objects are automatically cleaned up. Python's reference counting mechanism, along with a garbage collector that handles circular references, makes the process seamless and transparent to developers. However, Python also provides the flexibility to control garbage collection manually using the `gc` module.