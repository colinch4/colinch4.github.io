---
layout: post
title: "Building a URL shortener with Flask"
description: " "
date: 2023-09-29
tags: [URLShortener, Flask]
comments: true
share: true
---

The popularity of social media platforms and the need to share content quickly has made URL shorteners a valuable tool. In this blog post, we will explore how to build a URL shortener using Flask - a lightweight web framework for Python.

## Prerequisites
Before we dive into building the URL shortener, make sure you have the following:

1. Python installed on your machine
2. Flask installed (`pip install flask`)

## Setting Up the Flask App
To begin, let's create a new Flask app by creating a new Python file, `app.py`.

```python
# Import Flask module
from flask import Flask

# Create a new Flask App instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return "Welcome to the URL shortener!"

# Run the app on local host
if __name__ == '__main__':
    app.run()
```

## Adding URL Shortener Functionality
Now, let's add the functionality to generate short URLs. We will use a simple base conversion technique to convert the long URLs into shorter ones.

```python
# Import baseconvert module for base conversion
from baseconvert import base62

# Dictionary to store long URLs and their corresponding short URLs
url_mapping = {}

# Route to handle URL shortening
@app.route('/shorten/<path:long_url>')
def shorten_url(long_url):
    if long_url in url_mapping:
        return f"Short URL: http://example.com/{url_mapping[long_url]}"

    short_id = len(url_mapping) + 1
    short_url = base62.encode(short_id)
    url_mapping[long_url] = short_url

    return f"Short URL: http://example.com/{short_url}"
```

Here, we create a dictionary `url_mapping` to store the long URLs and their corresponding short URLs. When a long URL is provided, we check if it already exists in the dictionary. If it does, we return the associated short URL. Otherwise, we generate a short URL using the base62 encoding technique and store it in the dictionary.

## Testing the URL Shortener
To test the URL shortener, run the Flask app using `flask run` command. Access the home page by navigating to `http://localhost:5000/` in your browser. 

To generate a short URL, append `/shorten/` and the long URL you want to shorten, like `http://localhost:5000/shorten/www.example.com`.

Congrats! You have successfully built a simple URL shortener using Flask.

# Conclusion
In this blog post, we explored how to build a URL shortener using Flask. With Flask's simplicity and flexibility, you can extend the functionality of your URL shortener further based on your requirements. Remember to handle edge cases and add additional security measures to protect against malicious behavior.

Thanks for reading! #URLShortener #Flask