---
layout: post
title: "[python] Django와 AWS(Amazon Web Services) 연동 방법은 어떻게 되는가?"
description: " "
date: 2023-11-22
tags: [python]
comments: true
share: true
---

Django는 강력한 웹 프레임워크로 AWS와 연동하여 안정적이고 확장 가능한 웹 애플리케이션을 개발할 수 있습니다. 이번 블로그 포스트에서는 Django와 AWS 연동하는 방법을 소개하겠습니다.

## 1. AWS 계정 생성 및 Django 프로젝트 설정

먼저 AWS 계정을 생성하고 Django 프로젝트를 설정해야 합니다.

### 1-1. AWS 계정 생성

AWS 웹사이트에 가입하여 계정을 생성합니다. 정식 인증을 마치면 AWS 관리 콘솔에 로그인할 수 있습니다.

### 1-2. Django 프로젝트 설정

터미널에서 Django 프로젝트를 생성합니다.

```python
$ django-admin startproject myproject
```

그리고 AWS 연동에 필요한 패키지를 설치합니다.

```python
$ pip install boto3 django-storages
```

## 2. S3(Simple Storage Service) 버킷 생성 및 설정

Django와 AWS를 연동하기 위해 S3 버킷을 생성하고 설정해야 합니다.

### 2-1. S3 버킷 생성

AWS 관리 콘솔에서 S3 서비스로 이동하여 새로운 버킷을 생성합니다.

### 2-2. S3 버킷 설정

버킷 권한 설정에서 "모든 퍼블릭 액세스 차단"을 선택합니다. 이를 통해 외부에서 접근할 수 없도록 보안을 강화할 수 있습니다.

## 3. Django 설정 변경

Django 프로젝트의 설정 파일(`settings.py`)을 변경하여 AWS와 연동합니다.

```python
# settings.py

INSTALLED_APPS = (
    ...
    'storages',
)

AWS_ACCESS_KEY_ID = 'your_access_key'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
AWS_S3_REGION_NAME = 'your_bucket_region'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

## 4. 파일 업로드 테스트

이제 Django 애플리케이션에서 파일을 업로드하고 S3 버킷에 저장하는 것을 테스트해봅니다.

```python
# views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')
```

```html
<!-- upload.html -->
{% raw %}
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="file">
    <button type="submit">Upload</button>
</form>
{% endraw %}
```

## 마무리

이제 Django와 AWS를 연동하는 방법을 알게 되었습니다. Django 애플리케이션에서 AWS S3를 사용하여 파일을 업로드하고 저장하는 것은 매우 간단하며, 안정적이고 확장 가능한 웹 애플리케이션을 개발하는 데 도움이 됩니다.

더 많은 AWS 기능을 활용하려면 AWS 공식 문서를 참조하시기 바랍니다. [AWS 문서 링크](https://docs.aws.amazon.com/index.html)

Happy coding!