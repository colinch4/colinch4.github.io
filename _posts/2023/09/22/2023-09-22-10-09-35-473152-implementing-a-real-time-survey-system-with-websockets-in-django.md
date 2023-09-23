---
layout: post
title: "Implementing a real-time survey system with websockets in Django"
description: " "
date: 2023-09-22
tags: [survey, django]
comments: true
share: true
---

In this blog post, we will explore how to implement a real-time survey system using websockets in Django. Websockets provide a bi-directional communication channel between the client and the server, enabling us to build real-time applications.

## Prerequisites

Before we begin, make sure you have the following installed:

- Python 3.x
- Django
- Django Channels

## Setting up Django Project

1. Create a new Django project by running the following command:
   ```sh
   django-admin startproject mysurveyproject
   ```

2. Create a new Django app within the project:
   ```sh
   cd mysurveyproject
   python manage.py startapp surveyapp
   ```

3. Install Django Channels:
   ```sh
   pip install channels
   ```

4. Add 'channels' to the `INSTALLED_APPS` list in the `settings.py` file of your project:
   ```python
   INSTALLED_APPS = [
       ...
       'channels',
       ...
   ]
   ```

5. Configure channels in your project's `settings.py` file:
   ```python
   CHANNELS = {
       "default": {
           "BACKEND": "channels.layers.InMemoryChannelLayer",
       },
   }
   ```

6. Specify the URL routing for Django Channels in the project's `asgi.py` file:
   ```python
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysurveyproject.settings')
   application = get_asgi_application()

   from channels.routing import ProtocolTypeRouter, URLRouter
   from channels.auth import AuthMiddlewareStack

   from surveyapp.routing import websocket_urlpatterns

   application = ProtocolTypeRouter({
       'http': application,
       'websocket': AuthMiddlewareStack(
           URLRouter(
               websocket_urlpatterns
           )
       ),
   })
   ```

## Building a Real-time Survey App

1. Create a new file `routing.py` inside the `surveyapp` directory and add the following code:
   ```python
   from django.urls import re_path

   from . import consumers

   websocket_urlpatterns = [
       re_path(r'ws/survey/(?P<survey_id>\d+)/$', consumers.SurveyConsumer.as_asgi())
   ]
   ```

2. Create a new file `consumers.py` inside the `surveyapp` directory and add the following code:
   ```python
   from channels.generic.websocket import AsyncWebsocketConsumer
   import json

   class SurveyConsumer(AsyncWebsocketConsumer):
       async def connect(self):
           self.survey_id = self.scope['url_route']['kwargs']['survey_id']
           self.group_name = 'survey_%s' % self.survey_id

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
           message = json.loads(text_data)
           # Process the received survey response
           # Broadcast the response to all connected clients

           await self.channel_layer.group_send(
               self.group_name,
               {
                   'type': 'send_survey_response',
                   'message': message
               }
           )

       async def send_survey_response(self, event):
           message = event['message']
           await self.send(json.dumps(message))
   ```

3. Update the `urls.py` file in your project with the following code:
   ```python
   from django.urls import path
   from surveyapp import views

   urlpatterns = [
       path('survey/<int:survey_id>/', views.survey_view, name='survey'),
   ]
   ```

4. Create a new file `views.py` inside the `surveyapp` directory and add the following code:
   ```python
   from django.shortcuts import render

   def survey_view(request, survey_id):
       return render(request, 'survey.html', {'survey_id': survey_id})
   ```

5. Create a new template file `survey.html` inside a `templates/surveyapp` directory and add the following code:
   ```html
   {% raw %}
   <!DOCTYPE html>
   <html>
   <head>
       <title>Real-time Survey</title>
       <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
   </head>
   <body>
       <h1>Survey ID: {{ survey_id }}</h1>
       
       <form id="survey-form">
           <!-- your survey questions and inputs here -->
       </form>

       <script>
           var socket = new WebSocket('ws://' + window.location.host + '/ws/survey/{{ survey_id }}/');
           socket.onmessage = function (e) {
               // handle received survey response from server
           };

           $("#survey-form").on("submit", function (e) {
               e.preventDefault();
               var surveyData = $(this).serialize();
               socket.send(JSON.stringify(surveyData));
           });
       </script>
   </body>
   </html>
   {% endraw %}
   ```

## Testing the Real-time Survey App

1. Start the development server:
   ```sh
   python manage.py runserver
   ```

2. Open the browser and navigate to `http://localhost:8000/survey/1/`, where `1` is the survey ID. You will see the survey form.

3. Open another browser window and navigate to the same URL. Fill out the form in one window and observe how the response is instantly updated in both windows.

Congratulations! You have successfully implemented a real-time survey system using websockets in Django.

#django #websockets