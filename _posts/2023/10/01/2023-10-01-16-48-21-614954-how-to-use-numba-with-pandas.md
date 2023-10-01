---
layout: post
title: "How to use Numba with pandas?"
description: " "
date: 2023-10-01
tags: [Pandas, Numba]
comments: true
share: true
---

Pandas is a popular data manipulation library in Python, known for its powerful data analysis capabilities. However, when dealing with large datasets or complex operations, performance can become a concern. This is where Numba, a Just-In-Time (JIT) compiler for Python, comes into play. Numba can significantly speed up numerical computations by translating Python functions to machine code. In this blog post, we will explore how to use Numba with Pandas to optimize data processing tasks.

### Installing Numba
Before we begin, let's ensure we have Numba installed. You can easily install Numba using pip:

```bash
pip install numba
```

### Using Numba with Pandas
To illustrate the usage of Numba with Pandas, let's consider the following scenario: we have a large DataFrame that we want to apply a custom function to. Normally, when we apply a function using the `apply` method in Pandas, it applies the function row-wise, resulting in slower execution. However, by using Numba, we can compile the function and apply it using Numba's `njit` decorator for faster processing.

Let's first define a custom function that calculates the square of a number:

```python
import numpy as np

def square(x):
    return x**2
```

To use this function with Numba, we import the `njit` decorator from Numba and apply it to our custom function:

```python
from numba import njit

@njit
def square_numba(x):
    return x**2
```

Now, let's apply both the vanilla `square` function and the Numba-optimized `square_numba` function to a Pandas DataFrame:

```python
import pandas as pd

# Create a DataFrame with a large number of rows
df = pd.DataFrame({'numbers': np.random.randint(0, 100, 1000000)})

# Vanilla square function
df['squared_vanilla'] = df['numbers'].apply(square)

# Numba-optimized square function
df['squared_numba'] = df['numbers'].apply(square_numba)
```

By comparing the execution times of both approaches, we can observe a significant improvement in performance when using Numba. This improvement becomes more significant as the size of the DataFrame increases.

### Conclusion
In this blog post, we explored how to use Numba with Pandas to boost performance when applying custom functions to large datasets. By using Numba's JIT compilation capabilities, we were able to optimize the processing speed of our code significantly. Remember to be mindful of the cost of JIT compilation and use it selectively in computational-intensive parts of your code. By leveraging the power of Numba with Pandas, you can enhance the performance of your data processing tasks and unlock the full potential of your Python data analysis workflow.

# #Pandas #Numba