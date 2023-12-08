---
layout: post
title: "[flutter] RelativePositionedTransition을 이용한 상대적 위치 이동 애니메이션 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

애니메이션은 모바일 앱의 사용자 경험을 향상시키는 데 중요한 부분입니다. Flutter에서 상대적 위치 이동 애니메이션을 구현하는 방법 중 하나는 `RelativePositionedTransition` 위젯을 사용하는 것입니다. `RelativePositionedTransition` 위젯은 부모 위젯의 상대적인 위치에 따라 자식 위젯을 이동시키는 데 사용됩니다.

## RelativePositionedTransition 개요

`RelativePositionedTransition` 위젯은 상대적인 위치에 따라 자식 위젯을 애니메이션으로 이동시킵니다. 이 위젯은 `Rect`를 사용하여 자식 위젯의 상대적 위치를 정의하고, 애니메이션을 적용할 수 있습니다. 

```dart
RelativePositionedTransition(
  rect: _animation.drive<Rect>(
    Tween<Rect>(
      begin: Rect.fromLTWH(0, 0, 100, 100),
      end: Rect.fromLTWH(100, 100, 100, 100),
    ),
  ),
  child: YourChildWidget(),
)
```

위 코드에서 `_animation`은 애니메이션을 정의하는 `Animation<Rect>` 객체를 나타냅니다. `Rect.fromLTWH` 메서드는 위치와 크기를 기반으로 하는 `Rect`를 생성하는 데 사용됩니다.

## RelativePositionedTransition 예제

다음은 `RelativePositionedTransition`을 사용하여 상대적 위치 이동 애니메이션을 구현하는 간단한 예제입니다. 화면 상에서 버튼을 누르면 상자가 이동하도록 만들어볼 것입니다.

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

class _MyHomePageState extends State<MyHomePage> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<Rect> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(seconds: 1),
      vsync: this,
    )..repeat(reverse: true);
    _animation = _controller.drive(
      RectTween(
        begin: Rect.fromLTWH(0, 0, 100, 100),
        end: Rect.fromLTWH(100, 100, 100, 100),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('RelativePositionedTransition 예제'),
      ),
      body: Center(
        child: Stack(
          children: <Widget>[
            RelativePositionedTransition(
              rect: _animation,
              child: Container(
                width: 100,
                height: 100,
                color: Colors.blue,
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

위 코드는 `RelativePositionedTransition`을 사용하여 상자를 이동시키는 간단한 예제를 보여줍니다. 상자는 `RectTween`을 이용하여 시작 위치와 끝 위치로 애니메이션 됩니다.

상대적 위치 이동 애니메이션을 더 많이 사용하고 싶다면, [Flutter 애니메이션 가이드](https://flutter.dev/docs/development/ui/animations)에서 더 많은 정보를 얻을 수 있습니다.

RelativePositionedTransition을 사용하면 상대적인 위치에 따라 자식 위젯을 부드럽게 이동시키는 애니메이션을 구현할 수 있습니다. 이를 활용하여 앱의 사용자 경험을 향상시키는 멋진 애니메이션을 만들어보세요.