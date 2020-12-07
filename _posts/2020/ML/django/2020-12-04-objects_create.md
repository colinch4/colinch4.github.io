---
layout: post
title: "[django] objects.create"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# .objects.create()



**application package**의 `models.py` 에 다음과 같은 모델이 정의 되어 있다고 가정하자.

```python
class Gift_card(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()
    serial_number = models.IntegerField()

    def __str__(self):
        return self.name
```

* `Gift_card` : 상품권 모델이다.
* `name`, `value`, `serail_number` : 3개의 속성을 가진다.
* `return self.name`  : instance(튜플)이 `name`으로  보이게끔 만들어준다.



물론,  **admin 페이지** 에서 instance가 생성 가능하다.

그러나  `views.py `  에서 어떤 행위를 할때 다른 **table**에서 data를 받아서 개체 생성이 가끔씩 필요한 순간이 있다.



방법은 간단하다.

개체가 만들어지는 `views.py` 파일에서 다음과 같이 `.objects.create()` 를 사용하면 된다.

```python
from application.models import Gift_card

Gift_card.objects.create(name='5만원', value=50000, serial_number=10001005)
```









  

