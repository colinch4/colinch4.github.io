---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 AnimatedBuilder 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다보면 애니메이션 효과를 적용해야 하는 경우가 많습니다. 이때 `AnimatedContainer`와 함께 사용하는 `AnimatedBuilder`를 활용하면 앱의 화면 전환이 부드럽고 자연스러워집니다.

## AnimatedContainer

`AnimatedContainer`는 자식 위젯의 크기, 위치 또는 속성을 부드럽게 변경할 수 있는 위젯입니다. 이를 통해 애니메이션 효과를 쉽게 적용할 수 있습니다. 예를 들어, 버튼을 누를 때 컨테이너의 크기나 색상을 부드럽게 변경하고 싶을 때 `AnimatedContainer`를 활용할 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _isToggled ? 200.0 : 100.0,
  height: _isToggled ? 200.0 : 100.0,
  color: _isToggled ? Colors.blue : Colors.green,
  child: Center(
    child: Text('AnimatedContainer Example'),
  ),
)
```

위 코드에서 `_isToggled` 값이 변경될 때 `AnimatedContainer`의 속성들이 부드럽게 변경됩니다.

## AnimatedBuilder

하지만 `AnimatedContainer`만으로는 모든 애니메이션 효과를 다룰 수는 없습니다. 예를 들어, `AnimatedContainer`는 자식 위젯의 `transform` 속성을 변경하는 애니메이션을 처리하지 못합니다. 이때 `AnimatedBuilder`를 사용하여 원하는 애니메이션 효과를 직접 다룰 수 있습니다.

```dart
AnimatedBuilder(
  animation: _controller,
  builder: (BuildContext context, Widget child) {
    return Transform.rotate(
      angle: _controller.value * 2.0 * math.pi,
      child: Container(
        width: 200.0,
        height: 200.0,
        color: Colors.green,
        child: Center(
          child: Text('AnimatedBuilder Example'),
        ),
      ),
    );
  },
)
```

위 코드에서 `_controller`를 이용하여 `AnimatedBuilder`가 회전 애니메이션을 부드럽게 처리합니다.

`AnimatedContainer`와 `AnimatedBuilder`를 적절히 조합하여 Flutter 앱에서 다양한 애니메이션 효과를 자연스럽게 표현할 수 있습니다. 앱의 사용자 경험을 향상시키기 위해 이러한 애니메이션 효과들을 적극적으로 활용해 보시기 바랍니다.

더 많은 정보는 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하세요.