---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 앱 초기화 절차 진행 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

앱을 초기화하는 동안 사용자에게 초기화 절차가 진행 중임을 알리는 것은 중요합니다. **LinearProgressIndicator** 위젯을 사용하여 초기화 상태를 시각적으로 표시할 수 있습니다. 이 글에서는 **flutter** 앱에서 **LinearProgressIndicator**를 사용하여 초기화 절차를 표시하는 방법에 대해 알아보겠습니다.

## 코드 예시

먼저, **LinearProgressIndicator**를 사용하여 초기화 절차를 표시하는 간단한 예시 코드를 살펴봅시다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SplashScreen(),
    );
  }
}

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  bool _isInitializing = true;

  @override
  void initState() {
    super.initState();
    _initializeApp(); // 앱 초기화 함수 호출
  }

  // 앱 초기화 함수
  Future<void> _initializeApp() async {
    // 앱 초기화 작업 수행
    // ...

    setState(() {
      _isInitializing = false; // 초기화 완료 시 상태 변경
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('App Initialization'),
      ),
      body: Center(
        child: _isInitializing
            ? LinearProgressIndicator() // 초기화 중일 때 프로그레스 바 표시
            : Text('Initialization completed'), // 초기화 완료 후 메시지 표시
      ),
    );
  }
}
```

## 설명

위 예시 코드는 **flutter**에서 **LinearProgressIndicator**를 사용하여 앱 초기화 진행 상태를 표시하는 방법을 보여줍니다. **SplashScreen** 위젯의 상태를 사용하여 초기화 중인지 여부를 추적하고, **_isInitializing** 상태에 따라 **LinearProgressIndicator** 또는 초기화 완료 메시지를 보여줍니다.

## 결론

이 글에서는 **flutter** 앱에서 **LinearProgressIndicator**를 사용하여 앱 초기화 절차를 진행 상태를 표시하는 방법에 대해 알아보았습니다. 이를 통해 사용자가 초기화 작업이 진행 중인지를 명확히 알리고, 사용자 경험을 향상시킬 수 있습니다.

더 많은 정보를 원하시면 [공식 **flutter** 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.