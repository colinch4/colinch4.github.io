---
layout: post
title: "[flutter] Swipeable Widget과 Animated Container의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하면서 **Swipeable Widget**과 **Animated Container**은 두 가지 인기 있는 위젯이다. 하지만 이 두 위젯의 차이점은 무엇일까?

## Swipeable Widget
**Swipeable Widget**은 사용자가 위젯을 터치하고 드래그하여 다양한 동작을 수행할 수 있도록 하는 위젯이다. 일반적으로 리스트 항목을 삭제하거나 수정하는 데 사용된다. 예를 들어, 쇼핑 앱에서 장바구니 목록에서 항목을 스와이프하여 삭제하는 기능을 구현할 때 사용된다.

```dart
Swipeable(
  key: Key('itemKey'),
  onSwipeRight: () {
    _deleteItem();
  },
  child: ListTile(
    title: Text('Item Title'),
  ),
)
```

## Animated Container
한편, **Animated Container**는 위젯의 속성을 애니메이션화하고, 변경될 때 애니메이션 효과를 적용하는 데 사용된다. 예를 들어, 버튼을 클릭했을 때 너비와 높이가 변경되는 애니메이션 효과를 주고 싶을 때 사용된다.

```dart
bool _isExpanded = false;

AnimatedContainer(
  duration: Duration(milliseconds: 500),
  width: _isExpanded ? 200.0 : 100.0,
  height: _isExpanded ? 200.0 : 100.0,
  color: Colors.blue,
  child: FlatButton(
    onPressed: () {
      setState(() {
        _isExpanded = !_isExpanded;
      });
    },
    child: Text('Animate'),
  ),
)
```

## 결론
**Swipeable Widget**과 **Animated Container**는 각각 사용자 상호작용과 UI 애니메이션에 중점을 둔 다른 기능을 제공한다. 따라서 앱의 요구사항에 맞게 적절한 용도로 선택해야 한다.

위젯에 대한 자세한 내용은 공식 [Flutter 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.