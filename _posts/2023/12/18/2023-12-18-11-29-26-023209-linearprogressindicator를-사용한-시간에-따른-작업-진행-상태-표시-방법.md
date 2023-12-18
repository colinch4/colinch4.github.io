---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 시간에 따른 작업 진행 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

앱 또는 웹 애플리케이션에서 작업의 진척 상황을 시각적으로 표시하는 것은 사용자 경험을 개선하는 중요한 부분입니다. 시간에 따른 작업의 진행 상태를 표시할 때 `LinearProgressIndicator` 위젯을 사용하는 방법을 알아보겠습니다.

## 1. `LinearProgressIndicator` 위젯

`LinearProgressIndicator` 위젯은 진행 상태를 수평으로 표시하는 데 사용됩니다. 이를 통해 작업이 얼마나 완료되었는지 시각적으로 표시할 수 있습니다.

```dart
Widget build(BuildContext context){
  return Scaffold(
    body: Center(
      child: LinearProgressIndicator(
        value: 0.5, 
        backgroundColor: Colors.grey, 
        valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
      ),
    ),
  );
}
```

## 2. 시간에 따른 작업 진행 상태 표시

작업이 어느 정도 시간이 걸리는지에 따라 `LinearProgressIndicator`의 `value` 속성을 조절하여 작업의 진행 상태를 표시할 수 있습니다.

```dart
class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  double _progressValue = 0.0;

  @override
  void initState() {
    super.initState();
    _updateProgress();
  }

  void _updateProgress() {
    Future.delayed(Duration(seconds: 1), () {
      if (_progressValue < 1.0) {
        setState(() {
          _progressValue += 0.1;
        });
        _updateProgress();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: LinearProgressIndicator(
          value: _progressValue,
          backgroundColor: Colors.grey,
          valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
        ),
      ),
    );
  }
}
```

위 예제에서 `_updateProgress` 함수는 1초마다 `_progressValue`를 0.1씩 증가시키며, 이 값을 `LinearProgressIndicator`의 `value`로 설정하여 작업의 진행 상태를 표시합니다.

이제 `LinearProgressIndicator` 위젯을 사용하여 시간에 따른 작업 진행 상태를 효과적으로 표시할 수 있습니다.

## 참고 자료
- [Flutter 공식 문서: LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)