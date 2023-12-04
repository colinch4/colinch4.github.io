---
layout: post
title: "[flutter] 플러터(Flutter) 개발에서 상태 관리를 위해 GetX를 사용하면 왜 라이브러리(Flutter Hooks)를 함께 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 매우 효율적이고 반응형인 UI를 만들기 위해 상태 관리가 필요합니다. GetX는 플러터 개발을 위한 완전한 상태 관리 패키지로, 상태 관리와 라우팅, 의존성 주입 등을 모두 제공합니다. 반면, Flutter Hooks는 함수형 컴포넌트 기반의 상태 관리를 위한 라이브러리입니다.

GetX는 상태 관리를 위해 컨트롤러(Controller)와 오브젝트 상태(State)를 사용합니다. 컨트롤러는 GetX의 `GetxController` 클래스를 상속하여 관리하는 클래스이며, 오브젝트 상태는 해당 컨트롤러에 속하는 변수이고, 이를 GetX의 `Obx` 위젯을 통해 관찰합니다. 따라서 GetX는 상태 관리를 통합적으로 처리할 수 있으며, 효율적인 상태 업데이트와 재렌더링을 보장합니다.

반면, Flutter Hooks는 함수형 컴포넌트 기반의 상태 관리를 지원하는 라이브러리입니다. 클래스형 컨트롤러 대신에 훅(Hook)을 사용하여 상태를 관리하고, 이를 통해 플러터의 위젯 트리에서 핫 리로딩이 가능합니다. 또한, 훅은 플러터의 위젯 생명주기에 적용되기 때문에 상태 변경에 따른 적절한 처리를 할 수 있습니다.

왜 GetX와 Flutter Hooks를 함께 사용해야 할까요? 이는 두 가지 라이브러리의 각각의 장점을 결합하여 더욱 강력한 상태 관리를 제공하기 위함입니다. GetX는 상태 업데이트 및 재렌더링의 최적화에 뛰어나지만, 함수형 컴포넌트와 핫 리로딩을 사용하려면 Flutter Hooks가 필요합니다. 따라서 GetX와 Flutter Hooks를 함께 사용하면 효율적인 상태 관리와 개발 효율성을 동시에 얻을 수 있습니다.

예시 코드:

```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class MyController extends GetxController {
  var count = 0.obs;

  void increment() {
    count.value++;
  }
}

class MyWidget extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final count = useGetX<MyController>().count;

    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Count: ${count.value}'),
            ElevatedButton(
              onPressed: () => useGetX<MyController>.to().increment(),
              child: Text('Increment'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위 코드에서 `MyController`는 GetX의 컨트롤러이며, `MyWidget`은 Flutter Hooks의 훅을 사용하여 상태를 관리하는 함수형 컴포넌트입니다. GetX의 `Obx` 위젯을 통해 `count` 변수를 관찰하고, `increment` 함수를 호출해 상태를 업데이트할 수 있습니다.

참고 자료:
- [GetX 공식 문서](https://pub.dev/packages/get)
- [Flutter Hooks 공식 문서](https://pub.dev/packages/flutter_hooks)