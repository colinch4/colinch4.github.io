---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션의 초기화 진행 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 애플리케이션에서 초기화 단계를 진행하면서 사용자에게 진행 상태를 표시할 수 있습니다. 이를 위해 `CircularProgressIndicator` 위젯을 사용하여 간단하게 진행바를 표시할 수 있습니다.

### 1. CircularProgressIndicator 추가하기

```dart
import 'package:flutter/material.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Initialization Progress'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text('Initializing...'),
              SizedBox(height: 16),
              CircularProgressIndicator(), // CircularProgressIndicator 추가
            ],
          ),
        ),
      ),
    );
  }
}
```

### 2. CircularProgressIndicator 옵션 지정하기

`CircularProgressIndicator`는 여러 옵션을 지정하여 스타일을 수정할 수 있습니다. 예를 들어, 색상, 두께, 진행바의 상태 등을 조절할 수 있습니다. 

```dart
CircularProgressIndicator(
  value: _progress, // 진행 상태 표시 (0.0부터 1.0까지)
  backgroundColor: Colors.grey, // 배경색상 지정
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue), // 진행 바의 색상 지정
  strokeWidth: 5, // 진행 바의 두께 지정
)
```

### 3. 초기화 코드와 함께 사용하기

실제로 애플리케이션이 초기화되는 과정에서 `CircularProgressIndicator`를 활용할 수 있습니다. 예를 들어, 데이터를 받아오거나 API 호출을 하는 등의 작업이 초기화 과정에 있을 때 해당 부분에 `CircularProgressIndicator`를 추가하여 사용자에게 진행 상태를 시각적으로 표시할 수 있습니다.

Flutter에서는 `FutureBuilder`를 사용하여 비동기로 초기화 작업을 수행하고 그 결과에 따라 `CircularProgressIndicator`를 표시할 수도 있습니다.

애플리케이션의 초기화를 보다 사용자 친화적으로 만들기 위해 `CircularProgressIndicator`를 적절히 활용하여 진행 상태를 표시해보세요.

### 참고 자료
- Flutter 공식 문서: [CircularProgressIndicator 클래스](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)
- Flutter 공식 문서: [FutureBuilder 클래스](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html)