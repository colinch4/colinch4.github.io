---
layout: post
title: "Creating a CRUD application with Flask"
description: " "
date: 2023-09-29
tags: [flask, crud]
comments: true
share: true
---

Flask is a lightweight and powerful web framework written in Python. It provides a flexible and easy-to-use platform for building web applications. In this tutorial, we will learn how to create a CRUD (Create, Read, Update, Delete) application using Flask.

## Prerequisites
Before we get started, make sure you have the following installed:
- Python 3.x
- Flask (`pip install flask`)

## Setting up a Flask App
To begin, let's create a new Flask application. Open your favorite code editor and create a new file called `app.py`. In this file, we will define our Flask routes and functions.

```python
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Your code goes here

if __name__ == "__main__":
    app.run()
```

## Creating Routes and Views
The first step in building our CRUD application is to define the routes and views for each CRUD operation. Let's start by creating the route for the home page.

```python
@app.route("/")
def home():
    return render_template("index.html")
```

In the `home()` function, we return the `index.html` template using the `render_template()` method. We will create this template later.

Next, let's create the routes for the other CRUD operations. We'll define routes for creating, reading, updating, and deleting resources.

```python
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        # Process form data and create new resource
        # Redirect to the appropriate view
        return redirect("/")
    else:
        return render_template("create.html")

@app.route("/read")
def read():
    # Fetch resources from the database
    # Pass the resources to the template
    return render_template("read.html", resources=resources)

@app.route("/update")
def update():
    # Fetch the resource to be updated
    # Update the resource in the database
    # Redirect to the appropriate view
    return redirect("/read")

@app.route("/delete")
def delete():
    # Fetch the resource to be deleted
    # Delete the resource from the database
    # Redirect to the appropriate view
    return redirect("/read")
```

## Creating HTML Templates
Now that we have defined our routes, let's create the HTML templates for each view.

Create a new folder called `templates`, and inside it, create the following files:

- `index.html` - The home page template
- `create.html` - The form to create a new resource
- `read.html` - The page to display the list of resources

Here's an example of the `index.html` template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>CRUD Application</title>
</head>
<body>
    <h1>Welcome to CRUD App</h1>
    <p>Choose an option:</p>
    <ul>
        <li><a href="/create">Create a new resource</a></li>
        <li><a href="/read">View all resources</a></li>
    </ul>
</body>
</html>
```

## Running the Application
To start the Flask development server, navigate to the project folder in the terminal and run the following command:

```
python app.py
```

You should see the server starting up. Open your web browser and visit `http://localhost:5000` to access the CRUD application.

That's it! You have successfully created a CRUD application using Flask. You can further enhance it by adding database support and implementing the update and delete functionality.

#flask #crud