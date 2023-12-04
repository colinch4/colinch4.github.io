---
layout: post
title: "[flutter] 플러터(Flutter)에서 상태 관리를 위해 BLoC 패턴과 라이브러리(Flutter Hooks)를 같이 사용할 수 있을까요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서 BLoC 패턴은 많은 개발자들이 선호하는 상태 관리 방법 중 하나입니다. BLoC 패턴은 비즈니스 로직과 UI를 분리하여 상태를 관리하는 방식으로, 앱의 복잡성을 줄여줍니다. BLoC 패턴을 효과적으로 사용하기 위해 rxdart 라이브러리를 사용할 수도 있습니다.

한편, 플러터의 최신 버전에서는 Flutter Hooks라는 라이브러리도 도입되었습니다. Flutter Hooks는 함수형 컴포넌트와 훅(Hook)을 사용하여 상태를 관리하는 방식입니다. 이를 통해 클래스 기반의 BLoC 패턴을 사용하지 않고도 간편하게 상태를 관리할 수 있습니다.

두 가지 방식을 함께 사용해도 문제가 없습니다. 예를 들어, BLoC 패턴으로 비즈니스 로직을 구현하고, 훅(Hook)을 사용하여 UI 상태를 관리할 수 있습니다. 이렇게 함께 사용하면 BLoC의 강력한 비즈니스 로직과 Hook의 간결한 상태 관리를 모두 활용할 수 있습니다.

아래는 Flutter Hooks를 사용하여 간단한 Counter 앱의 예시 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: CounterPage(),
    );
  }
}

class CounterPage extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final counter = useState(0);

    return Scaffold(
      appBar: AppBar(
        title: Text('Counter App'),
      ),
      body: Center(
        child: Text(
          'Count: ${counter.value}',
          style: TextStyle(fontSize: 24),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => counter.value++,
        child: Icon(Icons.add),
      ),
    );
  }
}
```

위 예시 코드에서는 useState 훅을 사용하여 counter라는 상태를 생성하고, floatingActionButton이 클릭되면 counter.value를 증가시키는 방식으로 동작합니다. 이렇게 Hook을 사용하여 간단하게 상태를 관리할 수 있습니다.

따라서 플러터(Flutter)에서는 BLoC 패턴과 Hook을 함께 사용하여 상태 관리를 할 수 있으며, 각각의 장점을 적절히 활용할 수 있습니다. 올바른 방식을 선택하기 위해서는 프로젝트의 규모와 요구사항을 고려하고, 개발 팀의 선호도를 고려하는 것이 좋습니다.