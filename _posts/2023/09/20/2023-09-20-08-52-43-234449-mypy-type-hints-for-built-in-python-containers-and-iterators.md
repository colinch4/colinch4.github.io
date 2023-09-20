---
layout: post
title: "MyPy type hints for built-in Python containers and iterators"
description: " "
date: 2023-09-20
tags: [python, mypy]
comments: true
share: true
---

Type hints in Python can greatly enhance code readability, maintainability, and catch potential bugs early. The `typing` module in Python provides a rich set of tools for adding type hints to your code. In this blog post, we'll explore how to use MyPy type hints specifically for built-in Python containers and iterators.

## Lists

To annotate a list, we use the `List` type hint from the `typing` module. For example, to indicate a list of integers, we can write:

```python
from typing import List

my_list: List[int] = [1, 2, 3, 4, 5]
```

Now, MyPy will be able to enforce that `my_list` can only contain integers.

## Tuples

Similar to lists, we can annotate tuples using the `Tuple` type hint. A tuple with elements of different types can be annotated like this:

```python
from typing import Tuple

my_tuple: Tuple[int, str, bool] = (1, "hello", True)
```

Here, `my_tuple` is a tuple that contains an integer, a string, and a boolean value.

## Sets

For sets, we can use the `Set` type hint. To define a set of strings, we can do the following:

```python
from typing import Set

my_set: Set[str] = {"apple", "banana", "cherry"}
```

This will allow MyPy to enforce that `my_set` only contains strings.

## Dictionaries

Dictionaries can be annotated using the `Dict` type hint. To specify a dictionary with keys of type `str` and values of type `int`, we can write:

```python
from typing import Dict

my_dict: Dict[str, int] = {"apple": 1, "banana": 2, "cherry": 3}
```

Now, MyPy will ensure that the keys are strings and the values are integers.

## Iterators

To annotate an iterator, we can use the `Iterator` type hint. For example, if we have a function that returns an iterator over integers, we can annotate it like this:

```python
from typing import Iterator

def my_iterator() -> Iterator[int]:
    # Implementation of the iterator
    ...
```

MyPy will now check that the function returns an iterator with integer values.

## Conclusion

Type hints are a powerful feature in Python that can greatly improve code quality and catch potential bugs. By using MyPy type hints for built-in containers and iterators, we can leverage static type checking to ensure our code is correct and maintainable.

#python #mypy