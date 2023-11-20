---
layout: post
title: "[DB] Scale up 과 Scale out"
description: " "
date: 2021-06-28
tags: [SQL]
comments: true
share: true
---

### Scale up

#### 정의

접속된 서버의 대수를 늘려 처리 능력을 향상시키는 것으로 수평 스케일이라고 불리기도 한다.

서버의 가상화 기술을 사용하여 하나의 케이스 내에서 가상적으로 복수 서버를 구축해 스케일 아웃과 동등한 효과를 제공한다.

#### 적용

개개의 처리는 단순하지만 다수의 처리를 동시 병행적으로 실시하지 않으면 안 되는 경우에 적합하다.

웹서버, 검색엔진 데이터 분석처리, 메일 서버, 게시판 등에 적용될 수 있다.

### Scale out

#### 정의

프로세서 그 자체를 고성능 모델로 옮겨서 서버 그 자체를 증강하여 처리 능력을 향상시키는 것이다. 수직 스케일로 불리기도 한다.

#### 적용

어플리케이션 서버에서는 스케일 아웃이 가능해도 빈번히 갱신이 발생하여 데이터가 서로 모순 없이 일관되게 일치해야 하는 경우가 어려운 db 서버에서는 스케일 업이 필요하다. 즉 OLTP에는 스케일 업이 적합하다.

<img src="./scaleout,up prosandcons.png">

<img src="https://mblogthumb-phinf.pstatic.net/20151124_152/islove8587_1448357175274p9SjR_PNG/tech_img2603.png?type=w2">

    참조:
    https://m.blog.naver.com/islove8587/220548900044
