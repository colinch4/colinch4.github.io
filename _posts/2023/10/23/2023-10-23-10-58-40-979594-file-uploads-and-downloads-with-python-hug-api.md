---
layout: post
title: "File uploads and downloads with Python Hug API"
description: " "
date: 2023-10-23
tags: [HugAPI]
comments: true
share: true
---

Python Hug is a lightweight web framework that makes it easy to build APIs in Python. In this tutorial, we will explore how to handle file uploads and downloads using the Hug API framework.

## Table of Contents
- [Introduction](#introduction)
- [Setting up the Hug API](#setting-up-the-hug-api)
- [File Upload](#file-upload)
- [File Download](#file-download)
- [Conclusion](#conclusion)

## Introduction

File uploads and downloads are common functionalities in many web applications. With Hug API, handling file uploads and facilitating file downloads is straightforward. We will cover both these aspects in this blog post.

## Setting up the Hug API

First, we need to install the Hug library using `pip`:

```python
pip install hug
```

Next, let's create a basic Hug API server:

```python
import hug

@hug.get("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    hug.API(__name__).http.serve()
```

Save the above code in a file named `server.py`. Now, if you run the `server.py` script, you will have a basic Hug API server running at `http://localhost:8000`.

## File Upload

To handle file uploads, Hug provides a convenient decorator `@hug.post()` which allows you to define an endpoint that accepts `multipart/form-data` requests. Let's see an example:

```python
import hug

@hug.post("/upload")
def upload_file(file: hug.types.FileStorage):
    file.save("uploads/" + file.filename)
    return "File uploaded successfully!"

if __name__ == "__main__":
    hug.API(__name__).http.serve()
```

In the code above, we define an endpoint `/upload` using the `@hug.post()` decorator. The `upload_file` function accepts a `FileStorage` object as a parameter, which represents the uploaded file. We save the file in the `uploads` directory using its original filename.

To test the file upload functionality, you can use a tool like `curl`:

```bash
curl -F "file=@/path/to/file.ext" http://localhost:8000/upload
```

## File Download

To facilitate file downloads, we can define an endpoint that returns the file to the client. Here's an example:

```python
import hug

@hug.get("/download")
def download_file():
    return hug.HTTPResponse(
        content=open("downloads/file.ext", "rb"),
        content_type="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=file.ext"}
    )

if __name__ == "__main__":
    hug.API(__name__).http.serve()
```

In the code above, we define an endpoint `/download` using the `@hug.get()` decorator. The `download_file` function returns an `HTTPResponse` object with the file content, content type, and the appropriate `Content-Disposition` header to trigger the file download in the client's browser.

## Conclusion

In this tutorial, we saw how to handle file uploads and downloads with the Python Hug API framework. Hug provides a simple and intuitive way to build APIs, and its file handling capabilities make it convenient to handle file uploads and facilitate file downloads.

Start using Hug for your next API project and experience the ease of building powerful APIs in Python.

Hashtags: #Python #HugAPI