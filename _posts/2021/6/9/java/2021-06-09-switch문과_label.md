---
layout: post
title: "[java] Switch문과 Label"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

## Switch문과 Label

### switch

* 등가비교(==) 밖에 하지 못한다.
  - 문자상수
  - 정수상수
  - 문자열상수

### Label

* label 써주어서 첫번째 for문을 빠져나갔다

  * ```java
    Hyun : for(.......){
        for(.......){
            break Hyun;
        }
    }
    // label 이름은 Hyun
    ```



### \*헷갈리는 부분*

* 0.0 < = Math.random() < 1.0

  0<= (int)(Math.random())<1 로 만들어서 곱하고 더하여 원하는 범위의 값을 구한다.

  