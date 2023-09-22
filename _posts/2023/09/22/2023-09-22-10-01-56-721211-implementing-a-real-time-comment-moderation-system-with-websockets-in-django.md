---
layout: post
title: "Implementing a real-time comment moderation system with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

In this blog post, we'll explore how to build a real-time comment moderation system using websockets in Django. This system will allow for seamless and instant moderation of comments on a website by updating the comment status in real-time without the need for page refreshes.

## Prerequisites

Before we begin, make sure you have the following:

- [Django](https://www.djangoproject.com/) installed
- [Django Channels](https://channels.readthedocs.io/en/stable/) installed
- Basic knowledge of Django and HTML/CSS

## Setting up Django Channels

1. Install Django Channels using pip:

```python
pip install channels
```

2. Add 'channels' to your Django project's `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'channels',
    # ...
]
```

## Creating a Consumer

To handle real-time communication between the server and clients, we need to create a *consumer*. A consumer is a Python class that defines how to handle incoming messages.

1. Create a new file `consumers.py` in your Django app directory.

2. Import the necessary modules:

```python
from channels.generic.websocket import AsyncWebsocketConsumer
```

3. Define a consumer class that extends `AsyncWebsocketConsumer`:

```python
class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Logic to handle connection establishment
    
    async def disconnect(self, close_code):
        # Logic to handle connection closure
    
    async def receive(self, text_data):
        # Logic to handle incoming messages
```

4. Implement the connection, disconnection, and message handling logic as per your requirements. For example, you can add logic to authenticate the user connecting to the websocket and decide whether they have permission to moderate comments.

## Routing Websockets

Now that we have a consumer, we need to configure the routing to route the websocket connections to the consumer.

1. Create a new file `routing.py` in the same Django app directory.

2. Import the necessary modules:

```python
from . import consumers

from django.urls import re_path
```

3. Define the websocket URL patterns:

```python
websocket_urlpatterns = [
    re_path(r'ws/comments/(?P<post_id>\d+)/$', consumers.CommentConsumer.as_asgi()),
]
```

4. In your project's `routing.py` file, import the websocket URL patterns:

```python
from django.urls import include, re_path

urlpatterns = [
    # ...
    re_path(r'^', include('myapp.routing')),
    # ...
]
```

## Frontend Implementation

At this point, the backend setup for the real-time comment moderation system is complete. Let's now implement the frontend.

1. In your HTML template, include the JavaScript code to connect to the websocket and handle real-time updates:

```
{% raw %}
<script src="{% static 'js/comment_ws.js' %}"></script>
{% endraw %}
```

2. Create a new file `comment_ws.js` in your static files directory and write the following code:

```javascript
const commentSocket = new WebSocket('ws://' + window.location.host + '/ws/comments/' + post_id + '/');

// Event handlers for websocket connection
commentSocket.onopen = function(event) {
    console.log('WebSocket connection established.');
    // Additional logic if needed
};

commentSocket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    // Update the comment status in the UI
    // Additional logic if needed
};

commentSocket.onclose = function(event) {
    console.log('WebSocket connection closed.');
    // Additional logic if needed
};

// Additional functions for sending messages and handling user actions
```

3. Modify the comment moderation views to update the comment status using websockets.

## Conclusion

In this tutorial, we have learned how to implement a real-time comment moderation system using websockets in Django. By leveraging Django Channels, we can provide a seamless and efficient experience for moderators to handle comments in real-time. Remember to test and secure your implementation before deploying it to a production environment.

#django #websockets