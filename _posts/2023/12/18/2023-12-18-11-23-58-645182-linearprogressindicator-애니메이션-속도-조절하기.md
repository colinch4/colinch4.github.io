---
layout: post
title: "[flutter] LinearProgressIndicator 애니메이션 속도 조절하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter의 `LinearProgressIndicator`는 진행률 표시를 위한 간단하고 효과적인 위젯입니다. 기본적으로 이 위젯은 일정한 애니메이션 속도로 진행률 표시를 보여줍니다. 그러나 때때로 이 애니메이션 속도를 조절하고 싶을 수 있습니다.

이 블로그 포스트에서는 `LinearProgressIndicator` 위젯의 애니메이션 속도를 조절하는 방법을 알아보도록 하겠습니다.

## 1. 애니메이션 속도를 조절하는 방법

`LinearProgressIndicator`의 애니메이션 속도를 조절하려면 일반적으로 `LinearProgressIndicator`를 사용하는 부모 위젯에서 `AnimationController`를 정의하고, `LinearProgressIndicator`의 애니메이션을 해당 `AnimationController`와 연동시켜야 합니다.

아래는 `LinearProgressIndicator`의 애니메이션 속도를 조절하는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    AnimationController controller = AnimationController(
      duration: const Duration(milliseconds: 1000), // 애니메이션 기간 설정
      vsync: this, // 애니메이션 처리 방식 설정
    );

    return MaterialApp(
      home: Scaffold(
        body: Center(
          // LinearProgressIndicator를 AnimationController와 연동하여 애니메이션 속도를 조절
          child: LinearProgressIndicator(
            value: controller,
          ),
        ),
      ),
    );
  }
}
```

위의 예제 코드에서 `duration` 속성을 통해 애니메이션의 기간을 조절할 수 있습니다. 또한, `vsync` 속성은 `TickerProvider` 인터페이스를 구현한 클래스를 사용하여 화면 갱신 주기를 조절할 수 있습니다.

## 2. 마치며

이제 여러분은 `LinearProgressIndicator`의 애니메이션 속도를 조절하는 방법을 알게 되었습니다. 이를 통해 여러분의 앱에서 진행률 표시를 더욱 세밀하게 제어할 수 있을 것입니다.

더 많은 자세한 내용은 [공식 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)를 참고하시기 바랍니다.