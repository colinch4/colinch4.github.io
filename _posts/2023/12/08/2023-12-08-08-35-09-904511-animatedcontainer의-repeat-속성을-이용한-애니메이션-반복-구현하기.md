---
layout: post
title: "[flutter] AnimatedContainer의 repeat 속성을 이용한 애니메이션 반복 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter는 다양한 애니메이션을 편리하게 구현할 수 있는 많은 기능을 제공합니다. 그 중에서 AnimatedContainer 위젯은 애니메이션을 쉽게 적용할 수 있고, repeat 속성을 이용하여 애니메이션을 반복할 수도 있습니다.

이 블로그 포스트에서는 **AnimatedContainer의 repeat 속성을 이용한 애니메이션 반복 구현**에 대해 알아보겠습니다.

## AnimatedContainer의 repeat 속성

**AnimatedContainer**는 컨테이너의 속성을 변경할 때 부드러운 애니메이션 효과를 제공하는 위젯입니다. **repeat** 속성을 이용하면 애니메이션이 반복되도록 설정할 수 있습니다.

## 애니메이션 반복 구현하기

다음은 **AnimatedContainer**를 이용하여 반복 애니메이션을 구현하는 간단한 예제입니다.

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

class _MyHomePageState extends State<MyHomePage> {
  double _containerWidth = 50;
  Color _containerColor = Colors.blue;

  void _changeContainer() {
    setState(() {
      _containerWidth = _containerWidth == 50 ? 200 : 50;
      _containerColor = _containerColor == Colors.blue ? Colors.red : Colors.blue;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedContainer Repeat 예제'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () {
            _changeContainer();
          },
          child: AnimatedContainer(
            width: _containerWidth,
            height: 50,
            color: _containerColor,
            duration: Duration(seconds: 1),
            curve: Curves.easeInOut,
            repeat: true, // repeat 속성을 이용하여 애니메이션 반복 설정
          ),
        ),
      ),
    );
  }
}
```

위 예제에서는 터치 이벤트에 따라 애니메이션이 반복되도록 설정하였습니다.

## 결론

Flutter의 **AnimatedContainer**를 이용하여 애니메이션을 반복하려면 간단히 **repeat** 속성을 설정하면 됩니다. 이를 통해 애니메이션이 부드럽게 반복되는 사용자 경험을 제공할 수 있습니다.

더 많은 자세한 정보는 [공식 문서](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)를 참고할 수 있습니다.

이제 **AnimatedContainer의 repeat 속성을 이용한 애니메이션 반복 구현**에 대해 알아보았습니다. 감사합니다!