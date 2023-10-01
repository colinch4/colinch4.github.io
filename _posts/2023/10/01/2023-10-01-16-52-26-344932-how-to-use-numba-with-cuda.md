---
layout: post
title: "How to use Numba with CUDA?"
description: " "
date: 2023-10-01
tags: [numba, cuda]
comments: true
share: true
---

With the increasing demand for high-performance computing, GPUs have become a popular choice for accelerating compute-intensive tasks. Numba, a powerful Python library, provides a seamless way to utilize the full potential of GPUs through CUDA.

## What is CUDA?

CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model created by NVIDIA. It allows developers to harness the power of NVIDIA GPUs to accelerate computational tasks. To work with CUDA, you'll need an NVIDIA GPU that supports CUDA.

## Installing Numba

Before using Numba with CUDA, you need to install both Numba and CUDA on your system. Start by installing Numba using pip:

```shell
$ pip install numba
```

Next, you'll need to install CUDA Toolkit. Visit the NVIDIA CUDA website (https://developer.nvidia.com/cuda-downloads) and choose the version appropriate for your operating system.

## Writing CUDA Kernels with Numba

Numba provides a convenient way to write CUDA kernels directly in Python, making GPU programming accessible to Python developers without diving into low-level CUDA code. Here's an example of a simple vector addition CUDA kernel using Numba:

```python
import numpy as np
from numba import cuda

@cuda.jit
def vector_add(a, b, result):
    idx = cuda.threadIdx.x
    stride = cuda.blockDim.x

    for i in range(idx, len(a), stride):
        result[i] = a[i] + b[i]
```

In the example above, we are defining a `vector_add` function decorated with `@cuda.jit`. This indicates that the function is a CUDA kernel that can be executed in parallel on a CUDA device.

## Launching CUDA Kernels

To execute the CUDA kernel defined above, we can use Numba's `cuda.to_device()` and `cuda.synchronize()` functions. Here's an example of launching the `vector_add` kernel:

```python
# Input arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Allocate memory on the GPU
device_a = cuda.to_device(a)
device_b = cuda.to_device(b)
result = np.zeros_like(a)

# Define the grid size and block size
block_size = 32
grid_size = (len(a) + (block_size - 1)) // block_size

# Launch the CUDA kernel
vector_add[grid_size, block_size](device_a, device_b, result)

# Synchronize to ensure the kernel has finished executing
cuda.synchronize()

# Print the result
print(result)
```

In the example above, we allocate memory on the GPU using `cuda.to_device()` and create an output array using `np.zeros_like()`. We then define the grid size and block size to determine how the CUDA kernel is launched. Finally, we call the `vector_add` kernel with the input arrays and the output array.

## Conclusion

Thanks to Numba's integration with CUDA, Python developers can easily leverage the power of GPUs for accelerating compute-intensive tasks. By following the steps outlined in this tutorial, you can start using Numba with CUDA and unlock the potential of parallel computing using NVIDIA GPUs.

#numba #cuda