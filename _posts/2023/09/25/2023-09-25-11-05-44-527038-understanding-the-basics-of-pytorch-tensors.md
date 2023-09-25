---
layout: post
title: "Understanding the basics of PyTorch tensors"
description: " "
date: 2023-09-25
tags: [MachineLearning, PyTorch]
comments: true
share: true
---

## What are Tensors?

Tensors in PyTorch are multi-dimensional arrays, similar to NumPy arrays. They can be used to store and manipulate large amounts of data efficiently. Tensors are highly optimized for numerical operations and are the preferred data structure for computations in PyTorch.

## Creating Tensors

There are multiple ways to create tensors in PyTorch. Here are a few examples:

### Creating Tensors from Data

You can create a tensor directly from a Python list or a NumPy array using the `torch.tensor()` function. For example:

```python
import torch

data_list = [1, 2, 3]
tensor_from_list = torch.tensor(data_list)

data_array = np.array([4, 5, 6])
tensor_from_array = torch.tensor(data_array)
```

### Creating Tensors with Predefined Values

PyTorch provides functions to create tensors with predefined values. Some of the commonly used ones are:

- `torch.zeros()` creates a tensor filled with zeros.
- `torch.ones()` creates a tensor filled with ones.
- `torch.rand()` creates a tensor filled with random numbers between 0 and 1.

```python
zeros_tensor = torch.zeros(2, 3)
ones_tensor = torch.ones(4, 4)
random_tensor = torch.rand(3, 3)
```

### Creating Tensors with a Specific Data Type

By default, PyTorch creates tensors with the `torch.float32` data type. However, you can specify a different data type during tensor creation. For example:

```python
tensor_float = torch.tensor(data_list, dtype=torch.float32)
tensor_long = torch.tensor(data_list, dtype=torch.long)
```

## Tensor Operations

Once you have created tensors, you can perform a variety of operations on them. PyTorch tensors support mathematical operations such as addition, subtraction, multiplication, and division, as well as more advanced operations like matrix multiplication and element-wise operations.

Here's an example that demonstrates some basic tensor operations:

```python
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Element-wise addition
c = a + b

# Element-wise multiplication
d = a * b

# Matrix multiplication
e = torch.matmul(a, b)
```

## Conclusion

In this blog post, we have explored the basics of PyTorch tensors. We have learned how to create tensors using different methods, specify data types, and perform various operations on them. Understanding tensors is crucial for working with PyTorch and building deep learning models efficiently.

#MachineLearning #PyTorch