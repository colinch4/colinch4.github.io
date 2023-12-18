---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 서버 요청 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 애플리케이션에서 사용자에게 서버 요청이 진행 중임을 시각적으로 표시하고 싶을 때, `LinearProgressIndicator` 위젯을 사용할 수 있습니다. 이 위젯은 작업이 진행되고 있는 동안 진행률 표시 막대를 보여줍니다.

이번 포스트에서는 Flutter 앱에서 서버 요청이 진행 중일 때 화면에 진행률을 보여주기 위해 `LinearProgressIndicator`를 어떻게 사용하는지 알아보겠습니다.

## 1. `LinearProgressIndicator` 위젯 추가

먼저, `LinearProgressIndicator` 위젯을 화면에 추가합니다.

```dart
import 'package:flutter/material.dart';

class MyScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('서버 요청 진행률 표시'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('서버 요청 중...'),
            SizedBox(height: 20),
            LinearProgressIndicator(),
          ],
        ),
      ),
    );
  }
}
```

`LinearProgressIndicator` 위젯을 사용하여 서버 요청 진행 중임을 사용자에게 알릴 수 있습니다.

## 2. 서버 요청 처리

서버 요청을 처리하는 코드를 작성할 때, 앞에서 정의한 `MyScreen` 위젯을 사용하여 화면을 보여주고, 요청이 완료될 때 화면을 갱신하도록 합니다. 예를 들어, 다음과 같이 `Future`를 사용하여 비동기로 서버 요청을 하고, 요청이 완료되면 화면을 갱신할 수 있습니다.

```dart
Future<void> _fetchDataFromServer() async {
  // 서버 요청 시작
  // ...

  await Future.delayed(Duration(seconds: 2)); // 2초간 가짜 요청 처리 시간을 가정

  // 서버 요청 완료
  // ...

  // 화면 갱신
  setState(() {
    // 갱신할 데이터 설정
  });
}
```

## 결론

이제 `LinearProgressIndicator`를 사용하여 Flutter 애플리케이션에서 서버 요청 진행률을 표시하는 방법에 대해 알아보았습니다. 사용자는 이를 통해 서버 요청이 진행 중임을 쉽게 파악할 수 있고, 앱이 반응하고 있다는 것을 알 수 있습니다.

참고: [Flutter LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)