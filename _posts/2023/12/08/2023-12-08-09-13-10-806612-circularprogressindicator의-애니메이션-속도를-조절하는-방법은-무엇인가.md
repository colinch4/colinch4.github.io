---
layout: post
title: "[flutter] CircularProgressIndicator의 애니메이션 속도를 조절하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with TickerProviderStateMixin {
  AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(seconds: 2), // 애니메이션 지속 시간 설정 
    )..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('CircularProgressIndicator 애니메이션 속도 조절'),
      ),
      body: Center(
        child: CircularProgressIndicator(
          valueColor: AlwaysStoppedAnimation<Color>(Colors.blue), // 진행 바 색상 설정
          backgroundColor: Colors.grey, // 배경 색상 설정
          value: _controller.value, // 애니메이션 컨트롤러 값 설정
        ),
      ),
    );
  }
}
```

이 코드는 `vsync`를 위한 `TickerProviderStateMixin`을 사용하여 `AnimationController`를 생성하고 지속 시간을 설정한 후 `repeat` 메소드를 호출하여 애니메이션을 반복하도록 합니다. 여기서 `CircularProgressIndicator`의 `valueColor` 속성을 이용하여 진행 바의 컬러를 설정하고, `value` 속성을 `AnimationController`의 값으로 설정하여 애니메이션을 제어합니다.

참고로, 위 코드에서는 `vsync`에 `TickerProviderStateMixin`을 사용하여 `AnimationController`를 초기화하도록 했으며, `initState`에서 `AnimationController`를 생성하고, `dispose`에서는 `AnimationController`의 자원을 해제하도록 했습니다.

이렇게 함으로써 `CircularProgressIndicator`의 애니메이션 속도를 조절할 수 있습니다.

더 자세한 정보는 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하세요.