---
layout: post
title: "Implementing OCR (optical character recognition) with Pyramid"
description: " "
date: 2023-10-16
tags: [pyramid]
comments: true
share: true
---

![OCR](ocr.jpg)

Optical Character Recognition (OCR) is a technology that allows extracting text from images or scanned documents. It has many practical applications, such as digitizing printed materials, automating data entry, and enhancing accessibility for visually impaired individuals. In this blog post, we will explore how to implement OCR using the Pyramid framework in Python.

## Prerequisites

Before getting started, make sure you have the following prerequisites:

- Python installed on your system.
- Pyramid framework installed. You can install it using pip: `pip install pyramid`.
- Tesseract OCR engine installed. You can install it using your system's package manager or download it from the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

## Setting up the Project

1. Create a new directory for your project and navigate into it.
2. Initialize a new Python virtual environment: `python -m venv env`.
3. Activate the virtual environment:
   - On Windows: `env\Scripts\activate.bat`.
   - On Linux/Mac: `source env/bin/activate`.
4. Install the required dependencies: `pip install pyramid tesserocr Pillow`.

## Building the OCR Web Application

We will create a simple web application using Pyramid to upload an image and extract the text from it using OCR.

1. Create a new Python file named `app.py` and add the following code:

```python
import os
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from tesserocr import PyTessBaseAPI
from PIL import Image


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='upload', renderer='templates/result.jinja2')
def upload(request):
    image = request.POST['image'].file
    img = Image.open(image).convert('L')
    img.save('tmp_image.png')

    with PyTessBaseAPI() as api:
        api.SetImageFile('tmp_image.png')
        result = api.GetUTF8Text()

    os.remove('tmp_image.png')

    return {'result': result}


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('upload', '/upload')
    config.add_static_view(name='static', path='static')
    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=8080)
```

2. Create a new directory named `templates` and add two Jinja2 template files named `home.jinja2` and `result.jinja2`. In `home.jinja2`, add the following code:

```jinja2
<!DOCTYPE html>
<html>
<head>
    <title>OCR Demo</title>
</head>
<body>
    <h1>OCR Demo</h1>
    <form action="{{ request.route_url('upload') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="image">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

3. In `result.jinja2`, add the following code:

```jinja2
<!DOCTYPE html>
<html>
<head>
    <title>OCR Result</title>
</head>
<body>
    <h1>OCR Result</h1>
    <pre>{{ result }}</pre>
</body>
</html>
```

## Starting the Web Server

Run the following command to start the web server:

```bash
python app.py
```

Open your web browser and navigate to http://localhost:8080. You should see a form where you can upload an image. After selecting an image and clicking the "Upload" button, the application will extract the text from the image using OCR and display the result.

## Conclusion

In this blog post, we have learned how to implement OCR using the Pyramid framework in Python. We built a simple web application that allows users to upload an image and extract the text from it using the Tesseract OCR engine. You can further enhance this application by adding image preprocessing techniques, handling multiple images, or integrating it with other frameworks or APIs.

#pyramid #OCR