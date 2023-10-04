---
layout: post
title: "Building web servers with functions in Python"
description: " "
date: 2023-09-29
tags: [WebServers]
comments: true
share: true
---

Web servers are the backbone of the internet, handling requests, processing data, and delivering content to users. While there are many frameworks available for building web servers, it can be beneficial to understand the underlying concepts by building one from scratch.

In this tutorial, we will explore how to build a basic web server using Python functions.

## Prerequisites

Before we begin, make sure you have Python installed on your machine. You can download the latest version of Python from the official website.

## Setting up the Server

1. Start by creating a new Python file, let's name it `server.py`.

2. Import the required modules:
```python
import http.server
import socketserver
```

3. Define a handler class that extends the `http.server.SimpleHTTPRequestHandler`. This class will handle incoming requests:
```python
class MyHandler(http.server.SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory='path_to_static_files', **kwargs)
```
Make sure to replace `'path_to_static_files'` with the actual path to your static files directory.

4. Create a function that will start the server and handle incoming requests:
```python
def run_server(port):
  with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Server is running on port {port}")
    httpd.serve_forever()
```
The `run_server` function takes a `port` argument to specify which port the server should listen on.

5. Finally, add the following code at the end of the file to start the server:
```python
if __name__ == "__main__":
  run_server(8000)
```
This code ensures that the server is only started if the file is executed directly, not imported as a module.

## Running the Server

To run the server, navigate to the directory containing the `server.py` file in your terminal.

Execute the following command:
```
python server.py
```
You should see the message "Server is running on port 8000" indicating that the server has started successfully.

## Testing the Server

To test your server, open a web browser and navigate to `http://localhost:8000` (replace `8000` with the port you specified).

You should see the contents of the static files directory displayed in your browser.

## Conclusion

Building a web server with functions in Python provides a solid understanding of the underlying concepts. While this example only scratches the surface of what a full-fledged web server can do, it serves as a foundation for further exploration.

Feel free to experiment and enhance the server functionality as per your requirements. Have fun building web servers! 🚀

---

#Python #WebServers