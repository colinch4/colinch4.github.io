---
layout: post
title: "[Python] Union of multiple lists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Lists are a fundamental data structure in Python, and often we may need to combine or merge multiple lists together to create a union. In this blog post, we will explore different approaches to perform the union operation on multiple lists in Python.

## Method 1: Using the `+` Operator

The simplest way to merge lists in Python is by using the `+` operator. This operator concatenates two or more lists together, resulting in a new list that contains all the elements from the original lists.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

union_list = list1 + list2 + list3
print(union_list)
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Using the `+` operator is straightforward and works well for merging a small number of lists. However, it can become cumbersome when dealing with a large number of lists.

## Method 2: Using the `extend()` Method

Another way to merge lists is by using the `extend()` method. The `extend()` method allows us to add all the elements of one list to another list.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

union_list = list1.copy()
union_list.extend(list2)
union_list.extend(list3)
print(union_list)
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

By using the `extend()` method, we start with an initial list and then add each subsequent list using the `extend()` method. This approach is more readable and scalable compared to using the `+` operator when merging a large number of lists.

## Method 3: Using the `set()` Function

If preserving the order of elements is not a requirement, we can use the `set()` function to perform the union operation on multiple lists. The `set()` function eliminates duplicate elements and returns a new set containing unique values.

```python
list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [5, 6, 7]

union_list = list(set(list1 + list2 + list3))
print(union_list)
```

Output:
```
[1, 2, 3, 4, 5, 6, 7]
```

By converting the combined list into a set and back into a list again, we effectively eliminate duplicate values from the result. However, note that the order of elements may change as sets are unordered.

## Conclusion

Merging or performing the union operation on multiple lists is a common task in Python. Depending on the specific requirements and constraints, we can choose different approaches. The `+` operator and the `extend()` method work well for small numbers of lists, whereas the `set()` function is useful for removing duplicates. Choose the method that best suits your needs and enjoy the flexibility of combining multiple lists efficiently in Python.

I hope you found this blog post helpful! If you have any questions or suggestions, please feel free to leave a comment below.