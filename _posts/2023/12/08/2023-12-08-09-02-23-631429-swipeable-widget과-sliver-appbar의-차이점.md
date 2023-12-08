---
layout: post
title: "[flutter] Swipeable Widget과 Sliver AppBar의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

이번 글에서는 Flutter 앱 개발에 있어서 Swipeable Widget과 Sliver AppBar의 차이점에 대해 알아보겠습니다.

### Swipeable Widget

Swipeable Widget은 사용자가 화면에서 수평으로 움직여 다양한 작업을 수행하는 데 사용됩니다. 이를 통해 예를 들어 리스트 아이템을 왼쪽이나 오른쪽으로 스와이프하여 삭제하거나 추가하는 등의 작업을 할 수 있습니다. 

```dart
Swipeable(
  key: UniqueKey(),
  child: ListTile(title: Text('Swipe me')),
  backgroundWidget: Container(
    alignment: Alignment.centerRight,
    color: Colors.red,
    child: Icon(Icons.delete),
  ),
  onSwipeRight: () => print('Swiped right!'),
  onSwipeLeft: () => print('Swiped left!'),
)
```

### Sliver AppBar

Sliver AppBar은 스크롤 가능한 위젯 리스트에서 상단 탭 바와 같이 상단에 고정된 헤더를 만들기 위해 사용됩니다. 이는 많은 양의 컨텐츠를 가진 앱에서 유용하게 사용됩니다.

```dart
CustomScrollView(
  slivers: <Widget>[
    SliverAppBar(
      title: Text('My App'),
      floating: true,
      snap: true,
    ),
    // ...other sliver widgets
  ],
)
```

### 결론

Swipeable Widget은 사용자 상호 작용에 유용하며 주로 리스트 아이템과 같이 일부 위젯에 대한 기능을 추가하는 데 사용됩니다. 반면에 Sliver AppBar은 스크롤 가능한 화면에서 상단 영역에 고정된 헤더를 만들 때 사용됩니다.

따라서, 개발자는 앱의 사용 사례와 요구에 맞게 적합한 위젯을 선택하여 사용할 수 있습니다.

이상으로 Swipeable Widget과 Sliver AppBar의 차이점에 대해 알아보았습니다.

자료 출처: 
- [Flutter Official Documentation](https://flutter.dev/docs)
- [Flutter Pub Packages](https://pub.dev/)