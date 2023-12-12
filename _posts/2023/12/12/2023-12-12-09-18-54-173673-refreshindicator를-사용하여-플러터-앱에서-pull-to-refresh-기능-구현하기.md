---
layout: post
title: "[flutter] RefreshIndicator를 사용하여 플러터 앱에서 Pull-to-Refresh 기능 구현하기"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

웹 페이지나 앱에서 스크롤을 당겨서 새로고침하는 기능은 사용자 경험에 많은 도움이 됩니다. 플러터에서는 `RefreshIndicator`를 사용하여 간단하게 Pull-to-Refresh 기능을 구현할 수 있습니다.

## 1. RefreshIndicator 위젯 추가

우선, Pull-to-Refresh 기능이 필요한 플러터 위젯을 `RefreshIndicator`로 감싸줍니다. 

```dart
RefreshIndicator(
  onRefresh: _handleRefresh,
  child: ListView(
    children: <Widget>[
      // 리스트 아이템들
    ],
  ),
)
```

`onRefresh` 콜백은 새로고침이 요청될 때 호출될 함수를 지정합니다.

## 2. RefreshIndicator 콜백 함수 구현

다음으로는 `onRefresh` 콜백 함수인 `_handleRefresh`를 구현합니다. 이 함수에서는 새로고침이 발생했을 때 수행해야 할 작업을 정의합니다.

```dart
Future<void> _handleRefresh() async {
  // 새로고침 동작 수행
  // 데이터 갱신 등의 작업
}
```

`_handleRefresh` 함수는 비동기로 동작해야 하므로 `Future<void>`를 반환해야 합니다.

## 3. Pull-to-Refresh 효과 제공

이제 앱을 실행하고 리스트를 당겨보면 `RefreshIndicator`가 활성화되어 Pull-to-Refresh 효과가 제공됩니다. 아래는 참고할 수 있는 예시 코드입니다.

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
          title: Text('Pull-to-Refresh Example'),
        ),
        body: RefreshIndicator(
          onRefresh: _handleRefresh,
          child: ListView(
            children: <Widget>[
              ListTile(title: Text('Item 1')),
              ListTile(title: Text('Item 2')),
              // 리스트 아이템들
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _handleRefresh() async {
    // 새로고침 동작 수행
    // 데이터 갱신 등의 작업
  }
}
```

위 예시 코드를 참고하여 `RefreshIndicator`를 사용하여 간단하게 Pull-to-Refresh 기능을 구현할 수 있습니다.

---

참고 문헌:
- [플러터 공식 문서 - RefreshIndicator](https://api.flutter.dev/flutter/material/RefreshIndicator-class.html)