---
layout: post
title: "[파이썬] 파이썬으로 간단하게 웹서버 띄우기"
description: " "
date: 2021-06-17
tags: [python]
comments: true
share: true
---

## 파이썬으로 간단하게 웹서버 띄우기

d3-book에서 소스코드를 받아서 테스트를 하려고 하는데, 로컬환경에서는 파일 참조가 되지 않아서 제대로 동작하지 않았다. 웹서버를 통해서 테스트를 해야 하는데, 따로 서버를 셋팅하기가 번거로웠다. 이럴 때 손쉽게 바로 서버를 띄울 수 있는 파이썬 모듈이 존재한다. 어렴풋이 기억을 더듬어 실행을 했는데, 잘 동작하지 않아서, 이렇게 글로 남겨둔다.

## SimpleHTTPServer로 서버 띄우기

구글에서 검색하니, [공식 페이지](https://docs.python.org/2/library/simplehttpserver.html)로 포워딩이 되었다. 경고 문구가 있는데도 아무 생각 없이 `python -m SimpleHTTPServer 8000`라고 따라 쳤더니 동작하지 않았다. 파이썬 2용이었던 것이다.

## 파이썬3는 http.server

파이썬3에서는 모듈의 이름이 바뀌었다. 좀더 읽기 쉬워진 것 같다. 다음과 같이 쓰면 실행한 폴더를 루트로 한 웹서버가 돌아간다. 테스트용으로만 쓰자. 이걸 프로덕션 레벨로 쓰는 사람은 없겠지만, 걱정되는 사람이 있어서 적어둔다.

```bash
python -m http.server 8000
```

<vue-disqus/>
