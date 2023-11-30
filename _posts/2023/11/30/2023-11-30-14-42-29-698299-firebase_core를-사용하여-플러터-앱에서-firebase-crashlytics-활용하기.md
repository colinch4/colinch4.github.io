---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Crashlytics 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 안정성 및 이용성 문제를 식별하고 모니터링하기 위한 강력한 도구입니다. 플러터 앱에서 Crashlytics를 사용하기 위해 Firebase_core를 설정하는 방법에 대해 알아보겠습니다.

## 목차

1. Firebase_core 패키지 추가하기
2. Firebase 프로젝트 설정
3. Firebase_core 초기화하기
4. Crashlytics 설정
5. 예외 보고하기
6. 결과 확인하기

## 1. Firebase_core 패키지 추가하기

먼저, 플러터 프로젝트의 `pubspec.yaml` 파일에서 `firebase_core` 패키지를 추가해야 합니다. 다음 코드를 `dependencies` 항목에 추가하세요.

```yaml
dependencies:
  firebase_core: ^1.0.0
```

## 2. Firebase 프로젝트 설정

Firebase 콘솔에서 새 프로젝트를 생성하고, 앱을 추가해야 합니다. 해당 앱의 패키지 이름을 입력하고, `google-services.json` 파일을 다운로드하세요.

## 3. Firebase_core 초기화하기

플러터 앱에서 Firebase를 사용하기 위해, `main.dart` 파일에서 Firebase_core를 초기화해야 합니다. 다음 코드를 `main` 함수의 첫 줄에 추가하세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 4. Crashlytics 설정

`main.dart` 파일에 다음 코드를 추가하여 Crashlytics를 설정하세요.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
    WidgetsFlutterBinding.ensureInitialized();
    await Firebase.initializeApp();
    FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
    runApp(MyApp());
}
```

## 5. 예외 보고하기

Crashlytics는 앱에서 발생하는 예외를 자동으로 감지하고 보고합니다. 하지만, 특정 예외를 수동으로 보고하고 싶을 때도 있습니다. 다음은 수동으로 예외를 보고하는 방법입니다.

```dart
try {
  // 예외가 발생할 수 있는 부분
} catch (e, stackTrace) {
  FirebaseCrashlytics.instance.recordError(e, stackTrace);
}
```

## 6. 결과 확인하기

Crashlytics를 사용하면 Firebase 콘솔에서 앱의 예외 및 이용성 데이터를 확인할 수 있습니다. 콘솔에서 개별 예외를 확인하고 분석하여 앱의 안정성을 향상시킬 수 있습니다.

Firebase Crashlytics를 사용하여 플러터 앱의 안정성을 강화하고 사용성 문제를 식별하는 방법에 대해 알아보았습니다. 이를 통해 앱의 품질을 개선하고 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [FlutterFire documentation](https://firebase.flutter.dev/)
- [Firebase Crashlytics documentation](https://firebase.google.com/docs/crashlytics)