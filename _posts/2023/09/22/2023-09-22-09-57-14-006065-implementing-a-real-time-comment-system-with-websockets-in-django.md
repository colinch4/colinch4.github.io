---
layout: post
title: "Implementing a real-time comment system with websockets in Django"
description: " "
date: 2023-09-22
tags: [comments, commentForm]
comments: true
share: true
---

Websockets have become a popular choice for building real-time applications, allowing for bidirectional communication between the client and the server. In this tutorial, we will explore how to implement a real-time comment system in Django using websockets. 

## Prerequisites

Before we begin, make sure you have the following:

- Django installed on your local machine
- Basic knowledge of Django and JavaScript
- Understanding of how websockets work

## Setting up the Project

1. Create a new Django project:
```python
$ django-admin startproject comment_system
$ cd comment_system
```

2. Create a new Django app for our comment system:
```python
$ python manage.py startapp comments
```

3. Install the required dependencies:
```python
$ pip install channels channels_redis
```

4. Add 'channels' to the `INSTALLED_APPS` list in the `settings.py` file:
```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

5. Update the `settings.py` file to include the required configurations for channels:
```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        },
    },
}
```

## Creating the Comment Model

1. In the `models.py` file of the `comments` app, define the Comment model:
```python
from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

2. Apply the migrations to create the Comment model:
```python
$ python manage.py makemigrations
$ python manage.py migrate
```

## Creating the WebSocket Consumer

1. Create a new file called `consumers.py` in the `comments` app directory:

```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'comments_group',
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'comments_group',
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        
        # create a new comment object here
        
        await self.channel_layer.group_send(
            'comments_group',
            {
                'type': 'comment_message',
                'content': content
            }
        )
    
    async def comment_message(self, event):
        content = event['content']
        await self.send(text_data=json.dumps({
            'content': content
        }))
```

## Routing and Configuration

1. Create a new file called `routing.py` in the `comment_system` directory:

```python
from django.urls import re_path

from .consumers import CommentConsumer

websocket_urlpatterns = [
    re_path(r'ws/comments/$', CommentConsumer.as_asgi()),
]
```

2. Update the `urls.py` file in the `comment_system` directory to include the websocket routing:

```python
from django.urls import path
from . import routing

urlpatterns = [
    ...
]

websocket_urlpatterns = routing.websocket_urlpatterns
```

## Frontend Implementation

1. Include the required JavaScript libraries in your HTML file:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.form/4.3.0/jquery.form.min.js"></script>
```

2. Create a new JavaScript file called `comment.js` and add the following code:

```javascript
$(document).ready(function() { 
    var socket = new WebSocket("ws://" + window.location.host + "/ws/comments/");
    
    socket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var content = data.content;
        $("#comments").append('<li>' + content + '</li>');
    }
    
    $("#commentForm").ajaxForm({
        beforeSubmit: function(formData, jqForm, options) {
            var content = $("#commentContent").val();

            if (content === "") {
                alert("Please enter a comment.");
                return false;
            }
            
            $("#commentContent").val("");
            socket.send(JSON.stringify({
                'content': content
            }));
            
            return false;
        }
    });
});
```

3. Include the `comment.js` file in your HTML file:

```html
{% raw %}
<script src="{% static 'comment.js' %}"></script>
{% endraw %}
```

## Testing the Application

1. Start the Django development server:
```python
$ python manage.py runserver
```

2. Open your browser and navigate to `http://localhost:8000`. You should see a comment form.

3. Enter a comment in the form field and submit it. You should see the comment appear in the comment section without refreshing the page.

Congratulations! You have successfully implemented a real-time comment system with websockets in Django.

#django #websockets