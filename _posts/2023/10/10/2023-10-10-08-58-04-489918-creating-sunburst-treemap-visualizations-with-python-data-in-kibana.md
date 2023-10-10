---
layout: post
title: "Creating sunburst treemap visualizations with Python data in Kibana"
description: " "
date: 2023-10-10
tags: []
comments: true
share: true
---

Treemaps are a popular and effective way to visualize hierarchical data. The sunburst treemap, in particular, provides a radial view of the data, allowing for easy identification of the main categories and their subcategories. If you are working with Python data and want to create sunburst treemap visualizations, you can leverage the power of Kibana.

## What is Kibana?

Kibana is an open-source analytics and visualization platform that works with the Elastic Stack. It allows you to explore, analyze, and visualize your data stored in ElasticSearch. With Kibana, you can create stunning visualizations and dashboards using various chart types, including sunburst treemaps.

## Prerequisites

To follow along with this tutorial, you'll need the following prerequisites:

- Python installed on your machine
- ElasticSearch and Kibana set up and running
- Python libraries: elasticsearch, pandas, and matplotlib

You can install the necessary Python libraries using pip:

```python
pip install elasticsearch pandas matplotlib
```

## Getting the Data

First, you need to have the data you want to visualize in a format that is compatible with Kibana. One way to achieve this is to use the ElasticSearch Python library to index your data into ElasticSearch.

For example, let's assume you have a dataset of sales transactions with the following structure:

| Transaction ID | Category   | Subcategory   | Amount |
|----------------|------------|---------------|--------|
| 1              | Electronics| Laptops       | 1000   |
| 2              | Electronics| Smartphones   | 800    |
| 3              | Furniture  | Sofas         | 1500   |
| 4              | Furniture  | Chairs        | 500    |

You can index this data into ElasticSearch using the Python library like so:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch()

data = [
    {"TransactionID": 1, "Category": "Electronics", "Subcategory": "Laptops", "Amount": 1000},
    {"TransactionID": 2, "Category": "Electronics", "Subcategory": "Smartphones", "Amount": 800},
    {"TransactionID": 3, "Category": "Furniture", "Subcategory": "Sofas", "Amount": 1500},
    {"TransactionID": 4, "Category": "Furniture", "Subcategory": "Chairs", "Amount": 500},
]

for item in data:
    es.index(index="sales", body=item)
```

## Creating the Sunburst Treemap Visualization in Kibana

Now that you have the data indexed in ElasticSearch, you can create the sunburst treemap visualization in Kibana.

1. Open the Kibana dashboard in your web browser.
2. Go to the "Visualize" tab in the navigation menu.
3. Click on "Create new visualization" and select "Sunburst."

4. In the "Data" tab, configure the following settings:
   - Select the appropriate index pattern (e.g., "sales").
   - Choose "Count" as the aggregation.
   - Split the slices by "Category" and "Subcategory" using the "Add Sub-Buckets" option.

5. In the "Options" tab, you can customize the appearance of the sunburst treemap. You can modify colors, labels, and other settings to suit your preferences.

6. Click on the "Save" button to save the visualization.

Congratulations! You have successfully created a sunburst treemap visualization in Kibana using the Python data indexed in ElasticSearch. You can now use this visualization to explore and analyze your hierarchical data.

## Conclusion

In this tutorial, we discussed how to create sunburst treemap visualizations with Python data in Kibana. By leveraging the power of Kibana and ElasticSearch, you can easily analyze and visualize your hierarchical data in a dynamic and interactive manner.