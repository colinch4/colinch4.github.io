---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 특정 작업 완료 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

앱이나 웹 애플리케이션에서 어떤 작업이 실행 중일 때, 사용자에게 작업이 얼마나 진행되었는지를 표시하는 것은 중요합니다. `LinearProgressIndicator` 위젯은 플러터에서 이러한 작업 진행 상태를 시각적으로 나타내는데 사용됩니다. 이 포스트에서는 `LinearProgressIndicator`를 어떻게 사용하여 특정 작업의 완료 상태를 표시하는지 알아보겠습니다.

## 1. LinearProgressIndicator 위젯 추가

먼저, `LinearProgressIndicator`를 사용하기 위해 해당 위젯을 화면에 추가해야 합니다. 다음은 간단한 예시입니다.

```dart
import 'package:flutter/material.dart';

class MyProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Progress Indicator Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('작업이 진행 중입니다...'),
            LinearProgressIndicator(),
          ],
        ),
      ),
    );
  }
}
```

위 코드에서 `LinearProgressIndicator` 위젯을 `Column` 위젯 안에 추가하여 작업이 진행 중임을 나타내는 텍스트와 함께 화면에 표시됩니다.

## 2. 작업 완료 상태에 따라 표시 여부 결정

특정 작업의 완료 상태에 따라 `LinearProgressIndicator`를 화면에 보이거나 숨길 수 있습니다.

예를 들어, 작업이 완료되면 `LinearProgressIndicator`를 숨기고 완료 메시지를 표시할 수 있습니다. 다음은 작업이 완료될 때까지 일정 시간이 걸리는 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

class MyProgressIndicator extends StatefulWidget {
  @override
  _MyProgressIndicatorState createState() => _MyProgressIndicatorState();
}

class _MyProgressIndicatorState extends State<MyProgressIndicator> {
  bool _isTaskComplete = false;

  @override
  void initState() {
    super.initState();
    _doTask();
  }

  void _doTask() {
    Future.delayed(Duration(seconds: 3), () {
      setState(() {
        _isTaskComplete = true;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Progress Indicator Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            if (!_isTaskComplete) Text('작업이 진행 중입니다...'),
            if (!_isTaskComplete) LinearProgressIndicator(),
            if (_isTaskComplete) Text('작업이 완료되었습니다.'),
          ],
        ),
      ),
    );
  }
}
```

위 코드에서 `Future.delayed` 메서드를 사용하여 3초 후에 `_isTaskComplete` 변수를 `true`로 변경하여 작업이 완료되었음을 나타내고, 이에 따라 `LinearProgressIndicator`나 완료 메시지를 표시하거나 숨깁니다.

`LinearProgressIndicator`를 사용하여 애플리케이션에서 작업의 완료 상태를 시각적으로 나타내는 것은 사용자가 작업에 대한 투입감을 느끼도록 도와줍니다.

더 많은 정보는 [플러터 공식 문서](https://flutter.dev/docs/development/ui/widgets/material#LinearProgressIndicator)에서 확인할 수 있습니다.