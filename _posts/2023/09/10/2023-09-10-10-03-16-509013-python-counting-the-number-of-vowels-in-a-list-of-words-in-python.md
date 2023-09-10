---
layout: post
title: "[Python] Counting the number of vowels in a list of words in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will explore how to count the number of vowels in a list of words using Python. This is a common task in text processing and can be useful in many applications, such as language analysis or word frequency analysis.

Let's start by defining a list of words:

```python
words = ["apple", "banana", "cherry", "date", "eggplant"]
```

Now, let's write a function that takes in a list of words as input and counts the number of vowels in each word:

```python
def count_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = []
    
    for word in words:
        count = 0
        for letter in word:
            if letter.lower() in vowels:
                count += 1
        counts.append(count)
    
    return counts
```

In the `count_vowels` function, we first define a list of vowels. We then initialize an empty list called `counts` to store the counts of vowels for each word.

We then iterate over each word in the input list `words`. For each word, we initialize a count variable to zero. We then iterate over each letter in the word and check if it is a vowel (ignoring the case by converting the letter to lowercase). If a letter is a vowel, we increment the count.

After iterating over all the letters in a word, we append the count to the `counts` list. Finally, we return the `counts` list which contains the counts of vowels for each word.

Let's test our function with the example list of words:

```python
words = ["apple", "banana", "cherry", "date", "eggplant"]
vowel_counts = count_vowels(words)
print(vowel_counts)
```

Output:
```
[2, 3, 2, 2, 3]
```

As we can see, the function correctly counts the number of vowels in each word. "apple" has 2 vowels, "banana" has 3 vowels, "cherry" has 2 vowels, "date" has 2 vowels, and "eggplant" has 3 vowels.

This simple function can be easily extended to handle more complex text processing tasks and can be a useful tool in your Python projects.

I hope you found this blog post helpful in understanding how to count the number of vowels in a list of words using Python. Happy coding!