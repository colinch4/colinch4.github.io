---
layout: post
title: "[web] 행정구역 병합하여 보여주기"
description: " "
date: 2021-06-17
tags: [web]
comments: true
share: true
---

## 행정구역 병합하여 보여주기

## 배경

county-level로 지도를 그리는데, 여러 카운티를 선택하는 경우, 선택된 지역을 병합하여 하나의 지역으로 보여주고 싶었다.
현재 연구 중인 도시에서의 육류 소비를 시각화하는 과정에서, metropolitan area를 표시해주어야 했다.
결론적으로 ​말하자면, Mike Bostoc의 예제를 그대로 따라하면 별 문제 없이 해결 가능하다.

## 문제 해결

참고한 예제처럼 지도 데이터를 불러올 때, topojson.merge 함수를 이용하여 shape을 병합하면 된다.
대신 병합 이후에는 기존 인덱스가 작동하지 않기 때문에, 마우스 롤오버 같은 액션을 주고 싶으면, 인덱스를 알아내는 작업이 필요하다.
오늘은 읽어온 데이터에서 바로 하이라이트 해주는 방식으로 정리하였다.

## 참고문헌

* [https://bl.ocks.org/mbostock/5416405](https://bl.ocks.org/mbostock/5416405)
