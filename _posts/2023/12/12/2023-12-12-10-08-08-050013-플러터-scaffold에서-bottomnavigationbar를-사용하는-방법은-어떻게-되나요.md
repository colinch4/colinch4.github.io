---
layout: post
title: "[flutter] 플러터 Scaffold에서 BottomNavigationBar를 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

## BottomNavigationBar 추가하기

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  State createState() => MyHomePageState();
}

class MyHomePageState extends State<MyHomePage> {
  int _currentIndex = 0;
  final List<Widget> _children = [
    // 각 탭에 표시할 콘텐츠 위젯들을 추가합니다
    PlaceholderWidget(Colors.white),
    PlaceholderWidget(Colors.deepOrange),
    PlaceholderWidget(Colors.green)
  ];

  void onTabTapped(int index) {
    setState(() {
      _currentIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('BottomNavigationBar 예제'),
      ),
      body: _children[_currentIndex], // 현재 선택된 탭의 콘텐츠를 보여줍니다
      bottomNavigationBar: BottomNavigationBar(
        onTap: onTabTapped, // 탭을 눌렀을 때 호출되는 콜백 함수를 지정합니다
        currentIndex:
            _currentIndex, // 현재 선택된 탭의 인덱스. 콘텐츠 위젯과 매핑됩니다
        items: [
          // BottomNavigationBarItem을 통해 각 탭의 아이콘과 레이블을 지정합니다
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: '홈',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.notifications),
            label: '알림',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: '프로필',
          )
        ],
      ),
    );
  }
}

class PlaceholderWidget extends StatelessWidget {
  final Color color;

  PlaceholderWidget(this.color);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: color,
    );
  }
}
```

위 예제는 Scaffold와 BottomNavigationBar를 사용하여 간단한 앱을 만드는 방법을 보여줍니다. BottomNavigationBar를 추가하는 과정에서 각 탭의 아이콘, 레이블 및 콘텐츠 위젯을 지정하여 사용자 경험을 향상시킬 수 있습니다.

원하는 대로 수정하여 다양한 스타일의 BottomNavigationBar를 만들어 보세요. 

더 많은 정보는 [flutter.dev](https://flutter.dev/docs/cookbook/design/bottom-navigation)를 참고해주세요.