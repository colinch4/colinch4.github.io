---
layout: post
title: "[flutter] TransformationController를 이용한 변환 애니메이션 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter에서 이미지나 콘텐츠를 확대, 축소, 이동하는 애니메이션을 구현하려면 TransformationController를 사용할 수 있습니다. 이를 통해 화면에 제스처를 적용하여 객체를 변형하고 애니메이션을 쉽게 적용할 수 있습니다.

## TransformationController란?

TransformationController는 `flutter/widgets.dart`에 정의된 클래스로, `ValueNotifier`를 기반으로 하며, 행렬을 사용하여 변환을 정의합니다. 이를 통해 애니메이션을 지원하고, 상태가 변경될 때 알림을 수신할 수 있습니다.

TransformationController의 구조는 다음과 같습니다:

```dart
TransformationController({
  Matrix4? value,
  this.lowerBound,
  this.upperBound,
})
```

여기서 `value` 매개변수는 현재 변환 행렬을 나타내며, `lowerBound`와 `upperBound`는 변환 범위를 제한하는 값일 수 있습니다.

## TransformationController를 사용한 변환 애니메이션 구현 방법

1. 먼저, TransformationController 인스턴스를 생성합니다.

```dart
final TransformationController _transformationController = TransformationController();
```

2. 그런 다음, 사용하려는 위젯에 `InteractiveViewer`를 적용하면서 `transformationController` 속성에 위에서 생성한 TransformationController를 제공합니다.

```dart
InteractiveViewer(
  transformationController: _transformationController,
  boundaryMargin: EdgeInsets.all(double.infinity),
  minScale: 0.1,
  maxScale: 4.0,
  child: YourContentWidget(),
)
```

3. 제스처나 이벤트에 따라 TransformationController의 값을 업데이트하여 애니메이션을 구현할 수 있습니다.

```dart
_transformationController.value = Matrix4.identity()
  ..translate(dx, dy)
  ..scale(scale);
```

위 코드에서 `dx`, `dy`, `scale`은 각각 이동 및 확대/축소를 표현하는 값입니다.

이제, TransformationController를 사용하여 Flutter 앱에서 변환 애니메이션을 쉽게 구현할 수 있습니다.

다양한 속성과 메서드에 대한 자세한 내용은 Flutter 공식 문서를 참조하세요.

## 결론

TransformationController를 이용하면 Flutter 앱에서 이미지나 콘텐츠의 변환 애니메이션을 쉽게 구현할 수 있습니다. 이를 통해 사용자들이 콘텐츠를 더욱 집중하여 볼 수 있게 해주고, 상호작용성을 향상시킬 수 있습니다.