---
layout: post
title: "Creating a job recommendation platform with Flask"
description: " "
date: 2023-09-29
tags: [jobrecommendation, flask]
comments: true
share: true
---

Are you looking to build a job recommendation platform? Flask, a popular Python web framework, can help you achieve this. In this blog post, we'll guide you through the process of creating a job recommendation platform using Flask.

## Setting up the Environment

First, we need to set up our development environment. Make sure you have Python installed on your system. Create a virtual environment and activate it using the following commands:

```python
python3 -m venv myenv
source myenv/bin/activate
```

Next, we'll install Flask. Run the following command to install Flask:

```python
pip install flask
```

## Building the Database

For our job recommendation platform, we need a database to store job data. Let's use SQLite, a lightweight and easy-to-use database. Create a new file `database.py` and add the following code:

```python
import sqlite3

def create_database():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE jobs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT NOT NULL)''')
    conn.commit()
    conn.close()
```

This code creates a new SQLite database file `jobs.db` and defines a table `jobs` to store job details including title, company, location, and description.

## Creating the Flask Application

Now, let's create the Flask application. In the project directory, create a new file `app.py` and add the following code:

```python
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM jobs')
    jobs = c.fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)
```

In this code, we import the necessary modules and create a Flask instance. We define a route `/` and a corresponding function `home()` that retrieves job data from the database and passes it to the `index.html` template.

## Creating the HTML Template

Next, let's create the HTML template for displaying job recommendations. In the project directory, create a new folder `templates` and inside it, create a file `index.html`. Add the following code to the `index.html` file:

```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>Job Recommendations</title>
</head>
<body>
    <h1>Job Recommendations</h1>
    <ul>
        {% for job in jobs %}
        <li>{{ job.title }} - {{ job.company }}, {{ job.location }}</li>
        {% endfor %}
    </ul>
</body>
</html>
{% endraw %}
```

This template uses Jinja2, a popular templating engine for Flask, to iterate through the `jobs` list and display each job's details.

## Running the Application

To run the Flask application, save all files and execute the following command in the terminal:

```python
FLASK_APP=app.py flask run
```

You should see a message indicating that the Flask application is running. Open your browser and visit http://localhost:5000 to see the job recommendations.

## Conclusion

Congratulations! You have successfully created a job recommendation platform using Flask. Feel free to enhance the functionality by adding features like user authentication and personalized job recommendations based on user preferences. Flask provides a flexible and powerful framework for building web applications, making it an excellent choice for projects like this.

#jobrecommendation #flask