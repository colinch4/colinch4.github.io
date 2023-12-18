---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 비동기 작업 진행 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발할 때, 사용자에게 현재 진행 중인 작업의 상태를 시각적으로 표시하는 것은 매우 중요합니다. 이를 위해 비동기 작업 중에 LinearProgressIndicator를 사용하여 진행 상태를 표시할 수 있습니다. 이 글에서는 Flutter에서 LinearProgressIndicator를 사용하여 비동기 작업의 진행 상태를 표시하는 방법에 대해 알아보겠습니다.

## 1. LinearProgressIndicator 위젯 추가

우선, LinearProgressIndicator 위젯을 화면에 추가합니다. 아래는 간단한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatelessWidget {
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
            Text('Doing some heavy work...'),
            LinearProgressIndicator(),
          ],
        ),
      ),
    );
  }
}
```

## 2. 비동기 작업 수행 시 LinearProgressIndicator 상태 변경

비동기 작업을 수행하는 메소드 내에서 `setState`를 사용하여 `LinearProgressIndicator` 상태를 변경합니다. 아래는 간단한 비동기 작업 및 진행 상태 표시 코드 예시입니다.

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  bool _isLoading = false;

  void _startAsyncTask() {
    setState(() {
      _isLoading = true;
    });

    // 비동기 작업 수행
    Future.delayed(Duration(seconds: 2), () {
      setState(() {
        _isLoading = false;
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
            Text('Press the button to start the task'),
            if (_isLoading)
              LinearProgressIndicator(),
            ElevatedButton(
              onPressed: _startAsyncTask,
              child: Text('Start Task'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위 예제 코드에서, `_isLoading` 변수를 사용하여 비동기 작업이 진행 중인지 여부를 표시하고, `setState`를 호출하여 `_isLoading` 상태를 변경함으로써 `LinearProgressIndicator`의 상태를 업데이트합니다.

이제 Flutter에서 LinearProgressIndicator를 사용하여 비동기 작업의 진행 상태를 표시하는 방법에 대해 알아보았습니다. 이를 통해 사용자 경험을 향상시키고, 작업이 진행 중임을 시각적으로 전달할 수 있습니다.

더 많은 자료와 예시는 [Flutter 공식문서](https://flutter.dev/docs)에서 확인할 수 있습니다.