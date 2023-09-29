---
layout: post
title: "Flask and web scraping libraries (e.g., BeautifulSoup)"
description: " "
date: 2023-09-29
tags: [webdevelopment, python]
comments: true
share: true
---

# Introduction
Web scraping is a technique used to extract data from websites. It can be a powerful tool for gathering information, automating repetitive tasks, or conducting research. In this blog post, we will explore how to combine the Flask framework with web scraping libraries like BeautifulSoup to build web applications that retrieve and display data from websites. 

## Installing Flask and BeautifulSoup
First, we need to install Flask and BeautifulSoup. Open your terminal or command prompt and execute the following commands:
```
pip install flask
pip install beautifulsoup4
```

## Setting up a Flask Application
To get started, let's create a new directory for our Flask application and navigate into it. Inside the directory, create a new file called `app.py`. This will be our main Flask application file.

Open `app.py` in a text editor and let's start by importing the necessary modules:
```python
from flask import Flask, render_template
from bs4 import BeautifulSoup
```

Next, we need to initialize the Flask application:
```python
app = Flask(__name__)
```

## Web Scraping with BeautifulSoup
Now that we have Flask set up, let's dive into web scraping. For this example, we will scrape data from a website that lists the top headlines. Replace the contents of the `app` route in `app.py` with the following code:
```python
@app.route('/')
def index():
    url = 'https://example.com/top-headlines'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    for headline in soup.find_all('h2', class_='headline'):
        headlines.append(headline.text)
        
    return render_template('index.html', headlines=headlines)
```

In the code above, we make a request to the specified URL and create a BeautifulSoup object from the response HTML. We then find all the headline elements on the page and store their text content in a list. Finally, we pass the headlines list to the `render_template()` function, which will render the data in an HTML template.

## Creating the HTML Template
Now, let's create an HTML template to display the scraped headlines. Inside the same directory as `app.py`, create a new directory called `templates`. Inside the `templates` directory, create a file called `index.html`. Add the following code to `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Scraped Headlines</title>
</head>
<body>
    <h1>Top Headlines</h1>
    <ul>
        {% for headline in headlines %}
        <li>{{ headline }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

The above code creates a simple HTML page with a heading and a list. We use the Jinja templating engine to iterate over the headlines passed from the Flask route and dynamically generate list items.

## Running the Flask Application
To run the Flask application, go back to your terminal or command prompt and navigate to the directory where `app.py` is located. Execute the following command:
```
python app.py
```

Open your web browser and visit `http://localhost:5000`. You should see the scraped headlines displayed on the webpage.

# Conclusion
Combining Flask with web scraping libraries like BeautifulSoup allows us to build powerful web applications that retrieve and display data from websites. We explored the process of installing Flask and BeautifulSoup, setting up a Flask application, scraping data with BeautifulSoup, and rendering it in an HTML template. The possibilities for web scraping with Flask are endless, and it opens up opportunities for automating tasks, conducting research, and much more.

#webdevelopment #python