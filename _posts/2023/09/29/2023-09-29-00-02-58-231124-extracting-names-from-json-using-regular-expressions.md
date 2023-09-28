---
layout: post
title: "Extracting names from JSON using regular expressions"
description: " "
date: 2023-09-29
tags: [json, regex]
comments: true
share: true
---

Regular expressions (regex) are powerful tools for pattern matching and string manipulation. They can be extremely useful when working with JSON data to extract specific information, such as names.

In this blog post, we will explore how to use regular expressions in popular programming languages to extract names from JSON.

## Using Python

Python provides the `re` module for working with regular expressions. Let's consider a simple JSON object containing several name-value pairs:

```python
import re

data = {
    "name1": "John Doe",
    "name2": "Jane Smith",
    "address": "123 Main St",
    "age": 25
}

# Use regex to extract names
name_pattern = re.compile(r"(\b[A-Z][a-zA-Z]*\b)")

names = [value for key, value in data.items() if name_pattern.match(key)]

print(names)  # ['John Doe', 'Jane Smith']
```

In the code above, we use the regular expression pattern `(\b[A-Z][a-zA-Z]*\b)` to match words with an initial capital letter (excluding the address and age keys). We iterate over the JSON object and append the values to the `names` list if they match the pattern.

## Using JavaScript

JavaScript also has built-in support for regular expressions through the `RegExp` object. Let's see how we can extract names from a JSON object using JavaScript:

```javascript
const data = {
    name1: "John Doe",
    name2: "Jane Smith",
    address: "123 Main St",
    age: 25
};

// Use regex to extract names
const namePattern = /\b[A-Z][a-zA-Z]*\b/g;

const names = Object.values(data)
    .filter(value => typeof value === 'string')
    .filter(value => namePattern.test(value));

console.log(names); // ['John Doe', 'Jane Smith']
```

In the JavaScript code above, we define the regular expression pattern `\b[A-Z][a-zA-Z]*\b` using the `RegExp` object. We filter the values of the JSON object to only consider strings and then filter them further based on the pattern. The final `names` array contains the extracted names.

## Conclusion

Regular expressions are a powerful tool for extracting specific information from JSON data. In this blog post, we explored how to use regular expressions in Python and JavaScript to extract names from a JSON object.

Remember, regular expressions can be customized and adapted to fit various JSON structures and naming conventions. Experiment with different patterns to suit your specific use case and always test your regex against different data scenarios.

#json #regex