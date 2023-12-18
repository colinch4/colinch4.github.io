---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 네트워크 요청 진행률 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱에서 네트워크 요청을 처리할 때 사용자에게 진행 상태를 시각적으로 보여주는 것은 중요합니다. 이를 위해 `LinearProgressIndicator` 위젯을 사용하여 네트워크 요청 진행률을 실시간으로 표시할 수 있습니다.

## 1. LinearProgressIndicator 추가

우선, 네트워크 요청을 처리하는 화면의 `build` 메서드 안에서 `LinearProgressIndicator`를 추가합니다.

```dart
import 'package:flutter/material.dart';

class MyNetworkRequestWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('네트워크 요청 처리'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('네트워크 요청 진행 중...'),
            LinearProgressIndicator(), // 진행률 표시 위젯 추가
          ],
        ),
      ),
    );
  }
}
```

## 2. 네트워크 요청과 함께 LinearProgressIndicator 사용

이제 네트워크 요청을 보내는 메서드 내에서 `setState`를 사용하여 `LinearProgressIndicator`가 표시되도록 설정합니다.

```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class MyNetworkRequestWidget extends StatefulWidget {
  @override
  _MyNetworkRequestWidgetState createState() => _MyNetworkRequestWidgetState();
}

class _MyNetworkRequestWidgetState extends State<MyNetworkRequestWidget> {
  bool _isLoading = false; // 네트워크 요청 진행 여부 상태 변수

  Future<void> _makeNetworkRequest() async {
    setState(() {
      _isLoading = true; // 네트워크 요청 시작 시 진행 상태를 보여주기 위해 상태 변경
    });

    try {
      // 네트워크 요청 로직 작성
      var response = await http.get('https://api.example.com/data');
      // 요청 완료 후 진행 상태 감춤
      setState(() {
        _isLoading = false;
      });
    } catch (e) {
      // 에러 처리 로직
      // 진행 상태 감춤
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('네트워크 요청 처리'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('네트워크 요청 진행 중...'),
            if (_isLoading) // 진행 상태에 따라 LinearProgressIndicator 표시 여부 조건 추가
              LinearProgressIndicator(), // 진행률 표시 위젯 추가
            ElevatedButton(
              onPressed: _makeNetworkRequest,
              child: Text('네트워크 요청 시작'),
            ),
          ],
        ),
      ),
    );
  }
}
```

이렇게 하면 네트워크 요청이 진행 중일 때는 진행률 표시가 나타나고, 요청이 완료되면 표시가 사라지게 됩니다.

이상으로 `LinearProgressIndicator`를 사용하여 Flutter 앱에서 네트워크 요청 진행률을 표시하는 방법에 대해 알아보았습니다.

참고 문서: [Flutter - LinearProgressIndicator class](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)