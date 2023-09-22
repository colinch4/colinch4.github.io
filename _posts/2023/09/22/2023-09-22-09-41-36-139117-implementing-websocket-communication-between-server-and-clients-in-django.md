---
layout: post
title: "Implementing websocket communication between server and clients in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

WebSocket is a communication protocol that provides full-duplex communication between a client and a server over a single, streamlined connection. In Django, we can implement WebSocket communication using the Django Channels library, which provides a high-level interface to handle WebSocket connections.

In this tutorial, we will guide you through the process of setting up and implementing WebSocket communication between a server and clients in a Django application.

## Prerequisites

Before getting started, make sure you have the following prerequisites:

- Django installed on your machine
- Django Channels library installed (`pip install channels`)

## Step 1: Setting Up Django Channels

1. Open your Django project and add `'channels'` to the `INSTALLED_APPS` setting in your project's `settings.py` file.
2. Add `CHANNEL_LAYERS` setting to your `settings.py` file. This setting configures the backend layer that Channels will use for handling WebSocket connections. You can use Redis or other backends supported by Channels.

    ```python
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }
    ```

3. Configure your Django project to accept WebSocket connections. In your project's `asgi.py` file, replace the `get_asgi_application()` function with the following code:

    ```python
    import os
    from channels.routing import ProtocolTypeRouter, URLRouter
    from django.core.asgi import get_asgi_application
    from myapp.routing import websocket_urlpatterns
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    
    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": URLRouter(
            websocket_urlpatterns
        ),
    })
    ```

4. Create a new file named `routing.py` in your Django app folder with the following code:

    ```python
    from django.urls import re_path
    from . import consumers
    
    websocket_urlpatterns = [
        re_path(r'ws/', consumers.MyConsumer.as_asgi()),
    ]
    ```

5. Create a new file named `consumers.py` in your Django app folder with the following code:

    ```python
    import asyncio
    from channels.generic.websocket import AsyncWebsocketConsumer
    
    class MyConsumer(AsyncWebsocketConsumer):
        async def connect(self):
            await self.accept()
    
        async def disconnect(self, close_code):
            pass
    
        async def receive(self, text_data):
            pass
    ```

## Step 2: Implementing WebSocket Communication Logic

Now that we have set up Django Channels, it's time to implement the logic for WebSocket communication.

1. Modify the `connect()` method in the `MyConsumer` class in the `consumers.py` file to handle when a client connects to the WebSocket:

    ```python
    async def connect(self):
        await self.accept()
        # You can perform any initialization or checks here
    ```

2. Modify the `disconnect()` method to handle when a client disconnects from the WebSocket:

    ```python
    async def disconnect(self, close_code):
        # You can perform any cleanup or logging here
        pass
    ```

3. Modify the `receive()` method to handle when a client sends a message to the server:

    ```python
    async def receive(self, text_data):
        # Here, you can process the received message and send a response back to the client
        await self.send(text_data=f"Received: {text_data}")
    ```

4. Implement your own business logic inside the `receive()` method to handle the WebSocket communication based on your application's requirements.

## Step 3: Testing WebSocket Communication

To test the implemented WebSocket communication, follow these steps:

1. Start the Django development server by running `python manage.py runserver` in your project's root directory.
2. Open your preferred web browser and connect to `ws://localhost:8000/ws/` (update the URL if using a different port or domain).
3. Open the browser console and use the following JavaScript code to send a message to the server:

    ```javascript
    const socket = new WebSocket('ws://localhost:8000/ws/');
    
    socket.onopen = function() {
        socket.send('Hello, server!');
    }
    
    socket.onmessage = function(event) {
        console.log('Message from server:', event.data);
    }
    ```

4. Observe the server response in the browser console.

Congratulations! You've successfully implemented WebSocket communication between a server and clients in a Django application using Django Channels.

#django #websockets