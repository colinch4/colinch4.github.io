---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 실시간 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter에서 `LinearProgressIndicator`는 작업의 진행률을 시각적으로 표시하는 데 사용됩니다. 이를 통해 사용자에게 작업이 얼마나 완료되었는지 표시할 수 있습니다.

## LinearProgressIndicator란?

`LinearProgressIndicator`는 진행률을 수평으로 나타내는 위젯으로, 작업의 완료 정도를 시각적으로 표현할 때 사용됩니다. 사용자가 오랜 시간을 기다려야 하는 작업을 수행할 때 유용하게 활용될 수 있습니다.

## Flutter 앱에서 LinearProgressIndicator 사용하기

Flutter 앱에서 `LinearProgressIndicator`를 사용하는 방법은 매우 간단합니다. 아래는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('LinearProgressIndicator 예제'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text('작업이 진행 중입니다.'),
              LinearProgressIndicator(),
            ],
          ),
        ),
      ),
    );
  }
}
```

위 코드를 이용하여 앱을 실행하면 화면에 "작업이 진행 중입니다."와 함께 `LinearProgressIndicator`가 표시됩니다.

이제 여러분의 Flutter 앱에서 `LinearProgressIndicator`를 사용하여 시각적인 진행률을 표시해 보세요!

## 결론

`LinearProgressIndicator`는 Flutter 앱에서 작업의 진행률을 나타내는 데 유용한 위젯입니다. 앱에서 오랜 시간이 소요되는 작업을 수행할 때 사용자에게 진행 상황을 시각적으로 보여주어 사용자 경험을 향상시킬 수 있습니다.

편리한 사용과 유용한 시각적 요소를 제공하는 `LinearProgressIndicator`를 활용하여 여러분의 Flutter 앱을 더욱 현대적이고 사용자 친화적으로 만들어보세요.