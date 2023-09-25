---
layout: post
title: "Loading and saving PyTorch tensors"
description: " "
date: 2023-09-25
tags: [MachineLearning, PyTorch]
comments: true
share: true
---

PyTorch is a popular open-source machine learning framework that provides various functionalities for training and deploying deep neural networks. One common task in machine learning is loading and saving tensors, which are multi-dimensional arrays used to store and manipulate data. In this tutorial, we will explore different methods to load and save PyTorch tensors.

### Loading Tensors

To load a tensor from a file in PyTorch, you can use the `torch.load()` function. This function takes the file path as an argument and returns a Python object that contains the tensor data. Here's an example:

```python
import torch

# Load a tensor from a file
tensor = torch.load('path/to/tensor.pth')
```

By default, `torch.load()` loads the tensor onto the CPU. If you want to load it onto a specific device, such as a GPU, you can pass the `map_location` argument. For example:

```python
# Load a tensor and move it to GPU
tensor = torch.load('path/to/tensor.pth', map_location='cuda')
```

### Saving Tensors

To save a PyTorch tensor to a file, you can use the `torch.save()` function. This function takes two arguments: the tensor you want to save and the file path where you want to save it. Here's an example:

```python
import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3])

# Save the tensor to a file
torch.save(tensor, 'path/to/save/tensor.pth')
```

By default, `torch.save()` saves tensors in a binary format using Python's `pickle` module. You can also save tensors in other formats, such as JSON or CSV, by converting them to standard Python data structures first. For instance:

```python
import torch
import json

# Create a tensor
tensor = torch.tensor([4, 5, 6])

# Convert tensor to a Python list
data = tensor.tolist()

# Save the tensor as JSON
with open('path/to/save/tensor.json', 'w') as f:
    json.dump(data, f)
```

### Conclusion

In this tutorial, we learned how to load and save PyTorch tensors. Loading tensors can be done using the `torch.load()` function, while saving tensors can be achieved using `torch.save()`. Additionally, we saw how to save tensors in different formats, like JSON, by converting them to standard Python data structures. With these techniques, you can easily persist your tensor data and load it back when needed for future machine learning tasks.

#MachineLearning #PyTorch