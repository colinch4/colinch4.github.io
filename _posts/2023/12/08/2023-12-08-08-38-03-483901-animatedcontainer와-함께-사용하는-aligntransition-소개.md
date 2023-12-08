---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 AlignTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

## 목차
1. 개요
2. AnimatedContainer란?
3. AlignTransition란?
4. AnimatedContainer와 AlignTransition 함께 사용하기
5. 예제 코드
6. 결론

---

## 1. 개요
이번 글에서는 Flutter에서 UI 애니메이션을 구현할 때 유용하게 사용할 수 있는 `AnimatedContainer`와 함께 사용하는 `AlignTransition`에 대해 알아보겠습니다.

## 2. AnimatedContainer란?
`AnimatedContainer`는 자식 위젯의 사이즈나 속성을 부드럽게 애니메이션화해주는 위젯입니다. 이를 사용하면 속성을 변경할 때 초당 횟수로 자동으로 애니메이션됩니다.

## 3. AlignTransition란?
`AlignTransition`은 기존 상태와 애니메이션 상태 간의 정렬을 애니메이션화해주는 위젯입니다. AlignTransition은 Animation 객체를 통해 애니메이션을 제어할 수 있습니다.

## 4. AnimatedContainer와 AlignTransition 함께 사용하기
`AnimatedContainer`와 `AlignTransition`을 함께 사용하면 화면 상에서 위젯의 위치를 애니메이션화할 수 있습니다. 이를 통해 시각적으로 매끄러운 UI 변경을 구현할 수 있습니다.

## 5. 예제 코드
아래는 `AnimatedContainer`와 `AlignTransition`을 함께 사용하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class AlignTransitionExample extends StatefulWidget {
  @override
  _AlignTransitionExampleState createState() => _AlignTransitionExampleState();
}

class _AlignTransitionExampleState extends State<AlignTransitionExample>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<Alignment> _animation;

  @override
  void initState() {
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    );
    _animation = _controller.drive(
      AlignmentTween(
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
      ),
    );
    super.initState();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: AlignTransition(
        alignment: _animation,
        child: AnimatedContainer(
          width: 200,
          height: 200,
          color: Colors.blue,
          duration: Duration(seconds: 1),
        ),
      ),
    );
  }
}
```

## 6. 결론
이제 `AnimatedContainer`와 `AlignTransition`을 함께 사용하여 UI 애니메이션을 구현할 수 있는 방법에 대해 알아보았습니다. 이를 응용하여 다양한 애니메이션 효과를 구현할 수 있을 것입니다.

---

본문 작성자: [Flutter 공식 문서](https://flutter.dev/docs)