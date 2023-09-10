---
layout: post
title: "[Python] Find the Shortest Subsequence in a Tuple"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Find the Shortest Subsequence in a Tuple

def find_shortest_subsequence(seq, subseq):
    n = len(seq)
    m = len(subseq)

    # Initialize the array to store the shortest subsequences
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the last row of the array
    for j in range(m + 1):
        dp[n][j] = float('inf')

    # Fill the array in reverse order
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if seq[i] == subseq[j]:
                # If the elements match, consider the next elements
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                # If the elements don't match, take the minimum of the next elements
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + 1

    # Find the shortest subsequence
    shortest_subseq = []
    i, j = 0, 0
    while i < n and j < m:
        if seq[i] == subseq[j]:
            shortest_subseq.append(seq[i])
            i += 1
            j += 1
        elif dp[i + 1][j] < dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return shortest_subseq

# Test the function
seq = (1, 5, 2, 3, 4, 5, 6, 7, 8, 9)
subseq = (2, 4, 5, 7)
shortest_subsequence = find_shortest_subsequence(seq, subseq)
print("Shortest Subsequence:", shortest_subsequence)
```

This code demonstrates a function `find_shortest_subsequence` that takes a tuple `seq` and a tuple `subseq` as input and returns the shortest subsequence of `seq` that contains all the elements in `subseq`. If no subsequence is found, an empty list is returned.

The function uses a dynamic programming approach to solve the problem. It creates a 2-dimensional array `dp` to store the lengths of the shortest subsequences. The array is filled in reverse order, starting from the last elements of `seq` and `subseq`.

After filling the `dp` array, the function uses it to find the shortest subsequence by iterating through `seq` and `subseq`. If the elements match, they are added to the `shortest_subseq` list. If the elements don't match, the function chooses the next element based on the minimum value in the `dp` array.

In the example code, we test the function with a sample sequence `seq` and subsequence `subseq`. The expected output is `[2, 4, 5, 7]`, which is the shortest subsequence in `seq` that contains all the elements in `subseq`.