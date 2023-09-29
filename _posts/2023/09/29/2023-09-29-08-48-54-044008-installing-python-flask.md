---
layout: post
title: "Installing Python Flask"
description: " "
date: 2023-09-29
tags: [python, flask]
comments: true
share: true
---

If you're looking to build web applications using Python, Flask is a great choice for a micro web framework. Flask makes it easy to get started with web development and provides a flexible environment for building scalable and customizable applications.

In this tutorial, we'll walk you through the process of installing Flask on your local machine.

## Step 1: Set up a Virtual Environment

It's recommended to create a virtual environment before installing Flask. A virtual environment allows you to keep your project dependencies isolated from other Python projects. To set up a virtual environment, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create your project.
3. Run the following command to create a new virtual environment:

```shell
python -m venv myenv
```

Replace `myenv` with the name you want to give to your virtual environment.

4. Activate the virtual environment:

**For Windows**:

```shell
myenv\Scripts\activate
```

**For macOS and Linux**:

```shell
source myenv/bin/activate
```

## Step 2: Install Flask

With the virtual environment activated, you can now proceed to install Flask. Follow these steps:

1. In your terminal or command prompt, make sure you're still in the project directory with the virtual environment activated.
2. Run the following command to install Flask:

```shell
pip install flask
```

This will install Flask and its dependencies.

## Step 3: Verify the Installation

To verify that Flask has been installed successfully, you can create a simple Flask application. Create a new file named `app.py` and open it in a text editor. Add the following code to the file:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Save the file and navigate to the project directory in your terminal or command prompt. Run the following command:

```shell
flask run
```

If everything is set up correctly, you should see an output similar to this:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/). You should see the message "Hello, Flask!" displayed in your browser.

Congratulations! You've successfully installed Flask and created a simple Flask application.

Now you're ready to start building more complex web applications using Flask. Happy coding!

#python #flask