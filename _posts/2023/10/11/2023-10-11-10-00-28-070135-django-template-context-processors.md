---
layout: post
title: "Django template context processors"
description: " "
date: 2023-10-11
tags: []
comments: true
share: true
---

In Django, a template context processor is a function that adds data to the context of every template in your Django project. It allows you to provide additional context variables that can be used across all your templates without the need to manually pass them in each view function.

## How to Create a Template Context Processor

To create a template context processor in Django, follow these steps:

1. Create a Python module or file, e.g., `context_processors.py`, in your Django app directory.
2. Write a context processor function inside the module. This function should take a request as its first parameter and return a dictionary of context variables.
3. In your Django project's settings module, locate the `TEMPLATES` setting. Inside the `'OPTIONS'` list, add the path to your context processors module as a string.

For example, let's create a custom context processor that adds the current year to the template context:

```python
# context_processors.py

from datetime import date

def current_year(request):
    return {'current_year': date.today().year}
```

In the above example, we have created a context processor function called `current_year` that adds a `current_year` variable to the template context. It uses the `date` class from the `datetime` module to get the current year.

To include this context processor in your Django project, add the following line to your `settings.py` file:

```python
# settings.py

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'myapp.context_processors.current_year',
            ],
        },
    },
]
```

Make sure to replace `'myapp'` with the actual name of your Django app.

## Using the Context Variables in Templates

Once you have created and registered your template context processor, you can use the context variables in your templates. They will be available in all templates rendered by your views.

To use the `current_year` variable we created in our previous example, you can simply access it in a template like this:

```django
<!-- template.html -->

<p>&copy; {{ current_year }} My Django App. All rights reserved.</p>
```

In the above example, `{{ current_year }}` will be replaced with the actual current year value when the template is rendered.

## Conclusion

Django template context processors provide a convenient way to add data to the template context across your entire project without repetition. They allow you to keep your templates clean and DRY (Don't Repeat Yourself), and make it easier to pass common data to all your templates.

By following the steps outlined in this article, you can create and use your own custom context processors in Django.