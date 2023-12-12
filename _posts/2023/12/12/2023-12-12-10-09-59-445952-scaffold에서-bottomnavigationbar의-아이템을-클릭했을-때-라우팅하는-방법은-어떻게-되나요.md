---
layout: post
title: "[flutter] Scaffold에서 BottomNavigationBar의 아이템을 클릭했을 때 라우팅하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

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
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _currentIndex = 0;

  final List<Widget> _children = [
    FirstPage(),
    SecondPage(),
    ThirdPage(),
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
        title: Text('BottomNavigationBar 라우팅 예제'),
      ),
      body: _children[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        onTap: onTabTapped,
        currentIndex: _currentIndex,
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            title: Text('첫 번째 페이지'),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.mail),
            title: Text('두 번째 페이지'),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            title: Text('세 번째 페이지'),
          ),
        ],
      ),
    );
  }
}

class FirstPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(child: Text('첫 번째 페이지'));
  }
}

class SecondPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(child: Text('두 번째 페이지'));
  }
}

class ThirdPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(child: Text('세 번째 페이지'));
  }
}
```

이 예제는 BottomNavigationBar와 함께 세 개의 페이지를 보여주는 간단한 앱을 보여줍니다. BottomNavigationBar의 각 아이템을 클릭하면 onTabTapped 함수가 호출되어 해당 페이지로 라우팅됩니다.

이 예제를 참고하여 개발 환경에 맞게 수정하여 사용하시면 됩니다.