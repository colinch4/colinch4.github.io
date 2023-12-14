---
layout: post
title: "[flutter] 플러터에서 useAnimationController 훅(hook)을 이용한 동적인 애니메이션"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터는 애니메이션을 쉽게 다룰 수 있도록 다양한 훅(Hook)을 제공합니다. 이 중 `useAnimationController` 훅을 이용하면 **동적인 애니메이션을 쉽게 작성**할 수 있습니다. 이번 글에서는 `useAnimationController` 훅을 사용하여 플러터에서 동적인 애니메이션을 구현하는 방법에 대해 살펴보겠습니다.

## 목차
- [useAnimationController 훅 소개](#useanimationcontroller-훅-소개)
- [동적인 애니메이션 구현하기](#동적인-애니메이션-구현하기)
- [결론](#결론)

---

## useAnimationController 훅 소개

`useAnimationController` 훅은 애니메이션의 컨트롤러를 생성하고 반환하며, 이를 통해 애니메이션의 상태를 관리할 수 있습니다. 또한, 훅을 사용하면 애니메이션의 상태 변경에 따라 UI가 자동으로 업데이트됩니다.

## 동적인 애니메이션 구현하기

먼저, `useAnimationController` 훅을 사용하여 애니메이션 컨트롤러를 생성합니다.

```dart
AnimationController _controller = useAnimationController(
  duration: Duration(seconds: 1),
  initialValue: 0,
  lowerBound: 0,
  upperBound: 1,
);
```

그 다음, 원하는 애니메이션을 작성합니다. 예를 들어, 위 코드에서 생성한 `_controller`를 이용하여 컨테이너의 크기를 애니메이션화하는 방법은 다음과 같습니다.

```dart
Widget build(BuildContext context) {
  return AnimatedBuilder(
    animation: _controller,
    builder: (context, child) {
      return Container(
        width: 100 * _controller.value,
        height: 100 * _controller.value,
        color: Colors.blue,
      );
    },
  );
}
```

위 코드에서 `AnimatedBuilder`를 이용하여 애니메이션을 쉽게 작성할 수 있습니다.

## 결론

`useAnimationController` 훅을 이용하면 **플러터에서 동적인 애니메이션을 간편하게 작성**할 수 있습니다. 이를 통해 사용자의 상호작용에 따라 다양한 애니메이션 효과를 쉽게 적용할 수 있습니다.

참조 링크: [flutter.dev - Animations](https://flutter.dev/docs/development/ui/animations)