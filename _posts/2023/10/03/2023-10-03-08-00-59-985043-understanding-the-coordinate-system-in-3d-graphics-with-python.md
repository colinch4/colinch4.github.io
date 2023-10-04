---
layout: post
title: "Understanding the coordinate system in 3D graphics with Python"
description: " "
date: 2023-10-03
tags: [3DGraphics]
comments: true
share: true
---

In the world of 3D graphics, understanding the coordinate system is fundamental. It determines how objects are positioned and how light interacts with them. In this blog post, we will delve into the coordinate system used in 3D graphics and explore how to work with it using Python.

## The Cartesian Coordinate System

The most common coordinate system used in 3D graphics is the Cartesian coordinate system. It consists of three axes - X, Y, and Z - that intersect at a point called the origin. The X axis represents horizontal movement, the Y axis represents vertical movement, and the Z axis represents depth or distance from the viewer.

### Representing Points in 3D Space

In Python, we can use various libraries like `numpy` and `matplotlib` to visualize and manipulate points in 3D space. Let's take a look at a simple example using `matplotlib`:

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a point at (2, 3, 4)
x, y, z = 2, 3, 4
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
```

In this example, we create a figure and add a 3D subplot to it. We then create a point at coordinates (2, 3, 4) using the `scatter` function and specify the color and marker style. Finally, we label the axes and display the plot.

### Transformations in 3D Graphics

The coordinate system allows us to perform various transformations on 3D objects. Some common transformations include translation, rotation, and scaling.

#### Translation

Translation moves a 3D object in space without changing its orientation. In Python, we can achieve translation using vector addition. Here's an example using `numpy`:

```python
import numpy as np

# Define the original point
point = np.array([2, 3, 4])

# Define the translation vector
translation = np.array([1, 2, 3])

# Perform translation
translated_point = point + translation

print("Translated Point:", translated_point)
```

In this example, we define the original point at (2, 3, 4) and the translation vector as (1, 2, 3). We add the original point and the translation vector using element-wise addition to get the translated point.

#### Rotation

Rotation changes the orientation of a 3D object. Common rotation operations include rotating around the X, Y, or Z axis. In Python, we can use libraries like `numpy` to perform rotations. Here's an example:

```python
import numpy as np

# Define the original point
point = np.array([2, 3, 4])

# Define the rotation matrix around the X axis
angle = np.pi / 2
rotation_matrix = np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])

# Perform rotation
rotated_point = np.dot(rotation_matrix, point)

print("Rotated Point:", rotated_point)
```

In this example, we define the original point and the rotation matrix around the X axis. We then use the dot product between the rotation matrix and the original point to get the rotated point.

### Conclusion

Understanding the coordinate system is crucial in 3D graphics. It provides a framework for positioning objects in 3D space and performing transformations on them. By leveraging libraries like `numpy` and `matplotlib` in Python, we can easily visualize and manipulate points in 3D space.

#Python #3DGraphics