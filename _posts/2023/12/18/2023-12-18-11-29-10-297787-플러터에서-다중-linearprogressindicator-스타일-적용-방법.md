---
layout: post
title: "[flutter] 플러터에서 다중 LinearProgressIndicator 스타일 적용 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터에서 다중 `LinearProgressIndicator`에 서로 다른 스타일을 적용하는 방법에 대해 알아보겠습니다. 

## 1. 여러 개의 LinearProgressIndicator 생성

먼저, 다중 `LinearProgressIndicator` 위젯을 생성합니다.

```dart
Widget multipleProgressIndicators() {
  return Column(
    children: <Widget>[
      LinearProgressIndicator(
        value: 0.2,
        backgroundColor: Colors.grey,
        valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
      ),
      LinearProgressIndicator(
        value: 0.5,
        backgroundColor: Colors.grey,
        valueColor: AlwaysStoppedAnimation<Color>(Colors.green),
      ),
      LinearProgressIndicator(
        value: 0.7,
        backgroundColor: Colors.grey,
        valueColor: AlwaysStoppedAnimation<Color>(Colors.red),
      ),
    ],
  );
}
```

위 코드는 세 개의 `LinearProgressIndicator` 위젯을 포함하는 Column을 생성하는 예시입니다.

## 2. 각 LinearProgressIndicator에 스타일 적용

여러 `LinearProgressIndicator`를 생성한 후, 각 `LinearProgressIndicator`에 필요한 스타일을 적용할 수 있습니다. 

예를 들어, 위 코드에서 세 개의 `LinearProgressIndicator` 위젯은 각각 파란색, 초록색, 빨간색으로 설정되었습니다.

이와 같이, 각 `LinearProgressIndicator`에 원하는 스타일을 적용하여 다중 `LinearProgressIndicator`에 서로 다른 스타일을 적용할 수 있습니다.

이것으로 플러터에서 다중 `LinearProgressIndicator`에 스타일을 적용하는 방법을 확인해 보았습니다.

참고 : [Flutter 공식 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)