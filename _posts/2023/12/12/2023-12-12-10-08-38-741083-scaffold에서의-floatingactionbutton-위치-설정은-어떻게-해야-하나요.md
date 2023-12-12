---
layout: post
title: "[flutter] Scaffold에서의 floatingActionButton 위치 설정은 어떻게 해야 하나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

일반적으로 Scaffold 위젯은 MaterialApp이나 CupertinoApp의 body 속성에 사용되며, 화면의 기본 구조를 정의합니다. Scaffold 위젯 내에서 floatingActionButton의 위치를 설정하려면 floatingActionButton 속성을 사용합니다.

예를 들어, Scaffold의 floatingActionButton 속성에 FloatingActionButton 위젯을 지정하고, FloatingActionButton의 위치를 변경하려면 Scaffold의 floatingActionButtonLocation 속성을 사용하여 위치를 지정할 수 있습니다.

아래는 Scaffold 위젯을 사용하여 floatingActionButton를 화면 오른쪽 아래로 이동시키는 예제입니다.

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
          title: Text('FloatingActionButton 위치 설정'),
        ),
        body: Center(
          child: Text(
            '이것은 body입니다.',
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {},
          child: Icon(Icons.add),
        ),
        floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
      ),
    );
  }
}
```

이 코드에서는 Scaffold의 floatingActionButtonLocation 속성을 사용하여 endFloat로 설정하여 floatingActionButton를 오른쪽 아래로 이동시켰습니다.

위 예제와 같이 Scaffold 위젯에서 floatingActionButton의 위치를 조정하여 UI를 개선할 수 있습니다.

더 많은 세부 사항은 Flutter 공식 문서를 참조하시기 바랍니다:
- [Flutter 공식 문서 - Scaffold 클래스](https://api.flutter.dev/flutter/material/Scaffold-class.html)
- [Flutter 공식 문서 - FloatingActionButtonLocation 클래스](https://api.flutter.dev/flutter/material/FloatingActionButtonLocation-class.html)