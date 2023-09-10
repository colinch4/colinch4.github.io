---
layout: post
title: "[Python] The id() function in Python and variable identity"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

The `id()` function returns the **identity** of an object, which is a unique integer representing that object's memory address. This means that if two variables have the same `id()`, they refer to the same object in memory. On the other hand, if two variables have different `id()` values, they refer to different objects, even if their values are the same.

Let's explore some examples to understand the use of the `id()` function and variable identity in Python:

### Example 1: Checking variable identity

```python
x = 10
y = 10

print(id(x))
print(id(y))
```

Output:

```
140709023282608
140709023282608
```

In the above example, we assign the same value `10` to two different variables `x` and `y`. When we print the `id()` of both variables, we see that they are the same. This means that `x` and `y` refer to the same object in memory.

### Example 2: Modifying variable identity

```python
x = [1, 2, 3]
y = x

print(id(x))
print(id(y))

y.append(4)

print(x)
print(y)
```

Output:

```
140709023735808
140709023735808
[1, 2, 3, 4]
[1, 2, 3, 4]
```

In this example, we assign a list `[1, 2, 3]` to variable `x`. Then, we assign `x` to `y`, which means `y` now refers to the same list object as `x`. When we print the `id()` of both variables, we see that they are the same.

Next, we append `4` to `y`. Since `x` and `y` refer to the same list object, both `x` and `y` are modified. This demonstrates that modifying `y` also affects `x`.

### Example 3: Variable identity in function calls

```python
def modify_list(numbers):
    print(id(numbers))
    numbers.append(5)
    print(numbers)

my_list = [1, 2, 3]
print(id(my_list))
modify_list(my_list)
print(my_list)
```

Output:

```
140709023282608
140709023282608
[1, 2, 3, 5]
[1, 2, 3, 5]
```

In this example, we define a function `modify_list()` that appends `5` to a given list. We initialize a list `my_list` and pass it to `modify_list()` as an argument. Inside the function, we print the `id()` of the `numbers` parameter, which matches the `id()` of `my_list` outside the function. When we modify `numbers`, both `numbers` and `my_list` are affected, demonstrating that they refer to the same object.

Understanding variable identity using the `id()` function can be valuable when working with mutable objects and function calls. It helps determine whether two variables refer to the same object or different objects.