---
layout: post
title: "[flutter] flutter_custom_clippers 소개"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Flutter는 Google에서 개발한 크로스 플랫폼 모바일 앱 개발 프레임워크입니다. Flutter Custom Clippers는 Flutter 앱에서 사용할 수 있는 다양한 형태의 클리퍼(clipper)를 제공하는 패키지입니다.

## 클리퍼란 무엇인가요?

클리퍼는 그래픽 디자인에서 사용되는 용어로, 도형의 일부만을 그리고 나머지 부분은 가려주는 역할을 합니다. 이를 Flutter에서 구현하기 위해서는 `CustomClipper` 클래스를 상속받아 클리퍼를 직접 구현해야 합니다. 

## flutter_custom_clippers 사용하기

flutter_custom_clippers 패키지를 사용하려면, `pubspec.yaml` 파일에 의존성을 추가해야 합니다. 

```yaml
dependencies:
  flutter_custom_clippers: ^1.1.0
```

이후 `pub get` 명령을 실행하여 패키지를 다운로드합니다.

flutter_custom_clippers 패키지는 여러 가지 형태의 클리퍼를 제공합니다. 예를 들어, `WaveClipperOne`, `WaveClipperTwo`, `TriangleClipper`, `OvalTopBorderClipper` 등이 있습니다. 클리퍼를 사용하려면 해당 클래스를 `clipper` 속성에 지정해주면 됩니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_custom_clippers/flutter_custom_clippers.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ClipPath(
      clipper: WaveClipperOne(),
      child: Container(
        color: Colors.blue,
        height: 200,
        width: double.infinity,
      ),
    );
  }
}
```

위의 예제 코드에서는 `WaveClipperOne`을 사용하여 파도 모양의 클리퍼를 구현하고 있습니다. `ClipPath` 위젯을 사용하여 클리퍼를 적용하고, `Container` 위젯을 이용하여 클리퍼로 자른 영역을 채워줍니다.

## 결론

flutter_custom_clippers는 다양한 형태의 클리퍼를 제공하여 Flutter 앱의 UI 디자인을 보다 다채롭게 만들어 줍니다. 이 패키지를 사용하면 간단하게 클리퍼를 구현할 수 있으므로, Flutter 개발자라면 한번쯤 사용해보는 것을 추천합니다.

---

参考:
- [flutter_custom_clippers 패키지](https://pub.dev/packages/flutter_custom_clippers)
- [Flutter 공식 사이트](https://flutter.dev/)