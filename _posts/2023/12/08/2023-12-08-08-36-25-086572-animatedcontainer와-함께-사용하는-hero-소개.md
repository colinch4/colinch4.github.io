---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 Hero 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

플러터 앱 개발을 하다 보면 화면 간 전환 시 특정 위젯이 부드럽게 애니메이션 되면서 보여지고 싶을 때가 있습니다. 이때 `AnimatedContainer`와 `Hero` 위젯을 함께 사용하면 매끄러운 화면 전환을 구현할 수 있습니다.

## 1. `AnimatedContainer`란?

`AnimatedContainer`는 속성 (예: 색상, 크기, 위치 등) 이 변경될 때 부드럽게 애니메이션을 처리하는 위젯입니다. 예를 들어, 상태가 변할 때마다 `AnimatedContainer`의 높이나 색상을 부드럽게 변화시킬 수 있습니다.

다음은 `AnimatedContainer`를 사용한 간단한 예제 코드입니다.

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
  bool _selected = false;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('AnimatedContainer Example'),
        ),
        body: Center(
          child: GestureDetector(
            onTap: () {
              setState(() {
                _selected = !_selected;
              });
            },
            child: AnimatedContainer(
              width: _selected ? 200.0 : 100.0,
              height: _selected ? 100.0 : 200.0,
              color: _selected ? Colors.blue : Colors.red,
              duration: Duration(seconds: 1),
              curve: Curves.fastOutSlowIn,
            ),
          ),
        ),
      ),
    );
  }
}
```

위 코드를 실행하면 빨간색 상자를 탭할 때마다 상자의 크기와 색깔이 부드럽게 변화합니다.

## 2. `Hero`란?

`Hero` 위젯은 한 화면에서 다른 화면으로 넘어갈 때 특정 위젯이 부드럽게 애니메이션되며 보여지도록 해줍니다. 특히, 이미지나 컨테이너와 같은 일반적인 위젯에 사용할 수 있습니다.

다음은 `Hero`를 사용한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Screen1(),
  ));
}

class Screen1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen 1'),
      ),
      body: GestureDetector(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => Screen2()),
          );
        },
        child: Hero(
          tag: 'imageHero',
          child: Image.network('https://example.com/image.jpg'),
        ),
      ),
    );
  }
}

class Screen2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen 2'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () {
            Navigator.pop(context);
          },
          child: Hero(
            tag: 'imageHero',
            child: Image.network('https://example.com/image.jpg'),
          ),
        ),
      ),
    );
  }
}
```

`Screen1`에서 이미지를 탭하면 `Screen2`로 화면이 전환되면서 해당 이미지가 `Hero` 위젯에 의해 부드럽게 확대되어 보여집니다.

## 3. `AnimatedContainer`와 `Hero` 함께 사용하기

이제 `AnimatedContainer`와 `Hero`를 함께 사용하여 부드러운 전환 애니메이션을 만들어봅시다. 아래 예제 코드는 `AnimatedContainer`와 `Hero`를 같은 화면 전환에서 함께 사용한 것입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Screen1(),
  ));
}

class Screen1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen 1'),
      ),
      body: GestureDetector(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => Screen2()),
          );
        },
        child: Hero(
          tag: 'animatedContainerHero',
          child: AnimatedContainer(
            width: 100.0,
            height: 100.0,
            color: Colors.blue,
            duration: Duration(seconds: 1),
            curve: Curves.fastOutSlowIn,
          ),
        ),
      ),
    );
  }
}

class Screen2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen 2'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () {
            Navigator.pop(context);
          },
          child: Hero(
            tag: 'animatedContainerHero',
            child: AnimatedContainer(
              width: 200.0,
              height: 200.0,
              color: Colors.red,
              duration: Duration(seconds: 1),
              curve: Curves.fastOutSlowIn,
            ),
          ),
        ),
      ),
    );
  }
}
```

이제 `Screen1`에서 박스를 탭하면 `Screen2`로 화면이 전환되면서 `Hero` 위젯과 `AnimatedContainer`를 함께 사용하여 부드럽게 크기와 색상이 변하는 애니메이션을 구현할 수 있습니다.

`AnimatedContainer`와 `Hero`를 함께 사용하면 앱의 사용자 경험을 더욱 향상시킬 수 있습니다.

더 많은 자세한 내용은 [Flutter 공식 문서](https://flutter.dev/docs)를 참조하시기 바랍니다.