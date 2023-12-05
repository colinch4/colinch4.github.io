---
layout: post
title: "[flutter] flutter_custom_clippers의 사용 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

flutter_custom_clippers은 Flutter 개발자들이 UI를 작성할 때 사용할 수 있는 사용자 정의 클리퍼(clipper) 모음입니다. 클리퍼는 해당 도형 모양대로 위젯을 자르는 역할을 합니다. flutter_custom_clippers는 다양한 도형 클리퍼를 제공하며, 이를 사용하여 UI에 독특한 모양과 디자인을 추가할 수 있습니다.

다음은 flutter_custom_clippers를 사용하는 방법입니다:

## 1. 의존성 추가

먼저, `pubspec.yaml` 파일에 flutter_custom_clippers의 의존성을 추가해야 합니다. 아래와 같이 `dependencies` 섹션에 추가합니다:

```dart
dependencies:
  flutter_custom_clippers: ^1.1.0
```

의존성을 추가한 후, 패키지를 업데이트 해야 합니다. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지 업데이트를 수행합니다.

## 2. 클리퍼 사용하기

flutter_custom_clippers의 클리퍼는 `ClipPath` 위젯과 함께 사용됩니다. `ClipPath` 위젯은 자식 위젯을 지정된 도형에 맞게 클리핑하는 역할을 합니다.

예를 들어, 원 모양의 클리퍼를 사용하여 컨테이너 위젯을 동그랗게 자르는 방법은 다음과 같습니다:

```dart
import 'package:flutter/material.dart';
import 'package:flutter_custom_clippers/flutter_custom_clippers.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Flutter Custom Clippers'),
        ),
        body: Center(
          child: ClipPath(
            clipper: CircleClipper(),
            child: Container(
              width: 200,
              height: 200,
              color: Colors.blue,
            ),
          ),
        ),
      ),
    );
  }
}
```

위의 코드에서 `CircleClipper()`는 원 모양의 클리퍼를 생성합니다. 이 클리퍼를 `ClipPath` 위젯의 `clipper` 속성에 할당하면, 컨테이너 위젯이 원 모양으로 자르게 됩니다.

## 3. 다양한 클리퍼 사용하기

flutter_custom_clippers는 여러 가지 도형 클리퍼를 제공합니다. 다음은 일부 예시입니다:

- `WaveClipperOne()`: 파도 모양의 클리퍼
- `BevelClipper()`: 베벨 모양의 클리퍼
- `HexagonalClipper()`: 육각형 모양의 클리퍼
- `DiagonalPathClipper()`: 대각선 경로의 클리퍼

위의 예시와 같이, 사용하고자 하는 클리퍼를 `ClipPath` 위젯에 할당하여 자유롭게 UI를 디자인할 수 있습니다.

더 많은 flutter_custom_clippers 클리퍼에 대한 정보는 [공식 문서](https://pub.dev/packages/flutter_custom_clippers)에서 확인할 수 있습니다.

이렇게 사용자 정의 클리퍼를 사용하여 Flutter 앱의 UI를 개성있게 디자인할 수 있습니다. flutter_custom_clippers를 사용해보고 다양한 클리퍼를 적용해 보세요!