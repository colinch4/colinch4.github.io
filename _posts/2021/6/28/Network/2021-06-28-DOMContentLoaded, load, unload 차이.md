---
layout: post
title: "[네트워크] DOMContentLoaded, load, unload"
description: " "
date: 2021-06-28
tags: [네트워크]
comments: true
share: true
---

`아카이빙: https://mygumi.tistory.com/281`

## DOMContentLoaded, load, unload

- DOMContentLoaded - HTML 이 모두 로드되고, DOM 트리가 완성되었지만, 외부 리소스(img etc) 가 아직 로드되어지지 않았을 때

  - DOMContentLoaded - DOM 이 준비 상태이기 때문에, DOM 노드를 제어할 수 있다.

- load - 브라우저에 모든 리소스(img, style, script, etc) 가 로드되었을 때

  - load - 모든 리소스가 로드된 시점이기에, image 사이즈와 같은 것들을 얻을 수 있다.

- beforeunload / unload - 페이지를 떠날 때

  - beforeunload / unload - 변화에 따른 저장 여부 및 페이지 이탈 여부를 확인할 수 있다.

> 대부분 load 보다 ready 또는 DOMContentLoaded 를 사용하는 이유는 무엇인가?

load 는 모든 리소스를 로드해야하기 때문에 DOMContentLoaded 가 먼저 발생된 후 발생한다.

대부분 모든 리소스를 기다릴 필요가 없는 경우가 많기에, 단순히 빠른 실행을 위함이다.

> 관련 이벤트를 하단에 작성하는 이유는 무엇인가?

대부분 스크립트를 </body> 위에 작성하거나, 하단에 작성하는 경우가 많다.

HTML 문서를 파싱하는 과정에서 script 태그를 만난다면, DOM 구축 작업이 중단된다.

중단된 후, script 작업을 실행된 후에 다시 작업이 재실행되는 것이다.

DOMContentLoaded 이벤트가 발생하는 시점이 script 작업 완료 시간만큼 지연된다는 의미이다.

또한 상황에 따라, DOM 구축이 되지 않은 상태에서 DOM 을 가져오기 때문에, 정상적인 동작이 이루어지지 않는다.
