---
layout: post
title: "Flask template inheritance and macro usage"
description: " "
date: 2023-09-29
tags: [hashtags, Flask]
comments: true
share: true
---

Flask is a popular web framework for building Python-based web applications. One of the key features of Flask is its template engine, which allows you to separate the presentation layer from the business logic of your application. In this blog post, we will explore two important concepts in Flask templates: template inheritance and macro usage.

## Template Inheritance

Template inheritance is a powerful feature in Flask that allows you to create a base template with common layout and structure, and then extend or override specific sections in child templates. This way, you can maintain consistency across multiple pages while still being able to customize individual pages as needed.
{% raw %}
To create a base template, you need to define a template that contains all the common elements such as the header, footer, and navigation bar. You can use the `{% block %}` statement to indicate sections that can be overridden in child templates. For example:
{% endraw %}
```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    <header>
        <!-- header content here -->
    </header>
    
    <nav>
        <!-- navigation bar here -->
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <!-- footer content here -->
    </footer>
</body>
</html>
{% endraw %}
```
{% raw %}
In the above example, the `{% block %}` statements define three sections: `title`, `content`, and the rest of the content are default sections. Any child template that extends this base template can override these blocks by using the same block name. For example, the "about" page template could look like:
{% endraw %}
```html
{% raw %}
{% extends "base.html" %}

{% block title %}
    About Us - My App
{% endblock %}

{% block content %}
    <h1>About Us</h1>
    <p>This is the about page of our app.</p>
{% endblock %}
{% endraw %}
```

By using template inheritance, you can easily update the common elements across all pages by modifying the base template, without having to duplicate code in each child template.

## Macro Usage

In addition to template inheritance, Flask also provides macros, which are reusable chunks of code that can be included in different parts of your templates. Macros are useful for creating reusable UI components such as navigation bars, buttons, or forms.
{% raw %}
To define a macro, you can use the `{% macro %}` statement followed by the name of the macro. Inside the macro, you can define the HTML or other content that will be included when the macro is called. For example:
{% endraw %}
```html
{% raw %}
{% macro button(text, url) %}
    <a href="{{ url }}">{{ text }}</a>
{% endmacro %}
{% endraw %}
```

To use the macro, you can call it with the `{% call %}` statement, passing the required arguments. For example:

```html
{% call button('Click Me', '/my-url') %}
```

This will render the button macro with the specified text and URL.

Macros can also accept optional arguments and have default values. You can define default values by using the `default` keyword followed by the desired value. For example:

```html
{% raw %}
{% macro button(text, url, color='blue') %}
    <a href="{{ url }}" style="background-color: {{ color }}">{{ text }}</a>
{% endmacro %}
{% endraw %}
```

In this example, if the color argument is not specified when calling the macro, it will default to "blue".

Using macros can greatly improve code reusability and make your templates more concise and easier to maintain.

## Conclusion

Flask provides powerful features like template inheritance and macros to help you build dynamic and reusable templates for your web applications. Template inheritance allows you to create a base template with common elements and customize them in child templates, while macros enable you to create reusable UI components. By leveraging these features, you can create well-structured and maintainable templates for your Flask applications.

#hashtags: #Flask #Templates