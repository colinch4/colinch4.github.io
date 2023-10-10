---
layout: post
title: "Building nested pie charts with Python data in Kibana"
description: " "
date: 2023-10-10
tags: []
comments: true
share: true
---

Pie charts are a great way to visualize data distribution and proportions. However, sometimes we encounter situations where we need to further analyze specific segments within a pie chart. In such cases, nested pie charts can provide more detailed insights.

In this tutorial, we will explore how to build nested pie charts with Python data in Kibana. We will use the Elasticsearch and Kibana Python libraries to connect to Kibana and create the visualizations.

## Table of Contents
- [Setting up the Environment](#setting-up-the-environment)
- [Creating Nested Pie Charts](#creating-nested-pie-charts)
- [Conclusion](#conclusion)

## Setting up the Environment

Before we get started, we need to set up the environment by installing the necessary libraries and connecting to Kibana.

```
!pip install elasticsearch
!pip install kibana
```

Next, we import the required libraries and connect to Kibana.

```python
from elasticsearch import Elasticsearch
from kibana import Kibana

# Connect to Elasticsearch
es = Elasticsearch('http://localhost:9200')

# Connect to Kibana
kibana = Kibana('http://localhost:5601')
```

## Creating Nested Pie Charts

To create a nested pie chart in Kibana, we need to index the data into Elasticsearch and define the visualization in Kibana.

### Indexing Data

Let's assume we have a dataset that consists of sales data for different products in various regions. We will index this data into Elasticsearch.

```python
sales_data = [
    {'product': 'ProductA', 'region': 'North', 'sales': 100},
    {'product': 'ProductA', 'region': 'South', 'sales': 200},
    {'product': 'ProductB', 'region': 'North', 'sales': 150},
    {'product': 'ProductB', 'region': 'South', 'sales': 250},
    # ... more data
]

# Index the data into Elasticsearch
for sale in sales_data:
    es.index(index='sales', body=sale)
```

### Defining Nested Pie Chart Visualization

Once the data is indexed, we can define the nested pie chart visualization in Kibana. We will use the Kibana Python library to interact with the Kibana API.

```python
# Create a new Kibana visualization
visualization = kibana.visualization()

# Define the nested pie chart aggregation
aggregation = {
    'aggs': {
        'nested': {
            'nested': {
                'path': 'region'
            },
            'aggs': {
                'product': {
                    'terms': {
                        'field': 'product.keyword',
                        'size': 10
                    },
                    'aggs': {
                        'sales': {
                            'sum': {
                                'field': 'sales'
                            }
                        }
                    }
                }
            }
        }
    }
}

# Set the visualization type to nested pie chart
visualization.set_type('pie')

# Set the aggregation to the nested pie chart aggregation
visualization.set_aggregation(aggregation)

# Save the visualization in Kibana
visualization.save('Nested Pie Chart')
```

### Viewing the Nested Pie Chart

Now, we can view the created nested pie chart in Kibana. Open Kibana in your browser and navigate to the Dashboard section. Add a new visualization and select the "Nested Pie Chart" visualization we created. Customize the visualization to suit your needs, such as adding labels, colors, and filters.

## Conclusion

In this tutorial, we learned how to create nested pie charts with Python data in Kibana. We indexed the data into Elasticsearch, defined the nested pie chart visualization using the Kibana Python library, and viewed the visualization in Kibana. Nested pie charts can provide a more granular view of data distribution and allow for deeper analysis of specific segments.