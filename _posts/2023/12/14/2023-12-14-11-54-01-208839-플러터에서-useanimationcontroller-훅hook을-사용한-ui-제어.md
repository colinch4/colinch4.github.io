---
layout: post
title: "[flutter] 플러터에서 useAnimationController 훅(hook)을 사용한 UI 제어"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터 2.5부터 도입된 `useAnimationController` 훅은 애니메이션 컨트롤러를 훨씬 간단하게 관리할 수 있게 해준다. 기존의 애니메이션 처리 방식은 StatefulWidget과 SingleTickerProviderStateMixin 클래스를 사용하는 번거로운 방식이었다. `useAnimationController` 훅은 이러한 불편함을 해소하고 보다 간결한 코드로 애니메이션을 다룰 수 있게 해준다.

## useAnimationController 훅의 기본 사용법

`useAnimationController` 훅을 사용하려면 먼저 `flutter_hooks` 패키지를 프로젝트에 추가해야 한다. 프로젝트에 패키지를 추가한 후에는 다음과 같이 `useAnimationController` 훅을 사용할 수 있다.

```dart
final AnimationController animationController = useAnimationController(
  duration: Duration(seconds: 1),
  reverseDuration: Duration(seconds: 1),
  initialValue: 0.0,
  upperBound: 1.0,
  lowerBound: 0.0,
  debugLabel: 'MyAnimationController',
  animationBehavior: AnimationBehavior.normal,
);
```

위의 예제에서 `duration`은 애니메이션이 진행되는 시간을 나타내며, `initialValue`는 애니메이션 시작 값, `upperBound`와 `lowerBound`는 애니메이션의 상한선과 하한선을 나타낸다.

## 애니메이션 컨트롤러를 이용한 UI 제어

`useAnimationController` 훅을 사용하면 `AnimationController` 인스턴스를 손쉽게 제어하고 애니메이션을 다룰 수 있다. 아래는 간단한 버튼을 누를 때 애니메이션을 실행하는 예제다.

```dart
ElevatedButton(
  onPressed: () {
    if (animationController.status == AnimationStatus.completed) {
      animationController.reverse();
    } else {
      animationController.forward();
    }
  },
  child: Text('Animate'),
)
```

애니메이션 컨트롤러의 `forward` 메서드는 애니메이션을 시작하고, `reverse` 메서드는 애니메이션을 역재생한다. 애니메이션의 현재 상태를 확인하기 위해 `status` 속성을 사용하여 `completed` 상태인지 확인한 후 다음 동작을 결정할 수 있다.

## 결론

`useAnimationController` 훅은 플러터 애니메이션을 훨씬 더 쉽게 다룰 수 있게 해주는 강력한 도구이다. 이를 통해 코드의 가독성을 향상시키고 애니메이션을 더 효율적으로 관리할 수 있다. 앞으로의 플러터 앱 개발에서 `useAnimationController` 훅을 적극적으로 활용해보는 것을 권장한다.

**참고 문헌**  
[Flutter 공식 문서 - AnimationController](https://api.flutter.dev/flutter/animation/AnimationController-class.html)  
[Flutter 공식 문서 - flutter_hooks 패키지](https://pub.dev/packages/flutter_hooks)