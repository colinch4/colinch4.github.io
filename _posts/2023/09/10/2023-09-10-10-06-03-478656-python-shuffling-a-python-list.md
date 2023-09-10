---
layout: post
title: "[Python] Shuffling a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, shuffling a list means randomly rearranging the elements of the list. The `random` module in Python provides the `shuffle()` function that can be used to shuffle a Python list. In this blog post, we will explore how to shuffle a list in Python.

## Importing the `random` module
Before we can use the `shuffle()` function, we need to import the `random` module. To do this, add the following line of code at the beginning of your Python script:

```python
import random
```

## Shuffling a List
To actually shuffle a Python list, we can use the `shuffle()` function provided by the `random` module. The `shuffle()` function takes a list as input and shuffles its elements randomly. Here is an example:

```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

print(my_list)
```

In the above code, we first import the `random` module and then define a list called `my_list` with some elements. We then call the `shuffle()` function and pass `my_list` as the argument to shuffle its elements randomly. Finally, we print the shuffled list.

When you run the above code, you will get output similar to the following:

```
[2, 4, 1, 5, 3]
```

As you can see, the elements of the list have been randomly rearranged after shuffling.

## Shuffling a List In-place
The `shuffle()` function shuffles the list in-place, meaning it modifies the original list itself. If you want to retain the original list and get a new shuffled list, you can make a copy of the original list and then shuffle it. Here is an example:

```python
import random

my_list = [1, 2, 3, 4, 5]
shuffled_list = random.sample(my_list, len(my_list))

print(shuffled_list)
```

In this code, we use the `random.sample()` function to create a new shuffled list without modifying the original list. `random.sample()` returns a new list with elements randomly sampled from the input list. We pass `my_list` as the first argument and `len(my_list)` as the second argument to sample all the elements of the list. Finally, we print the shuffled list.

When you run the above code, you will get output similar to the following:

```
[2, 4, 1, 5, 3]
```

Again, the elements of the list have been randomly rearranged after shuffling.

## Conclusion
Shuffling a Python list can be done easily using the `shuffle()` function from the `random` module. By understanding how to shuffle a list in Python, you can add randomness to your programs and solve various problems that require random element selection or ordering.