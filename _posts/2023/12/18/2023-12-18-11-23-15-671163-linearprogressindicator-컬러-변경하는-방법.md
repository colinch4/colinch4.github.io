---
layout: post
title: "[flutter] LinearProgressIndicator 컬러 변경하는 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter의 `LinearProgressIndicator` 위젯은 진행률을 보여주는 유용한 기능을 제공합니다. 이 때, 기본적으로 제공되는 스타일을 변경하고 싶을 때가 있습니다. 이 포스트에서는 `LinearProgressIndicator`의 색상을 변경하는 방법에 대해 살펴보겠습니다.

## 1. `LinearProgressIndicator`의 색상 변경하기

`LinearProgressIndicator`의 색상을 변경하려면 `valueColor` 속성을 사용하면 됩니다. 이 속성을 사용하면 `LinearProgressIndicator`의 색상을 쉽게 변경할 수 있습니다.

다음은 `LinearProgressIndicator`의 색상을 변경하는 간단한 예제입니다.

```dart
LinearProgressIndicator(
  value: 0.5,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
)
```

위 예제에서는 `valueColor` 속성을 사용하여 `LinearProgressIndicator`의 색상을 파란색으로 변경하고 있습니다.

## 2. 상태에 따라 동적으로 색상 변경하기

상태에 따라 `LinearProgressIndicator`의 색상을 동적으로 변경하려면 `valueColor`에 `Animation<Color>`를 사용하여 색상 애니메이션을 적용할 수 있습니다.

다음은 `LinearProgressIndicator`의 상태에 따라 동적으로 색상을 변경하는 예제입니다.

```dart
LinearProgressIndicator(
  value: _progressValue,
  valueColor: AlwaysStoppedAnimation<Color>(
    _progressValue > 0.5 ? Colors.green : Colors.red,
  ),
)
```

위 예제에서는 `_progressValue`의 값에 따라 `LinearProgressIndicator`의 색상을 동적으로 변경하고 있습니다.

이렇게 하면 `LinearProgressIndicator`의 색상을 쉽게 변경하고 상태에 따라 동적으로 색상을 조절할 수 있습니다.

이상으로 Flutter에서 `LinearProgressIndicator`의 색상을 변경하는 방법에 대해 알아보았습니다.

참고 문헌: [Flutter API 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)