---
layout: post
title: "[flutter] TweenAnimationBuilder와 함께 사용하는 Tween 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter의 애니메이션을 만들 때 `Tween`은 매우 유용합니다. `Tween`을 사용하면 시작 값과 끝 값 사이를 보간(interpolate)하여 원하는 범위의 값을 생성할 수 있습니다. 이 포스트에서는 `TweenAnimationBuilder`와 함께 사용하는 `Tween`에 대해 알아보겠습니다.

## 1. Tween이란?

`Tween`은 보간을 수행하는 클래스로, 시작 값과 끝 값 사이의 값을 생성할 수 있도록 돕는 역할을 합니다. 예를 들어, `Tween`을 사용하여 0부터 1까지의 값을 선형으로 변환하거나 색상을 보간하는 등 다양한 애니메이션을 제작할 수 있습니다.

## 2. TweenAnimationBuilder

`TweenAnimationBuilder`는 애니메이션을 직접 제작하고 싶을 때 사용할 수 있는 강력한 위젯입니다. `Tween`을 사용하여 시작 값과 끝 값 사이를 보간하고, 이 보간된 값을 자식 위젯에 전달하여 애니메이션을 생성할 수 있습니다.

```dart
TweenAnimationBuilder(
  duration: Duration(seconds: 1),
  tween: Tween<double>(begin: 0, end: 1),
  builder: (BuildContext context, double value, Widget child) {
    return Opacity(
      opacity: value,
      child: child,
    );
  },
  child: MyWidget(),
)
```

위 예제에서 `TweenAnimationBuilder`는 0부터 1까지의 값을 1초 동안 보간하면서 `MyWidget` 위젯을 페이드 인/아웃하는 애니메이션을 생성합니다.

## 3. 예제

다음은 `Tween`과 `TweenAnimationBuilder`를 사용하여 위젯의 위치를 부드럽게 변경하는 예제입니다.

```dart
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return TweenAnimationBuilder(
      duration: Duration(seconds: 1),
      tween: Tween<Offset>(
        begin: Offset(0, 0),
        end: Offset(0.5, 1),
      ),
      builder: (BuildContext context, Offset offset, Widget? child) {
        return Transform.translate(
          offset: offset * 200,
          child: Container(
            width: 100,
            height: 100,
            color: Colors.blue,
          ),
        );
      },
    );
  }
}
```

위 코드는 1초 동안 `MyWidget` 위젯을 아래로 이동시키는 애니메이션을 생성합니다.

## 4. 결론

`Tween`은 애니메이션을 제작할 때 매우 유용한 도구이며, `TweenAnimationBuilder`를 사용하면 더욱 편리하고 강력한 애니메이션을 만들 수 있습니다. 애니메이션을 자연스럽게 제작하고 싶을 때는 `Tween`과 `TweenAnimationBuilder`를 적극 활용해보세요.

이러한 사용 예시와 함께 `Tween`과 `TweenAnimationBuilder`에 대해 설명했습니다. Flutter 애니메이션 제작에 도움이 되기를 바라며, 보다 자세한 정보를 원하시면 공식 문서를 참고해주세요.

[Flutter Tween 공식 문서](https://api.flutter.dev/flutter/widgets/TweenAnimationBuilder-class.html)

감사합니다!