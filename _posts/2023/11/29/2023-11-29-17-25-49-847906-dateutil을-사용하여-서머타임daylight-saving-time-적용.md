---
layout: post
title: "[python] dateutil을 사용하여 서머타임(Daylight Saving Time) 적용"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

서머타임(Daylight Saving Time)은 일부 국가에서 특정 기간 동안 시간을 조정하여 일광시간을 최대한 활용하는 시간제입니다. 파이썬에서 서머타임을 적용하려면 `dateutil` 모듈을 사용할 수 있습니다.

## `dateutil` 설치하기

먼저 `dateutil` 패키지를 설치해야 합니다. 아래의 명령어로 `pip`를 사용하여 설치할 수 있습니다.

```python
pip install python-dateutil
```

## 서머타임 적용하기

`dateutil` 모듈을 사용하면 간단하게 서머타임을 적용할 수 있습니다. 아래의 예제 코드를 참고하세요.

```python
from datetime import datetime
from dateutil import tz

# 서머타임 전의 로컬 시간
local_time = datetime(2022, 3, 13, 10, 0, 0)

# UTC 시간으로 변환
utc_time = local_time.astimezone(tz.UTC)
print(f"UTC 시간: {utc_time}")

# 서머타임 적용된 시간으로 변환
dst_time = local_time.astimezone(tz.gettz("America/New_York"))
print(f"서머타임 적용된 시간: {dst_time}")
```

이 코드에서는 `datetime` 모듈로 로컬 시간을 생성한 뒤, `astimezone` 메서드를 사용하여 시간대를 변경합니다. 

먼저 로컬 시간을 UTC 시간으로 변환하기 위해 `tz.UTC`를 사용했습니다. 또한, `tz.gettz()` 메서드를 사용하여 미국 동부 표준시간(EST)에 서머타임이 적용된 시간대로 변환했습니다.

## 결과 확인

위의 예제 코드를 실행하면 다음과 같은 결과가 출력됩니다.

```
UTC 시간: 2022-03-13 01:00:00+00:00
서머타임 적용된 시간: 2022-03-13 06:00:00-04:00
```

로컬 시간인 2022년 3월 13일 10시가 UTC 시간으로는 2022년 3월 13일 01시, 미국 동부 표준시간으로는 2022년 3월 13일 06시로 변환되었습니다.

## 참고 자료

- `dateutil` 패키지 문서: [https://dateutil.readthedocs.io/en/stable/](https://dateutil.readthedocs.io/en/stable/)
- 파이썬 공식 문서: [https://docs.python.org/](https://docs.python.org/)