---
layout: post
title: "[flutter] Scaffold에서의 BottomNavigationBar의 작동 방식은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

1. **BottomNavigationBar 위젯 생성**: Scaffold의 `bottomNavigationBar` 속성을 사용하여 BottomNavigationBar 위젯을 생성합니다.

```dart
bottomNavigationBar: BottomNavigationBar(
  items: const <BottomNavigationBarItem>[
    BottomNavigationBarItem(
      icon: Icon(Icons.home),
      label: 'Home',
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.business),
      label: 'Business',
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.school),
      label: 'School',
    ),
  ],
  // 나머지 속성 설정
)
```

2. **탭 선택 시 화면 전환**: BottomNavigationBar의 `onTap` 콜백을 사용하여 각 탭을 선택했을 때 화면을 전환하는 로직을 작성합니다.

```dart
// 현재 선택된 인덱스 상태 객체 생성
int _selectedIndex = 0;

// onTap 콜백에서 _selectedIndex를 업데이트하여 선택한 탭에 따라 화면을 변경
onTap: (int index) {
  setState(() {
    _selectedIndex = index;
    // 선택한 탭에 따라 화면 전환 등의 로직 수행
  });
},
```

3. **화면 전환**: _selectedIndex 상태를 기반으로 선택된 탭에 따라 해당 화면으로 전환하는 코드를 작성합니다.

이렇게 하면 Scaffold에서 BottomNavigationBar를 작동시킬 수 있습니다. **BottomNavigationBar 위젯을 사용하면 하단 탐색이 가능하며 사용자가 탭을 선택할 때 해당 화면으로 전환할 수 있습니다**.

더 자세한 내용은 [Flutter 공식 문서](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html)를 참조하세요.