---
layout: post
title: "[flutter] 플러터 Scaffold에서 BottomNavigationBar의 아이템을 구성하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

우선 Scaffold를 작성한 후에 아래의 코드로 BottomNavigationBar를 구성합니다.

```dart
Scaffold(
  bottomNavigationBar: BottomNavigationBar(
    items: <BottomNavigationBarItem>[
      BottomNavigationBarItem(
        icon: Icon(Icons.home),
        label: 'Home',
      ),
      BottomNavigationBarItem(
        icon: Icon(Icons.favorite),
        label: 'Favorites',
      ),
      BottomNavigationBarItem(
        icon: Icon(Icons.settings),
        label: 'Settings',
      ),
    ],
  ),
)
```

위의 코드에서 `BottomNavigationBar`의 `items` 속성에 BottomNavigationBarItem 위젯들을 작성하여 각 아이템이 어떤 아이콘과 라벨을 가지는지 지정할 수 있습니다.

또한 BottomNavigationBar에는 여러 속성을 설정할 수 있는데, 예를 들면 현재 선택된 아이템의 인덱스를 나타내는 `currentIndex` 속성 등이 있습니다.

더 많은 옵션들을 확인하시려면 공식 플러터 문서를 참고하시기 바랍니다.

[Flutter 공식 문서 - BottomNavigationBar](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html)