---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 비동기 처리 상태를 통지하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

`CircularProgressIndicator`는 주로 작업이 완료될 때까지 사용자에게 진행 상태를 시각적으로 알려주는 데 사용됩니다. 이를 사용하기 위해 일반적으로 다음과 같은 패턴을 따릅니다:

1. **비동기 처리 작업 시작**: 비동기 처리 작업을 시작할 때 `CircularProgressIndicator`를 화면에 표시합니다.
2. **비동기 처리 완료**: 비동기 처리가 완료되면 `CircularProgressIndicator`를 숨깁니다.

예를 들어, `FutureBuilder` 위젯을 사용하여 비동기 작업을 처리하고 결과에 따라 `CircularProgressIndicator`를 표시하거나 숨길 수 있습니다. 다음은 간단한 예제 코드입니다:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  Future<bool> fetchData() {
    return Future.delayed(Duration(seconds: 2), () => true); // 예시 비동기 처리 작업
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('CircularProgressIndicator 예제'),
      ),
      body: FutureBuilder(
        future: fetchData(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator()); // 비동기 처리 중에 CircularProgressIndictor 표시
          } else {
            // 비동기 처리 완료 후에 화면을 구성
            return Center(child: Text('데이터 로딩 완료'));
          }
        },
      ),
    );
  }
}
```
위의 예제 코드는 `CircularProgressIndicator`를 사용하여 비동기 처리 상태를 통지하는 방법을 보여줍니다. `fetchData` 함수는 2초 후에 `true`를 반환하는 비동기 처리 작업을 모방합니다. 이 작업 중에는 `CircularProgressIndicator`가 표시되고, 작업이 완료되면 "데이터 로딩 완료"라는 텍스트가 화면에 표시됩니다.

더 자세한 내용은 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.