---
layout: post
title: "[Python] Tuple as Function Arguments and Return Values"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Let's explore how we can use tuples as function arguments and return values in Python.

## Using Tuple as Function Arguments

To pass a tuple as an argument to a function, you can simply include the tuple as a parameter when defining the function. Let's look at an example:

```python
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = (3, 5, 7, 9, 11)
result = calculate_average(my_numbers)
print("Average:", result)
```

In the above code, we define a function `calculate_average` that takes a single parameter `numbers`. We pass a tuple `my_numbers` as an argument to the function, and it calculates the average of the numbers in the tuple and returns it. Finally, we print the result.

## Using Tuple as Function Return Values

Similarly, we can also use tuples to return multiple values from a function. Consider the following example:

```python
def get_circle_properties(radius):
    circumference = 2 * 3.14 * radius
    area = 3.14 * (radius ** 2)
    return circumference, area

radius = 5
circle_properties = get_circle_properties(radius)
print("Circumference:", circle_properties[0])
print("Area:", circle_properties[1])
```

In this code snippet, we have a function `get_circle_properties` that takes the radius of a circle as its parameter. The function calculates the circumference and area of the circle using the provided radius and returns them as a tuple. We then capture the returned tuple in the `circle_properties` variable and print its elements individually (circumference and area).

Alternatively, we can also unpack the returned tuple directly into separate variables:

```python
circumference, area = get_circle_properties(radius)
print("Circumference:", circumference)
print("Area:", area)
```

Here, we assign the first element of the returned tuple to the `circumference` variable and the second element to the `area` variable.

Using tuples as function arguments and return values can be a convenient way to handle multiple values within a single object. It allows for more organized and concise code, especially when dealing with related data or calculations.

By leveraging the power of tuples, you can enhance the flexibility and readability of your Python code.