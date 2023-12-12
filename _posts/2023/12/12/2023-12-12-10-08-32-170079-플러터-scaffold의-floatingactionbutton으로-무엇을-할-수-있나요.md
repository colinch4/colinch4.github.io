---
layout: post
title: "[flutter] 플러터 Scaffold의 floatingActionButton으로 무엇을 할 수 있나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

플러터의 Scaffold 위젯은 주로 앱 화면의 구조를 구성하는 데 사용되며, floatingActionButton 속성을 사용하여 스크린의 주요 작업 또는 교대 작업을 위한 부가 기능을 제공할 수 있습니다.

## floatingActionButton으로 할 수 있는 것들

1. **액션 수행** - 사용자가 화면의 주요 작업을 바로 수행할 수 있는 버튼을 추가할 수 있습니다. 예를 들어, 메세지 앱에서 새로운 메세지를 작성할 때 사용자가 한 번의 탭으로 새로운 메세지 창으로 이동할 수 있습니다.

```dart
floatingActionButton: FloatingActionButton(
  onPressed: () {
    // 새로운 메세지 작성 화면으로 이동
  },
  child: Icon(Icons.add),
),
```

2. **커스텀 액션 제공** - 특정 화면에서 필요한 커스텀 기능을 제공할 수 있습니다. 예를 들어, 카메라 앱에서는 사용자가 사진을 찍을 수 있게 하거나, 지도 앱에서는 현재 위치로 이동하는 기능을 제공할 수 있습니다.

```dart
floatingActionButton: FloatingActionButton(
  onPressed: () {
    // 커스텀 기능 실행
  },
  child: Icon(Icons.camera),
),
```

3. **플로팅 버튼 대신 메뉴 사용** - floatingActionButton 대신 PopupMenuButton을 사용하여 여러 액션을 제공할 수 있습니다.

```dart
floatingActionButton: PopupMenuButton(
  // 팝업 메뉴 버튼 설정
  itemBuilder: (context) => [
    PopupMenuItem(
      child: Text('액션 1'),
      onTap: () {
        // 액션 1 실행
      },
    ),
    PopupMenuItem(
      child: Text('액션 2'),
      onTap: () {
        // 액션 2 실행
      },
    ),
  ],
  child: FloatingActionButton(
    onPressed: () {
      // 메뉴 버튼 터치 시
    },
    child: Icon(Icons.more_vert),
  ),
),
```

Scaffold의 floatingActionButton은 사용자와의 상호작용을 강화하고, 중요한 작업을 더욱 쉽게 접근할 수 있도록 돕는 다양한 기능을 제공합니다.

자세한 내용은 [Scaffold 클래스](https://api.flutter.dev/flutter/material/Scaffold-class.html) 문서를 참조하세요.

---
위 내용은 플러터 Scaffold의 floatingActionButton에 대한 기능과 활용에 대한 내용을 담은 기술 블로그입니다.