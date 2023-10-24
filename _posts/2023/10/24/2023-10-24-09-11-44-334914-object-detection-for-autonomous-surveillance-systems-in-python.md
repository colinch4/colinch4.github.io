---
layout: post
title: "Object detection for autonomous surveillance systems in Python"
description: " "
date: 2023-10-24
tags: [References]
comments: true
share: true
---

In recent years, object detection has emerged as a crucial technology in the field of computer vision. It plays a key role in various applications, including autonomous surveillance systems. These systems rely on object detection algorithms to detect and track objects of interest in real-time video streams.

In this article, we will explore how to perform object detection using Python. We will utilize the powerful OpenCV library, along with a pre-trained deep learning model called YOLO (You Only Look Once).

## Table of Contents
1. Introduction to Object Detection
2. Installing OpenCV and YOLO
3. Loading the Pre-trained Model
4. Performing Object Detection
5. Visualizing the Detected Objects
6. Conclusion

## Introduction to Object Detection

Object detection is the task of locating and classifying objects within an image or video. It involves identifying the presence and location of specific objects of interest in the input data.

There are several approaches to object detection, ranging from traditional computer vision techniques to deep learning-based methods. Deep learning models, such as YOLO, have gained popularity due to their high accuracy and real-time performance.

## Installing OpenCV and YOLO

To get started with object detection in Python, we first need to install the necessary libraries. We can install OpenCV and other dependencies using the pip package manager:

```python
pip install opencv-python
```

For YOLO, we need to download the pre-trained model weights and configuration files. These can be obtained from the official repository:

```python
wget https://pjreddie.com/media/files/yolov3.weights
wget https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg
wget https://github.com/pjreddie/darknet/blob/master/data/coco.names
```

## Loading the Pre-trained Model

Once we have installed the required dependencies and downloaded the YOLO files, we can proceed to load the pre-trained model in Python:

```python
import cv2

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
```

The `cv2.dnn.readNet` function loads the pre-trained YOLO model from the weights and configuration files. We also load the list of object classes from the `coco.names` file.

## Performing Object Detection

To perform object detection on an input image, we need to pass the image through the YOLO model and extract the detected objects:

```python
def detect_objects(img):
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    output_layers = net.getUnconnectedOutLayersNames()
    outputs = net.forward(output_layers)
    return outputs

image = cv2.imread("input.jpg")
outputs = detect_objects(image)
```

The `cv2.dnn.blobFromImage` function preprocesses the input image and transforms it into a format suitable for YOLO. We then pass the preprocessed image through the model using the `net.forward` method.

## Visualizing the Detected Objects

Finally, we can visualize the detected objects by drawing bounding boxes around them in the original image:

```python
def draw_boxes(img, outputs):
    height, width, _ = img.shape
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                label = f"{classes[class_id]}: {confidence:.2f}"
                cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

draw_boxes(image, outputs)
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

The `draw_boxes` function iterates over the detected objects and draws bounding boxes around them. It also displays the label and confidence score for each object.

## Conclusion

Object detection is a fundamental task in computer vision and has numerous applications, particularly in autonomous surveillance systems. In this article, we explored how to perform object detection using Python and the popular YOLO model. By leveraging the power of deep learning and libraries like OpenCV, we can build advanced surveillance systems capable of detecting and tracking objects in real-time video streams.

#References:
- [OpenCV documentation](https://docs.opencv.org/4.5.3/)
- [YOLO official website](https://pjreddie.com/darknet/yolo/)