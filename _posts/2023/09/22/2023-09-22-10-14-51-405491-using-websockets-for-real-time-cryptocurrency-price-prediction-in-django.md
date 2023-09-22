---
layout: post
title: "Using websockets for real-time cryptocurrency price prediction in Django"
description: " "
date: 2023-09-22
tags: [Websockets, Django]
comments: true
share: true
---

In this blog post, we will explore how to leverage websockets to create a real-time cryptocurrency price prediction application using Django.

## Introduction
Real-time data is crucial in the world of finance, especially when it comes to predicting cryptocurrency prices. Traditional HTTP requests may not be sufficient for real-time updates as they rely on the client repeatedly sending requests to the server, creating unnecessary traffic.

Websockets provide a bidirectional communication channel between the client and server. This makes them ideal for real-time applications, where data needs to be streamed continuously to the client without requiring constant requests.

## Setting up Django Channels
Django Channels is a great library that allows us to integrate websockets into a Django application. To start, **make sure you have Django Channels installed** by running the following command:

```
pip install channels
```

Next, create a new Django project and app by running the following commands:

```
django-admin startproject real_time_crypto
cd real_time_crypto
python manage.py startapp prediction
```

## Creating the Websocket Consumer
In Django Channels, a consumer handles websocket connections and messages. We will create a websocket consumer in our `prediction` app to handle the real-time updates.

Inside the `prediction` app's `consumers.py` file, add the following code:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class PredictionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
```

## Routing Websocket Requests
To configure routing for the websocket requests, we need to create a `routing.py` file in the `real_time_crypto` project directory. Add the following code:

```python
from django.urls import re_path

from .prediction.consumers import PredictionConsumer

websocket_urlpatterns = [
    re_path(r'ws/prediction/$', PredictionConsumer.as_asgi()),
]
```

Next, update the `asgi.py` file in the project directory to include our websocket URL patterns:

```python
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
```

## Testing the Websocket Connection
To test the websocket connection, let's create a simple HTML and JavaScript file. Create a new file named `index.html` in the `real_time_crypto` project directory and add the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Real-Time Cryptocurrency Price Prediction</title>
</head>
<body>
    <h1>Real-Time Cryptocurrency Price Prediction</h1>

    <div id="price-container"></div>

    <script>
        const socket = new WebSocket('ws://' + window.location.host + '/ws/prediction/');

        socket.onopen = function() {
            console.log('Websocket connection established');
        };

        socket.onmessage = function(event) {
            const data = JSON.parse(event.data);
            console.log('Received data:', data);

            // Update the price container with the received data
            document.getElementById('price-container').innerHTML = data.price;
        };

        socket.onclose = function(event) {
            console.log('Websocket connection closed');
        };
    </script>
</body>
</html>
```

Open the `index.html` file in a web browser and check the console for the "Websocket connection established" message. We have successfully established a websocket connection.

## Broadcasting Cryptocurrency Prices
To simulate real-time price updates, let's create a periodic task that broadcasts random cryptocurrency prices to connected clients.

Inside the `PredictionConsumer` class in `consumers.py`, add the following code:

```python
import asyncio
import json
import random

class PredictionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Start broadcasting cryptocurrency prices
        await self.send_price_updates()

    async def send_price_updates(self):
        while True:
            # Generate random cryptocurrency price
            price = random.uniform(1000, 50000)

            # Prepare the message payload
            payload = json.dumps({'price': price})

            # Send the payload to all connected clients
            await self.send(payload)

            # Delay for 1 second
            await asyncio.sleep(1)
```

## Conclusion
In this blog post, we explored how to utilize websockets in Django to create a real-time cryptocurrency price prediction application. We covered setting up Django Channels, creating a websocket consumer, routing websocket requests, and broadcasting cryptocurrency prices.

By using websockets, we can ensure that our application provides users with up-to-date and real-time information, essential for accurate cryptocurrency price predictions. Embracing the power of websockets opens up endless possibilities for real-time applications in the finance industry.

#Websockets #Django #RealTime #Cryptocurrency #PricePrediction