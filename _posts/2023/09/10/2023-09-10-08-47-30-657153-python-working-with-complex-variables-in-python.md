---
layout: post
title: "[Python] Working with complex variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Complex numbers are an important concept in mathematics, and Python provides a built-in data type to work with complex numbers. In this blog post, we will explore how to work with complex variables in Python and perform various operations on them.

## Creating Complex Variables

To create a complex variable in Python, we can use the built-in `complex()` function or by directly assigning a value to it. Let's look at some examples:

```python
# Using complex()
z1 = complex(3, 4)
print(z1)  # Output: (3+4j)

# Directly assigning a value
z2 = 2 + 5j
print(z2)  # Output: (2+5j)
```

In both cases, we have created complex variables `z1` and `z2` which represent the complex numbers 3+4j and 2+5j respectively.

## Accessing Real and Imaginary Parts

To access the real and imaginary parts of a complex number, we can use the `real` and `imag` attributes. Let's see an example:

```python
z = complex(2, 3)
print(z.real)  # Output: 2.0
print(z.imag)  # Output: 3.0
```

Here, the `real` attribute returns the real part of `z` (which is 2.0) and the `imag` attribute returns the imaginary part (which is 3.0).

## Performing Operations on Complex Variables

Python provides various mathematical operations that can be performed on complex variables. Let's explore some of these operations:

### Addition and Subtraction

We can add and subtract complex variables using the `+` and `-` operators. Here's an example:

```python
z1 = complex(2, 3)
z2 = complex(4, 1)

result = z1 + z2
print(result)  # Output: (6+4j)

result = z1 - z2
print(result)  # Output: (-2+2j)
```

In this example, we have added `z1` and `z2` to get the result `(6+4j)` and subtracted `z2` from `z1` to get the result `(-2+2j)`.

### Multiplication and Division

We can multiply and divide complex variables using the `*` and `/` operators. Let's see an example:

```python
z1 = complex(2, 3)
z2 = complex(4, 1)

result = z1 * z2
print(result)  # Output: (5+14j)

result = z1 / z2
print(result)  # Output: (0.7647058823529412+0.4117647058823529j)
```

In this example, we have multiplied `z1` and `z2` to get the result `(5+14j)` and divided `z1` by `z2` to get the result `(0.7647058823529412+0.4117647058823529j)`.

### Conjugate

The conjugate of a complex number can be obtained using the `conjugate()` function. Let's see an example:

```python
z = complex(2, 3)
conjugate = z.conjugate()

print(conjugate)  # Output: (2-3j)
```

In this example, we have obtained the conjugate of `z` which is `(2-3j)`.

## Conclusion

In this blog post, we explored how to work with complex variables in Python. We learned how to create complex variables, access their real and imaginary parts, and perform various operations on them. Complex variables are useful in many mathematical calculations and Python provides a convenient way to work with them.