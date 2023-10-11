---
layout: post
title: "Django internationalization and localization"
description: " "
date: 2023-10-11
tags: [django, internationalization]
comments: true
share: true
---

## Introduction

In today's interconnected world, building websites and applications that cater to a global audience is essential. Django, a popular web framework, provides powerful tools for internationalization (i18n) and localization (l10n). Internationalization refers to the process of adapting an application to support multiple languages, while localization is the process of adapting it to specific regions or cultures.

In this blog post, we will explore how to enable internationalization and localization in a Django project.

## Setting up Internationalization

To enable internationalization in your Django project, follow these steps:

1. Open your project's `settings.py` file.
2. Locate the `LANGUAGE_CODE` setting and set it to the default language code for your project, e.g., 'en-us' for English (United States).

```python
LANGUAGE_CODE = 'en-us'
```

3. Add the `django.middleware.locale.LocaleMiddleware` middleware to the `MIDDLEWARE` setting in your `settings.py` file.

```python
MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]
```

4. Add the `django.contrib.sessions.middleware.SessionMiddleware` middleware above the `LocaleMiddleware` middleware to ensure that translations are stored in the session.

```python
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    ...
]
```

5. Create a directory named `locale` in your project's root directory. This directory will hold the translation files for different languages.

6. Run the following command to create the initial translation files for the default language:

```shell
python manage.py makemessages -l en
```

This command will create a `locale` directory with a subdirectory named `en` containing a `django.po` file.

## Translating Text

The `.po` file created in the previous step is where you can provide translations for the text in your project. To add translations:

1. Open the `django.po` file in a text editor.
2. Locate the `msgid` and `msgstr` fields.
3. Add the translated text in the `msgstr` field, following the format: `msgstr "Translated Text"`.
4. Save the file.

For example, to translate the text "Hello, World!" to Spanish, the `msgstr` field would look like this:

```
msgid "Hello, World!"
msgstr "¡Hola, Mundo!"
```

## Changing the Language

Django provides a convenient way to change the language preference for each user by adding a language switcher. To include a language switcher:

1. In your template, add the following code:

```html
{% load i18n %}

<form action="{% url 'set_language' %}" method="POST">
    {% csrf_token %}
    <input name="next" type="hidden" value="{{ request.get_full_path }}" />
    <select name="language" onchange="this.form.submit()">
        {% get_language_info_list for LANGUAGES as languages %}
        {% for language in languages %}
        <option value="{{ language.code }}" {% if language.code == LANGUAGE_CODE %}selected{% endif %}>
            {{ language.name_local }}
        </option>
        {% endfor %}
    </select>
</form>
```

2. In your project's `urls.py` file, add the following code:

```python
from django.urls import path
from django.views.i18n import set_language

urlpatterns = [
    ...
    path('set_language/', set_language, name='set_language'),
    ...
]
```

## Localization

Apart from translating text, Django also provides localization tools for formatting dates, times, numbers, and currency values according to the user's locale.

For example, to format a datetime object in a specific locale, use the `localize` template filter:

```html
{% load i18n tz %}

{{ my_datetime|localize }}
```

## Conclusion

Django's internationalization and localization features allow developers to build applications that can be easily adapted to various languages and regions. By following the steps outlined in this blog post, you can enable internationalization, translate text, and provide a language switcher for your Django project. Additionally, you can utilize Django's localization tools to format dates, times, numbers, and currency values according to the user's locale.

#django #internationalization