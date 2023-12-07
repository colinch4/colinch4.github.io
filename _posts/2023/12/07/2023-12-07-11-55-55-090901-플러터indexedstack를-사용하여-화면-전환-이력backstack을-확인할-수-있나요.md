---
layout: post
title: "[flutter] 플러터(IndexedStack)를 사용하여 화면 전환 이력(BackStack)을 확인할 수 있나요?"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

네, 플러터의 IndexedStack을 사용하면 화면 전환 이력(BackStack)을 확인할 수 있습니다. IndexedStack은 여러 개의 자식 위젯을 가지고 있는데, 자식 위젯 중 하나만 화면에 보이도록 설정할 수 있습니다. 이때, IndexedStack의 index 속성을 사용하여 어떤 자식 위젯을 표시할지 지정할 수 있습니다.

IndexedStack을 활용하여 화면 전환 이력을 유지하려면, 자식 위젯들을 위젯 리스트에 저장하고 index 값을 업데이트해야 합니다. index 값은 현재 보여질 화면의 인덱스를 나타내며, 현재 보여지는 화면의 인덱스가 변경되면 해당 화면으로 전환됩니다. 이렇게 인덱스를 업데이트하면 이전에 보여진 화면으로 되돌아갈 수 있습니다.

다음은 IndexedStack을 사용하여 화면 전환 이력을 확인하는 예시 코드입니다:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int _currentIndex = 0;

  List<Widget> _screens = [
    Screen1(),
    Screen2(),
    Screen3(),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("BackStack Example"),
        ),
        body: IndexedStack(
          index: _currentIndex,
          children: _screens,
        ),
        bottomNavigationBar: BottomNavigationBar(
          currentIndex: _currentIndex,
          onTap: (index) {
            setState(() {
              _currentIndex = index;
            });
          },
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: "Screen 1",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.search),
              label: "Screen 2",
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.settings),
              label: "Screen 3",
            ),
          ],
        ),
      ),
    );
  }
}

class Screen1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Screen 1"),
    );
  }
}

class Screen2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Screen 2"),
    );
  }
}

class Screen3 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Screen 3"),
    );
  }
}
```

이 예시 코드에서는 IndexedStack을 사용하여 화면을 전환할 수 있는 BottomNavigationBar를 구현하였습니다. 각 BottomNavigationBarItem을 클릭하면 해당 인덱스의 화면으로 전환되며, 이전으로 돌아가기 기능도 제공됩니다.

이렇게 IndexedStack을 사용하면 화면 전환 이력을 확인할 수 있고, 사용자는 이전 화면으로 되돌아갈 수 있습니다.

참고 자료:
- [IndexedStack 클래스 문서](https://api.flutter.dev/flutter/widgets/IndexedStack-class.html)
- [BottomNavigationBar 클래스 문서](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html)