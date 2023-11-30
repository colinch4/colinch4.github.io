---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Performance 모니터링하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 클라우드 기반의 모바일 백엔드 서비스로, Firebase Performance Monitoring을 통해 앱의 성능을 모니터링할 수 있습니다. 이번 포스트에서는 플러터 앱에서 Firebase_core를 사용하여 Firebase Performance Monitoring을 설정하는 방법에 대해 알아보겠습니다.

## Firebase Performance Monitoring 설정하기

Firebase Performance Monitoring을 사용하기 위해서는 Firebase 프로젝트를 생성하고 Firebase SDK를 설정해야 합니다. Firebase 프로젝트를 생성하고 Firebase SDK를 설정하는 방법은 Firebase 공식 문서를 참고하시기 바랍니다.

1. `pubspec.yaml` 파일을 열고 dependencies 섹션에 다음 코드를 추가합니다:

```dart
dependencies:
  firebase_core: ^0.7.0
  firebase_performance: ^0.6.0
```

2. `pubspec.yaml` 파일이 업데이트 되었으므로, 터미널에서 `flutter pub get` 명령을 실행하여 필요한 패키지를 가져옵니다.

3. 플러터 앱의 진입점인 `main.dart` 파일을 열고 다음 코드를 추가합니다:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_performance/firebase_performance.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Firebase 초기화
  await Firebase.initializeApp();
  
  // Firebase Performance Monitoring 시작
  await FirebasePerformance.instance.setPerformanceCollectionEnabled(true);

  runApp(MyApp());
}
```

위 코드에서 `await Firebase.initializeApp()`는 Firebase SDK를 초기화하는 역할을 합니다. `await FirebasePerformance.instance.setPerformanceCollectionEnabled(true)`는 Firebase Performance Monitoring을 활성화하는 역할을 합니다.

4. Firebase Performance Monitoring을 사용할 페이지나 함수 내에서 다음 코드를 추가하여 성능을 모니터링할 수 있습니다:

```dart
final Trace myTrace = FirebasePerformance.instance.newTrace('my_trace');
myTrace.start();

// 성능 모니터링을 원하는 작업 실행

myTrace.stop();
```

위 코드에서는 `FirebasePerformance.instance.newTrace('my_trace')`를 통해 성능 모니터링을 위한 Trace 객체를 생성하고, `myTrace.start()`와 `myTrace.stop()`을 사용하여 성능을 모니터링할 범위를 설정합니다.

## 마치며

이번 포스트에서는 Firebase_core를 사용하여 플러터 앱에서 Firebase Performance Monitoring을 설정하는 방법에 대해 알아보았습니다. Firebase Performance Monitoring을 통해 앱의 성능을 모니터링하여 효율적으로 최적화하고 사용자 경험을 향상시킬 수 있습니다. Firebase 공식 문서에서 더 많은 기능과 사용법을 확인해보세요.