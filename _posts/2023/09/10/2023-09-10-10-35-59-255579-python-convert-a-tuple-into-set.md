---
layout: post
title: "[Python] Convert a Tuple into Set"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Converting a Tuple into a Set using the set() function

The easiest way to convert a tuple into a set is by using the built-in `set()` function. The `set()` function takes an iterable as an argument and returns a new set containing all the elements of the iterable.

Here's an example:

```python
# Create a tuple
my_tuple = (1, 2, 3, 4, 4, 5)

# Convert tuple to set
my_set = set(my_tuple)

print(my_set)
```

Output:
```
{1, 2, 3, 4, 5}
```

In the above example, we define a tuple `my_tuple` containing some elements, including duplicates. We then use the `set()` function to convert the tuple into a set. The resulting set `my_set` contains all the unique elements from the tuple.

## Converting a Tuple into a Set using the {*tuple} syntax (Python 3.5+)

If you are using Python 3.5 or above, you can also use the `{*tuple}` syntax to convert a tuple into a set efficiently. This syntax is known as unpacking or splat operator.

Here's an example:

```python
# Create a tuple
my_tuple = (1, 2, 3, 4, 4, 5)

# Convert tuple to set using {*tuple} syntax
my_set = {*my_tuple}

print(my_set)
```

Output:
```
{1, 2, 3, 4, 5}
```

In the above example, we define a tuple `my_tuple` containing some elements with duplicates. We then use the `{*my_tuple}` syntax to convert the tuple into a set. The resulting set `my_set` contains all the unique elements from the tuple.

## Conclusion

Converting a tuple into a set in Python is a straightforward task. You can use the `set()` function or the `{*tuple}` syntax (Python 3.5+). This conversion can be useful when you want to perform set operations or remove duplicates from a collection of elements. Remember that a set is unordered and does not allow duplicates, so any duplicate elements in the tuple will be automatically removed when converting it into a set.

I hope this article was helpful in understanding how to convert a tuple into a set in Python. Happy coding!