---
layout: post
title: "[flutter] 플러터 Scaffold에서의 ListView.builder의 작동 방식은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

ListView.builder는 리스트 뷰를 만들 때 사용되며, 아이템을 필요할 때마다 생성하여 메모리를 효율적으로 관리합니다. ListView.builder는 itemBuilder 콜백을 통해 각 아이템의 위젯을 생성하고, itemCount 속성을 통해 전체 아이템 수를 지정합니다. 이 때, 화면에 보이지 않는 아이템은 생성되지 않고, 스크롤되는 동안에만 필요한 아이템들을 생성하여 성능을 최적화합니다.

아래는 Scaffold 내에서 ListView.builder를 사용한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('ListView.builder 예제'),
        ),
        body: ListView.builder(
          itemCount: 100,
          itemBuilder: (BuildContext context, int index) {
            return ListTile(
              title: Text('아이템 $index'),
            );
          },
        ),
      ),
    );
  }
}
```

위 코드는 ListView.builder를 사용하여 100개의 아이템을 가진 리스트 뷰를 Scaffold 내에 구현한 예시입니다.

참고 자료:
- ListView.builder 공식 문서: https://api.flutter.dev/flutter/widgets/ListView-class.html