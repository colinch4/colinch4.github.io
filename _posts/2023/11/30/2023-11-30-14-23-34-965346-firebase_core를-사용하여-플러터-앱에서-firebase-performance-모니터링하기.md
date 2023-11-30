---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Performance 모니터링하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Performance Monitoring은 앱의 성능을 모니터링하고 문제를 식별하는 데 도움이되는 강력한 도구입니다. 이 기능을 사용하면 앱의 네트워크 요청, 데이터베이스 작업, 화면 전환 및 기타 작업의 성능을 측정하고 비교할 수 있습니다. 이번에는 플러터 앱에서 Firebase Performance Monitoring을 활용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Performance Monitoring을 사용하려면 먼저 [Firebase 콘솔](https://console.firebase.google.com/)에서 프로젝트를 생성해야 합니다. 프로젝트를 생성한 후, 앱을 추가하고 구성 파일 (`google-services.json` 또는 `GoogleService-Info.plist`)을 다운로드하여 프로젝트의 `android/app` 또는 `ios` 폴더에 추가합니다.

플러터 프로젝트의 `pubspec.yaml` 파일에서 `firebase_core` 및 `firebase_performance` 패키지를 추가합니다:
```yaml
dependencies:
  firebase_core: ^1.0.3
  firebase_performance: ^0.6.0+13
```

## 2. Firebase Core 설정

Firebase Performance Monitoring을 사용하려면 먼저 Firebase Core를 초기화해야 합니다. `main.dart` 파일에서 다음과 같이 Firebase Core를 설정합니다:
```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 3. Firebase Performance 시작, 정지 및 데이터 전송

Firebase Performance Monitoring을 활성화하려면 앱의 시작 및 종료 시간을 추적해야 합니다. `main.dart`에서 앱 시작 시 `FirebasePerformance.instance.setPerformanceCollectionEnabled(true)`를 호출하여 Performance Monitoring을 시작하고, 앱 종료 시 `FirebasePerformance.instance.setPerformanceCollectionEnabled(false)`를 호출하여 Performance Monitoring을 중지합니다.

Firebase Performance Monitoring은 자동으로 네트워크 요청 및 데이터베이스 작업에 대한 정보를 캡처하지만, 세부적인 측정을 위해 사용자 정의 트레이스를 만들 수도 있습니다. 예를 들어, 원하는 부분에서 다음과 같이 트레이스를 만들 수 있습니다:
```dart
import 'package:firebase_performance/firebase_performance.dart';

void fetchData() async {
  final trace = FirebasePerformance.instance.newHttpMetric('GET', 'https://api.example.com/data');
  await trace.start();

  // 네트워크 요청 수행

  await trace.stop();
  await trace.putAttribute('status', 'success');
}
```

## 4. Firebase Performance 데이터 확인

Firebase 콘솔에서 앱의 Performance Monitoring 탭을 통해 Firebase Performance 데이터를 확인할 수 있습니다. 콘솔에서 성능 데이터를 시각적으로 확인하고 통찰력을 얻을 수 있습니다. 이를 통해 앱의 성능 문제를 식별하고 최적화할 수 있습니다.

Firebase Performance Monitoring을 사용하여 플러터 앱의 성능을 모니터링하고 개선하는 방법에 대해 알아보았습니다. Firebase Performance Monitoring 도큐먼트를 참조하여 더 자세한 내용을 탐색할 수 있습니다.

**참조:**
- [Firebase Performance Monitoring 도큐먼트](https://firebase.google.com/docs/perf-mon)
- [Firebase Core 패키지](https://pub.dev/packages/firebase_core)
- [Firebase Performance 패키지](https://pub.dev/packages/firebase_performance)