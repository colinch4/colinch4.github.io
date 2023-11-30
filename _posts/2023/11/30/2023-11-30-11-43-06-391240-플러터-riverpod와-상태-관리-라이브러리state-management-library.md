---
layout: post
title: "[flutter] 플러터 Riverpod와 상태 관리 라이브러리(State Management Library)"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 강력하고 유연한 크로스 플랫폼 모바일 애플리케이션 개발 프레임워크입니다. 하지만 플러터에서는 상태 관리를 위한 표준 방법이 없어 많은 개발자들이 다양한 상태 관리 라이브러리를 사용합니다. 그중에서도 Riverpod는 최근에 인기를 얻고 있는 상태 관리 라이브러리입니다.

## Riverpod란?

Riverpod는 플러터의 Provider 패키지를 기반으로한 상태 관리 라이브러리입니다. Provider 패키지는 의존성 주입(Dependency Injection, DI) 패턴을 기반으로한 상태 관리를 지원합니다. Riverpod는 이러한 Provider 패키지를 좀 더 간편하고 사용하기 쉽게 추상화하여 제공합니다.

## Riverpod의 특징

### 1. 간편한 상태 관리

Riverpod는 간편한 상태 관리를 위해 Provider 패턴을 사용합니다. Provider는 값을 제공하고, 변화를 감지하여 관련된 위젯에 알립니다. 이를 통해 상태의 변화에 따라 UI를 업데이트할 수 있습니다.

### 2. 의존성 주입(Dependency Injection)

Riverpod는 Provider 패턴을 기반으로한 DI 패턴을 사용하여 의존성을 주입합니다. 이를 통해 코드의 재사용성과 테스트 용이성을 높일 수 있습니다.

### 3. Immutable한 상태 관리

Riverpod는 최신 상태를 변경하기 위해 Immutable 객체를 사용합니다. 이를 통해 상태 변화를 추적하고 이전 상태와 비교하여 필요한 업데이트를 수행할 수 있습니다.

## Riverpod 사용 방법

Riverpod를 사용하기 위해서는 먼저 `riverpod` 패키지를 프로젝트에 추가해야 합니다. 이를 위해 `pubspec.yaml` 파일에 다음과 같은 의존성을 추가해주세요.

```yaml
dependencies:
  riverpod: ^0.14.0
```

의존성을 추가한 후, `import 'package:riverpod/riverpod.dart';` 코드로 Riverpod를 임포트할 수 있습니다.

이제 Riverpod를 사용하기 위해 다음과 같이 Provider를 설정할 수 있습니다.

```dart
final counterProvider = Provider<int>((ref) => 0);

class CounterApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ProviderScope(
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(
            title: Text('Counter App'),
          ),
          body: Center(
            child: Consumer(
              builder: (context, watch, _) {
                final counter = watch(counterProvider);
                return Text(
                  'Count: $counter',
                  style: TextStyle(fontSize: 20),
                );
              },
            ),
          ),
          floatingActionButton: FloatingActionButton(
            onPressed: () => context.read(counterProvider).state++,
            child: Icon(Icons.add),
          ),
        ),
      ),
    );
  }
}
```

위의 코드는 카운터 앱을 구현한 예시입니다. `counterProvider`는 현재 카운터 값을 제공하는 Provider입니다. `CounterApp` 위젯에서는 `Consumer` 위젯을 사용하여 해당 Provider의 값을 읽고 UI를 업데이트합니다. 또한 floatinActionButton을 누를 때마다 카운터 값을 증가시킵니다.

## 결론

플러터에서 상태 관리를 하기 위해 Riverpod를 사용해보세요. 간편한 상태 관리, 의존성 주입, Immutable한 상태 관리 등 다양한 기능을 제공하여 효율적인 애플리케이션 개발이 가능합니다.

> 참고: [Riverpod 공식 문서](https://pub.dev/packages/riverpod)