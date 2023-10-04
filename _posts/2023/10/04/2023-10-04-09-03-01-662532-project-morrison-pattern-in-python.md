---
layout: post
title: "Project Morrison pattern in Python"
description: " "
date: 2023-10-04
tags: [introduction, implementing]
comments: true
share: true
---

In this blog post, we will discuss how to implement the Morrison pattern in Python. The Morrison pattern is a beautiful and intricate geometric pattern that can be created using simple mathematical calculations. It is named after the mathematician Edward Morrison, who discovered the pattern.

## Table of Contents
- [Introduction to the Morrison Pattern](#introduction-to-the-morrison-pattern)
- [Implementing the Morrison Pattern in Python](#implementing-the-morrison-pattern-in-python)
- [Conclusion](#conclusion)

## Introduction to the Morrison Pattern

The Morrison pattern consists of a series of concentric circles intersected by radial lines. The number of circles and lines is determined by a set of mathematical formulas. The resulting pattern is symmetrical and visually stunning.

## Implementing the Morrison Pattern in Python

To implement the Morrison pattern in Python, we can use the `turtle` module, which provides a simple way to draw graphics. Follow the steps below to create the Morrison pattern:

1. Import the turtle module:

```python
import turtle
```

2. Create a turtle object and set the speed:

```python
pattern = turtle.Turtle()
pattern.speed(0)
```

3. Define the number of circles and lines using variables:

```python
num_circles = 10
num_lines = 36
```

4. Use a loop to draw the circles:

```python
for _ in range(num_circles):
    pattern.circle(100)
    pattern.up()
    pattern.left(90)
    pattern.forward(10)
    pattern.right(90)
    pattern.down()
```

5. Use another loop to draw the radial lines:

```python
for _ in range(num_lines):
    pattern.forward(200)
    pattern.backward(200)
    pattern.left(10)
```

6. Hide the turtle and display the final pattern:

```python
pattern.hideturtle()
turtle.done()
```

Here's the complete code snippet:

```python
import turtle

pattern = turtle.Turtle()
pattern.speed(0)

num_circles = 10
num_lines = 36

for _ in range(num_circles):
    pattern.circle(100)
    pattern.up()
    pattern.left(90)
    pattern.forward(10)
    pattern.right(90)
    pattern.down()

for _ in range(num_lines):
    pattern.forward(200)
    pattern.backward(200)
    pattern.left(10)

pattern.hideturtle()
turtle.done()
```

## Conclusion

In this blog post, we explored the Morrison pattern and implemented it in Python using the turtle module. By following the steps outlined above, you can create your own stunning Morrison pattern. This project is a great way to learn and practice programming concepts while creating beautiful visual designs. Have fun experimenting with different variations of the Morrison pattern and see what you can create! #Python #MorrisonPattern