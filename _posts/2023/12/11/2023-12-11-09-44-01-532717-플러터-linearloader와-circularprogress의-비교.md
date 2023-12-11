---
layout: post
title: "[flutter] 플러터 LinearLoader와 CircularProgress의 비교"
description: " "
date: 2023-12-11
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 애니메이션과 UI 요소를 다루는 데 특히 뛰어난 프레임워크입니다. 이번 포스트에서는 플러터에서 제공하는 `LinearProgressIndicator`와 `CircularProgressIndicator`를 비교해보겠습니다.

## 1. LinearProgressIndicator

`LinearProgressIndicator`는 선 모양의 프로그레스 바를 표시할 때 사용됩니다. 이 요소는 가로 방향으로 진행되는 진척 상황을 시각적으로 보여줍니다.

```dart
LinearProgressIndicator(
  value: 0.5,
)
```

위 코드에서 `value`는 프로그레스의 진행 정도를 나타내며, 0.0부터 1.0까지의 값을 갖습니다.

## 2. CircularProgressIndicator

`CircularProgressIndicator`는 원형으로 표시되는 프로그레스 바를 나타냅니다. 불규칙하거나 지속적으로 변하는 진행 상황을 나타내기에 적합합니다.

```dart
CircularProgressIndicator(
  value: 0.7,
)
```

위 코드에서도 `value`를 이용해 프로그레스의 진행 정도를 나타내며, 0.0부터 1.0까지의 값을 가집니다.

## 요약

- `LinearProgressIndicator`는 가로 방향의 진행 상황을, `CircularProgressIndicator`는 원형으로 나타낸다.
- 둘 다 `value` 속성을 사용하여 진행 정도를 조절할 수 있다.

각각의 상황에 맞게 선택하여 사용하면 됩니다. 물론 디자인과 사용성을 고려하여 적절히 활용하는 것이 좋습니다.

이상으로 플러터의 `LinearProgressIndicator`와 `CircularProgressIndicator`의 비교를 마치겠습니다.

[공식 플러터 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)

[공식 플러터 문서 - CircularProgressIndicator](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)