---
layout: post
title: "[flutter] 플러터에서의 Stack 위젯과 CustomScrollView 위젯의 조합 예시"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 사용자 인터페이스를 구축하기 위한 강력한 프레임워크입니다. Stack 위젯과 CustomScrollView 위젯은 플러터에서 주로 사용되는 위젯 중 하나입니다. 이들을 조합해서 다양한 사용자 인터페이스를 만들 수 있습니다.

## Stack 위젯

Stack은 겹쳐진 위젯들을 정렬하는 데 사용됩니다. 여러 가지 위젯을 겹치게 놓을 수 있으며, 부모 위젯의 크기에 맞게 자식 위젯을 배치할 수 있습니다. 일반적으로 Positioned 위젯과 함께 사용하여 자식 위젯을 정확한 위치에 배치합니다.

아래는 Stack 위젯의 기본적인 예시입니다.

```dart
Stack(
  children: [
    Container(
      color: Colors.red,
      width: 200,
      height: 200,
    ),
    Container(
      color: Colors.blue,
      width: 150,
      height: 150,
    ),
  ],
)
```

위 코드에서는 Stack 위젯을 사용하여 빨간색과 파란색의 정사각형을 겹쳐서 배치합니다. 크기와 색상은 각각의 Container 위젯을 통해 설정됩니다.

## CustomScrollView 위젯

CustomScrollView는 유연한 스크롤되는 사용자 인터페이스를 만들기 위해 사용됩니다. 여러 가지 스크롤 가능한 위젯을 포함하고 있으며, 사용자 정의 스크롤 동작을 구현할 수 있는 기능을 제공합니다.

아래는 CustomScrollView 위젯을 사용하여 스크롤 가능한 목록을 만드는 예시입니다.

```dart
CustomScrollView(
  slivers: <Widget>[
    SliverAppBar(
      title: Text('Custom Scroll View Example'),
      expandedHeight: 200,
      flexibleSpace: Placeholder(),
    ),
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (BuildContext context, int index) {
          return ListTile(
            title: Text('Item $index'),
          );
        },
      ),
    ),
  ],
)
```

위 코드에서는 CustomScrollView와 관련된 Sliver 위젯을 사용하여 스크롤 가능한 앱 바와 목록을 만듭니다. 목록은 SliverList 위젯을 사용하여 구현되며, SliverChildBuilderDelegate를 통해 각 아이템의 내용이 동적으로 생성됩니다.

## Stack 위젯과 CustomScrollView 위젯의 조합

Stack 위젯과 CustomScrollView 위젯은 함께 사용하면 매우 강력한 사용자 인터페이스를 만들 수 있습니다. 예를 들어, 스크롤 가능한 배경과 위에 겹쳐진 여러 개의 위젯을 함께 사용할 수 있습니다.

아래는 Stack 위젯과 CustomScrollView 위젯을 조합하여 만든 예시입니다.

```dart
Stack(
  children: [
    CustomScrollView(
      slivers: <Widget>[
        SliverAppBar(
          title: Text('Custom Scroll View Example'),
          expandedHeight: 200,
          flexibleSpace: Placeholder(),
        ),
        SliverList(
          delegate: SliverChildBuilderDelegate(
            (BuildContext context, int index) {
              return ListTile(
                title: Text('Item $index'),
              );
            },
          ),
        ),
      ],
    ),
    Positioned(
      top: 50,
      left: 20,
      child: Container(
        color: Colors.yellow,
        width: 100,
        height: 100,
      ),
    ),
  ],
)
```

위 코드에서는 CustomScrollView 위젯을 Stack 위젯 내에 배치하고, 배경으로 사용될 SliverAppBar와 목록으로 사용될 SliverList를 포함합니다. 또한, Positioned 위젯을 사용하여 노란색 정사각형을 Stack의 특정 위치에 배치합니다.

이와 같이 Stack 위젯과 CustomScrollView 위젯을 조합하여 다양한 사용자 인터페이스를 만들 수 있습니다. 추가로 필요한 위젯이나 레이아웃을 조합하여 원하는 디자인을 구현할 수 있습니다.

---

참고 자료:
- [Stack class - widgets library - Dart API](https://api.flutter.dev/flutter/widgets/Stack-class.html)
- [CustomScrollView class - widgets library - Dart API](https://api.flutter.dev/flutter/widgets/CustomScrollView-class.html)