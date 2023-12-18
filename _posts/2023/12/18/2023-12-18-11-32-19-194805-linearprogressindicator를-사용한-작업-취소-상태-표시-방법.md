---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 작업 취소 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱에서 사용자가 긴 작업이 진행 중일 때 작업을 취소할 수 있도록 해야 할 때가 있습니다. 사용자는 작업이 진행 중임을 알 수 있어야 하며, 작업이 취소되면 그 상태도 시각적으로 표시되어야 합니다. 이를 위해 LinearProgressIndicator를 사용하여 작업 진행 상태와 작업 취소 상태를 표시하는 방법을 알아보겠습니다.

## 작업 진행 상태 표시하기

먼저, LinearProgressIndicator를 사용하여 작업의 진행 상태를 표시하는 방법을 살펴보겠습니다. LinearProgressIndicator는 현재 진행 중인 작업의 진행률을 시각적으로 표시할 수 있는 위젯입니다.

```dart
import 'package:flutter/material.dart';

class MyProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return LinearProgressIndicator();
  }
}
```

위 예제 코드에서는 `MyProgressIndicator`라는 StatelessWidget를 정의하고, `build` 메서드에서 LinearProgressIndicator를 반환하도록 구현하였습니다.

## 작업 취소 상태 표시하기

작업이 취소될 때, LinearProgressIndicator를 사용하여 해당 상태를 시각적으로 표시할 수 있습니다. 취소되는 시점에 따라 작업 취소 상태를 표시하는 방법은 다양할 수 있지만, 여기서는 작업 취소 상태를 색상을 변경하여 표시하는 방법을 살펴보겠습니다.

```dart
import 'package:flutter/material.dart';

class MyProgressIndicator extends StatelessWidget {
  final bool isCancelled;

  MyProgressIndicator({this.isCancelled = false});

  @override
  Widget build(BuildContext context) {
    return LinearProgressIndicator(
      valueColor: isCancelled
          ? AlwaysStoppedAnimation<Color>(Colors.red)
          : AlwaysStoppedAnimation<Color>(Colors.blue),
    );
  }
}
```

위 예제 코드에서는 `MyProgressIndicator`에 `isCancelled`라는 속성을 추가하고, 작업이 취소되었을 때 `LinearProgressIndicator`의 색상을 빨간색으로 변경하도록 구현하였습니다.

## 결론

Flutter에서는 LinearProgressIndicator를 사용하여 작업의 진행 상태를 표시하고, 작업이 취소될 때 해당 상태를 시각적으로 표시할 수 있습니다. 사용자 경험을 고려하여 작업 진행 상태와 작업 취소 상태를 명확하게 표시하여 사용자가 언제든지 작업을 취소할 수 있도록 하는 것이 중요합니다.

마지막으로, 여기서 소개된 예제 코드는 UI 상태 관리 및 작업 취소 동작과 연결하여 사용해야 합니다.

## 참고 자료

- [Flutter 공식 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)