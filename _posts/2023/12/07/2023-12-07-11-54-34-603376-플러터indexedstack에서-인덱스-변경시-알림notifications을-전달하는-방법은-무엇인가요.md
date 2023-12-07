---
layout: post
title: "[flutter] 플러터(IndexedStack)에서 인덱스 변경시 알림(Notifications)을 전달하는 방법은 무엇인가요?"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

다음은 IndexedStack 위젯에서 인덱스 변경 시 알림을 전달하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class MyIndexedStack extends StatefulWidget {
  @override
  _MyIndexedStackState createState() => _MyIndexedStackState();
}

class _MyIndexedStackState extends State<MyIndexedStack> {
  int _currentIndex = 0;

  @override
  Widget build(BuildContext context) {
    return NotificationListener<IndexedStackNotification>(
      onNotification: (notification) {
        setState(() {
          _currentIndex = notification.newIndex;
        });
        return true;
      },
      child: IndexedStack(
        index: _currentIndex,
        children: [
          // 자식 위젯들을 여기에 추가
          Container(
            color: Colors.red,
            child: Center(
              child: Text('첫 번째 자식'),
            ),
          ),
          Container(
            color: Colors.blue,
            child: Center(
              child: Text('두 번째 자식'),
            ),
          ),
          Container(
            color: Colors.green,
            child: Center(
              child: Text('세 번째 자식'),
            ),
          ),
        ],
      ),
    );
  }
}

class IndexedStackNotification extends Notification {
  final int newIndex;

  IndexedStackNotification(this.newIndex);
}
```

위 예제 코드에서 `IndexedStackNotification`은 인덱스 변경을 나타내는 커스텀 알림 클래스입니다. `NotificationListener` 위젯은 `onNotification` 콜백을 사용하여 알림을 감지하고, 해당 알림을 받은 후 `setState` 메서드를 호출하여 인덱스를 업데이트합니다.

이렇게 하면 IndexedStack 위젯에서 인덱스 변경 시 알림을 전달하고 필요한 작업을 수행할 수 있습니다.