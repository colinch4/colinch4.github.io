---
layout: post
title: "[flutter] 플러터(Flutter) 앱에서 Firebase Crashlytics를 활용하여 실시간 오류 알림을 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 플러터(Flutter) 앱에서 발생하는 오류를 실시간으로 모니터링하고, 오류가 발생할 경우 개발자에게 알림을 제공해주는 도구입니다. 이번 포스트에서는 플러터 앱에서 Firebase Crashlytics를 설정하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 생성하기

Firebase Console에 접속하여 새로운 프로젝트를 생성합니다. Firebase 프로젝트 생성에 대한 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup?platform=android)를 참고하세요.

## 2. Flutter 프로젝트에 Firebase 추가하기

Flutter 프로젝트에서 Firebase를 사용하기 위해 아래와 같은 작업을 수행해야 합니다.

### 2.1. `pubspec.yaml` 파일 수정하기

`pubspec.yaml` 파일에 Firebase와 Crashlytics 관련 라이브러리를 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.1  # Firebase Core
  firebase_crashlytics: ^2.4.1  # Firebase Crashlytics
```

### 2.2. Firebase 설정 파일 추가하기

Firebase Console에서 다운로드한 `google-services.json` 또는 `GoogleService-Info.plist` 파일을 Flutter 프로젝트의 `android/app` 폴더(Android) 또는 `ios/Runner` 폴더(iOS)에 추가합니다.

### 2.3. Firebase 초기화 코드 추가하기

Flutter 앱 시작 시 Firebase를 초기화하는 코드를 추가합니다. 

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 3. Firebase Crashlytics 설정하기

Firebase Crashlytics를 활성화하고, 오류 알림을 설정하기 위해 아래와 같은 작업을 수행합니다.

### 3.1. Crashlytics 초기화 코드 추가하기

앱이 시작될 때 Crashlytics를 초기화하는 코드를 추가합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() {
  // ...

  // Initialize Crashlytics
  FirebaseCrashlytics.instance.initialize();

  runApp(MyApp());
}
```

### 3.2. Flutter 오류 핸들러 설정하기

Flutter 앱에서 발생하는 오류를 캐치하여 Crashlytics에 보고하는 오류 핸들러를 설정합니다. 오류 핸들러는 main 함수 위에 추가하여야 합니다. 

```dart
// ...

FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

void main() {
  // ...
  
  runApp(MyApp());
}
```

## 4. 오류 테스트하기

이제 Firebase Crashlytics 설정이 완료되었습니다. 앱을 실행하여 오류를 유발하여 Firebase Console의 Crashlytics에서 오류 알림을 확인할 수 있습니다.

## 마무리

이번 포스트에서는 플러터(Flutter) 앱에서 Firebase Crashlytics를 활용하여 실시간 오류 알림을 설정하는 방법에 대해 알아보았습니다. Firebase Crashlytics는 앱의 안정성을 향상시키고 사용자 경험을 개선하는 데 매우 유용한 도구입니다. Firebase를 활용하여 앱의 오류를 신속하게 해결할 수 있도록 하세요.