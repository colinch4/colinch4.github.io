---
layout: post
title: "[python] Django REST framework에서의 폼(Form)과 폼셋(Formset) 사용 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework는 웹 애플리케이션의 API를 개발할 때 많은 도움을 줍니다. 이 중에서도 폼(Form)과 폼셋(Formset)을 사용하여 데이터의 유효성 검사와 입력을 처리할 수 있습니다. 이번 포스트에서는 Django REST framework에서 폼과 폼셋을 어떻게 사용하는지 살펴보겠습니다.

## 1. 폼 (Form) 사용하기

Django REST framework에서 폼을 사용하려면 먼저 `forms.Form` 클래스를 상속받는 폼 클래스를 정의해야 합니다. 이 클래스는 필드와 각 필드의 유효성 검사 메소드를 포함합니다.

```python
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
```

위의 코드에서는 세 가지 필드인 `name`, `email`, `password`를 정의하고 있습니다. 각 필드는 `forms.CharField()` 또는 `forms.EmailField()`와 같은 유효성 검사 메소드를 사용하여 설정할 수 있습니다.

폼을 사용하기 위해선 뷰(view)에서 폼 인스턴스를 생성하고 요청(request) 데이터를 폼에 바인딩해야 합니다. 그리고 나서 `is_valid()` 메소드를 호출하여 데이터의 유효성을 검사할 수 있습니다.

```python
from rest_framework import views

class MyView(views.APIView):
    def post(self, request):
        form = MyForm(request.data)
        if form.is_valid():
            # 폼 데이터가 유효한 경우 처리 로직 수행
            return Response({'message': 'success'})
        else:
            # 폼 데이터가 유효하지 않은 경우 에러 메시지 반환
            return Response({'message': 'validation error', 'errors': form.errors})
```

위의 예제에서는 POST 요청 데이터를 받아와 `MyForm` 인스턴스를 생성하고 `is_valid()` 메소드를 호출하여 유효성 검사를 수행하고 있습니다. 유효하지 않은 경우 에러 메시지를 반환합니다.

## 2. 폼셋 (Formset) 사용하기

폼셋(Formset)은 동일한 형태의 폼을 여러 개 다룰 때 사용됩니다. Django REST framework에서 사용하는 방법은 Django의 기본적인 폼셋과 동일합니다.

```python
from django import forms
from django.forms import formset_factory

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

MyFormSet = formset_factory(MyForm, extra=3)
```

위의 코드에서는 `MyForm` 폼 클래스를 정의하고 `formset_factory` 함수를 사용하여 폼셋 클래스를 생성하고 있습니다. `extra` 파라미터를 사용하여 폼셋에 추가되는 폼의 개수를 지정할 수 있습니다.

폼셋을 사용하기 위해서는 뷰(view)에서 폼셋 인스턴스를 생성하고 요청(request) 데이터를 바인딩해야 합니다.

```python
from rest_framework import views

class MyView(views.APIView):
    def post(self, request):
        formset = MyFormSet(request.POST)
        if formset.is_valid():
            # 폼셋 데이터가 유효한 경우 처리 로직 수행
            return Response({'message': 'success'})
        else:
            # 폼셋 데이터가 유효하지 않은 경우 에러 메시지 반환
            return Response({'message': 'validation error', 'errors': formset.errors})
```

위의 예제에서는 POST 요청 데이터를 받아와 `MyFormSet` 인스턴스를 생성하고 `is_valid()` 메소드를 호출하여 유효성 검사를 수행하고 있습니다.

## 결론

Django REST framework에서 폼과 폼셋을 사용하면 API를 개발할 때 데이터의 입력과 유효성을 효과적으로 처리할 수 있습니다. 이 포스트에서는 Django REST framework에서 폼과 폼셋을 어떻게 사용하는지에 대해 알아보았습니다. 추가적인 정보는 Django REST framework 공식 문서를 참조하시기 바랍니다.

**참고 자료:**
- [Django REST framework 공식 문서](https://www.django-rest-framework.org/)