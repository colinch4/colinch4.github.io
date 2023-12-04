---
layout: post
title: "[flutter] 플러터(Flutter)에서 키보드 이벤트 처리를 위해 useTextEditingController Hook을 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

Flutter에서는 useTextEditingController라는 Hook을 사용하여 키보드 이벤트를 처리할 수 있습니다. 이 Hook을 사용하면 TextField나 TextFormField와 같은 입력 필드와 상호작용할 수 있습니다. 이제 useTextEditingController Hook을 사용하여 키보드 이벤트를 처리하는 방법을 알아보겠습니다.

### 1. useTextEditingController Hook 임포트하기

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
```

### 2. useTextEditingController Hook을 사용하여 키보드 이벤트 처리하기

```dart
class MyTextField extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final textEditingController = useTextEditingController();

    return TextField(
      controller: textEditingController,
      onChanged: (value) {
        // 텍스트 필드의 값이 변경될 때마다 호출됩니다.
        print('입력된 값: $value');
      },
      onSubmitted: (value) {
        // 텍스트 필드에서 입력한 값을 제출할 때 호출됩니다.
        print('제출된 값: $value');
      },
    );
  }
}
```

### 3. 사용자 입력값 가져오기

키보드 이벤트를 처리하려면 useTextEditingController Hook의 controller 속성을 TextField나 TextFormField의 controller 속성과 연결해야 합니다. 그런 다음 onChanged 콜백 함수를 사용하여 텍스트 필드의 값을 실시간으로 가져올 수 있고, onSubmitted 콜백 함수를 사용하여 제출된 값을 가져올 수 있습니다.

```dart
final textEditingController = useTextEditingController();

TextField(
  controller: textEditingController,
  onChanged: (value) {
    // 텍스트 필드의 값이 변경될 때마다 호출됩니다.
    print('입력된 값: $value');
  },
  onSubmitted: (value) {
    // 텍스트 필드에서 입력한 값을 제출할 때 호출됩니다.
    print('제출된 값: $value');
  },
);
```

### 4. Hook 사용 후 정리하기

Hook을 사용하는 경우, 메모리 누수를 방지하기 위해 컴포넌트가 dispose될 때 사용한 Hook을 정리해야 합니다. useEffect를 사용하여 Hook을 정리할 수 있습니다.

```dart
class MyTextField extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final textEditingController = useTextEditingController();

    useEffect(() {
      return () {
        textEditingController.dispose();
      };
    }, []);

    return TextField(
      controller: textEditingController,
      onChanged: (value) {
        // 텍스트 필드의 값이 변경될 때마다 호출됩니다.
        print('입력된 값: $value');
      },
      onSubmitted: (value) {
        // 텍스트 필드에서 입력한 값을 제출할 때 호출됩니다.
        print('제출된 값: $value');
      },
    );
  }
}
```

위와 같이 `useEffect`를 사용하여 Hook을 정리하면, 컴포넌트가 소멸되기 전에 `dispose()` 메서드를 호출하여 TextEditingController를 정리할 수 있습니다.

이제 useTextEditingController Hook을 사용하여 Flutter 앱에서 키보드 이벤트를 처리하는 방법을 알게 되었습니다. 이를 통해 텍스트 필드와 키보드 사이의 상호작용을 쉽게 구현할 수 있습니다. 

더 자세한 내용은 [공식 Flutter 문서](https://api.flutter.dev/flutter/widgets/TextEditingController-class.html)를 참조하세요.