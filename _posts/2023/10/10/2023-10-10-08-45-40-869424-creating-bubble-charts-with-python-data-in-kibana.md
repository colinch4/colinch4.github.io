---
layout: post
title: "Creating bubble charts with Python data in Kibana"
description: " "
date: 2023-10-10
tags: []
comments: true
share: true
---

Bubble charts are a great way to visualize multidimensional data, where each data point is represented by a circle (bubble) on a chart. These charts can be particularly useful in analyzing and comparing data points with multiple attributes.

In this blog post, we will explore how to create bubble charts using Python data in Kibana, an open-source visualization platform. We will go through the steps of preparing the data, importing it into Kibana, and finally visualizing it as a bubble chart.

## Table of Contents

1. [Preparing the Data](#preparing-the-data)
2. [Importing Data into Kibana](#importing-data-into-kibana)
3. [Creating the Bubble Chart](#creating-the-bubble-chart)
4. [Conclusion](#conclusion)

## Preparing the Data

Before we can create a bubble chart in Kibana, we need to have the data ready in the correct format. The data should include at least three columns: one for the x-axis values, one for the y-axis values, and one for the size of the bubbles.

Let's assume we have a dataset with the following structure:

| X-Value | Y-Value | Bubble Size |
|---------|---------|-------------|
| 1       | 5       | 10          |
| 2       | 3       | 15          |
| 3       | 8       | 20          |
| 4       | 6       | 12          |

In this example, the `X-Value` column represents the values for the x-axis, the `Y-Value` column represents the values for the y-axis, and the `Bubble Size` column represents the size of the bubbles.

## Importing Data into Kibana

Once our data is ready, we need to import it into Kibana. Follow these steps to import the data:

1. Launch Kibana and log in to the Kibana interface.
2. Navigate to the **Management** tab.
3. Click on **Index Patterns** and then **Create index pattern**.
4. Enter the name of the index pattern and select the index containing the data to visualize.
5. Define the time filter field if applicable, or click **Create index pattern**.

Your data is now imported and ready for visualization.

## Creating the Bubble Chart

Now that our data is imported into Kibana, we can create the bubble chart:

1. Go to the **Visualize** tab in Kibana.
2. Click on **Create visualization** and choose the **Markdown** visualization type.
3. In the markdown editor, enter the following code:

```python
```