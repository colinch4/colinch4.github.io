---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 해결 및 성능 향상하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 오류를 실시간으로 모니터링하고, 오류 발생 시 상세한 오류 보고서를 제공하여 오류 해결을 도와주는 도구입니다. 이 글에서는 Firebase Crashlytics를 사용하여 Flutter 앱의 오류를 해결하고 성능을 향상시키는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Crashlytics를 사용하기 위해서는 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에서 프로젝트를 생성하고, 안드로이드와 iOS 앱을 등록해야 합니다. 각 플랫폼별로 앱의 패키지명과 설정 파일을 다운로드 받아야 합니다.

## 2. Flutter 앱에 Firebase Crashlytics 추가하기

### 2.1. Firebase SDK 추가하기

먼저, Firebase SDK를 Flutter 앱에 추가해야 합니다. `pubspec.yaml` 파일을 열고 `firebase_core`, `firebase_crashlytics` 패키지를 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.11.0
  firebase_crashlytics: ^2.10.0
```

`pubspec.yaml` 파일을 저장한 후, 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드 받습니다.

### 2.2. Firebase Crashlytics 초기화하기

Firebase Crashlytics를 초기화하기 위해 `main()` 함수에서 `Firebase.initializeApp()` 메서드와 `FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled()` 메서드를 호출해야 합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  runApp(MyApp());
}
```

### 2.3. 앱 빌드하기

이제 Flutter 앱을 빌드해야 합니다. 터미널에서 `flutter build` 명령어를 실행하여 앱을 빌드합니다.

## 3. Firebase Crashlytics 사용하기

Firebase Crashlytics를 사용하여 앱의 오류를 실시간으로 모니터링하고 오류 보고서를 받을 수 있습니다. 오류 발생 시 다음과 같은 방법으로 오류를 해결할 수 있습니다.

### 3.1. 오류 로깅하기

Firebase Crashlytics는 자동으로 앱의 예외를 잡아내지만, 명시적으로 오류를 로깅할 수도 있습니다. 오류가 발생할 수 있는 곳에서 `FirebaseCrashlytics.instance.recordError()` 메서드를 호출하여 오류를 로깅합니다.

```dart
try {
  // 오류가 발생할 수 있는 코드
} catch (e, stackTrace) {
  FirebaseCrashlytics.instance.recordError(e, stackTrace);
}
```

### 3.2. 사용자 정의 데이터 로깅하기

Firebase Crashlytics는 사용자 정의 데이터를 로깅하여 오류 보고서에 추가 정보를 제공할 수 있습니다. `FirebaseCrashlytics.instance.setCustomKey()` 메서드를 사용하여 사용자 정의 데이터를 로깅합니다.

```dart
FirebaseCrashlytics.instance.setCustomKey('user_id', 'user1234');
FirebaseCrashlytics.instance.setCustomKey('authenticated', true);
```

### 3.3. 오류 해결하기

Firebase Crashlytics를 사용하여 오류를 해결할 때는 Firebase 콘솔에서 제공하는 다양한 도구와 정보를 활용할 수 있습니다. 오류 보고서를 통해 오류의 발생 위치 및 스택 트레이스를 확인하고, 해당 부분을 수정하여 앱의 오류를 해결할 수 있습니다.

## 4. 성능 향상을 위한 Firebase Crashlytics 사용하기

Firebase Crashlytics는 앱의 성능을 분석하여 성능 문제의 원인을 찾을 수 있습니다. Firebase 콘솔의 성능 탭에서 앱의 성능 데이터를 확인하고, 성능 저하의 원인을 분석하여 앱의 성능을 향상시킬 수 있습니다.

## 참고 자료

- [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)
- [FlutterFire GitHub 저장소](https://github.com/FirebaseExtended/flutterfire/tree/master/packages/firebase_crashlytics)

Firebase Crashlytics를 사용하여 Flutter 앱의 오류를 해결하고 성능을 향상시킬 수 있습니다. Firebase Crashlytics를 통해 앱의 사용자 경험을 개선하고, 안정성과 신뢰성을 높일 수 있습니다.