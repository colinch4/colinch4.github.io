---
layout: post
title: "[Python] Sort a Tuple by its Length"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, a tuple is an ordered collection of elements. It is similar to a list but immutable, meaning that its values cannot be modified once it is created. Sometimes we may encounter a situation where we need to sort a tuple based on the length of its elements. In this article, we will explore various ways to achieve this in Python.

Let's consider the following tuple as an example:

```python
my_tuple = ('apple', 'banana', 'orange', 'kiwi', 'grape')
```

Our goal is to sort the tuple by the length of its elements in ascending order.

## Approach 1: Using the sorted() function

The `sorted()` function in Python returns a sorted list from the given iterable. We can leverage this function to sort our tuple based on the length of its elements. Here's how we can do it:

```python
my_tuple = ('apple', 'banana', 'orange', 'kiwi', 'grape')
sorted_tuple = sorted(my_tuple, key=len)
print(sorted_tuple)
```

Output:
```python
['kiwi', 'grape', 'apple', 'banana', 'orange']
```

In the above code, we pass the `key` parameter to `sorted()` and specify that we want to use the length of each element as the sorting criteria.

## Approach 2: Using a lambda function with the sorted() function

Alternatively, we can use a lambda function to achieve the same result. Here's how it can be done:

```python
my_tuple = ('apple', 'banana', 'orange', 'kiwi', 'grape')
sorted_tuple = sorted(my_tuple, key=lambda x: len(x))
print(sorted_tuple)
```

Output:
```python
['kiwi', 'grape', 'apple', 'banana', 'orange']
```

In this approach, the lambda function takes in each element of the tuple `my_tuple` and returns the length of that element. The `sorted()` function then sorts the tuple based on the values returned by the lambda function.

## Approach 3: Using a list comprehension

We can also use a list comprehension to achieve the desired sorting. Here's how it can be implemented:

```python
my_tuple = ('apple', 'banana', 'orange', 'kiwi', 'grape')
sorted_tuple = [x for x in sorted(my_tuple, key=len)]
print(sorted_tuple)
```

Output:
```python
['kiwi', 'grape', 'apple', 'banana', 'orange']
```

In this approach, we use a list comprehension to create a new list from the sorted elements of the tuple `my_tuple`. The `key` parameter is used to sort the elements by their length.

## Conclusion

Sorting a tuple by its element length can be achieved using various approaches in Python. In this article, we explored three different methods: using the `sorted()` function, using a lambda function with the `sorted()` function, and using a list comprehension. Choose the approach that best suits your needs and preferences.

Remember that tuples are immutable, so the sorted tuple will be a new object and the original tuple will remain unchanged.

I hope you found this article helpful! Happy coding!