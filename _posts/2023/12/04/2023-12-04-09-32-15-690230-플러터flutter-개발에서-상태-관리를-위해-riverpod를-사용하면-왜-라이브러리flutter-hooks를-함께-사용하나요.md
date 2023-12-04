---
layout: post
title: "[flutter] 플러터(Flutter) 개발에서 상태 관리를 위해 Riverpod를 사용하면 왜 라이브러리(Flutter Hooks)를 함께 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱 개발을 하다 보면 상태 관리는 매우 중요한 부분입니다. 플러터에서는 다양한 상태 관리 라이브러리들이 있지만, 가장 인기있고 사용하기 편리한 라이브러리 중 하나는 Riverpod입니다. Riverpod는 강력한 상태 관리 기능을 제공하며, 이를 사용하여 앱의 상태를 관리할 수 있습니다.

하지만 Riverpod는 완전한 상태 관리 솔루션이 아니며, UI에 상태를 연결하는 작업이 필요합니다. 이때, Flutter Hooks 라이브러리를 함께 사용하면 상태 연결을 보다 쉽게 할 수 있습니다.

Flutter Hooks는 훅(Hook) 기반의 상태 관리 라이브러리로, Riverpod와 매우 호환됩니다. 이 라이브러리를 사용하면 상태를 선언하고 사용하는 것이 간단해집니다. 훅은 상태를 추적하고, 자동으로 앱을 다시 렌더링하며, 상태를 변경하는 데 도움을 줍니다. 이를 통해 플러터 앱의 개발 생산성을 향상시킬 수 있습니다.

예를 들어, Riverpod를 사용하여 앱의 테마를 관리한다고 가정해봅시다. Riverpod를 단독으로 사용하는 경우, UI에 상태를 연결하기 위해 상태를 선언하고, `Consumer` 위젯을 사용하여 상태를 감싸야 합니다. 하지만 Flutter Hooks를 사용하면 훅을 이용하여 간단히 상태를 선언하고 사용할 수 있습니다. 예를 들면 다음과 같습니다:

```dart
final themeProvider = Provider<ThemeData>((ref) {
  return useProvider(themeStateProvider); // Flutter Hooks를 이용하여 테마 상태를 가져옴
});

class MyHomePage extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final theme = useProvider(themeProvider); // 테마 상태를 사용
    return MaterialApp(
      theme: theme,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Hooks with Riverpod'),
        ),
        body: Center(
          child: Text(
            'Hello, World!',
            style: theme.textTheme.bodyText1,
          ),
        ),
      ),
    );
  }
}
```

위의 코드에서 `useProvider` 훅을 사용하여 `themeProvider` 상태를 가져와서 `theme` 변수에 할당하고, 이를 `MaterialApp`의 `theme` 속성에 적용하고 있습니다. 이렇게 함으로써 Riverpod와 Flutter Hooks를 함께 사용하여 상태 관리를 보다 효율적으로 할 수 있습니다.

참고로, Flutter Hooks는 필수적으로 Riverpod와 함께 사용해야 하는 것은 아니지만, Riverpod와 함께 사용하면 더욱 간편하고 편리한 상태 관리를 할 수 있습니다. 따라서 플러터(Flutter) 개발에서 Riverpod와 함께 Flutter Hooks를 사용하는 것을 권장합니다.

## 참고 자료
- [Riverpod Documentation](https://riverpod.dev/)
- [Flutter Hooks Repository](https://github.com/rrousselGit/flutter_hooks)