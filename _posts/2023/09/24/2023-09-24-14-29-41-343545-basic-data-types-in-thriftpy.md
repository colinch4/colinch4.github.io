---
layout: post
title: "Basic data types in ThriftPy"
description: " "
date: 2023-09-24
tags: [thriftpy, datatypes]
comments: true
share: true
---

## 1. Boolean

The boolean data type represents a binary value, either true or false. In ThriftPy, the boolean data type is represented by the `bool` class. Here is an example of how to define and use a boolean field in ThriftPy:

```python
from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TTransport import TMemoryBuffer
from tutorial.ttypes import MyStruct

# Create an instance of MyStruct
my_struct = MyStruct()

# Set a boolean field to true
my_struct.my_boolean_field = True

# Serialize the struct to a binary format
transport = TMemoryBuffer()
protocol = TBinaryProtocol(transport)
my_struct.write(protocol)

# Deserialize and access the boolean field
my_struct.read(protocol)
print(my_struct.my_boolean_field)  # Output: True
```

## 2. Numeric Types

ThriftPy supports various numeric data types, including:

### Integers

ThriftPy provides different integer types to represent various ranges of values. Some of the commonly used integer types are `byte`, `i16`, `i32`, and `i64`. Here is an example of defining and using an integer field in ThriftPy:

```python
# Create an instance of MyStruct
my_struct = MyStruct()

# Set an integer field
my_struct.my_integer_field = 42

# Serialize and deserialize the struct
...

# Access the integer field
print(my_struct.my_integer_field)  # Output: 42
```

### Floating-Point Numbers

ThriftPy also supports floating-point numbers with the `double` and `float` data types. Here's an example:

```python
# Create an instance of MyStruct
my_struct = MyStruct()

# Set a floating-point field
my_struct.my_float_field = 3.14

# Serialize and deserialize the struct
...

# Access the floating-point field
print(my_struct.my_float_field)  # Output: 3.14
```

These are just a few examples of the basic data types available in ThriftPy. Other data types include strings, maps, lists, and sets, which provide more flexibility in structuring your Thrift data models.

ThriftPy's support for these basic data types allows you to work with structured data in a seamless way, enabling efficient communication between different services using Apache Thrift. Understanding these data types is essential for building robust and interoperable applications with ThriftPy.

#thriftpy #datatypes