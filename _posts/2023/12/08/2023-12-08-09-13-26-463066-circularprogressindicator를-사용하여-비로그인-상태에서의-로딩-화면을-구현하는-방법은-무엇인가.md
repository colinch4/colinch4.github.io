---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 비로그인 상태에서의 로딩 화면을 구현하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

어플리케이션에서 데이터를 불러오는 동안에 로딩 화면을 표시하는 것은 사용자 경험을 향상시키는 데 중요합니다. Flutter에서는 CircularProgressIndicator를 사용하여 간단하게 로딩 화면을 구현할 수 있습니다.

## 1. CircularProgressIndicator 추가

먼저, 로딩 화면을 표시할 화면의 Widget에 CircularProgressIndicator를 추가합니다. 예를 들어, 다음과 같이 사용할 수 있습니다.

```dart
import 'package:flutter/material.dart';

class LoadingScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: CircularProgressIndicator(),
      ),
    );
  }
}
```

## 2. 비로그인 상태에서 호출

다음으로, 비로그인 상태에서 데이터를 불러올 때 LoadingScreen을 호출하여 로딩 화면을 표시합니다. 예를 들어, 비로그인 상태에서 데이터를 불러오는 로직을 수행하는 함수 내에서 LoadingScreen을 호출할 수 있습니다.

```dart
void fetchData() {
  // 사용자가 로그인되지 않은 경우
  if (!isLoggedIn) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => LoadingScreen(),
      ),
    );

    // 데이터 불러오는 로직 수행
    // ...
  }
}
```

이제, 사용자가 로그인되지 않은 상태에서 데이터를 불러올 때 CircularProgressIndicator를 표시하는 로딩 화면을 구현할 수 있습니다.

이 방법을 통해 사용자가 데이터가 로딩되는 동안에 어플리케이션이 멈춰있지 않고 진행 중임을 알 수 있으며, 사용자 경험을 향상시킬 수 있습니다.

참고: https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html