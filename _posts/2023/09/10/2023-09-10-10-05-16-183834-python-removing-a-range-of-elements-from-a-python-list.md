---
layout: post
title: "[Python] Removing a range of elements from a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Create a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove elements using slice assignment
my_list[3:6] = []

print(my_list)
```

The above code demonstrates how to remove a range of elements from a Python list using slice assignment. In this example, we have a list called `my_list` with elements from 1 to 10. 

To remove a range of elements, we use slice assignment. The syntax for slice assignment is `list[start_index:end_index] = []`, where `start_index` is the index of the first element to remove and `end_index` is the index of the element **after** the last element to remove. Assigning an empty list `[]` to this slice effectively removes the specified range of elements from the original list.

In the given code, we are removing elements from index 3 to 5 (`[4, 5, 6]`) by assigning an empty list `[]` to `my_list[3:6]`. After executing this line, the list will be updated without the removed elements.

The output of the code will be:

```
[1, 2, 3, 7, 8, 9, 10]
```

As you can see, the elements `[4, 5, 6]` have been successfully removed from the list.