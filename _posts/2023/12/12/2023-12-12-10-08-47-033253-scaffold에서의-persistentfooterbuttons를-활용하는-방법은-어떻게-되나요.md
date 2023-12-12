---
layout: post
title: "[flutter] Scaffold에서의 persistentFooterButtons를 활용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

```dart
Scaffold(
  appBar: AppBar(
    title: Text('Persistent Footer Buttons'),
  ),
  body: Center(
    child: Text('Add your content here'),
  ),
  persistentFooterButtons: <Widget>[
    ElevatedButton(
      onPressed: () {
        // Add your action here
      },
      child: Text('Button 1'),
    ),
    ElevatedButton(
      onPressed: () {
        // Add your action here
      },
      child: Text('Button 2'),
    ),
  ],
)
```

위 예시에서는 Scaffold의 persistentFooterButtons 속성을 사용하여 두 개의 ElevatedButton을 추가하고 있습니다. 이 버튼들은 화면 하단에 고정되어 있으며, onPressed 콜백을 통해 각 버튼의 동작을 정의할 수 있습니다.

참고 자료:
- https://api.flutter.dev/flutter/material/Scaffold/persistentFooterButtons.html