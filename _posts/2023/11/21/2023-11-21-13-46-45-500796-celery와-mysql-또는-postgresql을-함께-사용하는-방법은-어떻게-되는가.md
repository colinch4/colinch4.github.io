---
layout: post
title: "[python] Celery와 MySQL 또는 PostgreSQL을 함께 사용하는 방법은 어떻게 되는가?"
description: " "
date: 2023-11-21
tags: [python]
comments: true
share: true
---

Celery는 Python으로 작성된 분산 작업 큐 시스템입니다. 이를 사용하여 백그라운드에서 비동기 작업을 처리할 수 있습니다. MySQL 또는 PostgreSQL과 함께 Celery를 사용하려면 아래의 단계를 따라야 합니다.

## 1. Celery 설치

Celery를 사용하려면 우선 Celery 패키지를 설치해야 합니다. 아래의 명령을 사용하여 설치할 수 있습니다.

```python
pip install celery
```

## 2. MySQL 또는 PostgreSQL 설치 및 설정

Celery와 함께 MySQL 또는 PostgreSQL을 사용하기 위해서는 해당 데이터베이스를 설치하고 설정해야 합니다. 각 데이터베이스의 공식 문서를 참조하여 설치 및 설정을 진행하세요.

## 3. Celery 설정 파일 작성

Celery 설정 파일을 작성해야 합니다. 이 설정 파일에서는 Celery 애플리케이션의 설정 및 데이터베이스 연결 정보를 설정합니다. 아래는 Celery 설정 파일의 예시입니다.

```python
# celery.py

from celery import Celery

app = Celery('myapp', broker='pyamqp://guest@localhost//')

app.conf.update(
    result_backend='db+postgresql://user:password@localhost/mydatabase',
    timezone='Asia/Seoul',
    enable_utc=True,
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

위의 설정 파일에서 `broker`는 Celery에서 메시지 브로커를 사용하는데, 여기서는 RabbitMQ를 사용하고 있습니다. 필요에 따라 다른 브로커를 사용할 수도 있습니다. `result_backend`는 Celery 작업 결과를 저장할 데이터베이스의 연결 정보를 설정합니다.

## 4. Celery worker 실행

Celery를 실행하기 위해 Celery worker를 실행해야 합니다. 아래의 명령을 사용하여 Celery worker를 실행할 수 있습니다.

```python
celery -A myapp worker --loglevel=info
```

위의 명령에서 `myapp`은 Celery 설정 파일의 모듈 경로를 지정하고, `--loglevel`은 Celery 작업의 로깅 레벨을 설정합니다.

## 5. Celery task 작성 및 실행

Celery task를 작성하고 실행하는 예시 코드입니다.

```python
# tasks.py

from myapp.celery import app

@app.task
def add(x, y):
    return x + y
```

위의 예시 코드에서 `@app.task` 데코레이터를 사용하여 Celery task로 등록할 수 있습니다. 이후에 작성한 task는 Celery worker가 처리할 수 있습니다. task를 실행하기 위해서는 아래와 같은 방법을 사용할 수 있습니다.

```python
from myapp.tasks import add

add.delay(4, 5)
```

위의 코드에서 `delay()` 메서드를 사용하여 비동기적으로 task를 실행합니다. task의 실행 결과를 얻기 위해서는 `.get()` 메서드를 사용할 수도 있습니다.

이제 Celery와 MySQL 또는 PostgreSQL을 함께 사용하는 방법에 대한 기본적인 내용을 알아보았습니다. 이를 기반으로 원하는 비동기 작업을 처리할 수 있습니다. 추가적인 고급 설정이나 기능에 대해서는 Celery 공식 문서를 참조하시기 바랍니다.

## 참고 자료
- [Celery 공식 문서](https://docs.celeryproject.org/en/stable/)
- [MySQL 공식 문서](https://dev.mysql.com/doc/)
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/)