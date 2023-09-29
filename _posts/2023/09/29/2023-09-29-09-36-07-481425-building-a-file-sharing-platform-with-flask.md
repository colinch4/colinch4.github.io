---
layout: post
title: "Building a file-sharing platform with Flask"
description: " "
date: 2023-09-29
tags: [filesharing, Flask]
comments: true
share: true
---

In this blog post, we will explore how to build a file-sharing platform using Flask, a lightweight web framework in Python. Flask provides a simple and efficient way to handle web requests and build scalable web applications.

## Prerequisites

Before we start, make sure you have the following prerequisites:

- Python installed on your system
- Basic understanding of Python and web development

## Setting Up the Project

First, let's set up a new Flask project. Open your terminal and follow the steps below:

1. **Create a virtual environment**: Start by creating a virtual environment for your project to keep dependencies isolated. Run the following command:

   ```
   $ python3 -m venv file-sharing-env
   ```

2. **Activate the virtual environment**: Activate the virtual environment using the appropriate command for your OS:

   - For Mac/Linux:
     ```shell
     $ source file-sharing-env/bin/activate
     ```
   
   - For Windows:
     ```shell
     $ file-sharing-env\Scripts\activate
     ```

3. **Install Flask**: Once the virtual environment is activated, install Flask using pip:

   ```shell
   $ pip install Flask
   ```

## Creating the Flask Application

Now that we have our project set up, let's create our Flask application. Follow these steps:

1. **Create a new file**: Create a new file called `app.py` in the project directory.

2. **Import Flask**: In `app.py`, import the Flask module:

   ```python
   from flask import Flask
   ```

3. **Create the Flask app**: Create a Flask application instance:

   ```python
   app = Flask(__name__)
   ```

4. **Create a route**: Define a route to handle file uploads:

   ```python
   @app.route('/upload', methods=['POST'])
   def upload_file():
       # Handle file upload logic here
       return 'File uploaded successfully!'
   ```

## Handling File Uploads

Next, let's add logic to handle file uploads. Modify the `upload_file` route as follows:

```python
from flask import request

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file found!', 400

    file = request.files['file']
    # Save the file to desired location
    file.save('/path/to/save/file')

    return 'File uploaded successfully!'
```

In this code, we check if a file is present in the request. If not, we return an error message. Otherwise, we save the file to a desired location.

## Adding File Download Routes

Now that we can upload files, let's add routes to download them. Modify `app.py` as follows:

```python
from flask import send_file
import os

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Check if the file exists
    if not os.path.isfile('/path/to/save/file/' + filename):
        return 'File not found!', 404

    return send_file('/path/to/save/file/' + filename, as_attachment=True)
```

In this code, we define a route `download_file` that takes a filename as a parameter. We check if the file exists and use Flask's `send_file` method to send the file as an attachment.

## Conclusion

In this blog post, we learned how to build a basic file-sharing platform using Flask. We covered setting up a Flask project, handling file uploads, and implementing file download routes. With this foundation, you can further enhance the platform by adding user authentication, file sharing permissions, and more advanced features.

#filesharing #Flask