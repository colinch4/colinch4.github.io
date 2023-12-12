---
layout: post
title: "[flutter] 플러터 Scaffold에서 persistentFooterButtons를 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

먼저 Scaffold 위젯을 생성하고, scaffold의 persistentFooterButtons 속성 내에 ElevatedButton을 추가합니다. 아래는 예시 코드입니다:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Persistent Footer Buttons Example'),
      ),
      body: Center(
        child: Text('Add your content here'),
      ),
      persistentFooterButtons: <Widget>[
        ElevatedButton(
          onPressed: () {
            // Add your button 1 action here
          },
          child: Text('Button 1'),
        ),
        ElevatedButton(
          onPressed: () {
            // Add your button 2 action here
          },
          child: Text('Button 2'),
        ),
      ],
    );
  }
}
```

이 예시에서는 Scaffold의 persistentFooterButtons 속성을 사용하여 두 개의 ElevatedButton을 화면 하단에 추가하였습니다. 각 버튼을 누를 때 수행되는 액션을 정의하는 onPressed 콜백도 추가할 수 있습니다.

이와 유사하게, 여러 버튼을 추가하여 사용하거나 각 버튼에 아이콘을 추가하는 등 다양한 설정을 할 수 있습니다.

참고 자료:
- 플러터 위젯 카탈로그: https://flutter.dev/docs/development/ui/widgets
- Scaffold 클래스 문서: https://api.flutter.dev/flutter/material/Scaffold-class.html