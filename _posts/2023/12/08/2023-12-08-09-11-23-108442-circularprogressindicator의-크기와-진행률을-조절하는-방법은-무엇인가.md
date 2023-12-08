---
layout: post
title: "[flutter] CircularProgressIndicator의 크기와 진행률을 조절하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

`CircularProgressIndicator`는 애플리케이션이 작업을 수행하는 동안 진행률을 나타내는 데 사용됩니다. 이 지표의 크기와 진행률을 조절하는 방법을 알아보겠습니다.

## 1. 크기 조절

`CircularProgressIndicator`의 크기는 `Container` 위젯을 사용하여 조절할 수 있습니다.

```dart
Container(
  width: 50,
  height: 50,
  child: CircularProgressIndicator(),
)
```

위 예제에서는 `Container`의 `width`와 `height` 속성을 이용하여 `CircularProgressIndicator`의 크기를 50x50으로 조절하고 있습니다. 이렇게 하면 원하는 크기로 진행률 표시기를 조절할 수 있습니다.

## 2. 진행률 조절

진행률을 조절하는 방법은 `value` 속성을 이용하는 것입니다. `value` 속성은 0.0부터 1.0까지의 값을 가질 수 있으며, 이를 이용하여 진행률을 조절할 수 있습니다.

```dart
CircularProgressIndicator(
  value: 0.5,
)
```

위 예제에서는 `value`를 0.5로 설정하여 50%의 진행률을 표시하고 있습니다.

이렇게 `CircularProgressIndicator`의 크기와 진행률을 조절할 수 있습니다.

더 많은 정보는 [공식 문서](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)를 참고하세요.