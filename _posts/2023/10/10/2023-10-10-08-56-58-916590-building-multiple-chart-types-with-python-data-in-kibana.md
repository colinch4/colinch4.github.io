---
layout: post
title: "Building multiple chart types with Python data in Kibana"
description: " "
date: 2023-10-10
tags: [Kibana]
comments: true
share: true
---

Kibana is a powerful data visualization tool that allows you to explore, analyze, and visualize your data in real-time. While Kibana offers a wide range of built-in chart types, sometimes you may need to build custom charts to better represent your data. In this tutorial, we will explore how to build multiple chart types using Python data in Kibana.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setting up Kibana](#setting-up-kibana)
- [Generating Python Data](#generating-python-data)
- [Creating a Custom Index](#creating-a-custom-index)
- [Importing Python Data into Kibana](#importing-python-data-into-kibana)
- [Building Multiple Chart Types](#building-multiple-chart-types)
  - [Line Chart](#line-chart)
  - [Bar Chart](#bar-chart)
  - [Pie Chart](#pie-chart)
- [Conclusion](#conclusion)
- [Hashtags](#hashtags)

## Prerequisites

To follow along with this tutorial, you will need the following:

- Kibana installed and running on your local machine.
- Python installed on your machine.
- Knowledge of the Elasticsearch Query Language (EQL) and basic Python programming.

## Setting up Kibana

Before we begin, ensure that Kibana is up and running on your machine. You can download and install Kibana from the official Elastic website.

## Generating Python Data

In order to build multiple chart types, we need sample data to work with. Let's generate some random data using Python. Below is an example code snippet that generates a random dataset using the `pandas` library:

```python
import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)
data = pd.DataFrame({
    'Year': pd.date_range(start='2000-01-01', periods=10, freq='A'),
    'Sales': np.random.randint(low=100, high=1000, size=(10,))
})

print(data)
```

This code snippet generates a DataFrame with two columns: 'Year' and 'Sales'.

## Creating a Custom Index

In order to import the Python data into Kibana, we need to create a custom index in Elasticsearch. To create an index, we can use the following Python code snippet:

```python
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch()

# Create an index
index_name = "my_custom_index"
es.indices.create(index=index_name, ignore=400)
```

You can replace `"my_custom_index"` with your desired index name.

## Importing Python Data into Kibana

To import the Python data into Kibana, we can utilize the Elasticsearch Python client. Here's an example code snippet that demonstrates how to bulk index the data into Elasticsearch:

```python
from elasticsearch.helpers import bulk

# Prepare the data for bulk indexing
actions = [
    {
        '_index': index_name,
        '_source': {
            'Year': row['Year'].strftime('%Y-%m-%d'),
            'Sales': row['Sales']
        }
    }
    for _, row in data.iterrows()
]

# Bulk index the data
bulk(es, actions)
```

Make sure to replace `index_name` with your custom index name. This code snippet converts the 'Year' column into the required date format and bulk indexes the data into Elasticsearch.

## Building Multiple Chart Types

### Line Chart

To build a line chart in Kibana using Python data, follow these steps:

1. Access the Kibana UI via your web browser.
2. Click on "Create new visualization" from the sidebar.
3. Choose a new index pattern that matches your custom index.
4. Select the "Line" chart type.
5. Configure the X-axis to use the 'Year' field and the Y-axis to use the 'Sales' field.
6. Click "Apply changes" to generate the line chart.

### Bar Chart

To create a bar chart in Kibana using Python data, follow these steps:

1. Access the Kibana UI.
2. Click on "Create new visualization".
3. Choose a new index pattern.
4. Select the "Vertical bar" chart type.
5. Configure the X-axis to use the 'Year' field and the Y-axis to use the 'Sales' field.
6. Click "Apply changes" to generate the bar chart.

### Pie Chart

To generate a pie chart in Kibana using Python data, follow these steps:

1. Access the Kibana UI.
2. Click on "Create new visualization".
3. Choose a new index pattern.
4. Select the "Pie" chart type.
5. Configure the "Slice size" to use the 'Sales' field.
6. Click "Apply changes" to generate the pie chart.

## Conclusion

In this tutorial, we explored how to build multiple chart types using Python data in Kibana. We covered generating Python data, creating custom indices, importing data into Kibana, and building line, bar, and pie charts using Python data.

By leveraging Python's data generation capabilities and Kibana's visualization features, you can create powerful and customized charts to analyze your data effectively.

## Hashtags

#Python #Kibana