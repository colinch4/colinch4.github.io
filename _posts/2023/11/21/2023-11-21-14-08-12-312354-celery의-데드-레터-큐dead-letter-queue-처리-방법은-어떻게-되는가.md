---
layout: post
title: "[python] Celery의 데드 레터 큐(Dead Letter Queue) 처리 방법은 어떻게 되는가?"
description: " "
date: 2023-11-21
tags: [python]
comments: true
share: true
---

Celery는 분산된 작업 큐 시스템을 구축하기 위해 널리 사용되는 Python 라이브러리입니다. 데드 레터 큐는 Celery에서 발생하는 작업 실패를 처리하는 방법 중 하나입니다. 데드 레터 큐는 작업이 실패한 후 작업을 다시 처리하거나 작업에 대한 추가 조치를 취할 수 있는 기회를 제공합니다.

## 데드 레터 큐 설정하기

먼저, Celery 설정 파일에서 데드 레터 큐를 활성화해야 합니다. 설정 파일(예: `celeryconfig.py`)에 다음과 같은 옵션을 추가합니다:

```python
task_publish_retry = True
task_publish_retry_policy = {
    "max_retries": 3,
    "interval_start": 0,
    "interval_step": 0.2,
    "interval_max": 0.2
}
task_publish_retry_policy_LCELERY_QUEUES = {
    "default": {"dead_letter_exchange": "dead_letter_exchange"}
}
```

위의 설정은 일반적인 데드 레터 큐 기능을 활성화하며, 작업이 실패한 경우 최대 3번 재시도하며, 재시도 간격은 0.2초로 설정됩니다. `task_publish_retry_policy_LCELERY_QUEUES`는 큐에 실패한 작업이 속하는 대기열을 지정하는 데 사용됩니다. 이 예제에서는 "default" 큐를 사용하고 있습니다.

## 데드 레터 큐 처리하기

데드 레터 큐에서 실패한 작업을 처리하는 방법은 여러 가지가 있습니다. 이 예제에서는 작업을 재시도하는 방법을 설명하겠습니다.

```python
from celery import Celery
from kombu import Exchange, Queue

app = Celery()
dead_letter_exchange = Exchange("dead_letter_exchange", type="direct")

@app.task
def my_task():
    # 작업 수행
    try:
        # 작업 내용
        pass
    except Exception as e:
        # 작업 실패 처리
        my_task.retry(countdown=10, exchange=dead_letter_exchange, routing_key="default")
```

위의 코드에서 `my_task`는 Celery 작업으로 정의된 함수입니다. 작업 내용을 처리하는 동안 예외가 발생한 경우, `retry()` 메서드를 사용하여 작업을 재시도합니다. `countdown` 매개변수는 재시도가 실행되기 전에 대기해야 할 시간을 지정합니다. `exchange`와 `routing_key` 매개변수는 데드 레터 큐에 작업을 전달하기 위한 것입니다.

## 결론

Celery의 데드 레터 큐를 사용하면 작업 실패에 유연하게 대응할 수 있습니다. 작업을 재시도하거나 추가 조치를 취하여 문제를 해결할 수 있습니다. 설정 파일과 작업 함수에서 데드 레터 큐를 설정하고 처리하는 방법을 살펴보았습니다. 추가로 필요한 경우 Celery 공식 문서를 참조하여 더 자세한 내용을 확인할 수 있습니다.

참조:
- [Celery 공식 문서](https://docs.celeryproject.org/en/stable/getting-started/index.html)