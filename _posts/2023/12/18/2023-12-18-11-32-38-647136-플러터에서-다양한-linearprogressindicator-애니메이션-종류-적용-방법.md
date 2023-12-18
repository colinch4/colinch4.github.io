---
layout: post
title: "[flutter] 플러터에서 다양한 LinearProgressIndicator 애니메이션 종류 적용 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터에서 LinearProgressIndicator 위젯은 진행 상황을 시각적으로 나타내는 데 사용됩니다. 이 위젯에 다양한 애니메이션 효과를 적용할 수 있습니다. 이제 그 방법을 알아보겠습니다.

## 1. 기본 애니메이션

가장 간단한 방법은 기본 애니메이션을 사용하는 것입니다. 다음은 기본 LinearProgressIndicator 위젯을 생성하는 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Linear Progress Indicator')),
        body: Center(
          child: LinearProgressIndicator(),
        ),
      ),
    );
  }
}
```

위 코드에서 LinearProgressIndicator 위젯은 애니메이션이 적용되어 진행 상황을 보여줍니다.

## 2. 사용자 정의 애니메이션

더 다양하고 사용자 정의된 애니메이션 효과를 적용하려면 **`LinearProgressIndicator`** 위젯의 속성을 활용할 수 있습니다. 예를 들어, **`valueColor`** 속성을 사용하여 애니메이션 색상을 변경할 수 있습니다.

```dart
LinearProgressIndicator(
  valueColor: AlwaysStoppedAnimation<Color>(Colors.red),
)
```

또한, **`backgroundColor`** 속성을 이용하여 배경색을 변경할 수도 있습니다.

```dart
LinearProgressIndicator(
  backgroundColor: Colors.grey,
)
```

## 3. 커스텀 애니메이션

더 많은 커스터마이징이 필요한 경우, **`LinearProgressIndicator`**를 직접 커스텀하여 애니메이션을 적용할 수 있습니다. 이를 위해서는 **`CustomPainter`**와 **`CustomPaint`** 위젯을 사용하여 원하는 애니메이션 효과를 구현하게 됩니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Custom Linear Progress Indicator')),
        body: Center(child: CustomPaint(
          foregroundPainter: MyPainter(),
          child: Container(width: 200, height: 200),
        )),
      ),
    );
  }
}

class MyPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    // your custom painting implementation here
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
```

이 코드에서는 **`CustomPainter`**를 이용하여 직접 애니메이션을 커스텀하고 있습니다.

위와 같이 다양한 방법으로 플러터에서 LinearProgressIndicator에 애니메이션을 적용할 수 있습니다.

참고 링크: [Flutter 공식 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)