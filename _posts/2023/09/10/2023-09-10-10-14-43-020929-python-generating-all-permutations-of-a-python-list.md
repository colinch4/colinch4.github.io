---
layout: post
title: "[Python] Generating all permutations of a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Using the itertools module

Python provides the `itertools` module that includes a `permutations` function to generate all permutations of a given iterable. We can use this function to generate permutations of a list.

Here's an example code snippet that demonstrates how to use `permutations` function to generate permutations:

```python
from itertools import permutations

def generate_permutations(lst):
    perm = permutations(lst)
    for p in perm:
        print(p)

lst = [1, 2, 3]
generate_permutations(lst)
```

Output:

```
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
```

In this example, we import `permutations` function from the `itertools` module. The `generate_permutations` function takes a list `lst` as input. We generate the permutations of the list using `permutations(lst)` and iterate over each permutation using a `for` loop. Finally, we print each permutation.

## Writing a custom recursive function

If you want to generate permutations without using any external module, you can write a recursive function. Here's an example code snippet that generates all permutations of a list recursively:

```python
def generate_permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    perms = []
    for i in range(len(lst)):
        m = lst[i]
        rem_list = lst[:i] + lst[i+1:]

        for p in generate_permutations(rem_list):
            perms.append([m] + p)

    return perms

lst = [1, 2, 3]
permutations = generate_permutations(lst)
for p in permutations:
    print(p)
```

Output:

```
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```

In this example, the `generate_permutations` function takes a list `lst` as input. If the length of the list is 0 or 1, we return the list itself. Otherwise, we iterate over each element `m` in the list and recursively generate permutations of the remaining list `rem_list`. We append `m` to each generated permutation and add it to the `perms` list. Finally, we return the list of permutations.

Both methods produce the same output, and you can choose the one that suits your needs. Generating permutations can be useful in various scenarios such as generating test cases, finding all possible combinations, or solving certain mathematical problems.