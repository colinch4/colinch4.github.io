---
layout: post
title: "[django] DateField"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# DateField

 `DateField`는  `django` framework 의 `datafield ` 중 하나이다. 

 예를 들어, **django application package**의 `models.py` 에서 다음과 같은 모델이 있다고 하자.

 ```python
 class Histories(models.Model):
     date = models.DateField(auto_now=True)
 ```

 기본적으로 우리는 한국에 살고 있으므로 **project 폴더**의 `settings.py` 에서 `TIME_ZONE` 변수를 다음과 같이 설정 했다고 하자.

 ```python
 TIME_ZONE = 'Asia/Seoul'
 ```

그러나 이것은 `template` 에서 한국 시간이긴 하지만 영어로 표현되고 **달/일/년** 순서로 표기된다. 이 말은 즉슨, 다음의 코드를 html에 작성했을때, 밑의 사진과 같이 주문일자가 표기된다.

```html
<td >{{history.date}}</td>
```

![datefield](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/datefield.png?raw=true)

위의 사진에서는 **2020-08-24** 와 같은 표기법을 원하는데 구글링을 해보면 주로 `forms.py` 를 이용하는 방법이 나오는데 예제가 많이 없는만큼 따라하기 쉽지 않았다.

따라서 가장 간단한 방법을 제시하면 `template` 파일에서 html에서 data를 수정하는 방법이다.

다음과 같이 수정한다.

```html
<td >{{history.date|date:"Y-m-d"}}</td>
```

* `| `  는 왼쪽의 data를 오른쪽으로 넘겨 준다는 의미이다.
* `"Y-m-d"`  는 년-월-일 로 표기 한다는 의미이다.



마지막으로 결과는 다음과 같다.

![datefield1](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/datefield1.png?raw=true)