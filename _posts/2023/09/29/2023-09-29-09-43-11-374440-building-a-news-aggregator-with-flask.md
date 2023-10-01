---
layout: post
title: "Building a news aggregator with Flask"
description: " "
date: 2023-09-29
tags: [python, flask]
comments: true
share: true
---

In today's digital age, keeping up with the latest news can be overwhelming with the vast amount of information available on the internet. Luckily, we can leverage technology to create a news aggregator app that brings together the latest news from various sources into one convenient place. In this tutorial, we will explore how to build a news aggregator app using Flask, a popular web framework in Python.

## Prerequisites

Before we dive into building our news aggregator app, make sure you have the following prerequisites installed:

- Python 3.x
- Flask

You can install Flask by running the following command in your terminal:

```
pip install flask
```

## Setting Up the Project

First, let's create a new directory for our project and navigate into it:

```bash
mkdir news-aggregator
cd news-aggregator
```

Next, we'll create a virtual environment to isolate our project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

Now, let's install the necessary libraries for our project:

```bash
pip install flask requests
```

## Creating the Flask App

In the project directory, create a new file called `app.py` and open it with your favorite text editor.

```python
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch news articles using an API
    response = requests.get('https://api.example.com/news')

    # Process the data and pass it to the template
    articles = response.json()['articles']
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run()
```

In this code snippet, we import the necessary modules, create a Flask app instance, and define a route for the homepage (`/`). Inside the route function, we make a request to an example news API and retrieve a list of articles. Finally, we pass the articles to a template called `index.html`, which we will create shortly.

## Creating the Template

In the project directory, create a new directory called `templates` and navigate into it.

```bash
mkdir templates
cd templates
```

Inside the `templates` directory, create a new file called `index.html` and open it with your text editor.

```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>News Aggregator</title>
</head>
<body>
    <h1>Latest News</h1>
    <ul>
        {% for article in articles %}
        <li>
            <h3>{{ article['title'] }}</h3>
            <p>{{ article['description'] }}</p>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
{% endraw %}
```

In this template, we iterate over the `articles` list using Flask's templating engine to display each article's title and description. Feel free to customize the HTML structure and styling according to your preferences.

## Running the App

To run the Flask app, navigate back to the project directory and execute the following command in your terminal:

```bash
python app.py
```

Open your web browser and visit [http://localhost:5000](http://localhost:5000) to see the news aggregator app in action. You should see a list of the latest news articles fetched from the API.

## Conclusion

Congrats! You have successfully built a news aggregator app using Flask. This is just a starting point, and you can further enhance the app by adding features such as user authentication, article filtering, and personalized news recommendations. Happy coding!

#python #flask #news-aggregator