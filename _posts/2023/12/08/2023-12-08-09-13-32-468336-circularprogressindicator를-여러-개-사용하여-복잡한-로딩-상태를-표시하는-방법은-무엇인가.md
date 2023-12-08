---
layout: post
title: "[flutter] CircularProgressIndicator를 여러 개 사용하여 복잡한 로딩 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

개발 중인 앱에서 여러 가지 작업을 동시에 진행할 때 사용자에게 로딩 상태를 시각적으로 보여주는 것은 중요합니다. 이를 위해 CircularProgressIndicator를 사용하여 진행 상태를 시각적으로 표현할 수 있습니다. 만약 여러 가지 작업이 동시에 이루어지고 로딩 상태를 사용자에게 알리기 위해 여러 개의 CircularProgressIndicator를 사용하고 싶다면, 아래의 방법을 참고하세요.

## 다중 CircularProgressIndicator 사용하기

다음과 같이 Column을 사용하여 여러 개의 CircularProgressIndicator를 배치할 수 있습니다. 이를 통해 각 작업의 진행 상태를 별도로 표시할 수 있습니다.

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
          title: Text('다중 CircularProgressIndicator 예제'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              CircularProgressIndicator(),
              SizedBox(height: 20),
              CircularProgressIndicator(),
              SizedBox(height: 20),
              CircularProgressIndicator(),
            ],
          ),
        ),
      ),
    );
  }
}
```

위의 예제에서는 Column과 SizedBox를 사용하여 여러 개의 CircularProgressIndicator를 수직으로 배치하고 각각의 사이에 공간을 주었습니다.

이렇게 하면 여러 작업의 로딩 상태를 동시에 나타낼 수 있습니다.

## 마무리

여러 개의 CircularProgressIndicator를 사용하여 복잡한 작업의 로딩 상태를 표시하는 방법을 알아보았습니다. 이를 통해 사용자에게 각 작업의 진행 상태를 시각적으로 보여줄 수 있습니다.

더 많은 Flutter 관련 정보를 원하시면 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.