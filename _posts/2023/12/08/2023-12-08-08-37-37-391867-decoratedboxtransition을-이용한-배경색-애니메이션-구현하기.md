---
layout: post
title: "[flutter] DecoratedBoxTransition을 이용한 배경색 애니메이션 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter에서는 애니메이션을 쉽게 구현할 수 있는데, DecoratedBoxTransition을 이용하여 화면의 배경색을 부드럽게 바꾸는 애니메이션을 구현할 수 있습니다. 이번 글에서는 DecoratedBoxTransition을 이용하여 배경색 애니메이션을 만드는 방법에 대해 알아보겠습니다.

## DecoratedBoxTransition이란?

DecoratedBoxTransition은 Flutter의 애니메이션 위젯 중 하나로, DecoratedBox의 속성을 애니메이션화 시켜주는 위젯입니다. 이를 통해 배경색, 테두리 및 그림자 등을 애니메이션으로 변경할 수 있습니다.

## 배경색 애니메이션 구현하기

다음은 DecoratedBoxTransition을 이용하여 배경색 애니메이션을 구현하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<Color?> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(seconds: 2),
    )..repeat(reverse: true);
    _animation = ColorTween(begin: Colors.blue, end: Colors.green).animate(_controller);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: AnimatedBuilder(
          animation: _animation,
          builder: (ctx, child) {
            return DecoratedBoxTransition(
              position: DecorationPosition.background,
              decoration: BoxDecoration(color: _animation.value),
              child: child,
            );
          },
          child: const SizedBox.expand(),
        ),
      ),
    );
  }
}
```

위의 코드는 `DecoratedBoxTransition`과 `ColorTween`을 사용하여 배경색을 부드럽게 애니메이션화하는 방법을 보여줍니다.

## 마무리

이번 글에서는 DecoratedBoxTransition을 활용하여 배경색 애니메이션을 구현하는 방법에 대해 알아보았습니다. DecoratedBoxTransition을 이용하면 간단한 코드로 화면의 배경을 아름답게 변화시킬 수 있습니다. Flutter에서 애니메이션을 다룰 때 이러한 기술을 활용하면 UI에 다채로운 효과를 줄 수 있습니다.

더 많은 내용은 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.