---
layout: post
title: "[server] 서버 시간 조정하기"
description: " "
date: 2021-06-17
tags: [web]
comments: true
share: true
---

## 서버 시간 조정하기

보통 서버시간은 고칠 일이 거의 없는데, 오늘 작업 중 7-8분 정도 시간이 어긋나 있는 것을 확인했다.
시간 입력은 직접 입력하면, 몇 초라도 오차가 발생하기 마련이고, 시간정보를 제공해주는 서버와 동기화를 해주는 것이 가장 일반적인 해결법이다.
여기까지가 아는 내용이고, 하는 방법은 늘 까먹기 때문에, 오늘 한 작업을 메모로 남겨둔다.

```bash
rdate -s time.bora.net
```

로 설정하면 끝. 혹시 rdate 가 없다고 하면, 다음과 같이 설치하면 된다. 몇 초 안 걸린다.

```bash
sudo apt-get install rdate
```

## 참고 문헌

* [리눅스(Linux) 계열 운영체제에서 시간 동기화하기](http://jhrun.tistory.com/158)
