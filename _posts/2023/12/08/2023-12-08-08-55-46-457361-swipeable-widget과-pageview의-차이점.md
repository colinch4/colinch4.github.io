---
layout: post
title: "[flutter] Swipeable Widget과 PageView의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

### 1. 개요

본 포스트에서는 **Swipeable Widget**과 **PageView**의 차이점을 비교하고 어떤 상황에서 어떤 위젯을 사용해야 하는지에 대해 알아보겠습니다.

### 2. Swipeable Widget

**Swipeable Widget**은 **flutter_swipeable** 패키지에서 제공하는 위젯으로, 사용자가 화면을 좌우로 밀면 콘텐츠를 전환할 수 있는 기능을 제공합니다. 스와이프 동작을 감지하여 원하는 작업을 수행할 수 있습니다.

```dart
Swipeable(
  onSwipeLeft: () {
    // 왼쪽으로 스와이프했을 때 수행할 작업
  },
  onSwipeRight: () {
    // 오른쪽으로 스와이프했을 때 수행할 작업
  },
  child: YourContent(),
)
```

### 3. PageView

**PageView**는 여러 페이지를 슬라이드하여 전환할 수 있는 위젯입니다. 사용자에게 페이지 간의 전환을 가능하게 하며, 페이지 컨트롤을 위한 기능을 제공합니다.

```dart
PageView(
  children: <Widget>[
    Page1(),
    Page2(),
    Page3(),
  ],
)
```

### 4. 차이점 비교

**Swipeable Widget**은 단순히 스와이프 동작을 감지하여 작업을 수행하는 데에 중점을 둔 반면, **PageView**는 여러 페이지 간의 전환에 중점을 둔 위젯입니다.

### 5. 어떤 것을 사용해야 할까?

- **Swipeable Widget**: 사용자의 상호작용에 반응하여 특정 작업을 수행해야 할 때
- **PageView**: 여러 페이지를 전환할 때, 예를 들어 온보딩 화면이나 이미지 갤러리 등에서

### 6. 결론

**Swipeable Widget**과 **PageView**는 각각의 특징에 맞게 적절히 사용되어야 합니다. 필요에 맞게 적절한 위젯을 선택하여 화면 전환이나 상호작용을 구현하는 데 활용할 수 있습니다.

이상으로 **Swipeable Widget**과 **PageView**의 차이점에 대해 알아보았습니다.

### 참고 자료

- [flutter_swipeable 패키지](https://pub.dev/packages/flutter_swipeable)
- [Flutter 공식 문서 - PageView](https://api.flutter.dev/flutter/widgets/PageView-class.html)