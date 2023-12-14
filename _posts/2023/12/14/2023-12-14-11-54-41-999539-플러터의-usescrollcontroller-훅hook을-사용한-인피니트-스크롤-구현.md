---
layout: post
title: "[flutter] 플러터의 useScrollController 훅(hook)을 사용한 인피니트 스크롤 구현"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 사용자가 스크롤할 때 추가 데이터를 동적으로 불러오는 인피니트 스크롤을 구현하기 위해 **useScrollController** 훅을 제공합니다. 이 훅을 사용하여 앱의 성능을 향상시키고 사용자 경험을 향상시킬 수 있습니다.

## 인피니트 스크롤 구현

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: InfiniteScroll(),
    );
  }
}

class InfiniteScroll extends StatefulWidget {
  @override
  _InfiniteScrollState createState() => _InfiniteScrollState();
}

class _InfiniteScrollState extends State<InfiniteScroll> {
  final _scrollController = useScrollController(); // useScrollController 훅을 사용

  List<String> items = List.generate(20, (index) => 'Item $index'); // 초기 아이템

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Infinite Scroll'),
      ),
      body: ListView.builder(
        itemCount: items.length + 1, // 추가 아이템을 위한 항목 추가
        controller: _scrollController, // 스크롤 컨트롤러 설정
        itemBuilder: (context, index) {
          if (index < items.length) {
            return ListTile(
              title: Text(items[index]),
            );
          } else {
            // 추가 데이터를 불러오는 과정을 수행
            return Center(
              child: CircularProgressIndicator(),
            );
          }
        },
      ),
    );
  }
}
```

## 설명

1. **useScrollController** 훅을 사용하여 ListView의 스크롤 위치를 제어합니다.
2. 초기 아이템 목록을 생성하고, **ListView.builder**를 사용하여 아이템을 표시합니다.
3. 리스트의 마지막 항목에 도달하면 추가 데이터를 불러오는 과정을 수행합니다.

이와 같이 **useScrollController** 훅을 사용하여 플러터 앱에서 인피니트 스크롤을 구현할 수 있습니다.

## 참고 자료

- [Flutter 공식 문서 - 스크롤 제어하기](https://flutter.dev/docs/cookbook/lists/scrolling)