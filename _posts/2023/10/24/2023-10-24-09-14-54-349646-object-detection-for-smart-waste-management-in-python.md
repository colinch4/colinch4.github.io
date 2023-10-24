---
layout: post
title: "Object detection for smart waste management in Python"
description: " "
date: 2023-10-24
tags: []
comments: true
share: true
---

With the increasing concern for environmental conservation, the concept of smart waste management is gaining popularity. Object detection plays a vital role in automating waste segregation and monitoring waste disposal areas. In this blog post, we will explore how to perform object detection in Python using the OpenCV and TensorFlow libraries.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
- [Object Detection using OpenCV](#object-detection-using-opencv)
- [Object Detection using TensorFlow](#object-detection-using-tensorflow)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction
In smart waste management systems, object detection is used to identify different types of waste items such as plastic bottles, cans, and paper, among others. This enables efficient waste segregation and subsequent recycling or disposal. Python provides several libraries and tools that aid in object detection, including OpenCV and TensorFlow.

## Prerequisites
Before proceeding with object detection, ensure that you have the following prerequisites installed:
- Python (version 3.6+)
- OpenCV library
- TensorFlow library

## Setting Up the Environment
To begin, let's create a virtual environment and install the necessary libraries. Open your terminal and follow these steps:

1. Create a virtual environment:
```shell
$ python -m venv object_detection_env
```

2. Activate the virtual environment:
```shell
$ source object_detection_env/bin/activate
```

3. Install the OpenCV library:
```shell
$ pip install opencv-python
```

4. Install the TensorFlow library:
```shell
$ pip install tensorflow
```

### Object Detection using OpenCV
OpenCV is a powerful computer vision library that provides various functions and pre-trained models for object detection. Let's write a Python script that utilizes OpenCV for detecting objects in an image:

```python
import cv2

def detect_objects(image_path):
    # Load the pre-trained model
    net = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')

    # Load the image
    image = cv2.imread(image_path)

    # Obtain the dimensions of the image
    height, width, _ = image.shape

    # Prepare the input blob
    blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)

    # Set the input for the network
    net.setInput(blob)

    # Perform forward pass and get the detections
    detections = net.forward()

    # Process the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            class_name = class_names[class_id]
            print("Detected object: ", class_name)

# Specify the path to the image
image_path = 'waste_image.jpg'

# Call the detect_objects function
detect_objects(image_path)
```

In this example, we first load a pre-trained model using `cv2.dnn.readNetFromTensorflow()`. Then, we load an image and obtain its dimensions. Next, we prepare the input image using `cv2.dnn.blobFromImage()` and set it as the network input using `net.setInput()`. Finally, we perform a forward pass to obtain the detections and process them.

### Object Detection using TensorFlow
TensorFlow is a popular deep learning framework that provides pre-trained models for various computer vision tasks, including object detection. Let's use the TensorFlow Object Detection API to perform object detection:

```python
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

def detect_objects(image_path):
    # Path to the frozen graph and label map
    PATH_TO_FROZEN_GRAPH = 'frozen_inference_graph.pb'
    PATH_TO_LABELS = 'label_map.pbtxt'

    # Load the frozen graph
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    # Load the label map
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=90, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the image
    image = cv2.imread(image_path)
    image_expanded = np.expand_dims(image, axis=0)

    # Perform object detection
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # Get handles to input and output tensors
            tensor_dict = {}
            for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes', 'detection_masks']:
                tensor_name = key + ':0'
                tensor_dict[key] = detection_graph.get_tensor_by_name(tensor_name)

            # Run inference
            output_dict = sess.run(tensor_dict, feed_dict={image_tensor: image_expanded})

            # Visualization of the results
            vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(output_dict['detection_boxes']),
                np.squeeze(output_dict['detection_classes']).astype(np.int32),
                np.squeeze(output_dict['detection_scores']),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8)

            plt.figure(figsize=(12, 8))
            plt.imshow(image)
            plt.axis('off')
            plt.show()

# Specify the path to the image
image_path = 'waste_image.jpg'

# Call the detect_objects function
detect_objects(image_path)
```

In this example, we first load the frozen graph and label map. Then, we load the image and expand its dimensions to match the network input requirements. We use a TensorFlow session to run inference on the image and obtain the object detection results. Finally, we visualize the detected objects using `visualize_boxes_and_labels_on_image_array()`.

## Conclusion
Object detection plays a crucial role in smart waste management systems. In this blog post, we explored how to perform object detection using OpenCV and TensorFlow in Python. By applying these techniques, waste segregation and monitoring can be automated, leading to more efficient and sustainable waste management practices.

## References
- [OpenCV Documentation](https://docs.opencv.org/)
- [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)