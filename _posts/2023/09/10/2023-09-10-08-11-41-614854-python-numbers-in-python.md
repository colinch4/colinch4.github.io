---
layout: post
title: "[Python] Numbers in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Integer Numbers

Integers are whole numbers without any fractional part. In Python, you can declare an integer by assigning a numerical value to a variable. Here's an example:

```python
x = 10
```

In the above code snippet, we have assigned the value 10 to the variable `x`. Python automatically recognizes `x` as an integer data type.

You can perform various arithmetic operations with integers, such as addition, subtraction, multiplication, and division. Here are a few examples:

```python
a = 5
b = 3

# Addition
c = a + b  # Output: 8

# Subtraction
d = a - b  # Output: 2

# Multiplication
e = a * b  # Output: 15

# Division
f = a / b  # Output: 1.6666666666666667 (floating-point division)
g = a // b # Output: 1 (integer division)
```

## Floating-Point Numbers

Floating-point numbers, also known as floats, are numbers that have both an integer and fractional part. They are declared by using a decimal point or by using scientific notation. Here's an example:

```python
y = 3.14
```

In the above code snippet, we have assigned the value 3.14 to the variable `y`. Python recognizes `y` as a floating-point number.

Like integers, you can perform arithmetic operations with floating-point numbers. Here's an example:

```python
p = 2.5
q = 1.2

# Addition
r = p + q  # Output: 3.7

# Subtraction
s = p - q  # Output: 1.3

# Multiplication
t = p * q  # Output: 3.0

# Division
u = p / q  # Output: 2.0833333333333335
```

## Complex Numbers

Complex numbers consist of real and imaginary parts. They are declared by using the `j` or `J` suffix to denote the imaginary part. Here's an example:

```python
z = 2 + 3j
```

In the above code snippet, we have assigned the value `2 + 3j` to the variable `z`. Python recognizes `z` as a complex number.

To perform operations with complex numbers, Python provides built-in functions and operators. Here are a few examples:

```python
m = 1 + 2j
n = 3 + 4j

# Addition
o = m + n  # Output: (4+6j)

# Subtraction
p = m - n  # Output: (-2-2j)

# Multiplication
q = m * n  # Output: (-5+10j)

# Division
r = m / n  # Output: (0.44+0.08j)
```

In addition to the basic arithmetic operations, Python also provides various mathematical functions and modules for more advanced numerical computations.

Understanding the different types of numbers in Python is essential for any developer working with mathematical calculations and data manipulation. Whether you're working with integers, floating-point numbers, or complex numbers, Python offers a wide range of tools and capabilities to handle them effectively.