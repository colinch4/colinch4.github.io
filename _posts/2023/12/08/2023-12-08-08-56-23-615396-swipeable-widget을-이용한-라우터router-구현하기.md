---
layout: post
title: "[flutter] Swipeable Widget을 이용한 라우터(Router) 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

안녕하세요! 이번 포스트에서는 Flutter에서 Swipeable Widget을 이용하여 라우터를 구현하는 방법에 대해 알아보겠습니다. 

## Swipeable Widget

Swipeable Widget은 사용자의 스와이프 동작에 반응하여 화면 전환이나 다양한 동작을 수행할 수 있는 위젯입니다. 이를 이용하여 화면 전환 효과를 부드럽게 구현할 수 있습니다.

## 라우터(Router) 구현

우선, Swipeable Widget을 이용하여 라우터를 구현하려면, `flutter_swipe_action_card` 패키지를 이용할 수 있습니다. 

먼저, `flutter_swipe_action_card` 패키지를 프로젝트에 추가합니다.
```dart
dependencies:
  flutter_swipe_action_card: ^1.0.2
```

다음으로, 다음과 같이 Swipeable Widget을 사용하여 라우터를 구현할 수 있습니다.
```dart
import 'package:flutter_swipe_action_card/flutter_swipe_action_card.dart';

SwipeActionCard(
  child: YourWidget(),
  onLeftSwipe: () {
    // 왼쪽으로 스와이프할 때 수행할 작업
  },
  onRightSwipe: () {
    // 오른쪽으로 스와이프할 때 수행할 작업
  },
);
```

이렇게하면 Swipeable Widget을 이용하여 라우터를 구현할 수 있습니다.

## 마무리

Swipeable Widget을 이용하여 라우터를 구현하면 사용자가 앱을 보다 직관적으로 조작할 수 있는 장점이 있습니다. 터치 기반의 사용자 경험을 향상시키기 위해 Swipeable Widget을 활용하여 다양한 라우터를 구현해보세요.

이상으로 Swipeable Widget을 이용한 라우터 구현에 대해 알아보았습니다. 감사합니다!

## 참고 자료
- flutter_swipe_action_card 패키지: [https://pub.dev/packages/flutter_swipe_action_card](https://pub.dev/packages/flutter_swipe_action_card)