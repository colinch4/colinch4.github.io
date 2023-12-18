---
layout: post
title: "[flutter] LinearProgressIndicator의 모양 커스텀하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter의 `LinearProgressIndicator`는 기본적으로 Material Design에 맞추어 디자인된 프로그래스 바를 제공합니다. 그러나 때로는 애플리케이션의 디자인에 맞게 커스텀한 프로그래스 바가 필요할 수 있습니다. 이 블로그 포스트에서는 `LinearProgressIndicator`의 모양을 커스텀하는 방법에 대해 다루겠습니다.

## 1. CustomLinearProgressIndicator 위젯 만들기

먼저, 커스텀한 `LinearProgressIndicator` 위젯을 만들어 보겠습니다. 

```dart
import 'package:flutter/material.dart';

class CustomLinearProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 10,
      child: LinearProgressIndicator(
        backgroundColor: Colors.grey[200],
        valueColor: AlwaysStoppedAnimation(Colors.blue),
      ),
    );
  }
}
```

위 코드에서는 `CustomLinearProgressIndicator` 라는 새로운 위젯을 만들어 `LinearProgressIndicator`를 커스텀한 모양으로 구현했습니다. `Container` 위젯을 사용하여 높이를 조절하고, `LinearProgressIndicator`의 배경 색상과 값의 색상을 각각 `Colors.grey[200]`와 `Colors.blue`로 설정했습니다.

## 2. CustomLinearProgressIndicator 사용하기

이제 위에서 만든 `CustomLinearProgressIndicator` 위젯을 다른 곳에서 사용해 보겠습니다.

```dart
class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Custom Linear Progress Indicator'),
      ),
      body: Center(
        child: CustomLinearProgressIndicator(),
      ),
    );
  }
}
```

`CustomLinearProgressIndicator` 위젯을 다른 위젯 안에서 사용할 수 있습니다. 위의 예시에서는 `MyHomePage` 위젯 안에서 `CustomLinearProgressIndicator`를 사용하여 화면 중앙에 커스텀 프로그래스 바를 보여주도록 구현했습니다.

## 3. 커스텀 프로그래스 바 스타일링하기

`CustomLinearProgressIndicator`의 스타일을 더욱 세밀하게 구성하려면 `LinearProgressIndicator`의 다양한 속성을 활용하여 원하는 모양으로 커스텀할 수 있습니다. 이때 `LinearProgressIndicator`의 속성인 `value`와 `backgroundColor` 등을 활용하여 프로그래스 바의 형태를 세밀하게 조절할 수 있습니다.

간단한 예시로 `value`를 조절하여 프로그래스 바의 진행 정도를 나타내는 부분을 커스텀할 수 있습니다.

```dart
LinearProgressIndicator(
  value: 0.5,
  backgroundColor: Colors.grey[200],
  valueColor: AlwaysStoppedAnimation(Colors.blue),
)
```

위 코드에서 `value`를 `0.5`로 설정하여 프로그래스 바의 진행 정도를 50%로 나타내도록 하였습니다.

이처럼 `LinearProgressIndicator`의 속성들을 활용하여 프로그래스 바의 모양을 세밀하게 커스텀할 수 있습니다.

위의 예시를 참고하여, 필요에 따라 `LinearProgressIndicator`를 더욱 다양하고 세밀하게 커스텀할 수 있을 것입니다.

## 참고 자료
- [Flutter API 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)
- [Flutter Cookbook - Progress indicators](https://flutter.dev/docs/cookbook/misc/progress-indicators)