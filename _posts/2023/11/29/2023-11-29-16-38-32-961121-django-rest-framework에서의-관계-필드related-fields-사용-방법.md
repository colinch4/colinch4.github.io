---
layout: post
title: "[python] Django REST framework에서의 관계 필드(Related fields) 사용 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework은 Django 프레임워크를 통해 웹 API를 개발하는데 도움을 주는 강력한 도구입니다. 관계 필드(Related fields)는 Django 모델 간의 관계를 나타내는 필드로, Django REST framework에서 이러한 관계 필드를 사용하는 방법을 알아보겠습니다.

### ForeignKey 관계 필드
ForeignKey 관계 필드는 다른 모델과의 일대다(One-to-Many) 관계를 나타내는 필드입니다. 예를 들어, '글' 모델과 '작성자' 모델 간의 관계를 나타내는 경우를 생각해보겠습니다. 다음은 해당 관계 필드를 사용하는 방법입니다:

```python
from django.db import models

class 작성자(models.Model):
    이름 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.이름
    
class 글(models.Model):
    제목 = models.CharField(max_length=100)
    작성자 = models.ForeignKey(작성자, related_name='글', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.제목
```

위의 코드에서는 `ForeignKey` 필드를 사용하여 '글' 모델과 '작성자' 모델 간의 관계를 나타내고 있습니다. `related_name` 매개변수는 역방향 참조를 사용하여 '작성자' 모델에서 해당 작성자가 작성한 모든 글을 찾기 위해 사용됩니다. `on_delete` 매개변수는 참조되는 객체가 삭제되었을 때의 동작을 지정합니다.

### ManyToMany 관계 필드
ManyToMany 관계 필드는 다른 모델과의 다대다(Many-to-Many) 관계를 나타내는 필드입니다. 예를 들어, '학생' 모델과 '과목' 모델 간의 관계를 나타내는 경우를 생각해보겠습니다. 다음은 해당 관계 필드를 사용하는 방법입니다:

```python
from django.db import models

class 과목(models.Model):
    이름 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.이름
    
class 학생(models.Model):
    이름 = models.CharField(max_length=100)
    수강과목 = models.ManyToManyField(과목, related_name='수강학생')
    
    def __str__(self):
        return self.이름
```

위의 코드에서는 `ManyToManyField` 필드를 사용하여 '학생' 모델과 '과목' 모델 간의 관계를 나타내고 있습니다. `related_name` 매개변수는 역방향 참조를 사용하여 '과목' 모델에서 해당 과목을 수강하는 모든 학생을 찾기 위해 사용됩니다.

Django REST framework에서 관계 필드를 사용하는 방법은 이렇게 간단합니다. 관계를 정의하는 모델에 해당 필드를 추가하고, 직렬화를 위해 `serializers` 클래스에서 적절한 필드를 선언해주면 됩니다.

### 참고 자료
- Django 공식 문서: https://docs.djangoproject.com/
- Django REST framework 공식 문서: https://www.django-rest-framework.org/