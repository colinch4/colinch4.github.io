---
layout: post
title: "[Python] Serialization and deserialization in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Serialization
Serialization is the process of converting data into a format that can be easily stored or transmitted. In Python, **pickle** is the standard library for serialization. 

To demonstrate serialization, let's consider a simple example where we want to store a list of objects to a file:

```python
import pickle

# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 35)

# Create a list of objects
people = [person1, person2, person3]

# Serialize the list to a file
with open("people.pickle", "wb") as file:
    pickle.dump(people, file)
```

In the above code, we define a `Person` class with attributes for name and age. We then create instances of this class and store them in a list called `people`. Using `pickle.dump()` method, we serialize the list of `people` and write it to a file called `people.pickle`.

## Deserialization
Deserialization is the inverse process of serialization, where the stored data is retrieved and converted back to its original form. In Python, we can deserialize data using the `pickle.load()` method.

```python
import pickle

# Deserialize the list from the file
with open("people.pickle", "rb") as file:
    deserialized_people = pickle.load(file)

# Print the deserialized data
for person in deserialized_people:
    print(person.name, person.age)
```

In the above code, we use the `pickle.load()` method to read the serialized data from the file `people.pickle`. The data is then stored in a variable called `deserialized_people`, and we can access and work with the original objects.

Serialization and deserialization provide a convenient way to store and retrieve complex data structures in Python. It is important to note that the **pickle** module works only within Python and may not be secure when dealing with untrusted sources. In such cases, other serialization formats like JSON or XML should be considered.

In conclusion, serialization and deserialization are powerful techniques that allow us to persist and retrieve data in Python. The pickle module provides a straightforward way to accomplish this task. However, one should be cautious when using serialized data from unknown or untrusted sources.