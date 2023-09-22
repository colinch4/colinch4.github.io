---
layout: post
title: "Creating a basic websockets server in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

Websockets are a powerful protocol that allows real-time communication between a server and a client. They provide a bidirectional, full-duplex communication channel over a single TCP connection. In this blog post, we will go through the process of creating a basic websockets server in Django.

## Setting Up Django

First, make sure you have Django installed on your machine. If not, you can install it using `pip`:

```bash
pip install Django
```

Next, create a new Django project:

```bash
django-admin startproject websockets_server
```

Change to the project directory:

```bash
cd websockets_server
```

Create a new Django app:

```bash
python manage.py startapp chat
```

## Installing Channels

Django Channels is a third-party package that brings websockets and other asynchronous features to Django. Install it using `pip`:

```bash
pip install channels
```

Add Channels to your Django project by modifying the `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'channels',
    'chat',  # Add your app name here
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
```

## Creating the Websockets Server

Inside the `chat` directory, create a new file called `consumers.py`. This file will contain the logic for handling websockets connections and events. 

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
```

In the example above, we create a new consumer class called `ChatConsumer`. This class inherits from `AsyncWebsocketConsumer` provided by Django Channels. We override the three main methods: `connect`, `disconnect`, and `receive`.

The `connect` method is called when a new WebSocket connection is established. In this example, we simply accept the connection.

The `disconnect` method is called when a WebSocket connection is closed. We leave it blank for now.

The `receive` method is called when the server receives a message from the client. We also leave it blank for now.

## Routing Websockets

To route the websockets to the appropriate consumers, we need to modify the `routing.py` file in your project directory:

```python
from django.urls import re_path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]
```

In this example, we create a new URL pattern that matches the `ws/chat/` path and associates it with the `ChatConsumer` consumer that we defined earlier.

## Testing the Websockets Server

To start the websockets server, run the following command:

```bash
python manage.py runserver
```

Visit `http://localhost:8000/ws/chat/` in your browser and open the developer console. You should see that the connection is successfully established.

Now, you can start sending and receiving messages between the server and the client by implementing the logic inside the `connect`, `disconnect`, and `receive` methods in the `ChatConsumer` class.

That's it! You have successfully created a basic websockets server in Django using Django Channels. from here, you can expand and build more advanced real-time applications.

#django #websockets