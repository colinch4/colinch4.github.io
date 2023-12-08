---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 ColorTween 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 애플리케이션을 개발할 때 UI 요소를 부드럽게 변환시키는 데 많은 영향을 미치는 것 중 하나는 애니메이션입니다. **AnimatedContainer** 위젯은 UI 요소의 크기, 모양, 위치, 색상 등을 부드럽게 변경할 수 있도록 도와줍니다. 이 때 **ColorTween** 클래스를 함께 사용하여 색상을 부드럽게 변환할 수 있습니다.

## ColorTween이란?

**ColorTween**은 시작 색상과 종료 색상을 지정하고, 이러한 색상들 간의 부드러운 전환을 제공하는 클래스입니다. 이를 사용하면 애니메이션의 시작과 종료 지점 사이를 부드럽게 이동하면서 색상을 변환할 수 있습니다.

예를 들어, `ColorTween(begin: Colors.red, end: Colors.blue)`를 사용하여 빨간색에서 파란색으로의 부드러운 색상 전환을 정의할 수 있습니다.

## AnimatedContainer와 ColorTween 함께 사용하기

다음은 **AnimatedContainer**와 **ColorTween**을 함께 사용하여 부드러운 색상 변환 효과를 적용하는 예제입니다.

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
  bool _isBlue = false;

  void _changeColor() {
    setState(() {
      _isBlue = !_isBlue;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedContainer with ColorTween'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: _changeColor,
          child: AnimatedContainer(
            duration: Duration(seconds: 1),
            width: 200,
            height: 200,
            color: _isBlue ? Colors.blue : Colors.red,
            curve: Curves.ease,
          ),
        ),
      ),
    );
  }
}
```

위 예제에서 **AnimatedContainer**는 `color` 속성에 `_isBlue` 변수에 따라 빨간색 또는 파란색을 표시하도록 정의되어 있습니다. 이때 **ColorTween**을 사용하지 않으면 색상 전환이 순간적으로 일어날 것입니다. 하지만 **AnimatedContainer**와 함께 **ColorTween**을 사용하면 색상 전환 효과가 부드럽게 나타납니다.

**ColorTween**은 애니메이션의 시작과 종료 색상을 지정하는 데 유용합니다.

부드러운 색상 전환 효과를 적용할 때 **AnimatedContainer**와 **ColorTween**을 함께 사용하여 사용자 경험을 개선할 수 있습니다.

## 요약

**ColorTween** 클래스는 UI 요소의 색상을 부드럽게 변환하는 데 사용될 수 있으며, **AnimatedContainer**와 함께 사용하여 색상 전환 애니메이션 효과를 부드럽게 만들 수 있습니다. Flutter 앱의 UI 요소를 부드럽게 변경하고 사용자 경험을 향상시키기 위해 **AnimatedContainer**와 **ColorTween**을 적극적으로 활용해보세요.

[Flutter 공식 문서 - ColorTween](https://api.flutter.dev/flutter/material/ColorTween-class.html)
[Flutter 공식 문서 - AnimatedContainer](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)