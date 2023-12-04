---
layout: post
title: "[flutter] 플러터(Flutter) 개발에서 상태 관리를 위해 Riverpod와 Provider를 함께 사용하는 것이 가능한가요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

Flutter에서 상태 관리를 위해 가장 많이 사용되는 패키지 중 하나가 Provider입니다. Provider를 사용하면 위젯 트리의 상단부에서 데이터를 제공하고, 하위 위젯들은 필요한 데이터에 접근할 수 있습니다.

하지만 Provider만으로는 상태 관리가 복잡해질 수 있습니다. 이런 경우 Riverpod라는 패키지를 함께 사용하면 효과적으로 상태 관리를 할 수 있습니다. Riverpod는 Provider의 개선 버전으로, 보다 간편하고 효율적인 상태 관리를 제공합니다.

Riverpod와 Provider를 함께 사용하는 방법은 다음과 같습니다.

1. 먼저 `flutter_riverpod` 패키지를 프로젝트에 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같이 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_riverpod: ^0.14.0
```

2. `main.dart` 파일에서 `flutter_riverpod` 패키지를 import 합니다:

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
```

3. Provider를 정의하고 사용하는 방법은 동일합니다. `Provider` 대신 `ProviderContainer`를 사용하여 상태를 제공하고, `ProviderScope`로 감싸는 것으로 간단하게 사용할 수 있습니다.

```dart
final countProvider = Provider<int>((ref) {
  // 상태 값 제공
  return 0;
});

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ProviderScope(
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(
            title: Text('Riverpod with Provider Example'),
          ),
          body: Consumer(
            builder: (context, watch, _) {
              final count = watch(countProvider);
              return Center(
                child: Text('Count: $count'),
              );
            },
          ),
          floatingActionButton: FloatingActionButton(
            onPressed: () {
              // 상태 값 갱신
              context.read(countProvider).state++;
            },
            child: Icon(Icons.add),
          ),
        ),
      ),
    );
  }
}
```

위 코드에서 `countProvider`는 상태 값 제공을 위한 Provider입니다. `Consumer` 위젯을 사용하여 `countProvider`의 값을 읽어오고, `floatingActionButton`을 클릭할 때마다 상태 값을 갱신합니다.

이렇게 `flutter_riverpod`와 `Provider`를 함께 사용하여 편리하고 간편한 상태 관리를 할 수 있습니다. Riverpod는 Provider와 호환되므로, 기존에 Provider를 사용하던 코드를 손쉽게 Riverpod로 마이그레이션할 수도 있습니다.