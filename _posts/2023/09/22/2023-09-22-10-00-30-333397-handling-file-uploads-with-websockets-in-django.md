---
layout: post
title: "Handling file uploads with websockets in Django"
description: " "
date: 2023-09-22
tags: [initial, django]
comments: true
share: true
---

In modern web applications, file uploads have become a crucial feature. Traditionally, file uploads in Django are handled using synchronous requests, which can be inefficient for larger files. However, with the introduction of websockets, we can now handle file uploads asynchronously and provide real-time progress updates to the user. In this blog post, we will explore how to handle file uploads with websockets in Django.

## Setup

Before we begin, make sure you have Django and channels installed in your Django project:

```bash
pip install Django channels
```

Next, we need to configure Django Channels in our project. Follow the official Channels documentation to set up [ASGI](https://channels.readthedocs.io/en/stable/deploying.html) or [ASGI](https://channels.readthedocs.io/en/latest/tutorial/part_1.html#initial-setup) for your project.

## Implementing File Uploads with Websockets

To handle file uploads with websockets, we need to perform the following steps:

### Step 1: Set up a WebSocket consumer

Start by creating a new consumer that will listen for websocket connections and handle file uploads. This consumer will use the `Channels API` to send real-time progress updates to the client.

Create a new file `consumers.py`:

```python
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.files.base import ContentFile

class FileUploadConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connect to the websocket
        await self.accept()

    async def receive(self, text_data):
        # Process the file upload
        file_data = ContentFile(text_data)
        # Save the file or perform any other necessary processing
        # Notify the client about the progress
        await self.send(text_data='File uploaded successfully!')
```

### Step 2: Configure routing

Next, we need to configure our routing to connect to the WebSocket consumer. In your `routing.py` file, add the following code:

```python
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/upload/$', consumers.FileUploadConsumer.as_asgi()),
]
```

### Step 3: Update Django settings

Add `"channels"` to the `INSTALLED_APPS` list in your Django settings file:

```python
INSTALLED_APPS = [
    # ...
    'channels',
]
```

### Step 4: Update Django URL configuration

Finally, update your Django URL configuration to include the websocket routing:

```python
from django.urls import path, include
from . import views, routing   # Import the routing module

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('ws/', include(routing.websocket_urlpatterns)),
]
```

## Testing File Uploads with Websockets

To test file uploads with websockets, we need to create a simple HTML form that sends the file data to the websocket.

Add the following code to your HTML file:

```html
{% raw %}
<form method="post" action="{% url 'upload_file' %}" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>

<script>
    const socket = new WebSocket('ws://' + window.location.host + '/ws/upload/');

    socket.onopen = function() {
        console.log('WebSocket connection established.');
    }

    socket.onmessage = function(event) {
        console.log('Received message from server:', event.data);
    }

    socket.onclose = function(event) {
        console.log('WebSocket connection closed:', event);
    }

    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        const file = document.querySelector('input[type="file"]').files[0];
        const reader = new FileReader();

        reader.onload = function(event) {
            const data = event.target.result;
            socket.send(data);
        }

        reader.readAsText(file);
    });
</script>
{% endraw %}
```

## Conclusion

By implementing file uploads with websockets in Django, we can achieve faster and more efficient file transfers with real-time progress updates. This not only improves the user experience but also simplifies file handling on the server-side.

With the integration of websockets using Django Channels, you can explore more advanced features such as resumable file uploads, error handling, and additional client-side validations. Implementing file uploads with websockets opens up a wide range of possibilities to enhance your web application. #django #websockets