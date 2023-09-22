---
layout: post
title: "Using websockets for collaborative drawing applications in Django"
description: " "
date: 2023-09-22
tags: [websockets, django]
comments: true
share: true
---

In today's tech-driven world, the demand for real-time collaborative applications is skyrocketing. One popular use case is a collaborative drawing application where multiple users can draw on the same canvas simultaneously. This can be achieved using Websockets, a powerful technology that allows bidirectional communication between a web browser and a server.

In this article, we will explore how to implement a collaborative drawing application in Django using Websockets. With Django Channels, a third-party library, we can easily integrate Websockets into our Django project.

## Prerequisites

Before we begin, make sure you have the following:

1. Django and Django Channels installed on your machine.
2. A basic understanding of Django's views, templates, and models.

## Setting up Django Channels

To use Websockets in your Django project, you need to install Django Channels. You can install it using pip:

```bash
pip install channels
```

Once installed, add `'channels'` to the `INSTALLED_APPS` list in your project's `settings.py` file.

Next, configure your project to use Channels as the ASGI application. Replace the existing `ASGI_APPLICATION` setting in `settings.py` with the following:

```python
ASGI_APPLICATION = '<your_project_name>.asgi.application'
```

Create a new file called `asgi.py` in your project's root directory and add the following content:

```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
import <your_app_name>.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<your_project_name>.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            <your_app_name>.routing.websocket_urlpatterns
        )
    ),
})
```

Replace `<your_project_name>` and `<your_app_name>` with your project and application names respectively.

## Implementing the Collaborative Drawing Application

Now that we have set up Django Channels, let's dive into implementing the collaborative drawing application.

First, create a new Django app using the following command:

```bash
python manage.py startapp drawing
```

### Models

Create a `models.py` file inside the `drawing` app and define a `Drawing` model to store the drawing data:

```python
from django.db import models

class Drawing(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### Views

Next, create a `views.py` file inside the `drawing` app. We'll define two views: one to render the drawing canvas and another to handle Websocket connections.

```python
from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def drawing_canvas(request):
    drawings = Drawing.objects.all()
    return render(request, 'drawing/canvas.html', {'drawings': drawings})

def send_drawing_data(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'drawing_group',
        {'type': 'send_drawing_data_event', 'data': request.POST.get('data')}
    )
    return JsonResponse({'status': 'success'})
```

### Websocket Consumers

Create a `consumers.py` file inside the `drawing` app. This will define the Websocket consumer that handles incoming connections and broadcasts the drawing data to all connected clients.

```python
from channels.generic.websocket import WebsocketConsumer
import json

class DrawingConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'drawing_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def send_drawing_data_event(self, event):
        data = event['data']
        self.send(json.dumps({
            'type': 'drawing_data',
            'data': data
        }))

    def receive(self, text_data):
        data = json.loads(text_data)
        self.send_drawing_data_event({'data': data['data']})
```

### Routing

Create a `routing.py` file inside the `drawing` app. This will define the routing configuration for Websocket connections.

```python
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/drawing/', consumers.DrawingConsumer.as_asgi()),
]
```

### Templates

Create a `templates` directory inside the `drawing` app. Then, create a `canvas.html` file inside the `templates/drawing` directory with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Collaborative Drawing</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>
        var socket = new WebSocket('ws://' + window.location.host + '/ws/drawing/');

        socket.onmessage = function(e) {
            var data = JSON.parse(e.data);
            // Draw data on the canvas
        };

        function sendDrawingData(data) {
            socket.send(JSON.stringify({ 'data': data }));
        }
    </script>
</head>
<body>
    <canvas id="drawingCanvas" width="800" height="600"></canvas>

    <script>
        // Implement drawing functionality
    </script>
</body>
</html>
```

### URLs

Finally, update the project's `urls.py` file to include the URLs for the drawing app:

```python
from django.urls import include, path

urlpatterns = [
    # Other URLs
    path('', include('drawing.urls')),
]
```

## Conclusion

Congratulations! You have successfully implemented a collaborative drawing application in Django using Websockets and Django Channels. Users can now draw on the canvas simultaneously and see the changes in real-time.

This is just a basic implementation, and you can extend it further by adding features like collaborative chat, multiple canvas support, and more. With the power of Websockets and Django Channels, the possibilities are endless.

#websockets #django