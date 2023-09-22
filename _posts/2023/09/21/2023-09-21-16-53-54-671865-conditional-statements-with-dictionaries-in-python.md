---
layout: post
title: "Conditional statements with dictionaries in Python"
description: " "
date: 2023-09-21
tags: [dictionaries]
comments: true
share: true
---

In Python, dictionaries are used to store key-value pairs. They are versatile data structures that can be used in a variety of scenarios, including conditional statements. In this blog post, we will explore how to use dictionaries in conditional statements to make your code more concise and readable.

### Basic dictionary structure

Before we dive into conditional statements, let's quickly review the basic structure of a dictionary in Python. A dictionary is defined using curly braces, with each key-value pair separated by a colon (:). For example:

```python
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

To access a value in a dictionary, you can use the key inside square brackets ([]). For example:

```python
print(my_dict["key2"])
# Output: value2
```

### Using dictionaries in conditional statements

Conditional statements allow us to execute different blocks of code depending on a certain condition. By using dictionaries in conditional statements, we can simplify complex if-else structures and make our code more readable.

Let's say we have a dictionary that represents a person's age and their corresponding age group:

```python
age = {
    "Alice": 25,
    "Bob": 38,
    "Charlie": 17,
    "David": 42
}
```

We can use this dictionary to determine whether a person is a teenager, an adult, or a senior citizen:

```python
person = "Charlie"

if age[person] < 20:
    print("This person is a teenager.")
elif age[person] < 60:
    print("This person is an adult.")
else:
    print("This person is a senior citizen.")
```

The code above will output:

```
This person is a teenager.
```

By using the `age` dictionary in our conditional statements, we can easily determine the age group of a person without writing lengthy if-else chains.

### Handling missing keys

When using dictionaries in conditional statements, it's important to handle cases where the key doesn't exist in the dictionary. One way to do this is by using the `get()` method, which allows us to specify a default value if the key is not found.

```python
person = "Eve"

age_group = {
    "teenager": (13, 19),
    "adult": (20, 59),
    "senior citizen": (60, 120)
}

age_range = age_group.get(person, "Unknown")
print(f"The age range for {person} is {age_range}.")
```

The code above will output:

```
The age range for Eve is Unknown.
```

In this example, since the key "Eve" doesn't exist in the `age_group` dictionary, the `get()` method returns the default value "Unknown".

### Conclusion

Using dictionaries in conditional statements can make your code more concise and readable. By leveraging the key-value pairs in dictionaries, you can easily handle different cases without writing lengthy if-else chains. Remember to handle missing keys using the `get()` method to avoid potential errors.

Give it a try in your next Python project and enjoy the benefits of using dictionaries in conditional statements!

## #python #dictionaries