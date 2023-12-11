---
layout: post
title: "[design] 스크린 해상도 정의하기"
description: " "
date: 2021-09-09
tags: [uxui]
comments: true
share: true
---


## 스크린 해상도 정의하기

디자인시 스크린 사이즈에 대한 규격과 규칙을 정의한다. 

이는 디자인할 때 그리드 시스템 컬럼 갯수나 거터 사이즈 등을 설계하는 단초가 되며, 특히 각 디바이스별로 레이아웃이 달라질 경우 Break Point를 설정하는데 중요한 역할을 한다. 디자인하기 전 프로젝트 초기에 정의해두는것이 좋다. 

나의 경우 모바일 (IOS, Android)은 고려할 필요가 없어서 반응형 웹 구현을 고려해 정의했다.

* Desktop: 1440 x 1024
* Tablet: 768 x 1024
* Mobile: 320 x 1024

 [Statcounter](https://gs.statcounter.com/screen-resolution-stats/desktop/south-korea)의 통계를 검토해보면 1920 x 1280이 45.67% 이상 사용되고 있으며 나머지 해상도는 얼추 비슷해보인다. (2019년 10월 기준)

 하지만, 웹의 경우 처음부터 1920 기준으로 작업하면 스케치나 포토샵에서 보는것과 실제 퍼블리싱된 결과물 사이에 이질감이 들 수 있다. 브라우저의 타이틀바, 주소 및 검색바, 윈도우의 시작 표시줄, 스크롤바 등의 높이와 넓이때문에 실제 viewport는 스크린의 해상도보다 작아지게 된다. 특히 1920 이하 모니터를 사용하는 유저는 박스가 가득차 답답한 디자인을 경험하거나, 하단 정보가 잘리는 경험을 할 수 있다. 이러한 오류를 줄이기 위해 기존 디자인(3년 전)은 1280x800 사이즈를 최소 사이즈로 작업했다.

 위에 정의한 1440 x 1024 해상도의 기준은 Sketch 툴에서 영향을 받았다. (XD는 아래 내용과 별개의 스크린 해상도를 제공한다)

![Sketch에서 설정할 수 있는 해상도 기준](https://github.com/onlyeon/TIL/blob/master/%40images/screen-resolution.png) 

 Sketch는 기본적으로 반응형 웹의 데스크탑 사이즈를 1440 x 1024와 1024 x 1024로 제공한다. [Worldwid](https://gs.statcounter.com/screen-resolution-stats/desktop/worldwide) 기준 해상도 1위가 1366x768(22.98%, 2019년 10월 기준), 2위가 1920 x 1090(21.48%, 2019년 10월 기준) 인것을 고려하면 그 중간의 적절한 스크린 해상도를 정의한걸로 보여진다.

 처음부터 큰 해상도로 디자인하고 나중에 줄이는 것 보다, 최소 사이즈를 기준으로 보기 좋은 비율의 디자인을 한 후 더 큰 해상도는 좌우로 사이즈를 늘려 확인해보는것이 더욱 안전하다.

📖 **참고 자료**

* [KOREA HTML | 웹 브라우저, 운영체제 이용률](https://www.koreahtml5.kr/front/stats/browser/browserUseStats.do)
* [반응형 웹 디자인 기본 사항](https://developers.google.com/web/fundamentals/design-and-ux/responsive?hl=ko)