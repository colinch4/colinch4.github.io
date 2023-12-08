---
layout: post
title: "[flutter] CircularProgressIndicator의 애니메이션 속도를 느리게 조절하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

먼저, `CircularProgressIndicator` 위젯을 느리게 회전하도록 애니메이션을 커스터마이즈해보겠습니다. 

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Slow CircularProgressIndicator Animation'),
        ),
        body: Center(
          child: CircularProgressIndicator(
            strokeWidth: 5, // 원의 두께
            valueColor: AlwaysStoppedAnimation<Color>(Colors.blue), // 애니메이션 색상
            backgroundColor: Colors.grey, // 배경색상
          ),
        ),
      ),
    );
  }
}
```

`valueColor`는 `AlwaysStoppedAnimation<Color>`을 사용하여 애니메이션 색상을 지정할 수 있으며, `backgroundColor`는 배경색을 지정합니다. 위의 코드에서 `CircularProgressIndicator`의 `valueColor`와 `backgroundColor` 속성을 적절히 조절하여 애니메이션을 커스터마이즈할 수 있습니다.

Flutter 공식 문서에 자세한 내용이 있으니 참고하시기 바랍니다:
- [Flutter 공식 문서 - CircularProgressIndicator](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)