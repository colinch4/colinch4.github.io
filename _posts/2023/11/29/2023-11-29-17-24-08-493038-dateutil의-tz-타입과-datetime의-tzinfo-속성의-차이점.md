---
layout: post
title: "[python] dateutil의 tz 타입과 datetime의 tzinfo 속성의 차이점"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

파이썬으로 작업을 할 때 시간대(timezone)와 관련된 작업은 중요한 부분입니다. `dateutil` 패키지는 시간대를 다루는데 매우 편리한 도구입니다. 그러나 `dateutil`의 `tz` 타입과 `datetime`의 `tzinfo` 속성은 약간의 차이가 있습니다. 이 블로그 포스트에서는 이 둘의 차이점을 알아보겠습니다.

## `dateutil`의 `tz` 타입
`dateutil` 패키지에서 `tz` 타입은 시간대 정보를 나타내는 객체입니다. 일반적으로 `dateutil`의 `tz` 타입은 `dateutil.tz` 모듈에서 가져올 수 있습니다. 이 모듈은 다양한 시간대를 지원하며, `tz` 타입은 해당 시간대에 대한 세부 정보를 가지고 있습니다.

`tz` 타입은 `tzname`이라는 메소드를 제공합니다. 이 메소드를 호출하면 해당 시간대의 이름을 가져올 수 있습니다. 또한 `tz` 타입은 `utcoffset`이라는 속성을 가지고 있으며, 이 속성을 통해 해당 시간대의 UTC 오프셋을 얻을 수 있습니다.

```python
from dateutil import tz

# 서울 시간대 객체 생성
seoul_tz = tz.gettz('Asia/Seoul')
print(seoul_tz.tzname())         # 'KST'
print(seoul_tz.utcoffset(None))  # 9 hours

# 뉴욕 시간대 객체 생성
new_york_tz = tz.gettz('America/New_York')
print(new_york_tz.tzname())         # 'EST'
print(new_york_tz.utcoffset(None))  # -5 hours
```

## `datetime`의 `tzinfo` 속성
파이썬의 기본 `datetime` 모듈에는 `tzinfo` 속성이 있습니다. 이 속성을 사용하면 `datetime` 객체에 시간대 정보를 추가할 수 있습니다.

하지만, `datetime` 모듈은 시간대 정보를 자동으로 처리하지 않습니다. 대신, `tzinfo` 속성의 값을 사용자가 직접 설정해야 합니다. 이러한 방식은 사용자가 시간대 정보에 대한 세부 정보를 제공하는 데 유용합니다.

```python
from datetime import datetime, timedelta, timezone

# 서울 시간대의 UTC 오프셋 계산
seoul_offset = timedelta(hours=9)

# 현재 시간에 시간대 정보 추가
now = datetime.now(timezone(seoul_offset))
print(now)
```

## 결론
`dateutil`의 `tz` 타입과 `datetime`의 `tzinfo` 속성은 모두 시간대 정보를 처리하는 도구입니다. 그러나 `dateutil`의 `tz` 타입은 시간대 정보에 대한 세부 정보를 제공하는 반면, `datetime`의 `tzinfo` 속성은 사용자가 직접 시간대 정보를 설정해야 합니다.

따라서, 시간대 정보를 다룰 때는 `dateutil` 패키지의 `tz` 타입을 사용하는 것이 편리하고 신뢰할 수 있습니다.

## 참고 자료
- dateutil: https://dateutil.readthedocs.io/
- Python datetime: https://docs.python.org/3/library/datetime.html