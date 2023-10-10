---
layout: post
title: "Creating zooplot donut charts with Python data in Kibana"
description: " "
date: 2023-10-10
tags: []
comments: true
share: true
---

Kibana is a popular data visualization tool that allows you to explore, analyze, and visualize data stored in Elasticsearch. While Kibana provides a range of built-in visualizations, you may sometimes want to create custom visualizations using external libraries like Zooplot in Python. In this tutorial, we will walk through the process of creating donut charts using Python data in Kibana.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting up the environment](#setting-up-the-environment)
- [Exporting data from Kibana](#exporting-data-from-kibana)
- [Creating donut charts with Zooplot](#creating-donut-charts-with-zooplot)
- [Visualizing donut charts in Kibana](#visualizing-donut-charts-in-kibana)
- [Conclusion](#conclusion)

## Prerequisites

Before we get started, make sure you have the following prerequisites in place:

- Python installed on your machine
- Kibana and Elasticsearch installed and running

## Setting up the environment

To get started, we need to set up the environment to work with Zooplot and Python. Follow these steps:

1. Create a new virtual environment by running the following command in your terminal or command prompt:

   ```
   python -m venv zooplot_env
   ```

2. Activate the virtual environment:

   - On Windows:

     ```
     .\zooplot_env\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source zooplot_env/bin/activate
     ```

3. Install the required packages:

   ```
   pip install pandas zooplot
   ```

With the environment set up, we're ready to proceed to the next steps.

## Exporting data from Kibana

First, we need to export the data we want to visualize from Kibana in a format that can be loaded into Python. To export data from Kibana:

1. Open Kibana in your browser and navigate to the Discover tab.
2. Set up your desired filters and queries to narrow down the data.
3. Click on the **CSV** button in the toolbar at the top right of the screen.
4. Save the exported CSV file to a location on your local machine.

## Creating donut charts with Zooplot

Now, let's create the donut charts using the exported data in Python with the help of the Zooplot library.

```python
import pandas as pd
import zooplot as zp

# Load the exported CSV file into a DataFrame
data = pd.read_csv('path/to/exported/data.csv')

# Group the data by a categorical variable, and count the occurrences
grouped_data = data.groupby('category').size().reset_index(name='count')

# Create the donut chart using Zooplot
zp.donut(grouped_data['category'], labels=grouped_data['count'])
```

In the code above, we first load the exported CSV file into a Pandas DataFrame. Next, we group the data by a categorical variable (e.g., category) and count the occurrences of each category. Finally, we pass the category and count data to the `zp.donut` function to create the donut chart.

## Visualizing donut charts in Kibana

To visualize the donut charts in Kibana, we need to export the generated chart image from Python and import it into Kibana.

```python
zp.savefig('path/to/save/chart.png')
```

The `zp.savefig` function saves the chart image to a specified location on your local machine.

Now, follow these steps to import the chart image into Kibana:

1. Open Kibana in your browser and go to the Dashboard tab.
2. Click on "Create new" to create a new dashboard.
3. Click on "Add" to add a new visualization.
4. Choose the type of visualization you want to create (e.g., Markdown visualization).
5. In the Markdown editor, use the following syntax to display the chart image:

   ```
   ![Donut Chart](path/to/save/chart.png)
   ```

6. Save the visualization and add it to your dashboard.

## Conclusion

In this tutorial, we have seen how to create donut charts using Python data in Kibana. By combining the power of Zooplot and Kibana, you can create custom visualizations to better explore and present your data. Experiment with different chart types and settings to create visually appealing and insightful visualizations that meet your requirements.