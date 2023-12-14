---
layout: post
title: "[flutter] 플러터에서 useAnimationController 훅(hook)을 이용한 동적인 UI 효과"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터에서 UI를 동적으로 제어하기 위해서는 AnimationController를 사용하여 애니메이션을 작성하고, 애니메이션 상태를 관리해야 합니다. 최근 버전의 플러터에서는 **useAnimationController** 훅을 사용하여 더욱 간편하게 AnimationController를 만들고 관리할 수 있습니다.
UseAnimationController 훅은 **flutter_hooks** 패키지를 포함하고 있으며, **hookConsumer** 또는 **hookWidget**을 통해 사용할 수 있습니다.

## useAnimationController 훅 사용하기

useAnimationController 훅을 사용하려면 다음 단계를 따르면 됩니다.

1. flutter_hooks 패키지를 종속성으로 추가합니다.

```yaml
dependencies:
  flutter_hooks: ^0.18.0
```

2. 코드에서 useAnimationController를 import 합니다.

```dart
import 'package:flutter_hooks/flutter_hooks.dart';
```

3. useAnimationController 훅을 이용하여 AnimationController를 만듭니다.

```dart
final AnimationController animationController = useAnimationController(
  duration: Duration(seconds: 1),
);
```

## 예제

다음은 useAnimationController 훅을 사용하여 버튼을 클릭했을 때, 상자가 회전하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final AnimationController controller = useAnimationController(
      duration: Duration(milliseconds: 500),
      reverseDuration: Duration(milliseconds: 500),
    );

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Animation Example'),
        ),
        body: Center(
          child: RotationTransition(
            turns: Tween(begin: 0.0, end: 1.0).animate(controller),
            child: Container(
              width: 200,
              height: 200,
              color: Colors.blue,
            ),
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            if (!controller.isAnimating) {
              controller.forward();
            } else {
              controller.reverse();
            }
          },
          child: Icon(Icons.play_arrow),
        ),
      ),
    );
  }
}
```

위 코드를 실행하면 "play" 아이콘 버튼을 클릭할 때 마다 파란색 상자가 회전하게 됩니다.

이렇게 useAnimationController 훅을 사용하여 AnimationController를 통해 동적인 UI 효과를 간단히 구현할 수 있습니다.

## 마무리

이번 글에서는 플러터에서 useAnimationController 훅을 이용하여 동적인 UI 효과를 구현하는 방법에 대해 살펴보았습니다. useAnimationController 훅을 통해 AnimationController를 훨씬 간편하게 사용할 수 있으며, 애니메이션 기능을 더욱 쉽게 활용할 수 있습니다.