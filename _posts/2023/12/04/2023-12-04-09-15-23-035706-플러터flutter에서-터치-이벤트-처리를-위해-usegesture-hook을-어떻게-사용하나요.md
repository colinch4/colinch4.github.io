---
layout: post
title: "[flutter] 플러터(Flutter)에서 터치 이벤트 처리를 위해 useGesture Hook을 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서 터치 이벤트를 처리하기 위해서는 useGesture Hook을 사용할 수 있습니다. useGesture Hook은 터치 이벤트에 대한 관련한 상태와 이벤트 핸들러를 제공합니다.

먼저, 사용하기 위해 useGesture Hook이 포함된 패키지를 프로젝트에 추가해야 합니다. 이 패키지는 `flutter_hooks`입니다. 아래와 같이 `pubspec.yaml` 파일의 `dependencies` 섹션에 패키지를 추가합니다.

```yaml
dependencies:
  flutter_hooks: ^0.15.0
```

이제 패키지를 추가했으므로, useGesture Hook을 사용해보겠습니다. 아래는 간단한 예제입니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final position = useState(Offset.zero);

    return GestureDetector(
      behavior: HitTestBehavior.translucent,
      onPanStart: (details) {
        position.value = details.localPosition;
      },
      onPanUpdate: (details) {
        position.value = details.localPosition;
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text('Gesture Example'),
        ),
        body: Center(
          child: Container(
            width: 200,
            height: 200,
            color: Colors.blue,
            child: Align(
              alignment: Alignment(position.value.dx / 100, position.value.dy / 100),
              child: Text(
                'Drag me!',
                style: TextStyle(fontSize: 18, color: Colors.white),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
```
위의 예제는 터치 이벤트(드래그)를 감지하여 이벤트가 발생하는 지점의 좌표 값을 가져와 화면에 출력하는 간단한 예제입니다. useGesture Hook의 `onPanStart` 및 `onPanUpdate` 이벤트 핸들러를 사용하여 이벤트를 처리합니다. 이벤트 발생 시 position 변수의 값을 업데이트하여 좌표 값을 가져옵니다.

이제 앱을 실행하고 화면을 터치하고 드래그하여 텍스트가 이동하는 것을 확인할 수 있습니다.

더 많은 자세한 내용 및 사용 방법은 [flutter_hooks](https://pub.dev/packages/flutter_hooks) 패키지의 공식 문서를 참조하시기 바랍니다.

참고로, useGesture Hook은 `flutter_hooks` 패키지의 일부로 제공되므로, 해당 패키지 버전 및 임포트 구문을 적절하게 수정하여 사용해야 합니다.