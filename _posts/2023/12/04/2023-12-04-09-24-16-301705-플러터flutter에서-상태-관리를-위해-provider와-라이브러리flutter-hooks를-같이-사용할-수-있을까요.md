---
layout: post
title: "[flutter] 플러터(Flutter)에서 상태 관리를 위해 Provider와 라이브러리(Flutter Hooks)를 같이 사용할 수 있을까요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

Provider는 InheritedWidget을 기반으로한 상태 관리 패턴으로, 상태를 제공하고 변경사항을 감지하는 방식입니다. 상위 위젯에서 데이터를 제공하고, 하위 위젯에서 필요한 데이터를 사용할 수 있습니다. Provider를 사용하면 상태의 변화를 실시간으로 반영할 수 있어 UI 업데이트가 원활하게 이루어집니다.

Flutter Hooks는 함수형 위젯을 사용할 때 상태 관리를 돕는 패키지입니다. 앱의 상태를 간단하고 강력하게 관리할 수 있으며, 상태를 변경하기 위해 setState() 메서드를 사용하지 않고도 상태 업데이트를 할 수 있습니다. 모든 위젯에서 상태를 사용할 수 있으며, 훅(Hook) 형태로 사용되기 때문에 코드를 간결하게 작성할 수 있습니다.

Provider와 Flutter Hooks를 함께 사용하면 Provider를 사용하여 상태를 제공하고, Flutter Hooks를 사용하여 해당 상태를 사용하고 감지할 수 있습니다. 예를 들어, Provider로 제공된 상태를 Flutter Hooks의 useState() 훅을 사용하여 업데이트하고 해당 상태를 사용하는 방식입니다.

아래는 Provider와 Flutter Hooks를 함께 사용하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class CounterProvider with ChangeNotifier {
  int _count = 0;

  int get count => _count;

  void increment() {
    _count++;
    notifyListeners();
  }
}

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (context) => CounterProvider(),
        ),
      ],
      child: MyApp(),
    ),
  );
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final counter = useProvider<CounterProvider>();

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Flutter Provider & Hooks Example'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Count: ${counter.count}',
                style: TextStyle(fontSize: 24),
              ),
              SizedBox(height: 16),
              ElevatedButton(
                onPressed: () => counter.increment(),
                child: Text('Increment'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

위의 예제 코드에서는 CounterProvider라는 Provider 클래스를 정의하여 count라는 상태를 제공하고 있습니다. MyApp 위젯에서는 useProvider 훅을 사용하여 CounterProvider의 인스턴스를 가져와 count 상태를 사용하고 있습니다. 이때 count 상태는 Provider에서 관리되며, increment() 메서드를 통해 업데이트되어 UI가 자동으로 업데이트됩니다.