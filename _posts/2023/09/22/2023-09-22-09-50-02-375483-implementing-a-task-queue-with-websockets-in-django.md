---
layout: post
title: "Implementing a task queue with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, DjangoChannels]
comments: true
share: true
---

In Django, it's common to handle long-running tasks asynchronously using task queues. Traditional task queue systems involve polling for task completion status. However, with the advent of WebSockets, we can implement a more efficient and real-time approach to handle long-running tasks.

## Using Django Channels

[Django Channels](https://channels.readthedocs.io/) is a great package that enables WebSockets and asynchronous behavior in Django applications. We'll be using Channels to implement our task queue with WebSockets.

First, make sure you have Django Channels installed in your project:
```python
pip install channels
```

## Creating the Task Queue

To create a task queue, we need to define three components:

1. **Message Model**: This is the model that represents a task in the database. It should have fields for the task details (e.g., name, parameters, status).

2. **Task Consumer**: This is the consumer class that handles the task execution. It receives a WebSocket connection and listens for incoming tasks. When a task is received, it should be saved in the database and then executed asynchronously.

3. **Task Publisher**: This is the view or consumer that accepts incoming tasks from clients and forwards them to the task consumer. It should establish a WebSocket connection with the client and send/receive messages in real-time.

Let's look at an example implementation:

**models.py**
```python
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    # ... other fields for task details
    status = models.CharField(max_length=10, default='pending')  # or use choices for status options
```

**consumers.py**
```python
import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Task

class TaskConsumer(AsyncJsonWebsocketConsumer):
    async def receive_json(self, content, **kwargs):
        task = Task.objects.create(name=content['name'], ...)  # Save task in database
        await asyncio.sleep(1)  # Simulate task execution delay
        task.status = 'completed'
        task.save()
        await self.send_json({'status': 'completed', 'task_id': task.id})
```

**consumers.py** (Task Publisher)
```python
from channels.generic.websocket import WebsocketConsumer

class TaskPublisher(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        self.send(text_data)
```

## Setting Up Routing

To handle WebSocket connections and route them to the appropriate consumers, we need to define routing configuration.

**routing.py**
```python
from django.urls import path
from .consumers import TaskConsumer, TaskPublisher

websocket_urlpatterns = [
    path('tasks/', TaskPublisher.as_asgi()),
    path('task-consumer/', TaskConsumer.as_asgi()),
]
```

## Usage

To use the task queue, we can send WebSocket messages to the task publisher. For example:

**JavaScript client using WebSocket API**

```javascript
const socket = new WebSocket('ws://localhost:8000/tasks/');

socket.onopen = function(event) {
    const task = {name: 'Example Task'};  // your task details here
    socket.send(JSON.stringify(task));  // send task to the server
};

socket.onmessage = function(event) {
    const response = JSON.parse(event.data);
    if (response.status === 'completed') {
        console.log('Task completed!');
    }
};
```

## Conclusion

By combining Django Channels and WebSockets, we can implement a task queue system that provides real-time updates. This approach eliminates the need for constant polling and improves the efficiency and responsiveness of your application.

#django #DjangoChannels