---
layout: post
title: "[flutter] CircularProgressIndicator를 이용하여 간단한 타이머를 구현하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

타이머를 구현할 때 `CircularProgressIndicator`를 사용하여 UI에 시간 흐름을 표시할 수 있습니다. 이 글에서는 Flutter를 사용하여 간단한 타이머를 구현하는 방법을 알아보겠습니다.

## 필요한 패키지 설치

먼저, `flutter/material.dart` 패키지를 설치해야 합니다. 아래와 같이 `pubspec.yaml` 파일에 패키지를 추가하고 `flutter pub get` 명령을 실행하여 패키지를 설치하세요.

```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
```

## 타이머 구현

다음으로, 타이머를 구현하기 위해 `StatefulWidget`을 사용하고, `CircularProgressIndicator`를 이용하여 시간을 표시합니다. 아래는 간단한 타이머 구현 예제입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(TimerApp());
}

class TimerApp extends StatefulWidget {
  @override
  _TimerAppState createState() => _TimerAppState();
}

class _TimerAppState extends State<TimerApp> with TickerProviderStateMixin {
  AnimationController _controller;
  int _timerDuration = 10;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(seconds: _timerDuration),
    )..reverse(from: _timerDuration.toDouble());
    _controller.addListener(() {
      setState(() {});
    });
    _controller.addStatusListener((status) {
      if (status == AnimationStatus.dismissed) {
        // 타이머 종료 시 동작
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('타이머')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              CircularProgressIndicator(
                value: _controller.value,
                backgroundColor: Colors.grey,
                valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
              ),
              SizedBox(height: 20),
              Text('${(_controller.value * _timerDuration).round()} 초'),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

위 예제에서 `_controller`를 사용하여 타이머 시간을 표시하고, `_timerDuration` 변수에 원하는 시간을 설정할 수 있습니다. 타이머 종료 시 원하는 동작을 수행하도록 `_controller.addStatusListener`를 사용할 수 있습니다.

위의 예제를 실행하면 `CircularProgressIndicator`가 타이머와 함께 움직이는 것을 확인할 수 있습니다.

이제 여러분도 `CircularProgressIndicator`를 활용하여 Flutter에서 간단한 타이머를 만들 수 있을 것입니다! 만약 추가 질문이 있거나 더 도움이 필요하시다면 언제든지 물어주세요.

## 참고 자료
- Flutter 공식 문서: https://flutter.dev/docs
- Flutter Timer 예제: https://api.flutter.dev/flutter/widgets/AnimatedBuilder-class.html