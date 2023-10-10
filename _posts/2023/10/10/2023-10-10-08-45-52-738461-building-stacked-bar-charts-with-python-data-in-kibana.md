---
layout: post
title: "Building stacked bar charts with Python data in Kibana"
description: " "
date: 2023-10-10
tags: [stackedbarchart, Kibana]
comments: true
share: true
---

Kibana is a powerful data visualization tool that can be used to create various types of charts and graphs. In this tutorial, we will focus on building stacked bar charts using Python data in Kibana.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setting up Python Script](#setting-up-python-script)
- [Data Formatting](#data-formatting)
- [Creating Stacked Bar Chart in Kibana](#creating-stacked-bar-chart-in-kibana)
- [Conclusion](#conclusion)

## Introduction

Stacked bar charts are useful for comparing multiple categories of data and understanding their contributions to the total value. They provide a visual representation of the distributions and proportions within the data.

## Prerequisites

To follow along with this tutorial, you will need:

- Python 3 installed on your machine.
- A dataset in Python with categorical data.

## Setting up Python Script

First, we need to set up a Python script to generate the data we want to visualize in Kibana. You can use any method you prefer to generate the data, such as reading from a database, CSV file, or directly creating a Python list or dictionary.

Here's an example of generating a dataset using a Python list:

```python
data = [
    {"category": "A", "value": 10},
    {"category": "B", "value": 15},
    {"category": "C", "value": 20},
    {"category": "A", "value": 5},
    {"category": "B", "value": 8},
    {"category": "C", "value": 12}
]
```

## Data Formatting

Kibana requires data to be in a specific format for visualization. We need to format our Python data into a suitable JSON format.

```python
formatted_data = []
for item in data:
    formatted_data.append({
        "x": item["category"],
        "y": item["value"]
    })

import json
formatted_data_json = json.dumps(formatted_data)
```

## Creating Stacked Bar Chart in Kibana

1. Open Kibana in your web browser and log in to your account.

2. Create a new index pattern for your data.

3. Go to the "Visualize" tab in Kibana and click on "Create Visualization".

4. Select "Vertical Bar Chart" as the visualization type.

5. In the "Data" tab, select your index pattern and choose the appropriate aggregation and field settings.

6. In the "Metrics & Axes" tab, set the "Y-Axis" to use the "Sum" aggregation and select the field that represents the values.

7. In the "Buckets" tab, select the "X-Axis" aggregation type as "Terms" and choose the field that represents the categories.

8. Enable stacking by clicking on the "Advanced" tab and setting "Negative values" to "Stacked".

9. Customize the chart appearance and labels as needed.

10. Save the visualization and view it in the "Dashboard" tab.

## Conclusion

Stacked bar charts are an effective way to visualize categorical data in Kibana. By setting up a Python script to generate the required data and formatting it correctly, we can create informative and visually appealing visualizations. Experiment with different datasets and parameters to explore the capabilities of stacked bar charts in Kibana.

#stackedbarchart #Kibana