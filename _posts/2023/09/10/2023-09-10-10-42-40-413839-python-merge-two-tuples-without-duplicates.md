---
layout: post
title: "[Python] Merge Two Tuples Without Duplicates"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
def merge_tuples(tuple1, tuple2):
    merged_tuple = tuple1 + tuple2
    merged_tuple = tuple(set(merged_tuple))
    return merged_tuple

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

merged_tuple = merge_tuples(tuple1, tuple2)
print(merged_tuple)
```

Output:
```
(1, 2, 3, 4, 5, 6)
```