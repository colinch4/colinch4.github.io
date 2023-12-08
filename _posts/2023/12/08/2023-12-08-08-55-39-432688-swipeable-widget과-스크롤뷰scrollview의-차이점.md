---
layout: post
title: "[flutter] Swipeable Widget과 스크롤뷰(ScrollView)의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 애플리케이션을 개발하면서 사용되는 Swipeable Widget과 ScrollView는 둘 다 사용자 인터페이스(UI)를 다루는 데 사용되지만, 각각의 특징과 사용 시점에 따른 차이점이 있습니다. 이 글에서는 Swipeable Widget과 ScrollView의 차이점을 살펴보겠습니다.

## Swipeable Widget

Swipeable Widget은 화면을 swipe하여 사용자의 상호작용을 처리하는 데 사용됩니다. 주로 리스트나 그리드와 같은 요소를 swipe하여 메뉴를 열거나 손쉽게 삭제하는 등의 작업에 활용됩니다. 

```dart
Swipeable(
  child: Container(
    // 위젯 내용
  ),
  onSwipe: () {
    // Swipe 이벤트 핸들링
  },
);
```

Swipeable Widget은 swipe 동작을 감지하고 제스처 이벤트를 처리하기 위한 특화된 기능을 제공합니다.

## ScrollView

ScrollView는 사용자가 앱 내에서 스크롤하는 동작을 처리합니다. 앱에 맞는 컨텐츠들을 스크롤하여 내용을 볼 수 있도록 해줍니다. ListView, GridView와 같이 여러 요소를 스크롤하여 보여주기 위해 사용됩니다.

```dart
SingleChildScrollView(
  child: Column(
    children: <Widget>[
      // 스크롤 가능한 컨텐츠들
    ],
  ),
);
```

ScrollView는 여러 종류가 있으며, 해당하는 상황에 따라 각각의 특징을 고려하여 사용해야 합니다.

## 결론

Swipeable Widget과 ScrollView는 모두 사용자의 상호작용을 다루기 위한 도구로, 각각의 특징에 따라 적절한 상황에 사용되어야 합니다. Swipeable은 swipe 동작에 초점을 맞추고, ScrollView는 스크롤 기능을 위주로 제공하므로, 해당 기능을 고려하여 적절하게 활용해야 합니다.

이상으로 Swipeable Widget과 ScrollView의 차이점에 대해 알아보았습니다.

[Flutter - Swipeable](https://pub.dev/packages/swipeable)
[Flutter - ScrollView](https://api.flutter.dev/flutter/widgets/ScrollView-class.html)