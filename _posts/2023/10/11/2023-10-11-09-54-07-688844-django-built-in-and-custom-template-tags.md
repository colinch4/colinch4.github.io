---
layout: post
title: "Django built-in and custom template tags"
description: " "
date: 2023-10-11
tags: [django, templates]
comments: true
share: true
---

In Django, template tags are used to perform various operations and manipulate data within templates. They provide a way to extend the built-in template language and add additional functionality to the templates.

## Built-in Template Tags

Django provides a set of built-in template tags that cover common requirements in web development. These tags can be used directly in your templates without any additional configuration or setup. Some of the commonly used built-in template tags include:
{% raw %}
### {% if %} and {% else %}

The `{% if %}` tag is used to conditionally render content based on a certain condition. It takes an expression and displays the content within the block if the expression evaluates to true. The `{% else %}` tag is optional and can be used to handle the case when the condition is not met.

Example Usage:
```django
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in to continue.</p>
{% endif %}
```

### {% for %}

The `{% for %}` tag is used to iterate over a collection and render the content within the block for each item in the collection. It provides a convenient way to loop through lists, dictionaries, and other iterable objects.

Example Usage:
```django
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

### {% include %}

The `{% include %}` tag is used to include the content of another template within the current template. It allows for modularizing the template structure and reusing common components across multiple templates.

Example Usage:
```django
{% include 'header.html' %}
<body>
    <!-- Page content goes here -->
</body>
{% include 'footer.html' %}
```
{% endraw %}
These are just a few examples of the built-in template tags provided by Django. You can refer to the Django documentation for a complete list of available tags and their usage.

## Custom Template Tags

In addition to the built-in template tags, Django also allows you to create your own custom template tags. This provides flexibility to extend the template language and create tags specific to your application's needs.

To create a custom template tag, you need to define a Python function and register it as a template tag using the `register` decorator. The function should accept the context and any necessary arguments, and return a string that represents the rendered content.

Here's an example of a custom template tag that capitalizes the first letter of a string:

```python
from django import template
register = template.Library()

@register.filter
def capitalize_first(value):
    return value.capitalize()
```

To use this custom template tag in your template, you need to load the tag library and call the tag using the `|` operator:

```django
{% raw %}
{% load my_tags %}

{{ name|capitalize_first }}
{% endraw %}
```
{% raw %}
In the above example, `{% load my_tags %}` loads the custom tag library, and `{{ name|capitalize_first }}` applies the custom tag to the `name` variable.
{% endraw %}
Custom template tags in Django provide a powerful way to encapsulate complex logic and reuse it across templates. They enable you to extend the capabilities of the template language and make your templates more expressive and efficient.

## Conclusion

Django built-in template tags offer a wide range of functionality, including conditional rendering, loops, and template inclusion. Additionally, you have the flexibility to create your own custom template tags to meet the specific requirements of your application. Utilizing both built-in and custom tags can greatly enhance the power and flexibility of your Django templates. So go ahead and explore the possibilities! #django #templates