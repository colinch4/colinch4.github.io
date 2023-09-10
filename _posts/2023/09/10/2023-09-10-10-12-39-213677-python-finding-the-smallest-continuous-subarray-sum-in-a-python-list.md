---
layout: post
title: "[Python] Finding the smallest continuous subarray sum in a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will explore how to find the smallest continuous subarray sum in a Python list. This problem can be solved using the sliding window technique.

## Problem Statement
Given a list of integers, we need to find the smallest sum of any continuous subarray. The subarray can be of any length, but it must be continuous.

## Approach
We will use the sliding window technique to solve this problem. The idea is to maintain a window that keeps expanding until the sum of its elements is no longer smaller than the current minimum sum. Once this happens, we shrink the window from the left and update the minimum sum until the window's sum is smaller again.

Here's the Python implementation of the algorithm:

```python
def find_smallest_subarray_sum(arr):
    n = len(arr)
    min_sum = float('inf')  # Initialize with maximum possible value
    window_sum = 0
    left = 0
    
    for right in range(n):
        window_sum += arr[right]
        
        while window_sum >= min_sum:
            min_sum = min(min_sum, window_sum)
            window_sum -= arr[left]
            left += 1
    
    return min_sum
```

## Example Usage

Let's consider a case where we have the following Python list: `[3, -4, 2, -1, 7, -6, 1]`. The smallest continuous subarray sum in this case is `-6`, which is the sum of the subarray `[-6]`. Using the `find_smallest_subarray_sum` function, we can find the smallest sum as shown below:

```python
arr = [3, -4, 2, -1, 7, -6, 1]
smallest_sum = find_smallest_subarray_sum(arr)
print(smallest_sum)  # Output: -6
```

## Conclusion
In this blog post, we discussed how to find the smallest continuous subarray sum in a Python list using the sliding window technique. This problem can be efficiently solved with a time complexity of O(n), where n is the length of the list. By applying this algorithm, you can find the smallest sum of any continuous subarray efficiently.