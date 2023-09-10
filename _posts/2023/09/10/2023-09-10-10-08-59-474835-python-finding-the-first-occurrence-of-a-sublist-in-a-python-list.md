---
layout: post
title: "[Python] Finding the first occurrence of a sublist in a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
def find_sublist(parent_list, sublist):
    '''
    Function to find the index of the first occurrence of a sublist in a parent list.
    
    Parameters:
        - parent_list (list): The parent list to search in.
        - sublist (list): The sublist to search for.
    
    Returns:
        - The index of the first occurrence of the sublist in the parent list, or -1 if not found.
    '''
    n = len(parent_list)
    m = len(sublist)
    
    for i in range(n - m + 1):
        if parent_list[i:i+m] == sublist:
            return i
    
    return -1

# Example usage
parent_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublist = [3, 4, 5]

index = find_sublist(parent_list, sublist)
if index != -1:
    print(f"The sublist is found at index {index}.")
else:
    print("The sublist is not found in the parent list.")
```

In this code snippet, we define a function called `find_sublist` that takes in two parameters: `parent_list` and `sublist`. The `parent_list` is the list in which we want to find the first occurrence of the `sublist`.

The function uses a simple approach to iterate through the `parent_list` and check if there is a match for the `sublist`. It uses a `for` loop to iterate over each possible starting index of a sublist within the `parent_list`. It then compares the sublist of length `m` starting from each index `i` with the given `sublist` and checks for a match.

If a match is found, it returns the index of the first occurrence of the sublist in the parent list. If no match is found, it returns -1.

In the example usage, we have a `parent_list` containing the numbers 1 to 10, and we want to find the index of the first occurrence of the sublist `[3, 4, 5]`. We call the `find_sublist` function passing both lists as arguments. If the index returned is not -1, it means the sublist is found in the parent list and we print the corresponding message. Otherwise, we print that the sublist is not found.