---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 데이터 로딩 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

안녕하세요! 이번에는 **flutter** 앱에서 **LinearProgressIndicator**를 사용하여 데이터 로딩 진행률을 표시하는 방법에 대해 알아보겠습니다.

## 1. **LinearProgressIndicator**란?

**LinearProgressIndicator**는 일련의 작업이나 데이터 로딩이 진행 중임을 시각적으로 사용자에게 표시해주는 위젯입니다. 주로 데이터가 로딩되는 동안에 화면에 표시하여 사용자가 잠시의 대기 시간 동안도 앱이 활동 중임을 인지할 수 있도록 도와줍니다.

## 2. **LinearProgressIndicator** 사용하기

**LinearProgressIndicator**를 사용하는 예제 코드를 통해 간단한 사용법을 살펴보겠습니다.

```dart
import 'package:flutter/material.dart';

class MyLoadingScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('로딩 중...'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('데이터를 로딩하는 중입니다.'),
            SizedBox(height: 16.0),
            LinearProgressIndicator(), // LinearProgressIndicator 표시
          ],
        ),
      ),
    );
  }
}
```

## 3. **LinearProgressIndicator**에 로딩 진행률 표시하기

만약 실제 로딩 진행률을 표시하고 싶다면, **LinearProgressIndicator**의 **value** 속성을 활용할 수 있습니다. 이 값을 조절하여 실제 데이터 로딩 상황에 맞게 진행률을 표시할 수 있습니다.

```dart
LinearProgressIndicator(
  value: 0.5, // 로딩 진행률 50%
)
```

## 마치며

**LinearProgressIndicator**는 데이터 로딩이나 작업 진행 중에 사용자에게 시각적인 피드백을 제공하는데 유용한 위젯입니다. 데이터 로딩이나 작업 진행 시에 활용하여 사용자 경험을 향상시킬 수 있습니다. 부가적으로 **value** 속성을 이용하여 실제 진행률을 나타내는 것도 중요하니 참고하시기 바랍니다.

이상으로 **flutter**에서 **LinearProgressIndicator**를 사용한 데이터 로딩 진행률 표시에 대해 알아보았습니다. 감사합니다!