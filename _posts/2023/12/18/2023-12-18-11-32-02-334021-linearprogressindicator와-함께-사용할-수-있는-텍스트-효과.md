---
layout: post
title: "[flutter] LinearProgressIndicator와 함께 사용할 수 있는 텍스트 효과"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱에서 진행률을 보여주거나 작업이 진행 중임을 알려주기 위해 `LinearProgressIndicator` 위젯을 사용하는 것은 일반적입니다. 그러나 경우에 따라 이러한 진행률 표시에 함께 텍스트를 표시하는 것이 유용할 수 있습니다. 본 포스트에서는 `LinearProgressIndicator`와 함께 사용할 수 있는 텍스트 효과에 대해 알아보겠습니다.

## LinearProgressIndicator 위젯 생성하기

먼저 `LinearProgressIndicator` 위젯을 생성하는 방법을 알아봅시다.

```dart
LinearProgressIndicator(
  value: 0.5, // 진행률 값 (0.0부터 1.0까지)
  backgroundColor: Colors.grey,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
)
```

## 함께 사용할 텍스트 추가하기

`LinearProgressIndicator` 위젯과 함께 진행 상태를 텍스트로 함께 표시하려면 `LinearProgressIndicator`를 `Stack` 위젯과 함께 사용하여 표현할 수 있습니다.

```dart
Stack(
  children: <Widget>[
    LinearProgressIndicator(
      value: 0.5,
      backgroundColor: Colors.grey,
      valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
    ),
    Positioned(
      left: 0,
      right: 0,
      child: Text(
        '50% 완료',
        textAlign: TextAlign.center,
        style: TextStyle(
          color: Colors.black,
          fontSize: 16,
        ),
      ),
    ),
  ],
)
```

## 결론

`LinearProgressIndicator`와 함께 텍스트를 함께 사용하여 진행 상태를 시각적으로 표시하는 방법에 대해 알아보았습니다. 이를 통해 사용자가 진행 중인 작업에 대한 정보를 보다 명확하게 제공할 수 있게 됩니다.

참고 자료:
- Flutter 위젯 카탈로그: [LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)
- Flutter API 문서: [Stack](https://api.flutter.dev/flutter/widgets/Stack-class.html)

[flutter]: https://flutter.dev/