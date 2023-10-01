---
layout: post
title: "Creating a basic Falcon API"
description: " "
date: 2023-10-02
tags: []
comments: true
share: true
---

In this tutorial, we will walk through the process of creating a basic API using the Falcon framework in Python. Falcon is a minimalist web framework for building fast and scalable APIs.

## Pre-requisites
Before we begin, make sure you have the following installed on your machine:
- Python 3.x
- Falcon framework (`pip install falcon`)

## Step 1: Setting up a Falcon API
Create a new Python file named `app.py` and open it in your favorite editor. Let's import the required modules and create a simple Falcon API class:

```python
import falcon

class HelloWorldResource:
    def on_get(self, req, resp):
        resp.body = "Hello, World!"
        resp.status = falcon.HTTP_200
```

## Step 2: Configuring the Falcon API
Next, we need to setup the Falcon API instance and add the `HelloWorldResource` as a route:

```python
api = falcon.API()
api.add_route('/', HelloWorldResource())
```

## Step 3: Running the Falcon API
To run the API, we need to add a main function at the end of the file:

```python
if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
```

## Step 4: Testing the Falcon API
Save the file and execute it using the following command:

```
python app.py
```

You should see the Falcon API server running at `http://127.0.0.1:8000`. Open your preferred web browser and enter the URL. You should see the message "Hello, World!" displayed.

## Conclusion
In this tutorial, we have learned how to create a basic API using the Falcon framework in Python. Falcon provides a lightweight and efficient way to build APIs, making it ideal for building microservices and scalable applications.