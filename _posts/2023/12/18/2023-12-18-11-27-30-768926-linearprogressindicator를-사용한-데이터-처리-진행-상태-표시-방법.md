---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 데이터 처리 진행 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다 보면 데이터 처리나 네트워크 요청 등의 작업이 시간이 소요될 수 있습니다. 이러한 작업이 진행 중에는 사용자에게 진행 상태를 시각적으로 보여줄 필요가 있습니다. 이때 **LinearProgressIndicator** 위젯을 사용하여 데이터 처리 진행 상태를 표시할 수 있습니다.

## LinearProgressIndicator란?

**LinearProgressIndicator**는 작업이 얼마나 진행되었는지 시각적으로 보여주는 데 사용되는 Material Design의 프로그레스 바입니다. 작업이 진행될 때마다 증가하고 작업이 완료되면 사라지는 진행 바를 표시할 수 있습니다.

## LinearProgressIndicator 사용 방법

**LinearProgressIndicator**를 사용하여 데이터 처리 진행 상태를 표시하는 방법은 매우 간단합니다. 우선, 해당 작업이 진행되는 동안 **LinearProgressIndicator**를 화면에 표시하고, 작업이 완료된 후에는 해당 위젯을 숨겨주면 됩니다.

아래는 **LinearProgressIndicator**를 활용한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

class DataProcessingWidget extends StatefulWidget {
  @override
  _DataProcessingWidgetState createState() => _DataProcessingWidgetState();
}

class _DataProcessingWidgetState extends State<DataProcessingWidget> {
  bool _processing = false;

  void _startDataProcessing() {
    setState(() {
      _processing = true;
      // 여기서 데이터 처리 작업을 시작합니다.
      // 작업이 완료되면 _processing을 false로 변경하여 LinearProgressIndicator를 숨깁니다.
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        if (_processing) LinearProgressIndicator(),
        RaisedButton(
          onPressed: _startDataProcessing,
          child: Text('데이터 처리 시작'),
        ),
      ],
    );
  }
}
```

위 코드에서는 **LinearProgressIndicator**를 사용하여 데이터 처리 진행 상태를 표시하고, 버튼을 통해 데이터 처리 작업을 시작하는 예시를 보여주고 있습니다.

## 마무리

**LinearProgressIndicator**를 사용하여 데이터 처리 작업의 진행 상태를 보여주면, 사용자는 작업이 진행 중인지를 쉽게 파악할 수 있습니다. 이를 통해 사용자 경험을 향상시키고, 앱의 질을 향상시킬 수 있습니다.

작업이 진행 중일 때는 반드시 **LinearProgressIndicator**를 표시하는 것이 좋으며, 작업이 완료된 후에는 해당 위젯을 숨겨 사용자에게 완료되었음을 알려주는 것이 중요합니다.

## References

- [Flutter 공식 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)
- [Flutter Cookbook - Display a progress indicator](https://flutter.dev/docs/cookbook/misc/progress-indicator)