---
layout: post
title: "[flutter] Swipeable Widget과 Gesture Detector의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Swipeable Widget과 Gesture Detector는 모바일 앱 개발에서 사용되는 두 가지 다른 기술입니다. 각각의 특징과 사용 사례에 대해 살펴보겠습니다.

## Swipeable Widget

Swipeable Widget은 사용자가 스와이프 동작으로 상호 작용할 수 있는 위젯입니다. 이 위젯은 주로 리스트나 카드와 같은 요소를 왼쪽이나 오른쪽으로 스와이프하여 삭제나 수정과 같은 동작을 수행할 때 사용됩니다. Swipeable Widget은 사용자 경험을 향상시키고 직관적인 앱 인터페이스를 제공하는 데 유용합니다.

아래는 Swipeable Widget의 예시 코드입니다.

```dart
Swipeable(
  onSwipeLeft: () {
    // 왼쪽으로 스와이프했을 때 실행할 동작
  },
  onSwipeRight: () {
    // 오른쪽으로 스와이프했을 때 실행할 동작
  },
  child: Container(
    // Swipeable Widget의 자식 위젯
  ),
)
```

## Gesture Detector

Gesture Detector는 사용자의 제스처 동작을 감지하고 이에 대한 이벤트를 처리하는 위젯입니다. 터치, 스와이프, 탭과 같은 사용자 입력을 감지하고 이를 기반으로 앱 동작을 제어할 수 있습니다. Gesture Detector를 사용하여 사용자의 터치에 반응하는 사용자 정의 상호 작용을 구현할 수 있습니다.

아래는 Gesture Detector의 예시 코드입니다.

```dart
GestureDetector(
  onHorizontalDragStart: (DragStartDetails details) {
    // 수평 드래그 시작 시 실행할 동작
  },
  onHorizontalDragUpdate: (DragUpdateDetails details) {
    // 수평 드래그 중일 때 실행할 동작
  },
  child: Container(
    // Gesture Detector의 자식 위젯
  ),
)
```

## 결론

Swipeable Widget은 주로 스와이프 동작에 반응하여 상호 작용 가능한 UI 요소를 구현하는 데 사용되고, Gesture Detector는 다양한 제스처 동작을 감지하여 해당 동작에 대한 사용자 정의 동작을 구현하는 데 사용됩니다. 각각의 사용 사례에 따라 적합한 기술을 선택하여 모바일 앱의 사용자 경험을 향상시킬 수 있습니다.

이러한 기술들을 사용하면 모바일 앱의 인터페이스를 보다 유연하고 상호 작용성이 뛰어난 것으로 만들 수 있습니다.

참조:
- [Flutter Swipeable Package](https://pub.dev/packages/swipeable)
- [Flutter GestureDetector Class](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html)