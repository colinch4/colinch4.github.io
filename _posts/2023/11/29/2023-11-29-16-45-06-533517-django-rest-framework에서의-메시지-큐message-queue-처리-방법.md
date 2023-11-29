---
layout: post
title: "[python] Django REST framework에서의 메시지 큐(Message Queue) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 강력한 웹 프레임워크이며, 메시지 큐(Message Queue)를 통해 비동기 작업을 처리할 수 있습니다. 메시지 큐는 웹 애플리케이션의 성능과 확장성을 향상시키는 데 도움이 됩니다. 이 글에서는 Django REST framework에서 메시지 큐를 처리하는 방법에 대해 알아보겠습니다.

## 1. Celery 설치

먼저, Django 프로젝트에 Celery를 설치해야 합니다. Celery는 파이썬에서 비동기 작업을 처리하기 위한 일반적인 도구입니다. 아래의 명령을 사용하여 Celery를 설치합니다.

```shell
pip install celery
```

## 2. Django 설정 업데이트

Celery를 사용하려면 Django 설정 파일을 업데이트해야 합니다. `settings.py` 파일에 아래의 설정을 추가합니다.

```python
# settings.py

REDIS_HOST = 'localhost'  # Redis 호스트
REDIS_PORT = 6379  # Redis 포트

BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'  # Celery Broker URL
CELERY_RESULT_BACKEND = BROKER_URL  # Celery 결과 백엔드 URL

# Celery 설정
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'
```

## 3. 비동기 작업 정의

이제 비동기 작업을 정의할 수 있습니다. 예를 들어, 사용자에게 이메일을 보내는 작업을 비동기로 처리하고 싶다면, `tasks.py` 파일을 생성하고 아래의 코드를 추가합니다.

```python
# tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
```

## 4. 비동기 작업 실행

비동기 작업을 실행하려면 `views.py` 파일(또는 해당 작업을 수행하는 파일)에서 `send_email_task` 함수를 호출합니다.

```python
# views.py

from .tasks import send_email_task

def send_email(request):
    # 이메일 보내기 비동기 작업 실행
    send_email_task.delay('Subject', 'Message', 'from@example.com', ['to@example.com'])
    return HttpResponse("Email sent asynchronously!")
```

위의 예제에서는 `send_email_task.delay()`를 사용하여 비동기 작업을 실행합니다. `delay()` 함수를 호출하면 작업이 큐에 추가되고 Celery 워커가 작업을 처리합니다.

## 5. Celery 실행

마지막으로, Celery 워커를 실행해야 합니다. 아래의 명령을 사용하여 Celery를 실행합니다.

```shell
celery -A project_name worker --loglevel=info
```

위의 `project_name`은 Django 프로젝트의 이름으로 바꿔야 합니다. Celery 워커를 실행하면 큐에 있는 작업이 처리됩니다.

## 참고 자료

- [Django Documentation](https://docs.djangoproject.com/)
- [Celery Documentation](https://docs.celeryproject.org/)