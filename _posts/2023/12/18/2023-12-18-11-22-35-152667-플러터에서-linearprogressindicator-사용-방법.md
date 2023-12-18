---
layout: post
title: "[flutter] 플러터에서 LinearProgressIndicator 사용 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱에서 작업이나 데이터 로딩 상태를 알려주기 위해 **LinearProgressIndicator**를 사용할 수 있습니다.

## LinearProgressIndicator란?

**LinearProgressIndicator**는 작업이 진행 중임을 시각적으로 나타내기 위해 사용됩니다. 일반적으로 작업 완료에 따라 진행 표시줄이 채워지며 사용자에게 대기 중임을 알려줍니다.

## LinearProgressIndicator 사용 방법

다음은 플러터(Flutter) 코드에서 **LinearProgressIndicator**를 사용하는 간단한 예제입니다.

```dart
import 'package:flutter/material.dart';

class MyLinearProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Linear Progress Indicator Example'),
      ),
      body: Center(
        child: LinearProgressIndicator(),
      ),
    );
  }
}

void main() => runApp(MaterialApp(home: MyLinearProgressIndicator()));
```

위 코드에서는 **LinearProgressIndicator** 위젯을 사용하여 중앙에 진행 표시줄을 나타내는 간단한 예제를 살펴볼 수 있습니다.

## 요약

플러터(Flutter)에서 **LinearProgressIndicator**를 사용하여 작업이 진행 중임을 시각적으로 표시할 수 있습니다. 위 예제를 참고하여 앱의 작업 상태를 사용자에게 효과적으로 전달할 수 있습니다.

이상으로 **LinearProgressIndicator**를 사용하는 방법에 대한 간략한 안내였습니다.