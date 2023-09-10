---
layout: post
title: "[Python] Environment variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, *environment variables* are a way to store and access dynamic values that can be used by your application. These values can be used to configure various aspects of your program, such as database connection details, API keys, or any other sensitive information that you don't want to hardcode into your codebase.

## Setting environment variables

To set an environment variable in Python, you can use the `os` module which provides a function called `environ`. This function allows you to access and manipulate environment variables.

```python
import os

# Set environment variable
os.environ["KEY"] = "value"
```

In the above example, we are setting an environment variable named "KEY" with the value "value".

## Getting environment variables

To access the value of an environment variable, you can use the `os.environ` dictionary-like object. You can access the value of a specific environment variable by providing its name as the key.

```python
import os

# Get the value of an environment variable
value = os.environ.get("KEY")
print(value)  # Output: "value"
```

In the above example, we are getting the value of the "KEY" environment variable.

## Managing sensitive information

Environment variables are commonly used to store sensitive information like API keys or database credentials that should not be exposed in your codebase. By using environment variables, you can separate the sensitive information from your code and avoid accidentally exposing them when sharing or publishing your code.

For example, instead of hardcoding an API key directly in your code:

```python
api_key = "your_api_key"
```

You can use an environment variable to store the API key:

```python
import os

api_key = os.environ.get("API_KEY")
```

By doing this, you can keep the actual API key as a private value, separate from your codebase.

## Configuration management libraries

While manually setting and getting environment variables using the `os` module is straightforward, there are also libraries available to provide more advanced features for managing environment variables and configurations in Python.

Some popular libraries for configuration management in Python include:

- **dotenv**: A Python library that reads key-value pairs from a `.env` file and makes them available as environment variables.
- **python-decouple**: A library that allows you to define your settings in a `.env` file and access them using a simple API.

These libraries provide additional features like automatically loading environment variables from a file and support for different file formats for configuration management.

## Conclusion

Environment variables in Python are a useful way to store and access dynamic values that can be safely used within your application. By using environment variables, you can separate sensitive information from your codebase and easily manage configurations. Whether you manually set environment variables or use configuration management libraries, understanding and utilizing environment variables is an essential skill for any Python developer.