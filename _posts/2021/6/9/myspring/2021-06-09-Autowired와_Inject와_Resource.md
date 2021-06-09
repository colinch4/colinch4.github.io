---
layout: post
title: "[spring] Autowired vs Inject vs Resource"
description: " "
date: 2021-06-09
tags: [spring]
comments: true
share: true
---

# @Autowired vs @Inject vs @Resource

> 공통점은 의존 주입

### 차이

* @Autowired
  * 스프링 프레임워크안에서 지원
  * 스프링을 다른 프레임을 바꾸면 못사용 -> 바꾸고 싶을 땐 inject사용해야 됨
  * 즉 프로젝트가 다른 바꿀 필요 없는 프로젝트 일때
  * bean type(class type)으로 찾아감 -> 같은 class type이면 이름으로 찾음
  * Search Bean by Type

* @Inject
  * 자바에서 지원(JSR)
  * @Autowired 똑같음
  * Search Bean by Type

* @Resource
  * 자바에서 지원(JSR)
  * 무조건 걸어준 이름으로 찾음 
  * Search Bean by Name

