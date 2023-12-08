---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator를 활용하여 데이터 다운로드 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

ProgressIndicator 위젯은 선형 및 원형 진행률 표시를 제공합니다. 이 중 CircularProgressIndicator를 사용하여 원형으로 다운로드 상태를 표시할 수 있습니다. 

아래는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class DownloadScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('다운로드 상태'),
      ),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            Text('데이터를 다운로드 중입니다...'),
            SizedBox(height: 16.0),
            CircularProgressIndicator(),
          ],
        ),
      ),
    );
  }
}
```

이 예제에서는 Scaffold의 body에 다운로드 상태를 나타내기 위해 CircularProgressIndicator를 사용하고 있습니다.

다음과 같이 코드를 실행하여 다운로드 상태를 시각적으로 표시할 수 있습니다.