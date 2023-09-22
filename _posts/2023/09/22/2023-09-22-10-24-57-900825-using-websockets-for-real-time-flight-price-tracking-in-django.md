---
layout: post
title: "Using websockets for real-time flight price tracking in Django"
description: " "
date: 2023-09-22
tags: [Websockets, Django]
comments: true
share: true
---

In this blog post, we will explore how to incorporate websockets into a Django application to implement real-time flight price tracking. 

## Why use websockets?

Traditionally, when building web applications, the client would need to regularly send requests to the server to fetch updated data. This approach can be inefficient and slow, especially for scenarios where real-time data updates are required, such as flight prices.

Websockets offer a better solution for real-time communication between client and server. They establish a persistent, bidirectional connection, allowing for efficient and instantaneous data updates. This makes them ideal for implementing features like real-time flight price tracking.

## Setting up Django Channels

Django Channels is a third-party library that enables the use of websockets in Django applications. To get started, you will need to install Django Channels using pip:

```
pip install channels
```

After installation, add `'channels'` to your Django project's `INSTALLED_APPS`.

Next, you will need to configure your Django project for Channels. In your project's `settings.py` file, add the following:

```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
```

This configuration sets up an in-memory channel layer for simplicity. In a production environment, you would consider using a more robust and scalable channel layer like Redis.

## Implementing Flight Price tracking

Now that we have Django Channels set up, we can proceed with implementing real-time flight price tracking.

1. **Create a WebSocket consumer:** Start by creating a new file called `consumers.py` in your Django app directory. In this file, define a websocket consumer class that will handle incoming websocket connections.

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class FlightPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
```

2. **Register the consumer:** In your Django app's `routing.py` file, import the websocket consumer and define the routing configuration.

```python
from .consumers import FlightPriceConsumer

websocket_urlpatterns = [
    path('ws/flight-price/', FlightPriceConsumer.as_asgi()),
]
```

3. **Client-side implementation:** On the client-side, you will need to establish a websocket connection and handle the data received from the server. This can be done using JavaScript.

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/flight-price/');

ws.onmessage = function(event) {
    const flightPrice = JSON.parse(event.data);
    // Handle the flight price data
};

ws.onclose = function(event) {
    // Handle websocket closed event
};
```

4. **Sending flight price updates:** In the `FlightPriceConsumer` class, update the `receive` method to handle incoming flight price subscription requests and periodically send flight price updates back to the client.

```python
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class FlightPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Parse the subscription request from the client
        subscription = json.loads(text_data)

        # Simulate flight prices update every 1 second
        while True:
            # Fetch flight price from a data source or API
            flight_price = get_flight_price(subscription['flight_id'])

            # Send flight price data to client
            await self.send(json.dumps({'flight_price': flight_price}))

            # Wait for 1 second
            await asyncio.sleep(1)
```

5. **Handle flight price updates on the client side:** Finally, on the client-side, you can handle the flight price updates received from the server and update the UI accordingly.

```javascript
ws.onmessage = function(event) {
    const flightPrice = JSON.parse(event.data);
    // Update UI with the new flight price
};
```

## Conclusion

Using websockets with Django Channels, you can easily implement real-time flight price tracking in your Django application. This enables you to provide your users with instant updates on flight prices without the need for manual page refreshes. By leveraging the power of websockets, you can enhance the user experience and make your application more dynamic. 

#Websockets #Django