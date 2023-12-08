---
layout: post
title: "[flutter] Swipeable Widget과 Rive Animation의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

안녕하세요! Flutter와 Rive Animation에 대해 궁금해하는 많은 분들이 계십니다. 오늘은 Flutter에서 사용되는 Swipeable Widget과 Rive Animation의 차이점에 대해 알아보겠습니다.

## Swipeable Widget
Swipeable Widget은 사용자가 화면에서 좌우로 스와이프하여 상호작용하는 데 사용되는 터치 기반 위젯입니다. 이 위젯을 사용하면 스와이프 동작을 통해 항목을 삭제하거나 다른 동작을 수행할 수 있습니다. 

### 예시 코드:
```dart
Swipeable(
  key: UniqueKey(),
  child: ListTile(
    title: Text('Swipe me'),
  ),
  onSwipeLeft: () => _deleteItem(item),
  background: Container(
    color: Colors.red,
    child: Align(
      alignment: Alignment.centerLeft,
      child: Icon(Icons.delete),
    ),
  ),
)
```

## Rive Animation
반면에 Rive Animation은 Flutter 애플리케이션에 고품질의 애니메이션을 추가하기 위한 도구입니다. Rive는 벡터 기반의 그래픽을 제공하며, 다양한 애니메이션을 만들고 제어하는 데 사용됩니다. Rive는 Flutter 앱에서 화면 전환, 아이콘 애니메이션, 게임 등 다양한 시나리오에 활용됩니다.

### 예시 코드:
```dart
RiveAnimation.asset(
  'assets/rive_animation.flr',
  fit: BoxFit.cover,
)
```

## 결론
Swipeable Widget은 사용자와의 상호작용을 위한 터치 기반 위젯으로, 사용자의 제스처에 반응하여 동작하는데 사용됩니다. 반면 Rive Animation은 복잡한 애니메이션을 만들고 제어하기 위한 애니메이션 도구입니다.

두 기술은 각자의 사용 사례와 장점을 가지고 있으며, 애플리케이션에서 필요에 따라 적절히 활용할 수 있습니다. 기술적 요구에 따라 Swipeable Widget과 Rive Animation을 효과적으로 결합하여 Flutter 애플리케이션을 더욱 풍부하고 인터랙티브하게 만들 수 있습니다.

더 많은 정보를 원하신다면, 다음 링크를 참고해보세요.
- [Swipeable Widget 공식 문서](https://pub.dev/packages/swipeable)
- [Rive Animation 공식 웹사이트](https://rive.app/)