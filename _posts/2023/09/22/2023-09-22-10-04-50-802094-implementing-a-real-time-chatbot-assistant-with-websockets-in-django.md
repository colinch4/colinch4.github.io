---
layout: post
title: "Implementing a real-time chatbot assistant with websockets in Django"
description: " "
date: 2023-09-22
tags: [chat, chat]
comments: true
share: true
---

In this blog post, we will explore how to implement a real-time chatbot assistant using websockets in Django. Websockets provide a bidirectional communication channel between the client and the server, allowing for real-time updates without the need for frequent polling.

## Prerequisites

Before we begin, make sure you have the following:

1. Python and Django installed on your machine.
2. An understanding of Django views, models, and templates.
3. Basic knowledge of JavaScript and HTML.

## Installing Required Packages

To start, create a new Django project and navigate to its directory. Then, install the necessary packages by running the following command:

```bash
pip install channels channels-redis
```

We will be using the Channels library, which allows us to handle websockets in Django, and the Channels Redis backend for scalability.

## Setting Up Channels

Next, let's configure Channels in our Django project. Open the `settings.py` file and add the following lines:

```python
INSTALLED_APPS = [
    ...,
    'channels',
]

ASGI_APPLICATION = '<your_project_name>.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        },
    },
}
```

Here, we are adding Channels to the `INSTALLED_APPS` list and configuring the `ASGI_APPLICATION` to use Channels' application. We also specify the backend to use Redis as the channel layer.

## Creating the Chat Application

Now, let's create our chat application. In Django, an application is a self-contained module that encapsulates related functionalities.

Run the following command to create a new app:

```bash
python manage.py startapp chat
```

Inside the `chat` directory, create a file named `routing.py` with the following content:

```python
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]
```

This file defines the URL patterns for our chat websocket. In this example, we use the `/ws/chat/` path.

Next, create a new file called `consumers.py` inside the `chat` directory with the following code:

```python
import asyncio
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'chat_group'

        # Join the chat group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the chat group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming messages
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send the message to the chat group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send the chat message to the websocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
```

This consumer class handles the WebSocket connection, incoming messages, and sending messages to the chat group.

## Configuring the URL Routing

Open the project's main `urls.py` file and add the following lines:

```python
from django.urls import include, path
from django.contrib import admin

websocket_urlpatterns = [
    path('ws/', include('chat.routing.websocket_urlpatterns'))
]

urlpatterns = [
    ...,
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]
```

This configuration will include the routing configuration for our chat application.

## Creating the Chat Interface

Now, let's create the HTML template for the chat interface. Inside the `chat` application directory, create a new directory named `templates`. Inside the `templates` directory, create a new file called `chat.html` with the following code:

```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot Assistant</title>
    <script src="{% static 'chat/chat.js' %}"></script>
</head>
<body>
    <h1>Chatbot Assistant</h1>
    <div id="chat-log"></div>
    <input type="text" id="chat-input" />
    <button id="chat-send">Send</button>
</body>
</html>
{% endraw %}
```

This is a basic HTML template for our chat interface. It includes a script tag to load the `chat.js` script.

## Implementing the Chatbot

Inside the `static` directory of the `chat` application, create a new file called `chat.js` with the following code:

```javascript
const chatSocket = new WebSocket('ws://localhost:8000/ws/chat/');

chatSocket.onmessage = function (e) {
    const message = JSON.parse(e.data)['message'];
    document.querySelector('#chat-log').innerHTML += `<p>${message}</p>`;
};

document.querySelector('#chat-send').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-input');
    const message = messageInputDom.value;
    messageInputDom.value = '';

    chatSocket.send(JSON.stringify({
        'message': message
    }));
};
```

This JavaScript code establishes a WebSocket connection with our Django server and handles incoming and outgoing messages.

## Running the Application

To run the application, start the Django development server by running the following command:

```bash
$ python manage.py runserver
```

Visit `http://localhost:8000/` in your web browser. You should see the chat interface.

## Conclusion

In this tutorial, we have learned how to implement a real-time chatbot assistant using websockets in Django. By leveraging websockets and Channels, we can create interactive and responsive chat applications that provide a seamless user experience. Happy coding!

#Websockets #Django