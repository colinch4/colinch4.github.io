---
layout: post
title: "[Python] Assigning multiple values to variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Assigning multiple values to variables is a common task in Python. It allows you to assign multiple values to multiple variables in a single statement, simplifying your code and making it more readable.

## Multiple assignment syntax

The syntax for assigning multiple values to variables in Python is straightforward. You can use either parentheses or square brackets to enclose a comma-separated list of values, and then assign them to variables using multiple assignment.

Here is the general syntax:

```python
variable1, variable2, variable3 = value1, value2, value3
```

The number of variables on the left-hand side should match the number of values on the right-hand side. If they don't match, you'll get a `ValueError`.
    
## Assigning multiple values example

Let's look at some examples to understand how to assign multiple values to variables in Python.

### Example 1: Assigning multiple values to multiple variables

```python
first_name, last_name, age = "John", "Doe", 30
print(first_name)  # Output: John
print(last_name)  # Output: Doe
print(age)  # Output: 30
```

In this example, we assign the values "John", "Doe", and 30 to the variables `first_name`, `last_name`, and `age` respectively. When we print the values, we will get the expected output.

### Example 2: Assigning multiple values to a single variable

```python
numbers = 1, 2, 3, 4, 5
print(numbers)  # Output: (1, 2, 3, 4, 5)
```

In this example, we assign multiple values `(1, 2, 3, 4, 5)` to the variable `numbers`. The values are enclosed in parentheses, but you can also use square brackets if you prefer. When we print the `numbers` variable, we will get the output `(1, 2, 3, 4, 5)`.

### Example 3: Assigning multiple values using unpacking

```python
fruits = ["apple", "banana", "orange"]
first_fruit, second_fruit, third_fruit = fruits
print(first_fruit)  # Output: apple
print(second_fruit)  # Output: banana
print(third_fruit)  # Output: orange
```

In this example, we assign the values of the list `["apple", "banana", "orange"]` to the variables `first_fruit`, `second_fruit`, and `third_fruit` using unpacking. Each element of the list is assigned to the corresponding variable. When we print the variables, we will get the expected output.

## Conclusion

Assigning multiple values to variables in Python is a powerful feature that allows you to simplify your code and make it more efficient. By using multiple assignment, you can assign multiple values to multiple variables in a single statement, improving readability and reducing the number of lines of code. This is a crucial technique to master when working with Python.