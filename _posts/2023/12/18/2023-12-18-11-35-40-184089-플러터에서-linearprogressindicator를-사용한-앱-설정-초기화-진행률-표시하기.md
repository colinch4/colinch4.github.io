---
layout: post
title: "[flutter] 플러터에서 LinearProgressIndicator를 사용한 앱 설정 초기화 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

앱이 처음 시작될 때 설정을 초기화하는 과정은 일반적으로 시간이 오래 걸리며, 사용자는 초기화가 완료될 때까지 기다려야 합니다. 이러한 상황에서 사용자에게 초기화 진행 상황을 시각적으로 표시하는 것은 좋은 사용자 경험을 제공할 수 있습니다. 이를 위해 플러터에서는 LinearProgressIndicator 위젯을 사용하여 초기화 진행률을 표시할 수 있습니다.

## LinearProgressIndicator란?
`LinearProgressIndicator`는 작업이 진행되고 있음을 시각적으로 나타내는 데 사용되는 플러터 위젯입니다. 작업의 완료 상태에 따라 표시되는 눈금이 움직입니다.

## 플러터 앱에서 LinearProgressIndicator 사용하기
플러터에서 `LinearProgressIndicator` 위젯을 사용하여 초기화 진행률을 표시하는 방법을 살펴보겠습니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Initialization Progress'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text('Initializing...'),
              LinearProgressIndicator(),
            ],
          ),
        ),
      ),
    );
  }
}
```

위 코드는 앱이 초기화되는 동안 `LinearProgressIndicator`를 화면에 표시하는 간단한 앱을 보여줍니다. 

## 결론
`LinearProgressIndicator`는 앱 초기화나 긴 작업 진행 상황을 사용자에게 시각적으로 전달하는 데 유용한 플러터 위젯입니다. 앱의 사용자 경험을 향상시키기 위해 초기화나 작업 진행 상황을 표시해야 하는 경우, `LinearProgressIndicator`를 적절히 활용하여 사용자에게 편리하고 직관적인 경험을 제공할 수 있습니다.