---
layout: post
title: "[flutter] 플러터에서 useAnimationController 훅(hook)을 사용한 애니메이션 제어"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서 `useAnimationController` 훅을 사용하면 애니메이션을 쉽게 제어할 수 있습니다. 이 훅을 사용하면 애니메이션 컨트롤러를 만들고 초기화할 필요 없이 플러터 위젯에서 애니메이션을 쉽게 제어할 수 있습니다.

## useAnimationController란?

`useAnimationController`는 플러터 훅(Hooks) 라이브러리의 일부로, 애니메이션을 제어하기 위한 컨트롤러를 생성하는 역할을 합니다. 이를 사용하면 애니메이션의 duration(지속 시간) 및 애니메이션을 제어할 수 있는 여러 가지 속성을 쉽게 설정할 수 있습니다.

## 예시

다음은 `useAnimationController`를 사용하여 간단한 애니메이션을 제어하는 예제입니다.

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
      duration: Duration(seconds: 2),
    );

    return Scaffold(
      appBar: AppBar(
        title: Text('Animation Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            RotationTransition(
              turns: Tween(begin: 0.0, end: 1.0).animate(controller),
              child: Container(
                width: 200,
                height: 200,
                color: Colors.blue,
              ),
            ),
            SizedBox(
              height: 20,
            ),
            RaisedButton(
              onPressed: () {
                if (controller.isCompleted) {
                  controller.reverse();
                } else {
                  controller.forward();
                }
              },
              child: Text('Animate'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위 예제는 간단한 회전 애니메이션을 적용한 예제입니다. `useAnimationController`를 사용하여 `AnimationController`를 만들고, `RotationTransition`을 사용하여 애니메이션을 적용한 후 버튼을 눌러 애니메이션을 제어할 수 있습니다.

## 결론

`useAnimationController` 훅을 사용하면 플러터 애니메이션을 쉽게 제어할 수 있습니다. 이를 통해 더 많은 사용자 상호 작용 및 동적인 UI를 구현하는 데 도움이 될 것입니다.

참고 문헌:
- https://flutter.dev/docs/development/ui/animations
- https://pub.dev/packages/flutter_hooks

**수정사항:** 
- 플러터(Flutter)의 설명에 대한 문장을 추가하였습니다.
- 회전 애니메이션을 적용한 예제 코드를 추가하고, 해당 코드의 동작 방식을 설명하였습니다.