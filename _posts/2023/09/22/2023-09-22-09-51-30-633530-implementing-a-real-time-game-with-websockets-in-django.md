---
layout: post
title: "Implementing a real-time game with websockets in Django"
description: " "
date: 2023-09-22
tags: [websockets, Django]
comments: true
share: true
---

In this blog post, we will explore how to implement a real-time game using websockets in Django. Websockets are a powerful technology that allows for bidirectional communication between the server and the client, enabling real-time updates without the need for constant polling. This makes it an excellent choice for creating interactive and immersive games.

## Setting Up the Django Project

To get started, let's assume you already have Django installed on your machine. If not, you can install it by running the following command:

```shell
$ pip install django
```

Once Django is installed, let's create a new Django project by running the following command:

```shell
$ django-admin startproject real_time_game
```

Next, let's create a new Django app within our project:

```shell
$ cd real_time_game
$ python manage.py startapp game
```

### Installing Django Channels

To use websockets in Django, we need to install a package called Django Channels. This package provides a way to handle websockets and other real-time protocols in Django.

To install Django Channels, run the following command:

```shell
$ pip install channels
```

Once installed, we need to configure Django Channels in our project. Open the `settings.py` file in your project directory and add `'channels'` to the `INSTALLED_APPS` list.

In the same file, add the following lines at the end to configure the Channels layer:

```python
ASGI_APPLICATION = 'real_time_game.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
```

## Creating the Game Model

Now, let's create our game model. Open the `models.py` file in the `game` app and add the following code:

```python
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    players = models.ManyToManyField('Player')

    def __str__(self):
        return self.name
```

In this example, we have a `Game` model that has a `name` field and a many-to-many relationship with the `Player` model.

## Implementing Websockets with Django Channels

To handle websockets in Django, we need to define a consumer. A consumer is a class that handles the connection and manages the communication between the server and the client.

Create a new file called `consumers.py` in the `game` app and add the following code:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'game'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'game_update',
                'message': text_data
            }
        )

    async def game_update(self, event):
        message = event['message']
        await self.send(text_data=message)
```

In the above code, we define a `GameConsumer` class that inherits from `AsyncWebsocketConsumer`. We override the `connect`, `disconnect`, and `receive` methods to handle the websocket connection and communication.

The `connect` method is called when a client connects to the websocket. It adds the connection to a group and accepts the connection.

The `disconnect` method is called when a client disconnects from the websocket. It removes the connection from the group.

The `receive` method is called when the server receives a message from a client. It sends the received message to all clients in the group.

Finally, we define a `game_update` method to handle the group send event. It sends the updated message to all clients in the group.

## Wiring Up the URL Routing

To handle the websocket connection, we need to define a URL route that maps to our `GameConsumer`. Open the `routing.py` file in your project directory and add the following code:

```python
from django.urls import path
from .consumers import GameConsumer

websocket_urlpatterns = [
    path('ws/game/', GameConsumer.as_asgi()),
]
```

In the above code, we define a websocket URL route that maps to our `GameConsumer`.

Now, let's add this routing configuration to our ASGI application. Create a new file called `routing.py` in your project directory and add the following code:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from . import routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
```

In the above code, we define our ASGI application using `ProtocolTypeRouter`. We configure it to handle both HTTP and websocket protocols. The `URLRouter` class maps the websocket URL routes to their respective consumers.

## Conclusion

In this blog post, we explored how to implement a real-time game using websockets in Django. We started by setting up the Django project, installing Django Channels, and creating the game model. Then, we implemented the websockets functionality using Django Channels and wired up the URL routing.

Websockets provide a powerful mechanism for creating real-time applications, especially games, where immediate updates are crucial. Django, with the help of Django Channels, allows us to seamlessly integrate websockets into our Django projects.

By following the steps outlined in this post, you should now have a basic understanding of how to implement a real-time game with websockets in Django.

#websockets #Django