---
layout: post
title: "[flutter] CircularProgressIndicator의 사용자 정의 애니메이션을 만드는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter의 CircularProgressIndicator는 기본적으로 반시계 방향으로 회전하는 기본 애니메이션을 제공합니다. 하지만 때때로 이 기본 애니메이션이 아닌 **사용자 정의 애니메이션**을 만들어야 할 때가 있습니다. 사용자 정의 애니메이션을 만들기 위해서는 다음과 같은 단계를 따를 수 있습니다.

## 1. `CustomPainter` 클래스 생성
먼저 사용자 정의 애니메이션을 만들기 위해 `CustomPainter` 클래스를 생성해야 합니다. 이 클래스는 그래픽을 그리는 데 사용됩니다. 아래는 간단한 예시 코드입니다.
```dart
import 'package:flutter/material.dart';
import 'dart:math' as math;

class CustomProgressPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.blue
      ..strokeWidth = 5
      ..strokeCap = StrokeCap.round
      ..style = PaintingStyle.stroke;

    canvas.drawArc(
        Rect.fromLTWH(0, 0, size.width, size.height),
        math.pi * 1.5,
        math.pi * 2,
        false,
        paint);
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
```

## 2. `CustomProgressPainter`를 사용하여 CircularProgressIndicator 만들기
다음으로, 앞서 만든 `CustomPainter` 클래스를 이용하여 CircularProgressIndicator를 만들어야 합니다. 아래의 예시 코드는 `CustomProgressPainter`를 사용하여 Circular Custom Indicator를 만드는 방법을 보여줍니다.
```dart
class CustomProgressIndicator extends StatefulWidget {
  @override
  _CustomProgressIndicatorState createState() => _CustomProgressIndicatorState();
}

class _CustomProgressIndicatorState extends State<CustomProgressIndicator>
    with SingleTickerProviderStateMixin {
  AnimationController _animationController;

  @override
  void initState() {
    _animationController = AnimationController(
        vsync: this, duration: Duration(seconds: 1));
    _animationController.repeat();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: CustomPaint(
        size: Size(50, 50),
        painter: CustomProgressPainter(_animationController.value),
      ),
    );
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }
}
```

위의 코드에서 `CustomPaint` 위젯을 사용하여 사용자 정의 애니메이션을 적용할 수 있습니다.

## 마치며
이제 위에서 설명한 단계에 따라 사용자 정의 애니메이션을 만들 수 있습니다. **CustomPainter** 클래스를 사용하여 그래픽을 그리고, **CustomPaint** 위젯을 사용하여 CircularProgressIndicator 위젯에 사용자 정의 애니메이션을 적용합니다.

더 많은 자세한 내용은 [Flutter 공식 문서](https://flutter.dev/docs)를 참고해주세요.