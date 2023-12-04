---
layout: post
title: "[flutter] 플러터(Flutter)에서 타임 이벤트 처리를 위해 useValueListenable Hook을 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

Flutter에서는 Hooks 패키지를 통해 상태를 관리할 수 있습니다. 이 중에서도 `useValueListenable` Hook을 사용하면 Listenable 객체를 사용하여 상태를 업데이트할 수 있습니다. 따라서 타임 이벤트 처리에 이 Hook을 사용할 수 있습니다.

먼저, useValueListenable Hook을 사용하기 위해서는 `flutter_hooks` 패키지를 프로젝트에 추가해야 합니다. pubspec.yaml 파일에 아래와 같이 dependencies에 추가합니다:

```yaml
dependencies:
  flutter_hooks: ^0.21.0
```

그리고 이제 코드에서 `flutter_hooks` 패키지를 불러옵니다:

```dart
import 'package:flutter_hooks/flutter_hooks.dart';
```

이제 사용할 Listenable을 만들어보겠습니다. 여기서는 Timer를 사용하여 1초마다 상태를 업데이트하도록 구현하겠습니다:

```dart
import 'dart:async';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final count = useValueListenable(ValueNotifier(0));

    useEffect(() {
      Timer.periodic(Duration(seconds: 1), (timer) {
        count.value = timer.tick;
      });

      return () => timer.cancel();
    }, []);

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Time Event using useValueListenable'),
        ),
        body: Center(
          child: Text('Timer: ${count.value}'),
        ),
      ),
    );
  }
}
```

위 코드에서는 `useEffect` Hook을 사용하여 타이머를 생성하고 1초마다 `count` 상태를 업데이트합니다. `ValueListenableBuilder` 위젯을 사용하여 화면에 타이머 값을 표시합니다.

이렇게하면 useValueListenable Hook을 사용하여 플러터(Flutter)에서 타임 이벤트 처리를 할 수 있습니다. 더 많은 정보를 원한다면 프레임워크 공식 문서를 참조해주세요. [flutter_hooks 패키지 문서](https://pub.dev/documentation/flutter_hooks/latest/flutter_hooks/flutter_hooks-library.html)