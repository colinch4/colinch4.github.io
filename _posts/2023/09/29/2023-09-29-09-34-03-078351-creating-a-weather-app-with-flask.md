---
layout: post
title: "Creating a weather app with Flask"
description: " "
date: 2023-09-29
tags: [FlaskWeatherApp, PythonWebDevelopment]
comments: true
share: true
---

In this tutorial, we will be building a weather app using **Flask**, a popular Python web framework. Flask is known for its simplicity and flexibility, making it an excellent choice for developing small to medium-sized web applications.

## Setting Up the Project

### Installing Flask
To start, make sure you have Python installed on your system. You can check your Python version by opening a terminal or command prompt and running the following command:

`python --version`

Next, install Flask by running the following command:

`pip install Flask`

### Creating the Project Structure
Create a new directory for your project and navigate to it in your terminal or command prompt. Inside this directory, create the following files and folders:

- `app.py`: This will be the main file where we write our Flask application.
- `templates/`: This folder will contain our HTML templates.
- `static/`: This folder will contain static files such as CSS and JavaScript.

## Building the Weather App

### Importing Dependencies
In the `app.py` file, start by importing the necessary dependencies:

```python
from flask import Flask, render_template, request
import requests
```

### Creating the Flask App
Next, create an instance of the Flask app and set up a basic route:

```python
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
```

### Handling Form Submission
Add another route to handle the form submission. We will use the OpenWeatherMap API to retrieve weather data based on the user's input.

```python
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')

    # Make an API request to retrieve weather data

    return render_template('weather.html', city=city, weather=weather_data)
```

### Rendering HTML Templates
Create `index.html` and `weather.html` inside the `templates/` folder. These HTML templates will be used to display the home page and weather information, respectively.

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Weather App</title>
</head>
<body>
    <h1>Welcome to the Weather App!</h1>
    <form action="/weather" method="POST">
        <input type="text" name="city" placeholder="Enter a city">
        <button type="submit">Get Weather</button>
    </form>
</body>
</html>

<!-- weather.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Weather</title>
</head>
<body>
    <h1>Weather in {{ city }}</h1>
    <p>{{ weather }}</p>
</body>
</html>
```

### Fetching Weather Data from API
Inside the `weather` route, make a request to the OpenWeatherMap API to fetch weather data for the specified city:

```python
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY')
weather_data = response.json()
```

Remember to replace `YOUR_API_KEY` with your actual API key obtained from OpenWeatherMap.

## Running the App

To run the app, execute the following command in your terminal or command prompt:

`python app.py`

Visit `http://localhost:5000` in your web browser to see the weather app in action. Enter a city in the form and submit it to display the weather details.

That's it! You have successfully created a weather app using Flask. Feel free to explore and enhance the app by adding more features or improving the UI.

**#FlaskWeatherApp #PythonWebDevelopment**