---
layout: post
title: "[flutter] 플러터에서 다중 LinearProgressIndicator 구현 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱을 개발하다 보면 여러 작업의 진행 상황을 동시에 볼 수 있게 하고 싶을 때가 있습니다. 이때 **다중 LinearProgressIndicator**를 사용하여 여러 작업의 진행률을 한 눈에 확인할 수 있습니다.

다중 LinearProgressIndicator를 플러터에서 구현하는 방법을 알아보겠습니다.

## 1. 다중 LinearProgressIndicator 위젯 만들기

우선, 코드 상에서 다중 LinearProgressIndicator 위젯을 만들어보겠습니다. 

```dart
import 'package:flutter/material.dart';

class MultipleProgressIndicators extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: <Widget>[
        LinearProgressIndicator(value: 0.5),
        LinearProgressIndicator(value: 0.3),
        LinearProgressIndicator(value: 0.8),
      ],
    );
  }
}
```

위의 코드에서는 `MultipleProgressIndicators` 위젯을 만들고, `Column` 위젯을 사용하여 세 개의 `LinearProgressIndicator`를 배치했습니다. 각 `LinearProgressIndicator`는 각각의 진행률을 표시합니다.

## 2. 다중 LinearProgressIndicator 사용하기

만든 `MultipleProgressIndicators` 위젯을 다른 화면에서 사용하여 다중 진행률을 확인할 수 있습니다.

```dart
import 'package:flutter/material.dart';
import 'multiple_progress_indicators.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('다중 진행률 확인'),
        ),
        body: Center(
          child: MultipleProgressIndicators(),
        ),
      ),
    );
  }
}
```

위의 예시 코드에서 `MultipleProgressIndicators`를 화면에 나타내기 위해 `Center` 위젯을 사용했습니다.

이제 여러 작업의 진행 상황을 효과적으로 시각화할 수 있는 다중 LinearProgressIndicator를 구현하였습니다.

플러터에서는 위와 같이 간단하게 다중 LinearProgressIndicator를 구현할 수 있습니다.

참고자료: 
- [Flutter 공식 문서](https://flutter.dev/docs)
- ["Flutter in Action" (Eric Windmill 저)](https://www.manning.com/books/flutter-in-action)