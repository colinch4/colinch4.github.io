---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 빠른 네트워크 상태에 따른 변경상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

빠른 네트워크 상태에 따라 변하는 상태를 사용자에게 시각적으로 표시하는 것은 앱의 사용자 경험을 향상시키는 데 중요합니다. Flutter 앱에서는 CircularProgressIndicator를 사용하여 이러한 상태를 표시할 수 있습니다.

## 1. CircularProgressIndicator 사용하기

CircularProgressIndicator는 진행 중인 작업을 나타내는데 사용되는 일반적인 위젯입니다. 네트워크 요청이 진행 중일 때 이를 나타내기 위해 사용할 수 있습니다.

```dart
Center(
  child: CircularProgressIndicator(),
)
```

위의 예제는 네트워크 요청이 진행 중일 때 가운데에 회전하는 CircularProgress 인디케이터를 보여줍니다.

## 2. 빠른 네트워크 상태 감지

네트워크 상태를 감지하고, 연결 속도가 빨라질 때에 대한 조건을 정의합니다.

```dart
import 'package:connectivity/connectivity.dart';

var connectivityResult = await (Connectivity().checkConnectivity());
if (connectivityResult == ConnectivityResult.mobile) {
  // 모바일 데이터 네트워크가 연결될 때
} else if (connectivityResult == ConnectivityResult.wifi) {
  // WiFi 네트워크가 연결될 때
}
```

위의 코드에서 Connectivity 라이브러리를 사용하여 현재 네트워크 연결 상태를 확인합니다.

## 3. 네트워크 상태에 따른 UI 업데이트

네트워크 상태에 따라 UI를 업데이트하고 CircularProgress 인디케이터를 표시합니다.

```dart
bool _loading = false;

void fetchData() {
  setState(() {
    _loading = true; // 데이터를 가져오는 중에 CircularProgress 인디케이터를 보여줍니다.
  });
  
  // 데이터 가져오는 비동기 작업 수행

  setState(() {
    _loading = false; // 데이터를 가져오는 작업이 끝나면 CircularProgress 인디케이터를 숨깁니다.
  });
}

// Widget 빌드 메서드 안에서 CircularProgress 인디케이터를 표시합니다.
Center(
  child: _loading ? CircularProgressIndicator() : YourDataWidget(), 
)
```

위의 코드는 fetchData 메서드를 호출할 때 CircularProgress 인디케이터가 표시되고, 데이터를 가져오는 비동기 작업이 끝나면 인디케이터가 사라집니다.

CircularProgressIndicator를 사용하여 빠른 네트워크 상태에 따른 변경 상태를 효과적으로 표시할 수 있습니다. 사용자는 네트워크 작업이 진행 중임을 시각적으로 알 수 있고, 이는 앱의 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료
- [Flutter 공식 문서 - CircularProgressIndicator](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)
- [Connectivity 패키지 - Flutter Pub](https://pub.dev/packages/connectivity)