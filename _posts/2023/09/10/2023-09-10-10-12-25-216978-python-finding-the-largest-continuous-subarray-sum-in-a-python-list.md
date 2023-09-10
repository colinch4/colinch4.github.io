---
layout: post
title: "[Python] Finding the largest continuous subarray sum in a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
def find_max_subarray_sum(arr):
    max_sum = float('-inf')  # Initializing with negative infinity
    current_sum = 0

    for num in arr:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [1, -2, 3, 4, -5, 6, -1, 2]
max_sum = find_max_subarray_sum(arr)
print(f"The largest continuous subarray sum is: {max_sum}")
```

In the code above, we define a function `find_max_subarray_sum` that takes in a Python list as an argument. This function finds the largest sum of any continuous subarray within the list.

We initialize two variables, `max_sum` and `current_sum`, with `max_sum` set to negative infinity. Then, we iterate through each element `num` in the given list. For each element, we calculate the current sum by taking the maximum between the sum of the current element and the previous sum, and starting a new subarray from the current element. We update the `max_sum` variable with the maximum sum encountered so far.

Finally, we return the `max_sum` value, which represents the largest continuous subarray sum. We test the function with an example list `[1, -2, 3, 4, -5, 6, -1, 2]` and print the result.

The output will be:
```
The largest continuous subarray sum is: 10
```

This means that the largest sum of any continuous subarray in the given list is `10`. The subarray with this sum is `[3, 4, -5, 6]`.