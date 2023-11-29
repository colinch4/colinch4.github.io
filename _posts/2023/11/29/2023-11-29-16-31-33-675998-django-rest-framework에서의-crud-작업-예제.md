---
layout: post
title: "[python] Django REST framework에서의 CRUD 작업 예제"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST Framework는 Django 프레임워크를 기반으로한 웹 API 개발을 위한 강력한 도구입니다. 이 예제에서는 Django REST Framework를 사용하여 CRUD(create, retrieve, update, delete) 작업을 수행하는 방법을 다루겠습니다.

## 세팅

가상환경을 설정하고 Django와 Django REST Framework를 설치하세요.

```python
$ python3 -m venv myenv
$ source myenv/bin/activate
(myenv) $ pip install django djangorestframework
```

프로젝트를 생성하고 필요한 파일들을 세팅하세요.

```python
$ django-admin startproject myproject
$ cd myproject
$ django-admin startapp myapp
```

`settings.py` 파일에서 `rest_framework`를 추가하세요.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
    ...
]
```

## 모델 생성

`models.py` 파일을 열고 모델을 정의하세요.

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
```

모델이 정의된 후에 `python manage.py makemigrations`와 `python manage.py migrate` 커맨드를 실행하여 데이터베이스에 테이블을 생성하세요.

## Serializer 생성

`serializers.py` 파일을 생성하고 다음과 같이 Serializer 클래스를 정의하세요.

```python
from rest_framework import serializers
from myapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

## View 생성

`views.py` 파일을 생성하고 다음과 같이 APIView를 상속받는 클래스를 정의하세요.

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Product
from myapp.serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=204)
```

## URL 설정

`urls.py` 파일을 열고 URL을 설정하세요.

```python
from django.urls import path
from myapp.views import ProductList, ProductDetail

urlpatterns = [
    path('api/products/', ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetail.as_view()),
]
```

## 테스트

서버를 실행하고 API에 대한 요청을 테스트하세요.

```python
$ python manage.py runserver
```

- 모든 제품 조회: `GET /api/products/`
- 특정 제품 조회: `GET /api/products/<id>/`
- 제품 생성: `POST /api/products/`
- 제품 수정: `PUT /api/products/<id>/`
- 제품 삭제: `DELETE /api/products/<id>/`

## 결론

이 예제에서는 Django REST Framework를 사용하여 CRUD 작업을 수행하는 방법을 알아보았습니다. Django REST Framework는 강력하고 사용하기 쉬운 도구로 웹 API 개발을 더욱 효율적으로 만들어줍니다. 

더 자세한 정보는 [Django REST Framework 공식 문서](https://www.django-rest-framework.org/)를 참고하시기 바랍니다.