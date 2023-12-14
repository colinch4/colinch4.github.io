---
layout: post
title: "[flutter] 플러터에서 useVisibilityDetector 훅(hook)을 사용한 가시성 제어"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

가끔 화면에 특정 위젯이 나타나거나 사라질 때 이에 대한 이벤트를 다룰 필요가 있습니다. 이를 위해 플러터 프레임워크에서는 `VisibilityDetector` 위젯과 `useVisibilityDetector` 훅을 제공하여 위젯의 가시성 상태 변화에 대응할 수 있습니다.

## VisibilityDetector란?

`VisibilityDetector` 위젯은 플러터에서 화면에 보이는 상태를 감지할 수 있는 기능을 제공합니다. 이를 통해 화면에 표시되거나 사라질 때 발생하는 이벤트를 쉽게 처리할 수 있습니다. 

## useVisibilityDetector 훅 사용하기

`useVisibilityDetector` 훅은 플러터 훅(Flutter Hook) 라이브러리를 통해 제공되며, 함수형 위젯에서 위젯의 가시성 상태를 제어할 수 있습니다. 

### 코드 예시

아래는 `useVisibilityDetector` 훅을 사용하여 가시성 제어를 구현한 예시입니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() => runApp(MyApp());

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final visible = useState(false);

    return VisibilityDetector(
      key: Key('my-widget-key'),
      onVisibilityChanged: (visibilityInfo) {
        visible.value = visibilityInfo.visibleFraction > 0.5;
      },
      child: Container(
        color: visible.value ? Colors.red : Colors.blue,
        width: 200,
        height: 200,
      ),
    );
  }
}
```

이 예시에서 `useVisibilityDetector` 훅을 사용하여 `visible` 변수를 통해 위젯의 가시성 여부를 제어하고 있습니다.

## 결론

`useVisibilityDetector` 훅을 사용하면 화면에 표시되는 위젯의 가시성 상태를 쉽게 감지하고, 이에 대한 이벤트를 핸들링할 수 있습니다. 이를 통해 사용자 경험을 개선하고 상호작용하는 위젯을 만들 수 있습니다.

더 많은 정보는 [플러터 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.