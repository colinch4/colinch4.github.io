---
layout: post
title: "[Python] Concatenating two lists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Using the `+` operator

The simplest way to concatenate two lists in Python is by using the `+` operator. This operator allows you to add two lists together, resulting in a new list that contains all the elements from both lists.

Here's an example:

```python
# two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# concatenating lists using the + operator
concatenated_list = list1 + list2

print(concatenated_list)
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

As you can see, the `+` operator concatenates the two lists `list1` and `list2` into a single list called `concatenated_list`.

## Using the `extend()` method

Another way to concatenate two lists in Python is by using the `extend()` method. This method appends the elements of one list to another list.

Here's an example:

```python
# two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# concatenating lists using the extend() method
list1.extend(list2)

print(list1)
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

In the above example, we use the `extend()` method to append the elements of `list2` to `list1`. The end result is a combined list with all the elements.

## Using the `*` operator

If you want to concatenate a list with itself multiple times, you can use the `*` operator. This operator allows you to repeat a list a specified number of times.

Here's an example:

```python
# a list
list1 = [1, 2, 3]

# concatenating a list with itself
concatenated_list = list1 * 3

print(concatenated_list)
```

Output:
```
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

In the example above, we use the `*` operator to concatenate `list1` with itself three times. The resulting list, `concatenated_list`, contains the repeated elements.

## Conclusion

Concatenating two lists in Python is a simple process that can be done using the `+` operator, `extend()` method, or `*` operator. Choose the method that suits your needs and apply it to combine the lists effectively.

I hope you found this blog post helpful in understanding how to concatenate lists in Python! Happy coding!