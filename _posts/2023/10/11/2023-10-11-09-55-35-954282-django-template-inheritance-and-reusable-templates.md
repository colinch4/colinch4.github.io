---
layout: post
title: "Django template inheritance and reusable templates"
description: " "
date: 2023-10-11
tags: [django]
comments: true
share: true
---

In Django, template inheritance is a powerful feature that allows you to create reusable templates and build a consistent look and feel across your web application. With template inheritance, you can define a base template that contains common elements and then extend it in child templates to add or override specific content blocks.

### The Base Template

The base template serves as the foundation for your web pages. It typically includes the basic HTML structure, common CSS and JavaScript files, and any other elements that should be present on every page. To define a base template, create a new HTML file and add the following code:

```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <header>
        <!-- Common header content goes here -->
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <!-- Common footer content goes here -->
    </footer>
</body>
</html>
{% endraw %}
```

In this example, we have defined a base template that includes a title block, a header section, a main content block, and a footer section.

### Child Templates

To create a child template that extends the base template, create a new HTML file and add the following code:

```html
{% raw %}
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome to my website!</h1>
    <p>This is the home page content.</p>
{% endblock %}
{% endraw %}
```
{% raw %}
In this child template, we use the `{% extends 'base.html' %}` tag to indicate that we want to inherit from the base template. We can then define content within specific blocks to replace or add to the content defined in the base template. In this example, we override the title block with "Home" and add some content to the content block.
{% endraw %}
By using inheritance, you can easily create additional child templates that extend the base template and create a consistent layout across multiple pages. This allows you to make changes in one place and have them reflected across all of your web pages.

### Conclusion

Django template inheritance provides a powerful way to create reusable templates and maintain a consistent look and feel across your web application. By defining a base template and extending it in child templates, you can easily add or override specific content blocks while keeping the common elements intact. This helps to make your code more modular, maintainable, and DRY (Don't Repeat Yourself).

#seo #django