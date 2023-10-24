---
layout: post
title: "Non-maximum suppression (NMS) for post-processing in object detection in Python"
description: " "
date: 2023-10-24
tags: [references]
comments: true
share: true
---

In object detection tasks, the initial output of a model often includes multiple bounding boxes for the same object. This can lead to redundant detections and affect the overall accuracy of the system. One popular technique used for post-processing in object detection is *Non-maximum Suppression* (NMS).

NMS helps eliminate redundant bounding boxes by selecting the most accurate ones based on their intersection over union (IoU) value. This technique ensures that each object is represented by only one bounding box and improves the final results of the object detection algorithm.

In this article, we will discuss how to implement NMS in Python for object detection.

## What is Intersection over Union (IoU)?

Before diving into NMS, let's understand the concept of Intersection over Union (IoU). IoU is a measure of overlap between two bounding boxes. It is calculated by dividing the area of intersection between the boxes by the area of their union.

![IoU](https://i.imgur.com/6qbuBBu.png)

## NMS Algorithm

The NMS algorithm can be summarized in the following steps:

1. Sort the bounding boxes based on their confidence scores or probabilities.
2. Start with the highest confidence box and consider it as a selected box.
3. Calculate the IoU of this selected box with all other boxes.
4. Discard the boxes that have a high IoU (above a certain threshold) with the selected box.
5. Repeat steps 3 and 4 until all boxes have been processed.

## Implementing NMS in Python

Now, let's see how we can implement NMS in Python. We'll assume that we have a list of bounding boxes with their confidence scores.

```python
def nms(bboxes, iou_threshold):
    # Sort the bounding boxes based on their confidence scores
    sorted_bboxes = sorted(bboxes, key=lambda x: x['score'], reverse=True)

    selected_bboxes = []

    while sorted_bboxes:
        # Select the bounding box with the highest confidence score
        selected = sorted_bboxes.pop(0)
        selected_bboxes.append(selected)

        # Calculate the IoU of the selected box with remaining boxes
        remaining_bboxes = []
        for bbox in sorted_bboxes:
            iou = calculate_iou(selected, bbox)
            if iou < iou_threshold:
                remaining_bboxes.append(bbox)
        
        sorted_bboxes = remaining_bboxes

    return selected_bboxes
```

In the above example code, `bboxes` is a list of dictionaries containing the bounding box coordinates (`x1`, `y1`, `x2`, `y2`) and their respective confidence scores (`score`). The `iou_threshold` specifies the minimum IoU required for two boxes to be considered as redundant.

The `nms` function sorts the bounding boxes based on their confidence scores, selects the box with the highest score, and calculates the IoU with all remaining boxes. If the IoU is below the threshold, the box is considered as a selected box. The process is repeated until all boxes have been processed.

## Conclusion

Non-maximum Suppression (NMS) is an important step in object detection to remove redundant bounding boxes and improve the accuracy of the system. In this article, we discussed the concept of IoU and the steps involved in implementing NMS in Python.

By incorporating NMS in your object detection pipeline, you can ensure that only the most accurate bounding boxes are retained, leading to more precise and reliable object detection results.

#references:
- [Non-maximum Suppression](https://en.wikipedia.org/wiki/Non-maximum_suppression)
- [Intersection over Union (IoU)](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)
- [Object Detection using Deep Learning](https://towardsdatascience.com/object-detection-using-deep-learning-approaches-an-end-to-end-theoretical-perspective-4ca8b847987d)