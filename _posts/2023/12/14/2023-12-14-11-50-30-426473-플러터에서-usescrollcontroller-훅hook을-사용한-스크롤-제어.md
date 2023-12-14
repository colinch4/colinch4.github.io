---
layout: post
title: "[flutter] 플러터에서 useScrollController 훅(hook)을 사용한 스크롤 제어"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서 스크롤을 제어하는 방법에는 여러 가지가 있습니다. 이 중에서 useScrollController 훅을 사용하여 스크롤을 제어하는 방법을 알아보겠습니다.

## useScrollController 훅이란?

`useScrollController` 훅은 플러터 훅 기능 중 하나로, 화면의 스크롤을 제어할 때 사용됩니다. 기존의 ScrollController를 통한 스크롤 제어와는 다르게, 훅을 사용하면 훨씬 간편하고 효율적으로 스크롤을 다룰 수 있습니다.

## 실제 예제

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

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final scrollController = useScrollController();

    return Scaffold(
      appBar: AppBar(
        title: Text('Scroll Controller Hook'),
      ),
      body: ListView.builder(
        controller: scrollController,
        itemCount: 100,
        itemBuilder: (context, index) {
          return ListTile(title: Text('Item $index'));
        },
      ),
    );
  }
}
```

위의 예제에서 `useScrollController` 훅을 사용하여 스크롤을 제어하고 있습니다. `MyHomePage` 위젯에서 `useScrollController` 훅을 호출하여 `scrollController` 변수에 할당하고, ListView.builder의 controller 속성에 이를 전달함으로써 스크롤을 제어하고 있습니다.

`scrollController`를 통해 스크롤 위치를 가져오거나 설정할 수 있으며, 스크롤 이벤트를 처리하여 필요한 작업을 수행할 수 있습니다.

## 결론

`useScrollController` 훅은 플러터에서 스크롤을 간편하게 제어할 수 있는 강력한 도구입니다. 기존의 ScrollController보다 효율적으로 스크롤을 다룰 수 있는 점에서 많은 개발자들에게 선호되고 있으며, 새로운 프로젝트를 시작할 때 고려해볼만한 기술이라고 할 수 있습니다.

프로젝트를 진행하거나 새로운 기술을 습득할 때, `useScrollController` 훅을 활용하여 효율적인 스크롤 제어를 경험해보시기를 권장합니다.

## 참고 자료

- [Flutter - ScrollController class](https://api.flutter.dev/flutter/widgets/ScrollController-class.html)
- [Flutter - Hooks tutorial](https://flutter.dev/docs/development/ui/advanced/hooks-intro)