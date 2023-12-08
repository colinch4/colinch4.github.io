---
layout: post
title: "[flutter] CircularProgressIndicator의 값을 외부에서 동적으로 업데이트하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

CircularProgressIndicator는 작업이 진행 중임을 나타내는 데 사용되는 간단한 위젯입니다. 이 위젯의 값은 주로 Future나 Stream과 같은 비동기 작업의 진행률을 표시하기 위해 사용됩니다. 그러나 때로는 이 값을 외부에서 직접 제어하고 싶을 수도 있습니다. Flutter에서는 이 값을 외부에서 동적으로 업데이트하는 방법이 제공되고 있습니다. 아래에서 해당 방법을 살펴보겠습니다.

## 1. StatefulWidget 사용

CircularProgressIndicator의 값은 StatefulWidget을 사용하여 동적으로 업데이트할 수 있습니다. StatefulWidget은 상태를 가지고 있는 위젯으로, 상태가 변경될 때마다 화면을 다시 그리게 됩니다. 따라서 CircularProgressIndicator의 값을 변경할 때마다 해당 StatefulWidget의 `setState` 함수를 호출하여 화면을 다시 그리도록 할 수 있습니다.

예를 들어, 아래와 같이 StatefulWidget을 생성하고 해당 StatefulWidget 내에서 CircularProgressIndicator의 값을 동적으로 변경할 수 있습니다.

```dart
import 'package:flutter/material.dart';

class MyCircularProgressIndicator extends StatefulWidget {
  @override
  _MyCircularProgressIndicatorState createState() => _MyCircularProgressIndicatorState();
}

class _MyCircularProgressIndicatorState extends State<MyCircularProgressIndicator> {
  double _progress = 0.0;

  void updateProgress(double newProgress) {
    setState(() {
      _progress = newProgress;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(
        value: _progress,
      ),
    );
  }
}
```

위 코드에서 `_progress` 변수를 사용하여 CircularProgressIndicator의 값을 제어하고 있으며, `updateProgress` 함수를 통해 이 값을 업데이트하고 있습니다.

## 2. 상위 클래스에서 값을 전달

또 다른 방법은 CircularProgressIndicator를 포함하는 부모 위젯에서 값을 전달하는 것입니다. 이 방법은 StatefulWidget을 사용하지 않아도 되므로 코드가 더 간단해질 수 있습니다. 예를 들어, 부모 위젯에서 CircularProgressIndicator의 값이 변경된다면, 해당 값을 인자로 받아 CircularProgressIndicator를 재생성하는 방식으로 동적으로 업데이트할 수 있습니다.

```dart
import 'package:flutter/material.dart';

class MyCircularProgressIndicator extends StatelessWidget {
  final double progress;

  MyCircularProgressIndicator({required this.progress});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(
        value: progress,
      ),
    );
  }
}
```

## 마무리

이렇게하여 CircularProgressIndicator의 값을 외부에서 동적으로 업데이트하는 방법에 대해 살펴보았습니다. StatefulWidget을 사용하여 상태를 관리하거나, 부모 위젯으로부터 값을 전달받는 방법 중 선택하여 구현할 수 있습니다. 선택한 방법에 따라 코드를 작성하여 CircularProgressIndicator의 값을 필요에 따라 동적으로 변경할 수 있을 것입니다.

더 많은 정보를 원하신다면 [공식 Flutter 문서](https://flutter.dev/docs)를 참고해보세요.