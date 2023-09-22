---
layout: post
title: "Using websockets for real-time chat applications in Django"
description: " "
date: 2023-09-22
tags: [chat, chat]
comments: true
share: true
---

In modern web development, real-time communication has become essential for building interactive applications. Traditional HTTP requests and responses are not suitable for real-time updates and instant messaging. This is where Websockets come into play.

Websockets provide a persistent, bidirectional connection between the client and server, allowing real-time communication without the need for continuous polling or refreshing the page. In this blog post, we will explore how to use Websockets in Django to build a real-time chat application.

## Setting up Django Channels

[Django Channels](https://channels.readthedocs.io/) is a powerful library that extends Django to handle Websockets and other asynchronous protocols. To get started, we need to install Django Channels:

```shell
pip install channels
```

Once installed, we need to add Channels to our Django project. In the settings.py file, add the following to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

Next, we need to configure the routing for our Websocket connections. Create a new file called `routing.py` in your project directory and add the following code:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', ChatConsumer.as_asgi()),
    ]),
})
```

In this example, we assign the `ChatConsumer` as the consumer for the `'/ws/chat/'` route. The `ChatConsumer` is responsible for handling incoming Websocket connections and messages.

## Implementing the ChatConsumer

Now let's create the `ChatConsumer` class. Create a new file called `consumers.py` in your project directory and add the following code:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # called when the Websocket is handshaking as part of the connection process
        await self.accept()

    async def disconnect(self, close_code):
        # called when the socket closes for any reason
        pass

    async def receive(self, text_data):
        # called when data is received from Websocket
        pass
```

For now, we have implemented the basic skeleton of our `ChatConsumer`. We accept the Websocket connection, handle disconnections, and receive data from the client. In order to make our chat application functional, we will need to implement the actual logic for handling messages and broadcasting them to other connected clients.

## Broadcasting Messages

To broadcast messages to all connected clients, we will use Django Channels' **groups** feature. Groups allow us to send messages to multiple consumers at once. Update your `consumers.py` file with the following code:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # called when the Websocket is handshaking as part of the connection process
        await self.accept()

        # join a group named 'chat'
        await self.channel_layer.group_add('chat', self.channel_name)

    async def disconnect(self, close_code):
        # called when the socket closes for any reason
        await self.channel_layer.group_discard('chat', self.channel_name)

    async def receive(self, text_data):
        # called when data is received from Websocket
        await self.channel_layer.group_send(
            'chat',
            {'type': 'chat_message', 'message': text_data}
        )

    async def chat_message(self, event):
        # called when a message is received from the 'chat' group
        message = event['message']

        # send the message to the Websocket
        await self.send(text_data=message)
```

In the `connect` method, we join the 'chat' group using the channel's unique name. When a client sends a message, it is received in the `receive` method, which then broadcasts the message to all clients in the 'chat' group using the `group_send` method. Finally, the `chat_message` method sends the received message back to the client.

## Integrating Websockets with Django views

To integrate Websockets with Django views, we need to make a small change in our `settings.py` file. Add the following code to the end of your `settings.py` file:

```python
ASGI_APPLICATION = '<project_name>.routing.application'
```

Replace `<project_name>` with the name of your Django project.

Now, create a new file called `chat.html` in your project directory and add the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Real-time Chat Example</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            const chatSocket = new WebSocket('ws://localhost:8000/ws/chat/');
            
            chatSocket.onmessage = function(e) {
                const message = JSON.parse(e.data).message;
                $('#chat').append('<div>' + message + '</div>');
            };

            $('#chat-form').on('submit', function(event) {
                event.preventDefault();
                const messageInput = $('#message');
                const message = messageInput.val();
                chatSocket.send(JSON.stringify({'message': message}));
                messageInput.val('');
            });
        });
    </script>
</head>
<body>
    <div id="chat"></div>
    <form id="chat-form" action="#">
        <input type="text" id="message" autocomplete="off" placeholder="Type your message">
        <button type="submit">Send</button>
    </form>
</body>
</html>
```

This HTML template establishes a Websocket connection and sends messages to the server using jQuery. When a message is received, it is displayed in the chat window.

## Conclusion

In this blog post, we explored how to use Websockets in Django to build a real-time chat application. We learned how to set up Django Channels, implement the `ChatConsumer`, broadcast messages using groups, and integrate Websockets with Django views.

Websockets provide a powerful tool for building real-time features in web applications. By using Django Channels, we can easily implement Websockets functionality in our Django projects and provide a seamless real-time chat experience to our users.

#django #websockets