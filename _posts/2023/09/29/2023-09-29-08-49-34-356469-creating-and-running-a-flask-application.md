---
layout: post
title: "Creating and running a Flask application"
description: " "
date: 2023-09-29
tags: [flask, webdevelopment]
comments: true
share: true
---

Flask is a minimal and powerful web framework written in Python. It allows you to quickly build web applications with ease. In this blog post, we will walk through the steps of creating a Flask application and running it locally on your computer.

## Prerequisites
Before we start, make sure you have the following installed on your machine:

- Python (version 3.6 or higher)
- Pip (Python package installer)

## Step 1: Setting Up the Virtual Environment
It's a good practice to use a virtual environment to isolate your project dependencies. This ensures that your application runs with the correct versions of the required packages. 

Open your terminal and run the following commands:

```
$ python3 -m venv myenv
$ source myenv/bin/activate
```

## Step 2: Installing Flask
Now that we have our virtual environment set up, we can install Flask. Run the following command in your terminal:

```
$ pip install Flask
```

## Step 3: Creating a Flask Application
Create a new file called `app.py` and open it in your preferred text editor. 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

In the code above, we import the Flask module and create an instance of the Flask class called `app`. We define a route by using the `@app.route` decorator, and associate it with the `hello_world` function. This function returns the message "Hello, World!".

## Step 4: Running the Flask Application
To run the Flask application, go back to your terminal and navigate to the directory where `app.py` is located. Run the following command:

```
$ python app.py
```

You should see an output similar to the following:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now open your web browser and enter `http://localhost:5000` or `http://127.0.0.1:5000`. You should see the message "Hello, World!" displayed on the screen.

## Conclusion
Congratulations! You have successfully created and run a Flask application. Flask provides a simple and efficient way to build web applications in Python. With its extensive documentation and large community, you can explore and leverage various features to create even more complex applications. 

Stay tuned for more Flask tips and tricks!

#flask #webdevelopment