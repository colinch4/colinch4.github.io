---
layout: post
title: "Setting up a Django project for using websockets"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

In this tutorial, we will learn how to set up a Django project to use websockets. Websockets allow real-time communication between a web browser and a server, enabling features such as instant messaging, live updates, and notifications.

## Prerequisites

Before we begin, make sure you have the following:

- Python installed on your machine
- Django installed (you can install Django using pip: `pip install django`)
- [Channels](https://channels.readthedocs.io/en/stable/) library installed (`pip install channels`)

## Step 1: Create a new Django project

First, let's create a new Django project. Open your terminal or command prompt and navigate to the directory where you want to create your project. Run the following command:

```shell
django-admin startproject myproject
```

This will create a new directory named `myproject`, which contains the initial Django project files.

## Step 2: Install Django Channels

Django Channels is a third-party package that enables websockets in Django projects. Install it by running the following command:

```shell
pip install channels
```

## Step 3: Configure settings.py

Open the `settings.py` file located inside the `myproject` directory. Add `'channels'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'channels',
]
```

Next, add the following lines at the end of the `settings.py` file to configure Channels:

```python
ASGI_APPLICATION = 'myproject.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
```

## Step 4: Create routing.py

Inside the `myproject` directory, create a new file called `routing.py`. Add the following code to the file:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from myapp import consumers

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                [
                    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
                ]
            )
        ),
    }
)
```

Make sure to replace `'myapp'` with the name of your Django app, and `'ws/chat/'` with the desired websocket route.

## Step 5: Create a consumer

Inside your Django app directory, create a new file called `consumers.py`. Add the following code to the file:

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

This code sets up a basic websocket consumer that accepts connections, handles disconnections, and receives incoming messages.

## Step 6: Run the server

Now we are ready to run the Django development server with websocket support. Run the following command in your terminal:

```shell
python manage.py runserver
```

Congratulations! You have successfully set up a Django project with websocket support. You can now start building real-time features using websockets.

Keep in mind that this is just a basic setup. You can explore the Django Channels documentation to learn more about authentication, routing, and handling websocket events.

#django #websockets