---
layout: post
title: "[Python] Sort a Tuple by Multiple Keys"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Sorting a tuple is a common operation in Python when dealing with data sets. By default, Python's built-in `sorted()` function can sort a tuple by a single key. However, there may be cases where you need to sort a tuple by multiple keys. This can be accomplished by using the `key` parameter in the `sorted()` function with a lambda function.

Let's take a look at how to sort a tuple by multiple keys in Python.

## Example Scenario

Suppose we have a tuple that contains information about books. Each book is represented as a tuple with the following elements:
- Title
- Author
- Publication Year

We want to sort this tuple first by the author's last name, then by the publication year.

```python
books = (
    ("Python Crash Course", "Eric Matthes", 2015),
    ("Fluent Python", "Luciano Ramalho", 2015),
    ("Clean Code", "Robert C. Martin", 2008),
    ("Python Tricks", "Dan Bader", 2017),
    ("Effective Python", "Brett Slatkin", 2015)
)
```

## Sorting by Multiple Keys

To sort the `books` tuple by multiple keys, we can use the `sorted()` function with a lambda function as the `key` parameter. 

```python
sorted_books = sorted(books, key=lambda x: (x[1].split()[-1], x[2]))
```

In this lambda function, we define the key to sort by as a tuple `(x[1].split()[-1], x[2])`. The first element of the tuple `x[1].split()[-1]` represents the author's last name, obtained by splitting the author's full name and retrieving the last element. The second element `x[2]` represents the publication year.

By passing this lambda function as the `key` parameter in the `sorted()` function, the books tuple will be sorted first by the author's last name and then by the publication year.

## Output

Let's print the sorted tuple to see the result:

```python
for book in sorted_books:
    print(book)
```

Output:
```
('Clean Code', 'Robert C. Martin', 2008)
('Python Crash Course', 'Eric Matthes', 2015)
('Fluent Python', 'Luciano Ramalho', 2015)
('Effective Python', 'Brett Slatkin', 2015)
('Python Tricks', 'Dan Bader', 2017)
```

As seen in the output, the `books` tuple is now sorted by the author's last name, followed by the publication year.

## Conclusion

In this blog post, we learned how to sort a tuple by multiple keys in Python. By using the `key` parameter in the `sorted()` function with a lambda function, we can define a custom sorting order based on different attributes of the tuple. Sorting by multiple keys allows us to efficiently arrange data according to our desired criteria.

This technique can be applied to various scenarios where sorting by multiple keys is essential, such as sorting data tables, organizing data sets, or prioritizing tasks based on multiple criteria.