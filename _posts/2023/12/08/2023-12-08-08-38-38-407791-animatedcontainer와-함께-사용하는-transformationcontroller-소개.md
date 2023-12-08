---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 TransformationController 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter는 애니메이션 효과를 쉽게 추가할 수 있는 다양한 기능을 제공합니다. 이번 포스트에서는 **AnimatedContainer**와 **TransformationController**를 함께 사용하여 화면 전환 효과를 만드는 방법에 대해 알아보겠습니다.

## AnimatedContainer 소개

**AnimatedContainer**는 특정 시간에 걸쳐 특정 속성(예: 크기, 색상 등)을 부드럽게 변경할 수 있게 해주는 위젯입니다. 이를 사용하여 화면 상의 요소들의 크기, 위치, 색상 등을 부드럽게 변화시킬 수 있습니다.  

다음은 AnimatedContainer를 사용하여 크기와 색상을 변경하는 간단한 예제입니다.

```dart
AnimatedContainer(
  width: _isSelected ? 200 : 100,
  height: _isSelected ? 200 : 100,
  color: _isSelected ? Colors.blue : Colors.red,
  duration: Duration(seconds: 1),
  curve: Curves.easeInOut,
  child: Center(
    child: Text('Animated Container'),
  ),
)
```

이렇게 함으로써, `_isSelected` 값이 변경될 때마다 `AnimatedContainer`는 부드럽게 크기와 색상을 변경하게 됩니다.

## TransformationController 소개

**TransformationController**는 3D 변환을 쉽게 다루기 위한 컨트롤러입니다. 화면을 이동, 확대/축소, 회전 등의 제스처 이벤트를 통해 `TransformationController`를 이용하여 화면의 변환을 쉽게 다룰 수 있습니다.

다음은 TransformationController를 이용하여 이미지의 드래그와 확대/축소를 구현하는 간단한 예제입니다.

```dart
TransformationController _controller = TransformationController();

InteractiveViewer(
  transformationController: _controller,
  minScale: 0.1,
  maxScale: 1.0,
  boundaryMargin: EdgeInsets.all(double.infinity),
  child: Image.asset('assets/image.jpg'),
)
```

이렇게 함으로써, 사용자는 이미지를 드래그하거나 확대/축소할 수 있게 됩니다.

## AnimatedContainer와 TransformationController를 함께 활용하기

**AnimatedContainer**와 **TransformationController**를 함께 사용하면 화면 전환 효과를 더욱 다채롭게 구현할 수 있습니다. 예를 들어, 버튼을 클릭했을 때 이미지가 확대되면서 부드럽게 전환되도록 하는 등의 효과를 구현할 수 있습니다.

또한, 이 두 기능을 사용하여 사용자 경험을 더욱 향상시키는데 도움이 될 것입니다.

## 마치며

오늘은 **AnimatedContainer**와 **TransformationController**를 함께 사용하여 Flutter에서 화면 전환 효과를 다루는 방법에 대해 알아보았습니다. 각각의 기능을 잘 이해하고 활용한다면 다양한 애니메이션 효과를 손쉽게 구현할 수 있을 것입니다.

참고 자료:  
[Flutter AnimatedContainer 문서](https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html)  
[Flutter TransformationController 문서](https://api.flutter.dev/flutter/widgets/TransformationController-class.html)

감사합니다!