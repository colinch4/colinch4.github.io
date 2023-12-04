---
layout: post
title: "[flutter] 플러터(Flutter)에서 상태 관리를 위해 MobX와 라이브러리(Flutter Hooks)를 같이 사용할 수 있을까요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 UI 개발을 위한 모바일 애플리케이션 프레임워크로, 상태 관리가 매우 중요합니다. MobX는 플러터에서 상태 관리를 효율적으로 수행할 수 있는 라이브러리 중 하나이며, Flutter Hooks는 플러터와 함께 사용되는 함수형 프로그래밍 패턴을 지원하는 라이브러리입니다. 이러한 MobX와 Flutter Hooks를 함께 사용하면 상태 관리를 훨씬 간편하게 할 수 있습니다.

플러터에서 MobX를 사용하려면, 다음과 같이 의존성을 추가해야 합니다:
```dart
dependencies:
  flutter_mobx: ^2.0.0
```

Flutter Hooks를 사용하려면, 다음과 같이 의존성을 추가해야 합니다:
```dart
dependencies:
  flutter_hooks: ^0.18.0
```

MobX와 Flutter Hooks를 함께 사용하기 위해서는, 먼저 MobX의 상태 관리를 선언하고 변경하는데에 사용되는 `@observable`, `@computed`, `@action` 및 `@persist` 등의 어노테이션을 지정해야 합니다. 그리고 Flutter Hooks의 `useObserver` 함수를 이용하여 MobX의 상태를 옵저빙할 수 있습니다. 아래 예시를 참고해보세요:

```dart
import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:mobx/mobx.dart';

// MobX의 상태 관리 클래스 정의
class CounterStore = _CounterStore with _$CounterStore;

abstract class _CounterStore with Store {
  @observable
  int count = 0;

  @action
  void increment() {
    count++;
  }

  @computed
  bool get isEven => count % 2 == 0;
}

// 플러터 위젯 정의
class CounterPage extends HookWidget {
  final CounterStore _counterStore = CounterStore();

  @override
  Widget build(BuildContext context) {
    useEffect(() {
      // 플러터 Hooks의 useEffect를 이용하여 컴포넌트가 생성될 때 실행될 코드 작성
      _counterStore.increment(); // 예시로 초기값 1로 설정
      return null;
    }, []);

    return Scaffold(
      appBar: AppBar(
        title: Text('Counter'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Count: ${_counterStore.count}',
              style: TextStyle(fontSize: 24),
            ),
            SizedBox(height: 16),
            Observer(
              builder: (_) => Text(
                'Even? ${_counterStore.isEven}',
                style: TextStyle(fontSize: 18),
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _counterStore.increment,
        child: Icon(Icons.add),
      ),
    );
  }
}

// 실행
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MobX & Flutter Hooks Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: CounterPage(),
    );
  }
}
```

위의 예시 코드에서는 MobX의 `@observable` 어노테이션을 이용하여 `count` 변수를 상태로 선언하고, `@computed` 어노테이션을 이용하여 `isEven` 변수를 상태에 의존적으로 계산합니다. 그리고 `@action` 어노테이션을 이용하여 값을 변경하는 `increment` 메서드를 정의합니다. `useObserver` 함수를 이용하여 상태를 옵저빙하고, 상태가 변화할 때마다 UI가 업데이트됩니다.

이제 MobX와 Flutter Hooks를 함께 사용하여 플러터 애플리케이션의 상태 관리를 효율적으로 처리할 수 있습니다. 두 라이브러리는 각각의 장점을 가지고 있으며, 함께 사용하면 더욱 강력한 상태 관리 기능을 제공할 수 있습니다.