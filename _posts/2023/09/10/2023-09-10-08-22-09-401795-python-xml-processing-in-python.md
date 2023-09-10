---
layout: post
title: "[Python] XML processing in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

XML (eXtensible Markup Language) is a standard format for storing and transferring data. It is widely used in various industries and applications. In this blog post, we will explore how to process XML data in Python using the built-in `xml` module.

## Parsing XML

```python
import xml.etree.ElementTree as ET

# Load XML from file
tree = ET.parse('data.xml')

# Get the root element
root = tree.getroot()

# Access elements and attributes
for child in root:
    print(child.tag, child.attrib)

# Search for elements by tag name
elements = root.findall('book')

# Access element data
for elem in elements:
    print(elem.find('title').text)

# Modify element data
for elem in elements:
    elem.find('title').text = 'New Title'

# Save modified XML to file
tree.write('modified_data.xml')
```

## Generating XML

```python
import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element('data')

# Create child elements
element1 = ET.SubElement(root, 'element1')
element1.text = 'Value 1'

element2 = ET.SubElement(root, 'element2')
element2.text = 'Value 2'

# Create sub-elements with attributes
element3 = ET.SubElement(root, 'element3')
element3.attrib = {'attribute1': 'value1', 'attribute2': 'value2'}

# Convert the XML tree to a string
xml_string = ET.tostring(root)

# Save the XML to file
with open('output.xml', 'wb') as f:
    f.write(xml_string)
```

## Working with Namespaces

```python
import xml.etree.ElementTree as ET

# Define the namespace URI
namespace = '{http://www.example.com/namespace}'

# Parse the XML file with namespaces
tree = ET.parse('data.xml')

# Get the root element
root = tree.getroot()

# Access elements with namespace
elements = root.findall(namespace + 'element')

# Access element data with namespace
for elem in elements:
    print(elem.find(namespace + 'name').text)
```

XML processing in Python can be done efficiently using the `xml` module. Whether you need to parse existing XML data or generate new XML files, Python provides a convenient and powerful set of tools for working with XML.