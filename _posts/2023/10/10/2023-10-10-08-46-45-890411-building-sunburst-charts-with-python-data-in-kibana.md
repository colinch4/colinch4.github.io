---
layout: post
title: "Building sunburst charts with Python data in Kibana"
description: " "
date: 2023-10-10
tags: [data]
comments: true
share: true
---

Sunburst charts are a popular way of visualizing hierarchical data in a circular form. They provide a clear overview of the data structure, making it easier to spot patterns and relationships. In this blog post, we will explore how to build sunburst charts using Python data in Kibana.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Preparing the Data](#preparing-the-data)
- [Creating a Sunburst Chart](#creating-a-sunburst-chart)
- [Customizing the Chart](#customizing-the-chart)
- [Conclusion](#conclusion)

## Prerequisites

To follow along with this tutorial, you will need the following:
- Kibana installed and configured
- Python installed on your local machine
- Elasticsearch cluster running

## Getting Started

Before we dive into building sunburst charts, let's ensure that we have a basic knowledge of Kibana and how to connect Python with Elasticsearch.

## Preparing the Data

To create a sunburst chart, we need hierarchical data. For this example, let's assume we have data about different product categories and their subcategories.

```python
import json

data = {
    "name": "Products",
    "children": [
        {
            "name": "Electronics",
            "children": [
                {"name": "Mobile Phones", "value": 20},
                {"name": "Laptops", "value": 15},
                {"name": "Tablets", "value": 10}
            ]
        },
        {
            "name": "Clothing",
            "children": [
                {"name": "T-Shirts", "value": 30},
                {"name": "Jeans", "value": 25},
                {"name": "Dresses", "value": 20}
            ]
        },
        {
            "name": "Furniture",
            "children": [
                {"name": "Chairs", "value": 15},
                {"name": "Tables", "value": 12},
                {"name": "Sofas", "value": 10}
            ]
        }
    ]
}

data_json = json.dumps(data)
```

In the above code snippet, we have created a simple JSON object representing the hierarchical data of product categories and subcategories.

## Creating a Sunburst Chart

Now that we have our data prepared, let's move on to visualize it in Kibana.

1. Open Kibana and go to the Visualize tab.
2. Click on "Create a visualization" and select "Sunburst" from the available options.
3. In the "Data" tab, select "JSON Input" as the source of our data.
4. Paste the `data_json` variable containing our JSON data into the input box.
5. Click on the "Play" button to preview the sunburst chart.

Congratulations! You have successfully created a basic sunburst chart using your Python data in Kibana.

## Customizing the Chart

Kibana provides several options to customize the appearance and behavior of the sunburst chart. You can modify colors, labels, and enable or disable interactivity based on your requirements.

## Conclusion

Sunburst charts are a powerful way to visualize hierarchical data in Kibana. By leveraging Python, you can generate dynamic JSON data and present it in a visually engaging manner. This tutorial should serve as a starting point for building sunburst charts with your own data.

#python #data-visualization