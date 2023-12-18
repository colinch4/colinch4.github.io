---
layout: post
title: "[flutter] LinearProgressIndicator의 완료 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱에서 작업이 진행 중일 때 사용자에게 진행 상황을 시각적으로 표시하는 데에 LinearProgressIndicator 위젯을 사용할 수 있습니다. 하지만 작업이 완료된 후에도 사용자에게 완료 상태를 명확히 보여주는 것이 중요합니다. 

이 블로그 포스트에서는 Flutter에서의 LinearProgressIndicator의 완료 상태 표시 방법에 대해 알아보겠습니다.

## LinearProgressIndicator 사용하기

먼저 LinearProgressIndicator를 사용하여 작업의 진행 상황을 표시하는 방법에 대해 간단히 살펴보겠습니다. 다음은 LinearProgressIndicator를 생성하고 사용하는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('LinearProgressIndicator Example'),
        ),
        body: Center(
          child: LinearProgressIndicator(),
        ),
      ),
    );
  }
}
```

이 예제 코드는 간단한 앱을 생성하고 화면 중앙에 LinearProgressIndicator를 표시합니다.

## LinearProgressIndicator의 완료 상태 표시하기

작업이 완료된 후에는 LinearProgressIndicator를 제거하거나 다른 위젯으로 대체하여 사용자에게 완료 상태를 명확히 보여줄 수 있습니다. 다음은 작업이 완료된 후 완료 상태를 표시하는 예제 코드입니다.

```dart
class MyApp extends StatelessWidget {
  bool _isLoading = true;

  void _completeTask() {
    // 작업 완료 시 호출되는 메서드
    setState(() {
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('LinearProgressIndicator Example'),
        ),
        body: Center(
          child: _isLoading
              ? LinearProgressIndicator()
              : Text('작업이 완료되었습니다.'),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: _completeTask,
          child: Icon(Icons.check),
        ),
      ),
    );
  }
}
```

위 예제 코드에서는 `_isLoading` 변수를 사용하여 작업이 완료되었는지를 추적합니다. `_completeTask` 메서드는 작업이 완료되면 호출되어 `_isLoading` 값을 변경하고, 이에 따라 LinearProgressIndicator 또는 완료 메시지를 표시합니다.

## 결론

Flutter의 LinearProgressIndicator를 사용하여 작업의 진행 상황을 표시할 수 있습니다. 작업이 완료된 후에는 사용자에게 상태를 명확히 전달하기 위해 LinearProgressIndicator를 적절히 제거하거나 상태에 맞는 다른 위젯으로 대체하는 것이 좋습니다.

참고: [Flutter 공식 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)