---
layout: post
title: "[flutter] 플러터(Flutter)에서 동적인 UI 작성을 위해 useAnimatedValue Hook을 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서는 리액트 네이티브(React Native)와 비슷한 개념으로 **Hooks**를 제공합니다. Hooks를 사용하면 상태 관리와 같은 기능을 간편하게 처리할 수 있습니다. 이번에는 플러터에서 제공하는 **useAnimatedValue** Hook을 사용하여 동적인 UI를 작성하는 방법을 알아보겠습니다.

## useAnimatedValue Hook이란?

**useAnimatedValue** Hook은 애니메이션을 생성하기 위해 사용되는 Stateful 값입니다. 애니메이션을 제어하고 변환하는데 사용할 수 있습니다.

## useAnimatedValue Hook 사용 방법

다음은 useAnimatedValue Hook을 사용하여 동적인 UI를 작성하는 방법입니다.

```dart
import 'package:flutter/animation.dart';
import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';

class ExampleAnimationWidget extends HookConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final animationValue = ref.watch(animationProvider);

    return Scaffold(
      appBar: AppBar(
        title: Text('Animated Widget'),
      ),
      body: Center(
        child: AnimatedContainer(
          width: animationValue * 100, // 애니메이션 값에 따라 너비 조절
          height: animationValue * 100, // 애니메이션 값에 따라 높이 조절
          duration: Duration(milliseconds: 500), // 애니메이션 지속 시간
          color: Colors.blue,
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          if (animationValue >= 1.0) {
            ref.read(animationProvider.notifier).reset();
          } else {
            ref.read(animationProvider.notifier).animate();
          }
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}

final animationProvider = StateNotifierProvider<AnimationNotifier, double>((ref) {
  return AnimationNotifier();
});

class AnimationNotifier extends StateNotifier<double> {
  AnimationNotifier() : super(0.0);

  void animate() {
    state = 1.0; // 애니메이션 시작
  }

  void reset() {
    state = 0.0; // 애니메이션 초기화
  }
}
```

위 코드에서는 **useAnimatedValue** Hook을 사용하여 애니메이션 값을 생성합니다. 이 값은 `animationProvider`를 통해 공유됩니다. 애니메이션 값을 사용하여 `AnimatedContainer` 위젯의 너비와 높이를 조절하고, 애니메이션의 지속 시간을 설정합니다.

`floatingActionButton`의 `onPressed` 핸들러에서는 애니메이션 값이 1.0인지 확인한 후에 애니메이션을 시작하거나 초기화하는 `animate()` 메서드와 `reset()` 메서드를 호출합니다.

## 결론

이번에는 플러터에서 제공하는 **useAnimatedValue** Hook을 사용하여 동적인 UI를 작성하는 방법을 알아보았습니다. Hooks는 플러터 애플리케이션의 상태 관리를 더욱 편리하게 해주며, 애니메이션과 같이 동적인 UI를 구현할 때 유용하게 사용할 수 있습니다. 추가적으로 Hooks에 대해 더 알아보고 싶다면 [플러터 공식 문서](https://flutter.dev/docs/development/ui/widgets-intro)를 참고해주세요.