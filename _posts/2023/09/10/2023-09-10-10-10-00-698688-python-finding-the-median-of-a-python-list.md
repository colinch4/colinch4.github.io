---
layout: post
title: "[Python] Finding the median of a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will explore how to find the median of a Python list. The median is the middle value in a list, when it is sorted in ascending order. This is a commonly used statistic in data analysis and is useful for understanding the central tendency of a dataset.

## Method 1: Using the statistics module

Python provides a built-in module called `statistics`, which contains various statistical functions including finding the median of a list. Here's an example of using the `statistics` module to find the median:

```python
import statistics

my_list = [1, 2, 3, 4, 5]
median = statistics.median(my_list)

print("The median is:", median)
```

Output:
```
The median is: 3
```

The `statistics.median()` function takes a list as input and returns the median value. It handles both even and odd length lists correctly and returns the middle value(s) accordingly.

## Method 2: Sorting the list

Another approach to find the median is by sorting the list in ascending order and then finding the middle element(s). Here's an example of using this method:

```python
my_list = [7, 2, 9, 4, 5, 3, 1]
sorted_list = sorted(my_list)
length = len(sorted_list)
middle_index = length // 2

if length % 2 == 0:
    median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
else:
    median = sorted_list[middle_index]

print("The median is:", median)
```

Output:
```
The median is: 4
```

The above code first sorts the list using the `sorted()` function. Then, it checks if the length of the list is even or odd to determine the median value. If the length is even, it calculates the average of the middle two elements. If the length is odd, it simply returns the middle element.

## Conclusion

Finding the median of a Python list is a common task in data analysis. In this blog post, we discussed two methods to calculate the median. The first method uses the `statistics` module, which provides a convenient way to find the median. The second method involves sorting the list and finding the middle element(s). Both methods can be used depending on your specific requirements.

Remember to consider the size and content of your list when choosing a method, as sorting a large list can be computationally expensive.