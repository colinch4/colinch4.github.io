---
layout: post
title: "[flutter] 플러터 Swipeable과 Flutter PageView의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서는 Swipeable과 PageView를 사용하여 화면에서 스와이프(swipe) 기능을 구현할 수 있습니다. 그러나 두 위젯 간에는 몇 가지 중요한 차이점이 있습니다. 

## Swipeable

Swipeable은 플러터 패키지에서 제공하는 위젯 중 하나로, 슬라이드 제스처(slide gesture)에 반응하여 동적으로 화면을 변경하거나 특정 작업을 수행할 수 있습니다. 사용자가 스와이프할 때 제스처 동작에 따라 사용자 지정된 작업을 수행할 수 있는 커스터마이징 기능이 있습니다.

```dart
Swipeable(
  onSwipeLeft: () {
    // 왼쪽으로 스와이프할 때 수행할 작업
  },
  onSwipeRight: () {
    // 오른쪽으로 스와이프할 때 수행할 작업
  },
  child: Container(
    // Swipeable을 적용할 컨텐츠
  ),
)
```

## PageView

반면에, PageView는 여러 개의 화면(페이지)을 수평 또는 수직으로 스와이프하여 전환할 수 있게 해주는 위젯입니다. 보통 페이지가 표시되는 순서대로 인덱스를 가지고 있으며, 페이지 간의 전환에 대한 내비게이션 기능을 제공합니다.

```dart
PageView(
  children: <Widget>[
    Container(
      // 첫 번째 페이지
    ),
    Container(
      // 두 번째 페이지
    ),
    Container(
      // 세 번째 페이지
    ),
  ],
)
```

## 결론

간단히 말해서, Swipeable은 단일 화면에서 스와이프 제스처에 반응하여 작업을 수행하는 데 사용되고, PageView는 여러 페이지 간의 전환을 위해 사용됩니다. 따라서 작업의 성격에 맞게 두 위젯 중 하나를 선택하여 구현할 수 있습니다.

더 많은 정보를 원하시면 다음 공식 문서를 참고하세요:
- [Swipeable 공식 문서](https://api.flutter.dev/flutter/widgets/Swipeable-class.html)
- [PageView 공식 문서](https://api.flutter.dev/flutter/widgets/PageView-class.html)