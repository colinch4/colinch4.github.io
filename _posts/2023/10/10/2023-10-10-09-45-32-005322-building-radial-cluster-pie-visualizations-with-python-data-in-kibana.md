---
layout: post
title: "Building radial cluster pie visualizations with Python data in Kibana"
description: " "
date: 2023-10-10
tags: []
comments: true
share: true
---

Data visualization is a crucial aspect of data analysis, as it helps to identify patterns, trends, and relationships within the data. Kibana, a powerful open-source data visualization tool, provides various visualization options to explore your data effectively. In this blog post, we will explore how to build radial cluster pie visualizations using Python data in Kibana.

## What is a radial cluster pie visualization?

A radial cluster pie visualization is a type of chart that displays hierarchical data using concentric circles. It helps to represent the relationships between different categories and sub-categories in a clear and intuitive manner. Each circle represents a category, and the size of the slices within each circle indicates the proportion of data for each sub-category.

## Setting up the environment

Before we start, make sure you have Python and the Elasticsearch Python library installed. You can install it using the following command:

```python
pip install elasticsearch
```

Next, we need to import the necessary libraries and establish a connection to Elasticsearch:

```python
from elasticsearch import Elasticsearch
es = Elasticsearch('<your_elasticsearch_host>:<your_elasticsearch_port>')
```
Replace `<your_elasticsearch_host>` and `<your_elasticsearch_port>` with the appropriate values for your Elasticsearch instance.

## Retrieving data from Elasticsearch using Python

To fetch the data needed for the radial cluster pie visualization, we'll run a query using the Elasticsearch Python library. Let's assume we want to visualize the number of orders by product category. Here is an example query:

```python
body = {
  "size": 0,
  "aggs": {
    "categories": {
      "terms": {
        "field": "product_category.keyword",
        "size": 10
      }
    }
  }
}

response = es.search(index='your_index_name', body=body)
```

In the above code, we set the size to 0 to exclude the actual documents from the response and only retrieve the aggregations. We then use the terms aggregation to aggregate the `product_category` field and limit the number of categories to 10.

## Transforming the data for radial cluster pie visualization

To prepare the data for the radial cluster pie visualization, we need to extract the categories and their corresponding counts from the Elasticsearch response. Here is an example code snippet that accomplishes this:

```python
categories = []
counts = []

agg_buckets = response['aggregations']['categories']['buckets']

for bucket in agg_buckets:
    category = bucket['key']
    count = bucket['doc_count']
    categories.append(category)
    counts.append(count)
```

Now, we have two lists: `categories` that contains the categories and `counts` that contains the corresponding counts.

## Visualizing the data in Kibana

To create a radial cluster pie visualization in Kibana:

1. Open Kibana and go to the dashboard where you want to add the visualization.
2. Click on "Visualize" in the left-hand navigation menu.
3. Click on "Create Visualization" and select "Pie" from the available options.
4. In the "Data" tab, ensure that the Elasticsearch index containing your data is selected.
5. In the "Bucket" section, select the "Split Slices" aggregation.
6. Choose the field where you stored your categories (e.g., `product_category`).
7. Customize the visualization by adjusting the labels, colors, and other options as per your preference.
8. Click on "Save" to save the radial cluster pie visualization.

## Conclusion

In this blog post, we explored how to build radial cluster pie visualizations using Python data in Kibana. We learned how to set up the environment, retrieve data from Elasticsearch using Python, transform the data for the visualization, and create the visualization in Kibana. Radial cluster pies are an excellent choice for representing hierarchical data and can provide valuable insights into the relationships between categories and sub-categories.