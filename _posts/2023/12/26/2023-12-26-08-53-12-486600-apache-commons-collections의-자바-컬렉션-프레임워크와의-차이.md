---
layout: post
title: "[java] Apache Commons Collections의 자바 컬렉션 프레임워크와의 차이"
description: " "
date: 2023-12-26
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 언어에 기존 컬렉션 프레임워크를 보완하기 위한 유용한 도구 모음입니다. 이 라이브러리는 내장된 자바 컬렉션 프레임워크와 비교해서 어떤 점이 다른지 알아보겠습니다.

## 1. 기능

Apache Commons Collections는 기존 자바 컬렉션 프레임워크에 비해 추가적인 유용한 기능을 제공합니다. 예를 들어, **`CollectionUtils`** 클래스를 사용하면 컬렉션을 합치거나 필터링할 수 있으며, **`MapUtils`** 클래스를 사용하면 맵과 관련된 다양한 유틸리티 기능을 제공받을 수 있습니다.

## 2. 컬렉션 타입

Apache Commons Collections는 자바 컬렉션 프레임워크에 존재하지 않는 추가적인 컬렉션 타입을 제공합니다. 예를 들어, **`BidiMap`**은 키-값 쌍에서 양방향 검색을 지원하는 맵을 제공하며, **`Bag`**은 중복 요소를 허용하는 컬렉션을 제공합니다.

## 3. 라이브러리 크기

Apache Commons Collections는 자바 컬렉션 프레임워크보다 더 큰 라이브러리입니다. 이에 따라 프로젝트에 라이브러리를 추가할 때 고려해야 합니다.

## 4. 호환성

Apache Commons Collections는 자바의 여러 버전과 호환됩니다. 따라서 다양한 환경에서 쉽게 사용할 수 있습니다.

Apache Commons Collections는 자바 컬렉션 프레임워크를 보완하기 위한 강력한 도구 모음으로, 다양한 상황에서 유용하게 활용될 수 있습니다.

더 많은 정보를 원하신다면 [공식 웹사이트](https://commons.apache.org/proper/commons-collections/)를 방문해보세요.