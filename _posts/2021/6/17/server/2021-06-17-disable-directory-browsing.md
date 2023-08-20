---
layout: post
title: "[server] 웹서버에서 디렉토리 보이는 것 감추기"
description: " "
date: 2021-06-17
tags: [server]
comments: true
share: true
---

## 웹서버에서 디렉토리 보이는 것 감추기

apache 설정파일에서 Indexes 옵션을 지우고, apache를 다시 시작한다.

```bash
sudo service apache2 restart
```

* 출처: [(stackoverflow) How do I disable directory browsing?](https://stackoverflow.com/questions/2530372/how-do-i-disable-directory-browsing)
