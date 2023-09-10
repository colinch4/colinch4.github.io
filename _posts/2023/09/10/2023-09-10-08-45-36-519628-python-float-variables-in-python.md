---
layout: post
title: "[Python] Float variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Declaring Float Variables

To declare a float variable in Python, simply assign a decimal or fractional value to it. Here's an example:

```python
# Declare float variables
pi = 3.14159
rate = 4.5
```

In the above example, we have declared two float variables: `pi` and `rate`. `pi` is assigned the value 3.14159, and `rate` is assigned the value 4.5.

## Working with Float Variables

Float variables in Python can be used for various mathematical operations. Let's explore some common operations:

### Addition and Subtraction

```python
# Adding float variables
total = 4.5 + 2.3

# Subtracting float variables
difference = 6.7 - 3.2
```

In the above examples, we add `2.3` to `4.5` and store the result in the variable `total`. Similarly, we subtract `3.2` from `6.7` and store the result in the variable `difference`.

### Multiplication and Division

```python
# Multiply float variables
product = 2.5 * 3.1

# Divide float variables
quotient = 10.2 / 2.0
```

In the above examples, we multiply `2.5` by `3.1` and store the result in the variable `product`. Similarly, we divide `10.2` by `2.0` and store the result in the variable `quotient`.

### Exponentiation and Floor Division

```python
# Exponentiation
power = 2.0 ** 3.0

# Floor division
result = 7.0 // 3.0
```

In the above examples, we calculate `2.0` raised to the power of `3.0` and store the result in the variable `power`. Similarly, we perform floor division on `7.0` and `3.0` and store the result in the variable `result`.

## Converting Float to Integer

Sometimes, you may need to convert a float variable to an integer. You can achieve this using the `int()` function in Python:

```python
float_number = 3.14
int_number = int(float_number)
```

In the above example, we convert the float variable `3.14` to an integer using the `int()` function.

## Conclusion

Float variables are essential when working with fractional numbers in Python. They allow you to perform various mathematical operations and provide flexibility in handling decimal values. By understanding how to declare and use float variables, you can effectively work with fractional values in your Python programs.