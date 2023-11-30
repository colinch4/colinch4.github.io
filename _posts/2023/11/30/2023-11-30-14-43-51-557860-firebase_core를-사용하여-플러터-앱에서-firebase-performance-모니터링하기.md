---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Performance 모니터링하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들에게 확장성이 높고 신뢰성이 있는 백엔드 서비스를 제공하는 Google의 플랫폼입니다. Firebase Performance Monitoring은 앱의 성능을 모니터링하고 최적화하기 위한 강력한 도구를 제공합니다. 이번 포스트에서는 Flutter 앱에서 Firebase Performance Monitoring을 활용하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정하기

Firebase Performance Monitoring을 사용하려면 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에서 프로젝트를 생성한 뒤, 프로젝트의 iOS 및 Android 앱을 추가해주세요. 그리고 Firebase SDK를 설정하여 앱에 Firebase를 연동하세요.

## 2. firebase_performance 패키지 추가하기

플러터 앱에서 Firebase Performance Monitoring을 사용하기 위해서는 `firebase_performance` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 다음을 추가해주세요:

```yaml
dependencies:
  firebase_performance: ^X.X.X
```

여기서 `X.X.X`에는 사용하고 있는 Firebase Performance Monitoring SDK의 버전을 입력하면 됩니다.

## 3. Firebase_core와 연동하기

먼저, `firebase_core` 패키지를 사용하여 Firebase를 앱에 연동해야 합니다. `firebase_core` 패키지를 추가하려면 `pubspec.yaml` 파일에 다음을 추가해야 합니다:

```yaml
dependencies:
  firebase_core: ^X.X.X
```

여기서 `X.X.X`에는 사용하고 있는 Firebase SDK의 버전을 입력하면 됩니다.

그리고 `main.dart` 파일에서 다음 코드를 추가해 Firebase를 초기화합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // Firebase 초기화
  Future<void> initializeFirebase() async {
    await Firebase.initializeApp();
  }

  @override
  Widget build(BuildContext context) {
    initializeFirebase();
    return MaterialApp(
      title: 'Flutter Firebase Performance Monitoring',
      home: HomePage(),
    );
  }
}
```

## 4. Firebase Performance 모니터링 사용하기

이제 Firebase Performance Monitoring을 사용할 준비가 되었습니다. 성능을 모니터링하고 싶은 부분의 코드를 감싸는 방법은 다음과 같습니다:

```dart
import 'package:firebase_performance/firebase_performance.dart';

void myFunction() {
  final Trace myTrace = FirebasePerformance.instance.newTrace('my_trace');
  myTrace.start();
  
  // 성능을 모니터링하고 싶은 코드 작성
  
  myTrace.stop();
}
```

Trace 객체를 생성한 뒤 `start()`와 `stop()` 메서드로 성능을 모니터링할 코드를 감쌉니다. 이렇게 하면 해당 코드 블록의 실행 시간과 성능 데이터가 Firebase Performance Monitoring 콘솔에서 확인할 수 있습니다.

## 마무리

이제 Firebase Performance Monitoring을 통해 플러터 앱의 성능을 효과적으로 모니터링할 수 있게 되었습니다. Firebase Performance Monitoring의 다양한 기능을 활용하여 앱의 성능을 최적화할 수 있습니다. 자세한 내용은 [Firebase Performance Monitoring 문서](https://firebase.flutter.dev/docs/performance/overview)를 참고하세요.