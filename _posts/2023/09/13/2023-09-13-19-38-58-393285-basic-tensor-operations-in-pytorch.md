---
layout: post
title: "Basic tensor operations in PyTorch"
description: " "
date: 2023-09-13
tags: [deeplearning, pytorch]
comments: true
share: true
---

PyTorch is a popular deep learning library that provides efficient tensor computation with automatic differentiation. In this article, we will explore some of the basic tensor operations available in PyTorch.

## 1. Creating Tensors

Tensors are the fundamental data structures in PyTorch. You can create tensors using the `torch.Tensor` class. Here are a few ways to create tensors:

### Creating an Empty Tensor

```python
import torch

empty_tensor = torch.Tensor()
```

### Creating a Tensor from a List or NumPy array

```python
import torch
import numpy as np

list_data = [1, 2, 3, 4, 5]
tensor_from_list = torch.Tensor(list_data)

array_data = np.array([1, 2, 3, 4, 5])
tensor_from_numpy = torch.from_numpy(array_data)
```


## 2. Tensor Operations

Once you have created tensors, you can perform various operations on them. Here are some commonly used tensor operations:

### Element-Wise Operations
Element-wise operations apply the same operation to each element of a tensor. Examples of element-wise operations include addition, subtraction, multiplication, and division.

```python
import torch

# Create tensors
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Element-wise addition
result = x + y
print(result)  # Output: tensor([5, 7, 9])

# Element-wise multiplication
result = x * y
print(result)  # Output: tensor([4, 10, 18])
```

### Matrix Operations
PyTorch also provides various matrix operations like matrix multiplication, transpose, and dot product.

```python
import torch

# Create tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Matrix multiplication
result = torch.mm(a, b)
print(result)  # Output: tensor([[19, 22], [43, 50]])

# Matrix transpose
result = a.T
print(result)  # Output: tensor([[1, 3], [2, 4]])
```

### Reshaping Tensors
You can reshape a tensor using the `view` method.

```python
import torch

# Create a tensor
x = torch.arange(6)

# Reshape the tensor
reshaped_tensor = x.view(2, 3)
print(reshaped_tensor)  # Output: tensor([[0, 1, 2], [3, 4, 5]])
```


## Conclusion

In this article, we covered some of the basic tensor operations available in PyTorch. We learned how to create tensors and perform common operations like element-wise operations, matrix operations, and reshaping tensors. Keep exploring the PyTorch documentation to discover more advanced tensor operations that can help you in your deep learning projects.

#deeplearning #pytorch