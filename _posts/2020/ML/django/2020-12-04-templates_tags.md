---
layout: post
title: "[django] template tags"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# Built-in template tags and filters

> `django` 에서 유용한 template tags들을 간단하게 정리한다.



## {%csrf_token%}

* CSRF : Cross-site request forgery 라는 웹사이트 취약점 공격 중 하나를 뜻하고 이에 대응하기 위해

  위에 template tag가 사용된다.

* 주로 `<form>` tag 안에서 사용된다.



## for

* python `for` 문과 마지막에 `{% endfor %}`을 작성하는것을 제외하고 거의 비슷하게 작동한다.

* (예제1)

  ```html
  <ul>
  {% for athlete in athlete_list %}
      <li>{{ athlete.name }}</li>
  {% endfor %}
  </ul>
  ```

* (예제2)

  ```html
  {% for x, y in points %}  <!-- (x,y) in points-->
      There is a point at {{ x }},{{ y }}
  {% endfor %}
  ```

* (예제3)

  ```html
  {% for key, value in data.items %}  <!--data is dictionary-->
      {{ key }}: {{ value }}
  {% endfor %}
  ```

* for문과  관련된 variable

  * {{forloop.counter}} : 1부터 시작해 iteration 횟수를 세준다.
  * {{forloop.counter0}} : 0부터 시작해 iteration 횟수를 세준다. 
  * {{forloop.revcounter}} : iteration횟수를 역으로 시작해 마지막이 1이 되게 세준다.
  * {{forloop.revcounter0}} : iteration횟수를 역으로 시작해 마지막이 0이 되게 세준다.
  * 

