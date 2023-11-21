---
layout: post
title: "[python] Celery worker와 Celery beat의 차이점은 무엇인가?"
description: " "
date: 2023-11-21
tags: [python]
comments: true
share: true
---

Celery는 분산 작업 큐 시스템으로, 비동기 작업을 처리하는 데 사용됩니다. Celery Worker와 Celery Beat은 Celery 시스템에서 각각 다른 역할을 수행합니다. 

### Celery Worker
Celery Worker는 Celery 시스템에서 비동기 작업을 실행하는 주체입니다. 이 worker는 큐에 추가된 작업들을 가져와 실행하고, 작업의 결과를 반환합니다. Worker는 일반적으로 웹 어플리케이션 서버와 분리되어 독립적으로 동작합니다.

Celery Worker는 비동기적으로 실행되는 작업들을 처리하며, 필요한 작업을 여러 개의 쓰레드나 프로세스로 나누어 병렬로 실행할 수도 있습니다. 이를 통해 작업 처리 성능을 향상시킬 수 있습니다.

### Celery Beat
Celery Beat는 Celery 시스템에서 주기적으로 실행되어야 하는 작업들을 스케줄링합니다. 일반적으로 주기적으로 실행되어야 하는 작업은 큐에 추가되지 않고, Celery Beat에 의해 직접 스케줄되어 Worker로 전달됩니다. 예를 들어, 매 시간마다 데이터베이스를 백업하는 작업은 Celery Beat에 의해 주기적으로 스케줄되어 Worker로 전달되어 실행됩니다.

Celery Beat는 스케줄링을 위해 crontab 형식의 표현식을 사용합니다. 이를 사용하여 작업을 초, 분, 시간, 날짜 등에 맞게 스케줄링할 수 있습니다.

### 결론
Celery Worker와 Celery Beat은 Celery 시스템에서 각각 다른 역할을 수행합니다. Worker는 비동기 작업의 실행을 담당하고, Beat는 주기적으로 실행되어야 하는 작업을 스케줄링합니다. 이 두 가지 컴포넌트를 함께 사용하여 Celery를 활용하면 비동기 작업 처리와 주기적 작업 스케줄링을 효과적으로 관리할 수 있습니다.

**참고 자료:**
- [Celery Documentation](https://docs.celeryproject.org/en/stable/)
- [Celery Architecture](https://en.wikipedia.org/wiki/Celery_(software)#:~:text=Celery%20is%20a%20distributed%20task,default%20message%20broker%20for%20Celery.)