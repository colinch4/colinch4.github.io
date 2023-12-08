---
layout: post
title: "[flutter] Swipeable Widget과 Drag & Drop의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

오늘은 **Flutter**에서 Swipeable Widget과 Drag & Drop이 어떻게 다른지에 대해 알아보겠습니다. 이 두 가지 기능은 모바일 앱 개발에서 사용자 경험을 향상시키는 데 중요한 역할을 합니다.

## Swipeable Widget

Swipeable Widget은 **사용자가 항목을 좌우로 스와이프하여 작업을 수행**할 수 있는 기능을 제공합니다. 예를 들어, 이메일 앱에서 메일을 읽거나 삭제하는 등의 동작을 수행할 때 사용될 수 있습니다.

이를 구현하기 위해서는 **Dismissible** 위젯을 사용하여 각 항목에 스와이프 제스처를 추가하고, 스와이프 동작에 따라 적절한 작업을 수행하는 핸들러를 정의해야 합니다.

```dart
Dismissible(
  key: Key(item.id),
  onDismissed: (direction) {
    // 핸들러 정의
    if (direction == DismissDirection.endToStart) {
      // 삭제 동작 수행
    } else if (direction == DismissDirection.startToEnd) {
      // 다른 작업 수행
    }
  },
  child: YourListItem(item: item),
);
```

## Drag & Drop

반면에, Drag & Drop은 **사용자가 항목을 끌어서 다른 위치로 이동하거나 다른 동작을 수행**할 수 있도록 합니다. 이는 리스트를 재정렬하거나 항목을 그룹으로 묶는 등의 기능을 구현할 때 유용합니다.

이를 구현하기 위해서는 **Draggable** 및 **DragTarget** 위젯을 사용하여 드래그 가능한 항목을 생성하고, 드롭 타겟에 해당 항목을 놓았을 때 어떤 작업을 수행할지 정의해야 합니다.

```dart
Draggable<int>(
  data: item,
  feedback: YourDraggableFeedback(item: item),
  childWhenDragging: YourPlaceholder(),
  child: YourListItem(item: item),
),
DragTarget<int>(
  builder: (context, candidateData, rejectedData) {
    // 드롭 타겟 위젯 빌더 함수
  },
  onWillAccept: (data) {
    // 수락 여부 판단
  },
  onAccept: (data) {
    // 드롭 동작 수행
  },
);
```

## 결론

Swipeable Widget은 주로 좌우 스와이프 동작으로 작업을 수행하는 데 사용되고, Drag & Drop은 항목을 드래그하여 다른 위치로 이동하거나 다른 동작을 수행하는 데 사용됩니다. 이러한 차이점을 이해하고 적절하게 활용한다면, 사용자들이 앱을 더 효율적으로 활용할 수 있는 기능을 제공할 수 있을 것입니다.

그럼 이번에는 **Flutter** 앱 개발에서 Swipeable Widget과 Drag & Drop의 차이점에 대해 알아보았는데, 도움이 되었기를 바랍니다.

References:
- Flutter Documentation: https://flutter.dev/docs
- Medium article on Swipeable Widget: [link to the article]
- Stack Overflow thread on Drag & Drop in Flutter: [link to the thread]