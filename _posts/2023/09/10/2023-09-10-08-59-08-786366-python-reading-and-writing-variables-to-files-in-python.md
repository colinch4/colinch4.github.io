---
layout: post
title: "[Python] Reading and writing variables to files in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you can easily read and write variables to files using the built-in `open()` function and appropriate file modes. This allows you to store and retrieve data persistently, which is useful for tasks like saving configurations or caching data.

## Writing Variables to a File

To write variables to a file, follow these steps:

1. Open the file in write mode using the `open()` function.
2. Write the variables to the file using the `write()` method or the `print()` function.
3. Close the file using the `close()` method.

Here's an example that demonstrates writing variables to a file:

```python
# Define variables
name = "John Doe"
age = 30
city = "New York"

# Open the file in write mode
file = open("person.txt", "w")

# Write variables to the file
file.write(f"Name: {name}\n")
file.write(f"Age: {age}\n")
file.write(f"City: {city}\n")

# Close the file
file.close()
```

In this example, we define three variables (`name`, `age`, and `city`). We then open the file `person.txt` in write mode, write the variables followed by a newline character `\n` to separate each variable, and finally close the file.

## Reading Variables from a File

To read variables from a file, follow these steps:

1. Open the file in read mode using the `open()` function.
2. Read the file contents using the appropriate method (`read()`, `readline()`, or `readlines()`).
3. Close the file using the `close()` method.

Here's an example that demonstrates reading variables from a file:

```python
# Open the file in read mode
file = open("person.txt", "r")

# Read the file contents
file_contents = file.readlines()

# Close the file
file.close()

# Extract variables from file contents
name = file_contents[0].split(": ")[1].strip()
age = int(file_contents[1].split(": ")[1].strip())
city = file_contents[2].split(": ")[1].strip()

# Print the variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

In this example, we open the file `person.txt` in read mode and read its contents using the `readlines()` method. We then close the file and extract the variables by splitting and stripping the lines accordingly. Finally, we print the variables.

By following these steps, you can easily read and write variables to files in Python. This provides you with a convenient way to store and retrieve data, making your code more flexible and scalable.