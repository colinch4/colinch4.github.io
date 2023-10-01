---
layout: post
title: "How to use Numba with multiple GPUs?"
description: " "
date: 2023-10-01
tags: [numba, multiplegpus]
comments: true
share: true
---

Numba is a just-in-time compiler for Python that can be used to accelerate computations. It is especially useful when working with numerical and scientific computations. Numba supports GPU acceleration, allowing you to leverage the power of multiple GPUs to speed up your code.

In this blog post, we will explore how to use Numba with multiple GPUs to achieve faster computation times.

## Prerequisites

Before we get started, make sure you have the following prerequisites installed:

- Numba: You can install Numba by running `pip install numba`.
- CUDA Toolkit: Numba relies on the CUDA Toolkit to interact with GPUs. Make sure you have a compatible version of CUDA Toolkit installed on your system.

## Setting up Multiple GPUs

To use multiple GPUs with Numba, you need to set up your system to recognize and access the GPUs. Check your system documentation to configure the GPUs correctly.

## Example Code

Let's start by writing a simple example code to demonstrate how to use Numba with multiple GPUs. 

```python
import numba.cuda as cuda

@cuda.jit
def add_vectors(a, b, result):
    i = cuda.grid(1)
    if i < len(a):
        result[i] = a[i] + b[i]

def main():
    # Initialize input arrays
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    result = [0] * len(a)

    # Setting up the GPUs
    num_gpus = cuda.get_num_devices()
    for i in range(num_gpus):
        device = cuda.get_device(i)
        device.reset()

    # Allocate memory on multiple GPUs
    gpu_mem = []
    for i in range(num_gpus):
        with cuda.gpus[i]:
            gpu_mem.append(cuda.to_device(a))

    # Launch parallel computations on multiple GPUs
    for i in range(num_gpus):
        with cuda.gpus[i]:
            add_vectors[gpu_mem[i].shape[0], 1](gpu_mem[i], b, result)

    # Wait for all GPUs to finish
    cuda.synchronize()

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
```

In the example above, we define a `add_vectors` function that adds two arrays `a` and `b` element-wise and stores the result in the `result` array. We use the `cuda.jit` decorator provided by Numba to specify that this function will be executed on the GPU.

To use multiple GPUs, we first determine the number of available GPUs using `cuda.get_num_devices()`. We then reset each device to ensure a clean state before allocating memory.

We allocate memory on each GPU using the `cuda.to_device()` function. This function takes a NumPy array and transfers it to the GPU memory.

We then launch parallel computations on each GPU by using the `with cuda.gpus[i]` context manager. Inside this context manager, we calculate the grid size and launch the `add_vectors` kernel with the appropriate grid and block sizes to process the data on the GPU.

Finally, we synchronize all GPUs using `cuda.synchronize()`, which ensures that all computations have completed before proceeding. We print the final result, which should be the element-wise addition of arrays `a` and `b`.

## Conclusion

In this blog post, we have learned how to use Numba with multiple GPUs to accelerate computations. By leveraging the power of multiple GPUs and Numba's GPU programming capabilities, you can achieve significant speed-ups for your numerical computations.

Remember to set up your system to recognize and access the multiple GPUs correctly. Then, by using Numba's GPU programming features like the `cuda.jit` decorator and `cuda.gpus[i]` context manager, you can easily distribute your workload across multiple GPUs.

#numba #multiplegpus