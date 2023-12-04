---
layout: post
title: "[flutter] 플러터(Flutter)에서 상태 관리를 위해 useReducer Hook을 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 React Native 등과 유사한 방식으로 상태 관리를 위해 Hook을 제공합니다. 그 중 하나인 `useReducer` Hook을 사용하면 상태와 상태를 변경하는 함수를 하나의 객체로 관리할 수 있습니다. 이를 통해 복잡한 상태 관리를 간결하게 처리할 수 있습니다.

## `useReducer` Hook 사용 방법

`useReducer` Hook을 사용하기 위해서는 `flutter_hooks` 패키지가 필요합니다. 따라서 프로젝트의 `pubspec.yaml` 파일에 `flutter_hooks`를 추가해야 합니다. 예를 들어,

```yaml
dependencies:
  flutter_hooks: ^0.14.0
```

위와 같이 `flutter_hooks`라는 패키지를 사용하겠다고 선언해야 합니다. 그런 다음 `main.dart` 파일에서 `flutter_hooks` 패키지를 가져옵니다.

```dart
import 'package:flutter_hooks/flutter_hooks.dart';
```

이제 `useReducer` Hook을 사용하여 상태 관리를 할 수 있습니다. 예를 들어 다음과 같이 Counter 앱을 만들어보겠습니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final counterState =
        useReducer((int state, int action) => state + action, 0);

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Counter App'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text('Count:', style: TextStyle(fontSize: 24)),
              Text('${counterState.value}', style: TextStyle(fontSize: 48)),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  RaisedButton(
                    onPressed: () {
                      counterState.dispatch(-1);
                    },
                    child: Text('-'),
                  ),
                  SizedBox(width: 16),
                  RaisedButton(
                    onPressed: () {
                      counterState.dispatch(1);
                    },
                    child: Text('+'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

위의 코드에서 `useReducer` Hook으로 `counterState`라는 변수를 선언합니다. `counterState.value`는 현재의 상태를 가리키고, `counterState.dispatch`는 상태를 변경하는 함수를 호출할 수 있습니다.

위 코드에서는 `useReducer` Hook을 사용하여 초기 상태를 `0`으로 설정하고, 상태를 변경하는 로직이 `state + action`이라는 간단한 함수로 정의됩니다.

마지막으로, `counterState.value`를 사용하여 현재 상태를 표시하고, `counterState.dispatch`를 사용하여 `+`와 `-` 버튼을 클릭했을 때 상태를 변경합니다.

## 결론

플러터(Flutter)에서 `useReducer` Hook을 사용하여 상태 관리를 쉽고 간결하게 할 수 있습니다. 이를 통해 복잡한 애플리케이션에서도 상태를 효율적으로 관리할 수 있습니다. `useReducer`를 사용하면 Redux와 비슷한 패턴을 간단하게 구현할 수 있으므로, 플러터 앱 개발을 할 때 유용하게 활용할 수 있습니다.

## 참고 자료

- [flutter_hooks 패키지](https://pub.dev/packages/flutter_hooks)
- [플러터(Flutter) 공식 문서](https://flutter.dev/docs)