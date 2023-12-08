---
layout: post
title: "[flutter] Swipeable Widget과 Hero Animation의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

이번에는 **Swipeable** 위젯과 **Hero** 애니메이션에 대해 알아보겠습니다. 이 두 가지는 모바일 앱의 사용자 경험을 향상시키는 데 사용됩니다. 그러나 각각의 동작 및 사용 사례에는 명확한 차이가 있습니다.

## Swipeable Widget

**Swipeable** 위젯은 화면에서 좌우로 드래그할 수 있는 기능을 제공합니다. 일반적으로 리스트 및 카드 항목에 적용되어 사용자가 항목을 좌우로 스와이프하여 작업을 수행할 수 있게 합니다. 예를 들어, 전자메일 앱에서 이메일을 삭제하거나 아카이브하는 작업을 수행하는 데 사용될 수 있습니다.

```dart
Swipeable(
  child: ListTile(
    title: Text('Swipeable Item'),
    subtitle: Text('Swipe left or right'),
  ),
  onSwipeLeft: () {
    // Perform action when swiped left
  },
  onSwipeRight: () {
    // Perform action when swiped right
  },
)
```

## Hero Animation

**Hero** 애니메이션은 화면 간의 전환 시 두 요소 간의 매끄러운 애니메이션을 제공합니다. 일반적으로 리스트 아이템이나 이미지와 같은 요소가 화면 간에 이동할 때 사용됩니다. 예를 들어, 이미지 갤러리 앱에서 이미지를 탭하면 다음 화면으로 전환되면서 해당 이미지가 자연스럽게 확대되는 효과를 볼 수 있습니다.

```dart
Navigator.push(
  context,
  MaterialPageRoute(
    builder: (context) => DetailScreen(
      image: selectedImage,
    ),
  ),
)
```

## 결론

**Swipeable** 위젯과 **Hero** 애니메이션은 모바일 앱의 사용자 경험을 향상시키는 데 사용되지만, 각각의 사용 사례 및 동작에는 차이가 있습니다. Swipeable 위젯은 좌우 드래그 작업을 허용하는 반면, Hero 애니메이션은 화면 간의 요소 이동 시 자연스러운 애니메이션을 제공합니다.

해당 위젯 및 애니메이션을 효과적으로 활용하여 사용자가 앱을 더 쉽게 이용할 수 있도록 고려해보시기 바랍니다.

### 참고 자료

- [Official Flutter Documentation](https://flutter.dev/docs)
- [Flutter Community](https://flutter.dev/community)