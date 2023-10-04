---
layout: post
title: "Iterator pattern in Python"
description: " "
date: 2023-10-04
tags: [designpatterns]
comments: true
share: true
---

The Iterator Pattern is a behavioral design pattern that allows you to access the elements of a collection sequentially without exposing the underlying implementation of the collection. 

## When to use the Iterator Pattern?

You can use the Iterator Pattern in Python when:

- You have a collection of objects and you want to provide a way to iterate over them without exposing the inner workings of the collection.
- You want to provide a common interface for iterating over different types of collections.

## Implementing the Iterator Pattern

To implement the Iterator Pattern in Python, you typically need two classes:

1. **Iterable**: This is the interface or class that defines the method for creating an iterator.
2. **Iterator**: This class implements the iterator interface and provides the methods for traversing the collection.

## Example Code

```python
class Numbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return NumberIterator(self.start, self.end)


class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result


numbers = Numbers(1, 5)
for num in numbers:
    print(num)
```

In the above example, we have a `Numbers` class that represents a collection of numbers. The `Numbers` class implements the `__iter__` method, which returns an instance of the `NumberIterator` class.

The `NumberIterator` class implements the `__iter__` and `__next__` methods. The `__next__` method provides the logic for iterating over the collection and returns the next element in the sequence. When there are no more elements to iterate over, it raises the `StopIteration` exception.

Finally, we create an instance of the `Numbers` class and iterate over it using a `for` loop. The `for` loop internally calls the `__iter__` method and `__next__` method on the iterator to iterate over the collection.

This is a simple example of implementing the Iterator Pattern in Python. You can extend this pattern to create more complex iterators for various types of collections.

Remember to import the necessary modules and subclasses when working with the Iterator Pattern in your own projects.


#python #designpatterns