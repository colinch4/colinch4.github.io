---
layout: post
title: "[Python] Tuple Indexing and Negative Indexing"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, a **tuple** is an immutable sequence, just like a list or a string. Each item in a tuple is called an element, and it is accessed using an index. This blog post will explain how to access elements in a tuple using **indexing** and **negative indexing**.

### Accessing Elements using Indexing

To access an element in a tuple, you can use square brackets `[]` with the index of the desired element. The index starts from 0 for the first element and increments by 1 for each subsequent element.

Let's consider a tuple `fruits` with the following elements:

```python
fruits = ('apple', 'banana', 'cherry', 'durian', 'elderberry')
```

To access the first element (apple), you can use:

```python
first_fruit = fruits[0]
print(first_fruit)  # Output: apple
```

Similarly, you can access other elements by changing the index:

```python
second_fruit = fruits[1]  # banana
third_fruit = fruits[2]  # cherry
```

### Negative Indexing in Tuples

Python allows negative indexing, which means you can access elements from the end of the tuple by using negative numbers. The last element of a tuple has an index of -1, the second-to-last element has an index of -2, and so on.

Let's consider the same `fruits` tuple as before.

```python
last_fruit = fruits[-1]
print(last_fruit)  # Output: elderberry
```

Accessing the second-to-last element using negative indexing:

```python
second_to_last_fruit = fruits[-2]
print(second_to_last_fruit)  # Output: durian
```

Using negative indexing, you can easily access elements from the end of the tuple without knowing its length. This can be especially useful when dealing with large tuples.

### Conclusion

In this blog post, we learned how to access elements in a tuple using indexing and negative indexing in Python. Indexing starts from 0 for the first element, and negative indexing allows accessing elements from the end of the tuple. Understanding tuple indexing is crucial for working with tuples effectively in Python programming.