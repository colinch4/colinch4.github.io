---
layout: post
title: "Creating sunburst cluster bar charts with Python data in Kibana"
description: " "
date: 2023-10-10
tags: [Kibana]
comments: true
share: true
---

In this tutorial, we will explore how to create Sunburst Cluster Bar Charts using Python data in Kibana. Sunburst Cluster Bar Charts are a great way to visualize hierarchical data and display the relationship between different categories. 

## Prerequisites

Before we get started, make sure you have the following:

- Python installed on your machine
- Kibana installed and running
- Python Elasticsearch library installed (`pip install elasticsearch`)

## Step 1: Preparing the Data

To create the Sunburst Cluster Bar Chart, we need to have our data in the appropriate format. The data should represent a hierarchical structure, where each level has a parent-child relationship. For example, let's assume we have data representing different countries, their regions, and the number of sales in each region. 

Here is an example dataset:

| Country   | Region      | Sales |
| --------- | ----------- | ----- |
| USA       | West        | 100   |
| USA       | East        | 150   |
| Canada    | East        | 200   |
| Canada    | West        | 120   |
| Australia | North       | 80    |
| Australia | South       | 90    |

## Step 2: Setting up the ElasticSearch Index

To use our Python data in Kibana, we need to index it in Elasticsearch. In this step, we will create an Elasticsearch index and populate it with our dataset.

First, let's establish a connection to Elasticsearch using the Python Elasticsearch library:

```python
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["localhost"])
```

Next, we will create an index and define the mapping for our data:

```python
index_name = "sales_data"
mapping = {
    "mappings": {
        "properties": {
            "country": {"type": "keyword"},
            "region": {"type": "keyword"},
            "sales": {"type": "integer"}
        }
    }
}

es.indices.create(index=index_name, body=mapping)
```

Finally, we can loop through our dataset and index the documents in Elasticsearch:

```python
data = [
    {"country": "USA", "region": "West", "sales": 100},
    {"country": "USA", "region": "East", "sales": 150},
    {"country": "Canada", "region": "East", "sales": 200},
    {"country": "Canada", "region": "West", "sales": 120},
    {"country": "Australia", "region": "North", "sales": 80},
    {"country": "Australia", "region": "South", "sales": 90}
]

for doc in data:
    es.index(index=index_name, body=doc)
```

## Step 3: Visualizing Sunburst Cluster Bar Charts in Kibana

Now that our data is indexed in Elasticsearch, we can create the Sunburst Cluster Bar Chart in Kibana.

1. Open Kibana in your web browser by navigating to `http://localhost:5601` (assuming Kibana is running on the default port).
2. Click on **Explore on my own** to start creating a new visualization.
3. Select the Elasticsearch index you created in Step 2 as the index pattern.
4. Go to the **Visualize** section and click on **Create visualization**.
5. Choose **Sunburst** as the visualization type.
6. Configure the following settings:
   - **Metric**: Choose **Sum** and specify the field as `sales`.
   - **Buckets**: 
     - **Split Slices**: Add a **Terms** aggregation for `country` and `region` in the hierarchical order. Set the order to **Desc** based on the sum of sales.
     - **Split Chart**: Add a **Metrics** aggregation for `sales` and choose **Sum**. This will display the sales for each country and region.
7. Click on **Apply changes** to see the preview of the Sunburst Cluster Bar Chart.
8. Customize the chart appearance by modifying labels, colors, and other settings according to your preference.
9. Save the visualization to display it on your Kibana dashboard.

## Conclusion

By following these steps, you can create visually appealing Sunburst Cluster Bar Charts using Python data in Kibana. This allows you to effectively analyze and present hierarchical data with ease. 

Make sure to experiment with different datasets and visual options to achieve the best visualization for your specific needs.

#python #Kibana