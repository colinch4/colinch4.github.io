---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 반복 작업 진행 상태 표시 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

이번 포스트에서는 `LinearProgressIndicator`를 사용하여 플러터(Flutter) 앱에서 반복 작업 진행 상태를 표시하는 방법에 대해 알아보겠습니다.

## 1. LinearProgressIndicator란?

`LinearProgressIndicator`는 플러터에서 진행 상태를 시각적으로 나타내기 위한 위젯으로, 사용자에게 작업이 진행 중임을 알려줄 수 있습니다. 주로 네트워크 요청, 파일 다운로드, 데이터 처리 등의 작업 진행 상태를 표시하는 데 사용됩니다.

## 2. 코드 예제

아래는 `LinearProgressIndicator`를 사용하여 반복 작업 진행 상태를 표시하는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class MyPage extends StatefulWidget {
  @override
  _MyPageState createState() => _MyPageState();
}

class _MyPageState extends State<MyPage> {
  bool _isLoading = false;

  void _startTask() {
    setState(() {
      _isLoading = true;
      // 여기에 반복 작업 코드를 추가합니다.
      // 예를 들어 Future.delayed나 비동기 작업을 시작할 수 있습니다.
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('LinearProgressIndicator 예제'),
      ),
      body: Center(
        child: _isLoading
            ? CircularProgressIndicator() // 로딩 상태일 때는 Circular 프로그레스 바를 표시합니다.
            : ElevatedButton(
                onPressed: _startTask,
                child: Text('작업 시작'),
              ),
      ),
    );
  }
}
```  

위의 코드에서 `_startTask` 함수에서 반복 작업을 시작하며, 그 사이에 `LinearProgressIndicator`를 표시하고 있습니다.

## 3. 결론

이렇게하면 사용자에게 작업이 진행 중임을 분명히 알려주고, 진행 상태를 시각적으로 표현하여 사용자 경험을 향상시킬 수 있습니다.

`LinearProgressIndicator`를 사용하여 플러터 앱에서 반복 작업 진행 상태를 표시하는 방법에 대해 알아보았습니다. 이제 여러분도 이를 활용하여 사용자에게 진행 상태를 보다 명확하게 전달할 수 있을 것입니다.