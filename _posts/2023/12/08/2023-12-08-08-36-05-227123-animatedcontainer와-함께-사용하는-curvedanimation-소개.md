---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 CurvedAnimation 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱에서 애니메이션을 추가하는 것은 사용자 경험을 향상시키는 데 중요합니다. `AnimatedContainer`와 `CurvedAnimation`을 함께 사용하면 스무스한 애니메이션을 쉽게 구현할 수 있습니다. 이 포스트에서는 `AnimatedContainer`를 사용하는 방법과 `CurvedAnimation`을 통해 애니메이션을 조절하는 방법에 대해 알아보겠습니다.

## AnimatedContainer 개요

`AnimatedContainer`는 Flutter에서 UI 요소의 크기, 위치 또는 속성을 바꿀 때 애니메이션을 적용하는 데 사용됩니다. 자식 위젯을 래핑하여 속성이 변경될 때 자동으로 애니메이션을 적용합니다.

다음은 `AnimatedContainer`의 간단한 예제입니다.

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

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedContainer Example'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () {
            setState(() {
              _width = _width == 200.0 ? 100.0 : 200.0;
            });
          },
          child: AnimatedContainer(
            width: _width,
            height: 100.0,
            color: Colors.blue,
            duration: Duration(seconds: 1),
            curve: Curves.fastOutSlowIn,
          ),
        ),
      ),
    );
  }
}
```

위의 예제에서는 `AnimatedContainer`를 사용하여 너비가 변경될 때 애니메이션을 적용했습니다.

## CurvedAnimation 소개

`CurvedAnimation`은 `Animation` 객체를 인자로 받아서 세밀한 애니메이션 효과를 주는 데 사용됩니다. `Curves` 클래스에서 제공되는 곡선 중 하나를 선택하여 애니메이션을 조절할 수 있습니다.

다음은 `CurvedAnimation`을 사용하여 `AnimatedContainer`의 애니메이션을 조절하는 간단한 예제입니다.

```dart
AnimationController _controller;
Animation<double> _animation;

@override
void initState() {
  super.initState();
  _controller = AnimationController(
    duration: const Duration(seconds: 2),
    vsync: this,
  );
  _animation = CurvedAnimation(
    parent: _controller,
    curve: Curves.easeInOut,
  );
  _controller.forward();
}
```

`CurvedAnimation`을 사용하면 `AnimatedContainer`의 애니메이션을 세부적으로 제어할 수 있습니다. 선택 가능한 곡선은 `Curves` 클래스를 통해 확인할 수 있습니다.

애니메이션을 통해 사용자 경험을 향상시키는 데는 다양한 방법이 있지만, `AnimatedContainer`와 `CurvedAnimation`을 함께 사용하는 것은 강력한 선택지입니다.

이제 앱에 스무스한 애니메이션을 추가할 때 `AnimatedContainer`와 `CurvedAnimation`을 사용해보세요!

참고 자료: [Flutter 공식 문서](https://flutter.dev/docs)