---
layout: post
title: "[Python] Image processing in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Installing Pillow

Before we begin, make sure you have Pillow installed. You can install it using pip with the following command:

```python
pip install Pillow
```

## Loading and Displaying Images

To start, let's learn how to load and display images using Pillow. We can use the `Image` module from the Pillow library for this task.

```python
from PIL import Image

# Load the image
img = Image.open('image.jpg')

# Display the image
img.show()
```

In the above code, we first import the `Image` module from Pillow. We then use the `open()` method to load an image file. The `show()` method displays the image in a separate window.

## Image Manipulation

Now that we know how to load and display images, let's dive into some image manipulation techniques. Pillow provides various methods to modify an image, such as cropping, resizing, rotating, and applying filters.

### Cropping an Image

To crop an image, we can use the `crop()` method. This method takes a tuple as an argument specifying the left, upper, right, and lower pixel coordinates of the region to crop.

```python
# Crop the image
cropped_img = img.crop((100, 100, 500, 500))

# Display the cropped image
cropped_img.show()
```

### Resizing an Image

Resizing an image can be achieved using the `resize()` method. This method takes a tuple as an argument specifying the new width and height of the image.

```python
# Resize the image
resized_img = img.resize((800, 600))

# Display the resized image
resized_img.show()
```

### Rotating an Image

To rotate an image, we can use the `rotate()` method. This method takes an angle as an argument specifying the degree of rotation.

```python
# Rotate the image by 90 degrees
rotated_img = img.rotate(90)

# Display the rotated image
rotated_img.show()
```

### Applying Filters

Pillow also provides various filters that can be applied to an image. Some common filters include blur, sharpen, and grayscale.

```python
from PIL import ImageFilter

# Apply a blur filter to the image
blurred_img = img.filter(ImageFilter.BLUR)

# Display the blurred image
blurred_img.show()

# Convert the image to grayscale
grayscale_img = img.convert('L')

# Display the grayscale image
grayscale_img.show()
```

## Conclusion

Python, along with the Pillow library, provides a powerful and easy-to-use solution for image processing tasks. In this blog post, we explored some basic image manipulation techniques like cropping, resizing, rotating, and applying filters. With Pillow's extensive capabilities, you can apply more advanced image processing techniques to enhance your images or extract useful information.

Remember to explore the Pillow documentation for more details on available methods and options. Happy image processing in Python!