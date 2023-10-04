---
layout: post
title: "Creating basic geometrical shapes in Python 3D graphics"
description: " "
date: 2023-10-03
tags: [graphics]
comments: true
share: true
---

Python provides a variety of libraries for creating 3D graphics, including NumPy and Matplotlib. In this tutorial, we will explore how to create basic geometrical shapes using these libraries.

## Prerequisites

Before we begin, make sure you have the following installed:

- Python 3: https://www.python.org/downloads/
- NumPy: `pip install numpy`
- Matplotlib: `pip install matplotlib`

## Creating a Sphere

To create a sphere in Python 3D graphics, we can use the `mplot3d` toolkit from Matplotlib. Here's an example code snippet:

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='b')

plt.show()
```

In this code, we first import the necessary libraries and set up the figure and subplot. We then define the u, v parameters that determine the space in which the sphere is created.

Next, we use the NumPy `outer` function to create x, y, and z arrays representing the points on the surface of the sphere. Finally, we use the `plot_surface` function of the Axes3D object to actually create and display the sphere.

## Creating a Cube

To create a cube in Python 3D graphics, we can again use the `mplot3d` toolkit from Matplotlib. Here's an example code snippet:

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.array([[0, 0, 1, 1, 0, 0, 1, 1],
              [1, 1, 1, 1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 1, 1, 0]])
y = np.array([[0, 1, 1, 0, 0, 1, 1, 0],
              [0, 0, 1, 1, 0, 0, 1, 1],
              [1, 1, 1, 1, 0, 0, 0, 0]])
z = np.array([[0, 0, 0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 1, 1, 1, 1],
              [0, 1, 1, 0, 0, 0, 1, 1]])

ax.plot_surface(x, y, z, alpha=0.5, color='r')

plt.show()
```

In this code, we first import the necessary libraries and set up the figure and subplot. We then define the x, y, and z arrays representing the coordinates of the cube's vertices.

Next, we use the `plot_surface` function of the Axes3D object to create and display the cube. The `alpha` parameter controls the transparency of the cube, and the `color` parameter sets its color.

## Conclusion

With the help of libraries such as NumPy and Matplotlib, creating basic geometrical shapes in Python 3D graphics becomes quite straightforward. You can further customize and enhance these shapes to suit your specific needs.

#python #graphics