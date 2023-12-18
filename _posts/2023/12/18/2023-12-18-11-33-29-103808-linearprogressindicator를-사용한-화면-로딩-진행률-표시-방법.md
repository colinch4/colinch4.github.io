---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 화면 로딩 진행률 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

### 1. LinearProgressIndicator 위젯 추가

먼저, 화면의 로딩 진행률을 표시할 **LinearProgressIndicator** 위젯을 화면에 추가합니다. 다음은 **Scaffold** 위젯 내에 **LinearProgressIndicator**를 추가하는 예제 코드입니다.

```dart
Scaffold(
  appBar: AppBar(
    title: Text('로딩 테스트'),
  ),
  body: Center(
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text('로딩 중...'),
        LinearProgressIndicator(),  // 이 부분에 LinearProgressIndicator를 추가합니다.
      ],
    ),
  ),
);
```

### 2. 진행률 업데이트

만약 실제 작업의 진행률을 반영해야 하는 경우, **LinearProgressIndicator**의 **value** 속성을 업데이트하여 진행률을 바로 반영할 수 있습니다. 다음은 **AsyncTask** 클래스를 사용하여 작업의 진행률을 업데이트하는 예제 코드입니다.

```dart
class AsyncTask {
  void start(TaskCallback callback) {
    // 작업 실행 전
    callback(0.2);  // 작업 진행률을 20%로 업데이트
    // 작업 실행 중
    callback(0.5);  // 작업 진행률을 50%로 업데이트
    // 작업 완료 후
    callback(1.0);  // 작업 진행률을 100%로 업데이트
  }
}

typedef TaskCallback = void Function(double progress);

class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  double _progress = 0.0;

  void updateProgress(double progress) {
    setState(() {
      _progress = progress;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('로딩 테스트'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('로딩 중...'),
            LinearProgressIndicator(value: _progress),  // value 속성에 진행률을 반영
          ],
        ),
      ),
    );
  }
}
```

### 결론

**Flutter** 앱에서 **LinearProgressIndicator**를 사용하여 화면 로딩 진행률을 표시하는 방법에 대해 알아보았습니다. 사용자에게 작업이 진행 중임을 시각적으로 전달하고, 작업의 실제 진행률을 업데이트하는 방법에 대해 배웠습니다. **LinearProgressIndicator**를 적절히 활용하여 사용자 경험을 향상시킬 수 있습니다.

참고: [Flutter 공식 문서](https://flutter.dev/docs/development/ui/widgets/material#LinearProgressIndicator)