---
layout: post
title: "[Python] Counting the number of even and odd numbers in a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will explore how to count the number of even and odd numbers in a Python list. We will write a Python function to perform this task efficiently.

## Problem Statement

Given a list of integers, we need to count the number of even and odd numbers present in the list.

## Approach

We will iterate over the list and check each number against the modulus 2. If the result is 0, the number is even, and if the result is 1, the number is odd. We will maintain counters for even and odd numbers and increment them accordingly.

Let's take a look at the code:

```python
def count_even_odd(numbers_list):
    even_count = 0
    odd_count = 0

    for num in numbers_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count
```

The `count_even_odd` function takes in a list of numbers as input. It initializes the counters `even_count` and `odd_count` to 0. Then, it iterates over each number in the list and checks if it is even or odd. If it is even, it increments `even_count`, otherwise it increments `odd_count`. Finally, it returns the values of both counters.

## Usage

To use the `count_even_odd` function, you can simply call it with a list of numbers as an argument. Here's an example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(numbers)

print(f"The list contains {even_count} even numbers and {odd_count} odd numbers.")
```

Output:
```
The list contains 5 even numbers and 5 odd numbers.
```

## Conclusion

In this blog post, we have seen how to count the number of even and odd numbers in a Python list. By using the modulus operator and maintaining separate counters, we can efficiently determine the count of even and odd numbers. This can be useful in various applications where analyzing the distribution of numbers is required.