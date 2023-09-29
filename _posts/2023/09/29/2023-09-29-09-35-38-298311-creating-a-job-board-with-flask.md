---
layout: post
title: "Creating a job board with Flask"
description: " "
date: 2023-09-29
tags: [jobboard, Flask]
comments: true
share: true
---

In this blog post, we will explore how to create a job board using Flask, a popular Python web framework. Flask provides a simple and lightweight way of building web applications, making it a great choice for projects like a job board.

## Setting up the Project

Before we dive into the implementation, let's make sure we have Flask installed. You can install Flask by running the following command:

```
pip install flask
```

Once Flask is installed, let's create a new Flask application. Create a new directory for your project and navigate to it in your terminal. Then, create a new Python file, `app.py`, and open it in your preferred text editor.

## Creating the Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Job Board'

if __name__ == '__main__':
    app.run(debug=True)
```

In the code above, we import the `Flask` class from the `flask` module and create a new instance of the `Flask` class. We then define a route decorator (`@app.route('/')`) to handle requests to the root URL. Inside the route function, we return a simple message to indicate that the app is running.

To start the Flask application, we add a conditional block at the end of the file (`if __name__ == '__main__':`) to ensure that the app only runs when the file is executed directly, not when it is imported as a module.

## Adding Job Listings

Now that we have our basic Flask app set up, let's add the ability to display job listings. We can start by creating a dummy job listing data structure. Replace the `home()` function with the following code:

```python
job_listings = [
    {'title': 'Software Engineer', 'company': 'Example Inc.', 'location': 'New York'},
    {'title': 'Web Designer', 'company': 'Sample Co.', 'location': 'San Francisco'},
    {'title': 'Data Analyst', 'company': 'Test Corp.', 'location': 'London'},
]

@app.route('/')
def home():
    return render_template('index.html', job_listings=job_listings)
```

In the code above, we define a list called `job_listings` that contains dictionaries representing job listings. Each dictionary has keys such as `title`, `company`, and `location`, which hold information about each job.

We then modify the `home()` function to render an HTML template called `index.html` and pass the `job_listings` data to the template as a variable.

## Creating the HTML Template

Create a new directory called `templates` in your project folder and create a new HTML file inside it called `index.html`. Open `index.html` in your text editor and add the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Board</title>
</head>
<body>
    <h1>Job Listings</h1>
    <ul>
    {% for job in job_listings %}
        <li>{{ job.title }} - {{ job.company }} - {{ job.location }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

In the HTML template, we use a Jinja2 for loop to iterate over each job in the `job_listings` variable. We then display the job title, company, and location using the `{{ }}` syntax.

## Conclusion

In this blog post, we learned how to create a simple job board using Flask. We set up a basic Flask application, added job listing data, and created an HTML template to display the job listings. This is just the starting point, and you can extend the application by adding features like job search, filtering, and user authentication. Flask provides a flexible foundation for building powerful web applications. Happy building!

#jobboard #Flask