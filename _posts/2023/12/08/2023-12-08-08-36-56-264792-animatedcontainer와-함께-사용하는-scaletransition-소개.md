---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 ScaleTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 만들 때 사용자 경험을 높이기 위해 애니메이션을 활용하는 것은 매우 중요합니다. 이를 위해 Flutter는 다양한 내장 애니메이션을 제공합니다. 오늘은 `AnimatedContainer`와 함께 사용할 수 있는 `ScaleTransition`에 대해 알아보겠습니다.

## AnimatedContainer

`AnimatedContainer` 클래스는 컨테이너의 속성을 변경할 때 부드럽게 애니메이션을 적용할 수 있는 위젯입니다. 크기, 색상, 여백 등을 변경할 때 애니메이션 효과를 적용할 수 있어 사용자 인터랙션을 더 풍부하게 만들어줍니다.

예를 들어, 다음과 같이 `AnimatedContainer`를 사용하여 너비와 높이를 애니메이션화할 수 있습니다.

```dart
AnimatedContainer(
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  duration: Duration(seconds: 1),
  curve: Curves.fastOutSlowIn,
  child: YourChildWidget(),
)
```

## ScaleTransition

`ScaleTransition` 위젯은 자식 위젯의 크기를 애니메이션화합니다. 이를 `AnimatedContainer`와 함께 사용하면 컨테이너의 크기 외에도 내부의 컨텐츠 크기까지 애니메이션화할 수 있어 눈에 띄는 효과를 줄 수 있습니다.

다음은 `ScaleTransition`를 사용하여 내부 위젯의 크기를 애니메이션화하는 예제입니다.

```dart
ScaleTransition(
  scale: _controller,
  child: YourChildWidget(),
)
```

## 결론

`AnimatedContainer`와 `ScaleTransition`은 Flutter 앱에서 사용자 경험을 향상시키는 데 유용한 도구입니다. 이 두 가지를 함께 사용하면 효과적인 애니메이션 효과를 구현할 수 있습니다. Flutter의 다양한 애니메이션 기능을 활용하여 사용자들에게 더욱 뛰어난 앱 경험을 제공해보세요!

더 자세한 내용은 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.