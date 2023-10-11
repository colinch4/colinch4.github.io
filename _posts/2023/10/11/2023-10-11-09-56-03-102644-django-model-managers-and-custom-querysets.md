---
layout: post
title: "Django model managers and custom querysets"
description: " "
date: 2023-10-11
tags: [django, modelmanagers]
comments: true
share: true
---

## Introduction

In Django, model managers and custom querysets are powerful tools that allow developers to customize and enhance the querying capabilities of their models. Model managers provide a convenient way to create custom methods for querying and manipulating model instances, while custom querysets enable developers to define reusable query logic that can be applied to multiple models.

## Django Model Managers

A model manager is a class that controls the behavior of a model's database queries. By default, every Django model has a default manager that provides basic querying functionality. However, you can also create custom managers to add additional methods or modify the default behavior of queries.

To define a custom manager, you need to subclass the `django.db.models.Manager` class. Let's consider an example where we have a `Book` model and we want to create a custom manager to retrieve only the available books:

```python
from django.db import models

class AvailableBooksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    available = models.BooleanField(default=False)

    objects = models.Manager()  # default manager
    available_objects = AvailableBooksManager()  # custom manager
```
In the above example, we define a custom manager called `AvailableBooksManager` that overrides the `get_queryset` method to filter only the available books. We then create a `Book` model with two managers: the default `objects` manager and the `available_objects` custom manager.

Now, we can use the custom manager to retrieve only the available books:

```python
books = Book.available_objects.all()
```

## Custom Querysets

A queryset is a collection of model objects that can be filtered, sliced, and ordered. While model managers provide methods for querying and manipulating the database, custom querysets allow you to define reusable query logic that can be applied across multiple models.

To create a custom queryset, you need to subclass the `django.db.models.query.QuerySet` class and define your custom methods. Let's extend our previous example and create a custom queryset to retrieve books published in the last year:

```python
from django.db import models
from django.utils import timezone

class PublishedLastYearQuerySet(models.QuerySet):
    def published_last_year(self):
        return self.filter(publish_date__gte=timezone.now().year - 1)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    available = models.BooleanField(default=False)

    objects = models.Manager()  # default manager
    available_objects = AvailableBooksManager()  # custom manager
    published_last_year = PublishedLastYearQuerySet.as_manager()
```

In the example above, we define a custom queryset called `PublishedLastYearQuerySet`, which adds a `published_last_year` method to retrieve books published in the last year. We use the `as_manager()` method to convert the queryset into a manager, allowing us to chain the method directly on the model class.

Now, we can retrieve books published last year using the custom queryset:

```python
books = Book.published_last_year.all()
```

## Conclusion

Django model managers and custom querysets offer a great deal of flexibility when it comes to querying and manipulating data. They allow developers to create custom methods and reusable query logic, making it easier to work with complex queries and enhance the querying capabilities of their models. By leveraging these tools, you can build more efficient and maintainable Django applications.

#django #modelmanagers #querysets