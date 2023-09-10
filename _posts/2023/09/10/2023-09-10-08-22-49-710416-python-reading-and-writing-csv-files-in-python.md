---
layout: post
title: "[Python] Reading and writing CSV files in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

CSV (Comma Separated Values) files are a popular way of storing and exchanging data in a plain text format. They are widely used for data manipulation and analysis tasks. In this blog post, we will explore how to read and write CSV files in Python.

### Reading CSV Files

Python provides a built-in module called `csv` that makes it easy to read CSV files. The `csv` module provides a `reader` object that allows us to iterate over the rows of a CSV file.

Here's an example that demonstrates how to read a CSV file and print its contents:

```python
import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
```

In the above example, we first open the file using the `open` function in read mode (`'r'`). Then, we create a `csv_reader` object using the `reader` function from the `csv` module. Finally, we loop over the rows of the CSV file and print each row.

### Writing CSV Files

In addition to reading CSV files, Python's `csv` module also allows us to write data to CSV files. We can use the `writer` object to write data to a CSV file.

Here's an example that demonstrates how to write data to a CSV file:

```python
import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'London'],
    ['Bob', '35', 'Paris']
]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)
```

In the above example, we define a list of lists `data`, where each inner list represents a row of data. We open a new file called `output.csv` in write mode (`'w'`) and create a `csv_writer` object. Next, we loop through each row in `data` and use the `writerow` function to write the row to the CSV file.

### Handling CSV Header

CSV files often include a header row that contains the names of the columns. When reading or writing CSV files, it's common to handle the header row separately.

To skip the header row when reading a CSV file, we can use the `next` function to advance the reader object by one row:

```python
import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        print(row)
```

To include a header row when writing a CSV file, we can write the header row before the data rows:

```python
import csv

data = [
    ['Name', 'Age', 'City'],
    # Data rows...
]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(data[0])  # Write the header row
    for row in data[1:]:
        csv_writer.writerow(row)
```

By default, the `csv` module uses a comma as the default field delimiter. If your CSV file uses a different delimiter, you can specify it using the `delimiter` parameter in the `csv.reader` and `csv.writer` functions.

Reading and writing CSV files is a common task in data analysis and manipulation. Python's `csv` module provides a simple and straightforward way to work with CSV files in your Python programs.

Happy coding!