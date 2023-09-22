---
layout: post
title: "Implementing a real-time job board with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

In this blog post, we will explore how to implement a real-time job board using websockets in Django. The real-time functionality will allow job seekers and employers to see updates to job listings without having to manually refresh the page. We will be utilizing Django Channels, which is a third-party library that enables the use of websockets in Django projects.

## Prerequisites

To follow along with this tutorial, you should have the following:

- Basic knowledge of Django
- Django project set up with Django Channels installed

## Setting up Django Channels

Let's start by setting up Django Channels in our Django project.

1. Install Django Channels using pip:

```
pip install channels
```

2. Add `'channels'` to the `INSTALLED_APPS` list in your project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

3. Include Channels in your project's `urls.py` file:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from myapp.consumers import JobConsumer

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                [
                    path('ws/jobs/', JobConsumer.as_asgi()),
                ]
            )
        ),
    }
)
```

4. Create a new file called `consumers.py` in your app directory and add the following code:

```python
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class JobConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content, **kwargs):
        # Process received message
        # Logic to update job board

        # Example logic to send updated job listings
        await self.send_json({
            'type': 'job_update',
            'content': {
                'job_id': 1,
                'job_title': 'Software Engineer',
                'company': 'Acme Corp',
                'location': 'New York',
            },
        })
```

## Implementing the Real-Time Job Board

Now that we have set up the necessary infrastructure for websockets in Django, let's implement the real-time job board.

1. Create a new template called `job_board.html`:

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>Real-Time Job Board</title>
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/websocket.js' %}"></script>
</head>
<body>
    <h1>Real-Time Job Board</h1>
    <ul id="job-listings"></ul>

    <script>
        const socket = new WebSocket('ws://' + window.location.host + '/ws/jobs/');

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);

            if (data.type === 'job_update') {
                // Update job listings
                const jobListing = document.createElement('li');
                jobListing.innerHTML = `
                    <strong>${data.content.job_title}</strong> at ${data.content.company}
                    - ${data.content.location}
                `;
                document.getElementById('job-listings').appendChild(jobListing);
            }
        };
    </script>
</body>
</html>
```

2. Create a new Django view to render the job board template:

```python
from django.shortcuts import render

def job_board(request):
    return render(request, 'job_board.html')
```

3. Add a new URL pattern in your app's `urls.py` to map to the `job_board` view:

```python
from django.urls import path
from .views import job_board

urlpatterns = [
    ...
    path('jobs/', job_board, name='job_board'),
    ...
]
```

4. Run the Django development server:

```
python manage.py runserver
```

5. Visit `http://localhost:8000/jobs/` in your browser, and you should see the real-time job board in action!

## Conclusion

In this blog post, we have learned how to implement a real-time job board using websockets in Django. By leveraging Django Channels, we were able to create a seamless user experience where job listings update in real-time without the need for manual refreshes. This functionality can greatly enhance the usability and efficiency of job board applications.

#django #websockets