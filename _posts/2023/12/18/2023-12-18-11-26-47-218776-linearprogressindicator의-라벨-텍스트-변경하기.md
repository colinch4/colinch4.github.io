---
layout: post
title: "[flutter] LinearProgressIndicator의 라벨 텍스트 변경하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter의 `LinearProgressIndicator` 위젯은 진행률 인디케이터를 표시하는데 사용됩니다. 기본적으로는 퍼센트 값을 나타내는 라벨이 표시되지 않지만, 원하는 경우에 라벨 텍스트를 변경할 수 있습니다.

이번 포스트에서는 `LinearProgressIndicator`의 라벨 텍스트를 변경하는 방법에 대해 알아보겠습니다.

## 1. LinearProgressIndicator를 포함한 위젯 생성

먼저, `LinearProgressIndicator`를 포함한 위젯을 생성합니다.

```dart
import 'package:flutter/material.dart';

class CustomProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Custom Progress Indicator'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Downloading...'),
            LinearProgressIndicator(),
          ],
        ),
      ),
    );
  }
}
```

위 예제에서는 `Scaffold`와 `AppBar`를 포함하고, `LinearProgressIndicator`를 사용하여 진행률을 나타내고 있습니다.

## 2. CustomLinearProgressIndicator 위젯 생성

다음으로, `LinearProgressIndicator`의 라벨 텍스트를 변경하는 새로운 커스텀 위젯을 생성합니다.

```dart
class CustomLinearProgressIndicator extends StatelessWidget {
  final String label;

  CustomLinearProgressIndicator({@required this.label});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(label),
        LinearProgressIndicator(),
      ],
    );
  }
}
```

위 예제에서는 `CustomLinearProgressIndicator` 위젯을 생성하고, `label` 속성을 통해 원하는 라벨 텍스트를 전달할 수 있습니다.

## 3. 사용 예

마지막으로, `CustomLinearProgressIndicator` 위젯을 사용하여 라벨 텍스트를 변경하는 예를 살펴봅시다.

```dart
class CustomProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Custom Progress Indicator'),
      ),
      body: Center(
        child: CustomLinearProgressIndicator(label: 'Loading...'),
      ),
    );
  }
}
```

위 예제에서는 `CustomLinearProgressIndicator` 위젯을 사용하여 라벨 텍스트를 "Loading..."으로 설정하고 있습니다.

이제 여러분은 `LinearProgressIndicator`의 라벨 텍스트를 변경하는 방법을 이해하고 있습니다.

더 많은 정보를 원하시면 [공식 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)를 참고하세요.