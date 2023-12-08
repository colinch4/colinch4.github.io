---
layout: post
title: "[flutter] AnimatedContainer와 AnimatedBuilder를 함께 사용한 복합적인 애니메이션 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter에서 애니메이션을 구현할 때 `AnimatedContainer`와 `AnimatedBuilder`를 함께 사용하여 다양하고 복합적인 애니메이션을 구현할 수 있습니다. 이 블로그 포스트에서는 두 가지 위젯을 함께 사용하여 간단한 예제를 통해 복합적인 애니메이션을 어떻게 구현하는지 살펴보겠습니다.

## 목차
- [AnimatedContainer란?](#animatedcontainer란)
- [AnimatedBuilder란?](#animatedbuilder란)
- [AnimatedContainer와 AnimatedBuilder를 함께 사용하기](#animatedcontainer와-animatedbuilder를-함께-사용하기)
- [예제: 크기와 투명도 애니메이션](#예제:-크기와-투명도-애니메이션)
- [결론](#결론)

## AnimatedContainer란?

`AnimatedContainer` 위젯은 자체적으로 애니메이션을 처리할 수 있는 위젯입니다. 크기, 색상, 모양 및 위치 등을 애니메이션화하는 데 사용됩니다. 상태가 변경될 때 속성을 부드럽게 변화시키는 방식으로 애니메이션을 처리합니다.

## AnimatedBuilder란?

`AnimatedBuilder`는 `Animation` 객체를 이용하여 애니메이션을 직접 제어할 수 있는 위젯입니다. `AnimatedContainer`와는 달리 애니메이션의 상태에 대한 직접적인 제어를 할 수 있어 더 많은 유연성을 제공합니다.

## AnimatedContainer와 AnimatedBuilder를 함께 사용하기

`AnimatedContainer`는 위젯이 자체적으로 애니메이션을 처리할 수 있지만, 복합적인 애니메이션을 구현하려면 `AnimatedBuilder`와 함께 사용하는 것이 효과적입니다. `AnimatedBuilder`를 사용하면 커스텀한 애니메이션을 만들 수 있으며, `AnimatedContainer`와 조합하여 더 다양한 효과를 생성할 수 있습니다.

## 예제: 크기와 투명도 애니메이션

아래 예제는 `AnimatedContainer`와 `AnimatedBuilder`를 함께 사용하여 크기와 투명도를 애니메이션화하는 간단한 예제입니다.

```dart
import 'package:flutter/material.dart';

class AnimatedExample extends StatefulWidget {
  @override
  _AnimatedExampleState createState() => _AnimatedExampleState();
}

class _AnimatedExampleState extends State<AnimatedExample>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _sizeAnimation;
  late Animation<double> _opacityAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    );
    _sizeAnimation = Tween<double>(begin: 100.0, end: 200.0).animate(_controller);
    _opacityAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(_controller);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: AnimatedBuilder(
          animation: _controller,
          builder: (context, child) {
            return AnimatedContainer(
              duration: Duration(seconds: 1),
              width: _sizeAnimation.value,
              height: _sizeAnimation.value,
              color: Colors.blue,
              child: Opacity(
                opacity: _opacityAnimation.value,
                child: child,
              ),
            );
          },
          child: Text('Hello, Flutter!'),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          if (_controller.isCompleted) {
            _controller.reverse();
          } else {
            _controller.forward();
          }
        },
        child: Icon(Icons.play_arrow),
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

위 예제에서는 `AnimatedContainer`와 `AnimatedBuilder`를 함께 사용하여 애니메이션을 구현했습니다. `AnimatedContainer`는 크기를 애니메이션화하고, `AnimatedBuilder`는 투명도를 애니메이션화했습니다.

## 결론

`AnimatedContainer`와 `AnimatedBuilder`는 Flutter에서 다양하고 복합적인 애니메이션을 구현하는 데 유용한 도구입니다. 두 가지 위젯을 조합하여 복잡한 애니메이션을 구현할 수 있으며, 유연하고 화려한 UI를 구축하는 데 도움이 됩니다. 복합적인 애니메이션을 구현할 때는 두 위젯을 함께 사용하여 원하는 효과를 쉽게 달성할 수 있습니다.

이러한 방법들은 Flutter의 다양한 화면 전환이나 UI/UX 구현에 응용될 수 있으며, 효율적인 사용자 경험을 구현하는데 큰 도움이 됩니다.

참고문헌:
- Flutter AnimatedContainer: https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html
- Flutter AnimatedBuilder: https://api.flutter.dev/flutter/widgets/AnimatedBuilder-class.html