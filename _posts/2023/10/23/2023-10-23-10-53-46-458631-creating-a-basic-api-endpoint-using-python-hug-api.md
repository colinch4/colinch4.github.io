---
layout: post
title: "Creating a basic API endpoint using Python Hug API"
description: " "
date: 2023-10-23
tags: []
comments: true
share: true
---

In this tutorial, we will explore how to create a basic API endpoint using Python Hug API. Hug is a python web framework that simplifies the process of building APIs in a fast and developer-friendly way.

## Table of Contents
1. [Setting up Hug API](#setting-up-hug-api)
2. [Defining the API endpoint](#defining-the-api-endpoint)
3. [Running the API](#running-the-api)
4. [Conclusion](#conclusion)

## Setting up Hug API<a name="setting-up-hug-api"></a>

To begin, let's set up our development environment. Make sure you have Python installed on your machine. You can install Hug API using pip, by running the following command:

```python
pip install hug
```

Once the installation is complete, we can start building our API endpoint.

## Defining the API endpoint<a name="defining-the-api-endpoint"></a>

In this example, we will create a simple API endpoint that returns a JSON response with a welcome message. Open up a new Python file and import the necessary dependencies:

```python
import hug
```

Next, let's define the API endpoint using the `@hug.get()` decorator:

```python
@hug.get('/welcome')
def welcome():
    return {"message": "Welcome to the API!"}
```

In this code, we are defining an API endpoint `/welcome` using the `@hug.get()` decorator. The `welcome()` function returns a dictionary containing a message that will be converted to JSON and sent as the response.

## Running the API<a name="running-the-api"></a>

To run the API, save the file with a `.py` extension, for example, `api.py`. Open a terminal or command prompt, navigate to the directory where the file is saved, and run the following command:

```python
hug -f api.py
```

You should see output like `Serving on http://localhost:8000/`. This means the API is now running on your local machine.

To test the API, open up a web browser or use a tool like `curl` and navigate to `http://localhost:8000/welcome`. You should see a JSON response with the welcome message.

## Conclusion<a name="conclusion"></a>

In this tutorial, we learned how to create a basic API endpoint using Python Hug API. Hug simplifies the process of building APIs by providing a clean and intuitive interface. With Hug, you can quickly define endpoints and handle requests and responses in an efficient manner.