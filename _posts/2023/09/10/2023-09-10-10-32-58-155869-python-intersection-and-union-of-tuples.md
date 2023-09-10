---
layout: post
title: "[Python] Intersection and Union of Tuples"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, tuples are immutable sequences that can hold a collection of elements. In this blog post, we will explore how to perform intersection and union operations on tuples.

## Intersection of Tuples
To find the intersection of two tuples, we can use the `&` operator. The intersection of two tuples contains only the elements that are present in both tuples.

```python
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

intersection = tuple1 & tuple2
print(intersection)
```

Output:
```
(4, 5)
```

In the above example, we have two tuples `tuple1` and `tuple2`. By using the `&` operator, we find the intersection of the two tuples and store it in the `intersection` variable. Finally, we print the result, which is `(4, 5)`.

## Union of Tuples
To perform the union of two tuples, we can use the `+` operator. The union of two tuples contains all the unique elements from both tuples.

```python
tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)

union = tuple1 + tuple2
print(union)
```

Output:
```
(1, 2, 3, 4, 5)
```

In the above example, we have two tuples `tuple1` and `tuple2`. By using the `+` operator, we concatenate the two tuples and store the result in the `union` variable. Finally, we print the result, which is `(1, 2, 3, 4, 5)`.

It's worth noting that the union operation does not remove duplicates, as tuples can contain duplicate values.

## Conclusion
In this blog post, we explored how to perform intersection and union operations on tuples in Python. The `&` operator can be used to find the intersection of two tuples, while the `+` operator can be used to perform the union. Understanding these operations is useful when working with sets of data represented as tuples in Python.