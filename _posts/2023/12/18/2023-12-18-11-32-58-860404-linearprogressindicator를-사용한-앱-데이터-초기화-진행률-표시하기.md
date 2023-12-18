---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 앱 데이터 초기화 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

앱을 처음 실행할 때 데이터를 초기화해야 하는 경우가 있습니다. 이때 초기화 작업의 진행률을 사용자에게 시각적으로 표시하려면 `LinearProgressIndicator` 위젯을 활용할 수 있습니다. 이번 포스트에서는 Flutter 앱에서 `LinearProgressIndicator`를 사용하여 데이터 초기화 작업의 진행률을 표시하는 방법에 대해 알아보겠습니다.

## 1. `LinearProgressIndicator` 위젯 추가

가장 먼저, 앱의 초기화 작업을 수행하는 화면에 `LinearProgressIndicator` 위젯을 추가해야 합니다. 예를 들어, 다음과 같이 화면의 상단에 `LinearProgressIndicator`를 추가할 수 있습니다.
```dart
import 'package:flutter/material.dart';

class DataInitializationScreen extends StatefulWidget {
  @override
  _DataInitializationScreenState createState() => _DataInitializationScreenState();
}

class _DataInitializationScreenState extends State<DataInitializationScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('데이터 초기화'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              '데이터 초기화 중...',
            ),
            LinearProgressIndicator(), // 진행률 표시
          ],
        ),
      ),
    );
  }
}
```

## 2. 데이터 초기화 작업과 `LinearProgressIndicator` 연동

실제로 데이터 초기화 작업을 수행하는 부분에서는 `LinearProgressIndicator`의 진행률을 업데이트해줘어야 합니다. 일반적으로 비동기 함수 내에서 `LinearProgressIndicator`의 진행률을 업데이트하며, 예를 들면 다음과 같이 작성할 수 있습니다.
```dart
void initializeData() async {
  // 데이터 초기화 작업 수행
  int totalSteps = 10;
  for (int i = 0; i < totalSteps; i++) {
    await performIndividualStep(); // 각각의 단계 수행
    setState(() {
      // 진행률 업데이트
      _progress = (i + 1) / totalSteps;
    });
  }
}
```

위 코드에서 `performIndividualStep` 함수는 각각의 초기화 작업을 수행하고, `setState` 함수를 통해 `_progress` 값을 업데이트하여 `LinearProgressIndicator`의 진행률을 표시합니다.

## 3. 진행률 표시 화면

위의 코드를 이용하면 초기화 작업의 진행률을 표시하는 화면을 만들 수 있습니다. 사용자는 `LinearProgressIndicator`를 통해 초기화 작업이 얼마나 진행되었는지를 실시간으로 확인할 수 있게 됩니다.

이렇게하면 사용자가 앱이 작동 중임을 이해하고, 초기화 작업이 얼마나 남았는지 쉽게 파악할 수 있습니다. 이는 앱 초기 사용 경험을 향상시키는 데 도움이 될 것입니다.

나중에 앱의 초기화 작업이 변경되면, `LinearProgressIndicator`를 적절하게 업데이트하여 사용자에게 정확한 진행률을 제공할 수 있습니다.