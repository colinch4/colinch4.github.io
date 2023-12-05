---
layout: post
title: "[flutter] flutter_custom_clippers와 다른 클리퍼 라이브러리 비교"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

## 소개

`flutter_custom_clippers`는 Flutter에서 사용할 수 있는 다양한 형태의 클리퍼(clipper)를 제공하는 라이브러리입니다. 클리퍼를 사용하면 원하는 모양으로 위젯의 형태를 자를 수 있습니다. 하지만, `flutter_custom_clippers`는 다른 클리퍼 라이브러리와 비교하여 어떤 장단점을 가지고 있는지 알아보는 것이 중요합니다.

## 비교 대상 라이브러리

- `flutter_custom_clippers`: Flutter에서 클리퍼를 사용하기 위한 기본 라이브러리
- `flutter_clip_path`: Flutter에서 클리퍼를 사용할 수 있는 라이브러리
- `clip_path_transformer`: Flutter에서 클리퍼를 사용할 수 있는 라이브러리

## 비교 요소

- 다양한 클리퍼 제공
- 사용 편의성
- 성능

## 다양한 클리퍼 제공

- `flutter_custom_clippers`: `flutter_custom_clippers`는 50여 가지의 다양한 형태의 클리퍼를 제공합니다. 심플한 형태부터 복잡한 형태까지 원하는 클리퍼를 적용할 수 있습니다.

- `flutter_clip_path`: `flutter_clip_path`는 20여 가지의 다양한 형태의 클리퍼를 제공합니다. `flutter_custom_clippers`보다 제공되는 클리퍼의 종류는 적지만, 기본적인 클리퍼들이 제공되어 다양한 형태의 UI를 만들 수 있습니다.

- `clip_path_transformer`: `clip_path_transformer`는 10여 가지의 다양한 형태의 클리퍼를 제공합니다. 제공되는 클리퍼의 종류는 제한적이지만, 기본적인 형태들을 사용할 수 있습니다.

## 사용 편의성

- `flutter_custom_clippers`: `flutter_custom_clippers`는 간단한 설정으로 클리퍼를 적용할 수 있습니다. `ClipPath` 위젯을 사용하여 쉽게 클리퍼를 적용할 수 있습니다.

- `flutter_clip_path`: `flutter_clip_path`는 `CustomClipper` 클래스를 상속받아 자신만의 클리퍼를 만들어야 합니다. 커스텀 클리퍼를 만들어 사용해야 하기 때문에 초기 설정에 시간이 조금 더 소요될 수 있습니다.

- `clip_path_transformer`: `clip_path_transformer`는 `ClipPathTransformer` 클래스를 사용하여 클리퍼를 설정합니다. 초기 설정은 간단하지만, 많은 변형을 주기 위해서는 좀 더 복잡한 설정이 필요할 수 있습니다.

## 성능

- `flutter_custom_clippers`, `flutter_clip_path`, `clip_path_transformer` 세 라이브러리 모두 성능 측면에서 큰 차이는 없습니다. 하지만, 클리핑은 레이아웃을 재계산하는 과정이므로 과도한 클리핑은 성능에 영향을 끼칠 수 있으므로 주의해야 합니다.

## 결론

- `flutter_custom_clippers`는 다양한 형태의 클리퍼를 제공하여 다양한 UI를 만들 수 있으며, 간단한 설정으로 사용할 수 있습니다.
- `flutter_clip_path`는 커스텀 클리퍼를 만들어야 하기 때문에 초기 설정에 시간이 소요될 수 있습니다. 하지만, 제공되는 클리퍼를 사용하면서 다양한 UI를 만들 수 있습니다.
- `clip_path_transformer`는 제한적인 클리퍼를 제공하지만, 간단한 설정으로 사용할 수 있습니다.

각 라이브러리의 장단점을 고려하여 프로젝트에 맞는 클리퍼 라이브러리를 선택하는 것이 중요합니다.