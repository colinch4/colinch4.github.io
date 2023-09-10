---
layout: post
title: "[Python] Local variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Local variables are created when their assignment statement is executed and are destroyed when the block of code they are defined in is exited. This means that local variables cannot be accessed or modified from outside the block of code in which they are defined.

To better understand local variables, let's look at some examples:

```python
def calculate_sum(a, b):
    total = a + b
    print("The sum is:", total)

calculate_sum(5, 7)
# Output: The sum is: 12

print(total)  # Raises NameError: name 'total' is not defined
```

In the above example, the `total` variable is defined within the `calculate_sum` function. This variable can only be accessed inside the function and is not accessible outside of it. Trying to access the `total` variable outside of the function will result in a `NameError` since it is not defined in the global scope.

```python
def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    return average

numbers = [2, 4, 6, 8, 10]
print(calculate_average(numbers))
# Output: 6.0

print(average)  # Raises NameError: name 'average' is not defined
```

In this example, the `average` variable is defined within the `calculate_average` function. It calculates the average of a list of numbers and returns the result. Again, trying to access the `average` variable outside of the function will throw a `NameError` since it is a local variable.

Local variables are useful for encapsulating data within a specific block of code, allowing for better organization and code readability. It also helps in preventing accidental modifications to variables from other parts of the code. However, it's important to note that attempting to access local variables outside their scope will result in an error.