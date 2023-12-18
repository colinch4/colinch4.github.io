---
layout: post
title: "[flutter] LinearProgressIndicator의 바 형태 변경하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter의 `LinearProgressIndicator` 위젯은 진행률을 시각적으로 보여주는 데 사용됩니다. 기본적으로는 일렬로 놓인 바 형태로 표시되지만, 이를 커스터마이징하여 다양한 모양으로 변경할 수 있습니다.

이 포스트에서는 `LinearProgressIndicator`의 바 형태를 변경하는 방법에 대해 알아보겠습니다.

## 기본 바 형태

먼저, 기본적인 `LinearProgressIndicator`를 생성하는 방법을 알아보겠습니다.

```dart
LinearProgressIndicator()
```

위와 같이 코드를 작성하면, 기본 바 형태의 `LinearProgressIndicator`가 생성됩니다. 

## 커스텀 바 형태

이제, `LinearProgressIndicator`의 바 형태를 변경해보겠습니다. 

`LinearProgressIndicator` 위젯은 `LinearProgressIndicator` 클래스 밑에 `LinearProgressIndicator.build` 메서드를 사용하여 커스터마이징할 수 있습니다.

커스텀 바 형태를 생성하는 예시는 다음과 같습니다.
```dart
LinearProgressIndicator(
  value: 0.5, // 진행률
  backgroundColor: Colors.grey[300], // 바의 배경색
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue), // 진행률에 대한 바의 색상
)
```

위의 코드에서 `value` 속성은 진행률을 나타내며, `backgroundColor`와 `valueColor` 속성은 각각 바의 배경색과 진행률에 대한 바의 색상을 설정합니다.

## 마무리

이렇게 `LinearProgressIndicator`를 사용하여 바 형태를 변형하고 커스터마이징할 수 있습니다. 필요에 따라 진행률 표시 모양을 변경하여 사용자 경험을 향상시킬 수 있습니다.

참고: [Flutter API 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)