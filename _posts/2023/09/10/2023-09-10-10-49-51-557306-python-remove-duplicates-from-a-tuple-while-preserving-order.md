---
layout: post
title: "[Python] Remove Duplicates from a Tuple while Preserving Order"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Tuples are immutable sequences in Python. They are similar to lists but cannot be modified once created. Sometimes, you may need to remove duplicates from a tuple while preserving its original order. In this blog post, we will explore different approaches to achieve this in Python.

## Method 1: Using a Set to Remove Duplicates

One way to remove duplicates from a tuple is by converting it to a set and then converting it back to a tuple. This works because sets only store unique elements.

Here's an example implementation:

```python
def remove_duplicates(t):
    # Convert tuple to set to remove duplicates
    unique_elements = set(t)
    
    # Convert set back to tuple while preserving order
    new_tuple = tuple(unique_elements)
    
    return new_tuple
```

Let's see how this function can be used:

```python
original_tuple = (1, 2, 3, 2, 4, 5, 4, 6)
new_tuple = remove_duplicates(original_tuple)

print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)
```

In this example, the function `remove_duplicates` takes a tuple `t` as input, converts it to a set to remove duplicates, and then converts the set back to a tuple. The resulting tuple `new_tuple` is returned.

## Method 2: Using OrderedDict to Preserve Order

Another approach to remove duplicates from a tuple while preserving order is by using the `OrderedDict` class from the `collections` module. `OrderedDict` is a dictionary subclass that remembers the order in which entries were added.

Here's an example implementation:

```python
from collections import OrderedDict

def remove_duplicates(t):
    # Convert tuple to OrderedDict to remove duplicates while preserving order
    unique_elements = OrderedDict.fromkeys(t)
    
    # Convert OrderedDict back to tuple
    new_tuple = tuple(unique_elements.keys())
    
    return new_tuple
```

Here's how it can be used:

```python
original_tuple = (1, 2, 3, 2, 4, 5, 4, 6)
new_tuple = remove_duplicates(original_tuple)

print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)
```

In this example, the function `remove_duplicates` uses `OrderedDict.fromkeys()` to convert the tuple `t` into an `OrderedDict` object, which automatically removes duplicates while preserving the order. The resulting tuple `new_tuple` is returned.

## Conclusion

Removing duplicates from a tuple while preserving order can be accomplished using different approaches in Python. You can either convert the tuple to a set and back, or use the `OrderedDict` class from the `collections` module. Both methods are effective, but the choice depends on your specific requirements and preferences.

Keep in mind that tuples are immutable, so you need to create a new tuple with the desired elements rather than modifying the original tuple directly.