---
layout: post
title: "[flutter] LinearProgressIndicator의 우측 정렬 설정하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

이 포스트에서는 Flutter 앱에서 LinearProgressIndicator를 우측으로 정렬하는 방법에 대해 알아보겠습니다.

## 1. LinearProgressIndicator 우측 정렬

우측으로 정렬된 LinearProgressIndicator를 구현하려면 `Row` 위젯을 사용하여 `Spacer`를 추가하고 `LinearProgressIndicator`를 배치해야 합니다. 아래는 간단한 예시 코드입니다.

```dart
Row(
  children: <Widget>[
    Text('Some Text'),
    Spacer(),
    LinearProgressIndicator(),
  ],
),
```

위 코드에서 `Spacer`는 주어진 공간을 최대한 확장하여 나머지 요소를 모두 우측으로 밀어내는 역할을 합니다.

## 2. 레이아웃 수정

`LinearProgressIndicator`의 색상, 높이, 너비 등의 속성은 필요에 따라 수정할 수 있습니다. 예를 들어, 더 많은 공간을 차지하도록 너비를 조절하거나, 다른 색상을 사용할 수 있습니다.

```dart
LinearProgressIndicator(
  valueColor: AlwaysStoppedAnimation<Color>(Colors.red),
  minHeight: 10,
  backgroundColor: Colors.transparent,
),
```

## 결론

Flutter의 `LinearProgressIndicator`를 우측 정렬하는 방법과 레이아웃을 수정하는 방법에 대해 살펴보았습니다. 필요에 맞게 적절히 활용하여 앱의 UI/UX를 개선할 수 있을 것입니다.

더 자세한 내용은 [공식 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)를 참고해 주세요.