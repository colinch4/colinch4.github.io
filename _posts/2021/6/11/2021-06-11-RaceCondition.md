---
layout: post
title: "[programing] race condition (경쟁상태)"
description: " "
date: 2021-06-11
tags: [개발]
comments: true
share: true
---

## race condition (경쟁상태)

* 책 `리눅스 시스템 프로그래밍`을 참조하였습니다. 

**race condition**이란 `공유 리소스(=Critical Section)에 동기화되지 않은 둘 이상의 스레드가 접근하여 프로그램의 오동작을 유발하는 상황`을 말함.

Q) 그리고 애초에 race condtion이 일어나는 이유는?

A) 코드가 not atomic 하므로, 즉 non-thread-safe 하기 때문에 일어난다. 