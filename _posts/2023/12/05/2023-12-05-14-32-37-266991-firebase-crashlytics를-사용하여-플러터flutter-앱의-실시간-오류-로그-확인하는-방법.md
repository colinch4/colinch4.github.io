---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 실시간 오류 로그 확인하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Flutter는 Google의 개발한 UI 프레임워크로, 크로스 플랫폼 앱 개발을 가능하게 해줍니다. Firebase는 Google의 클라우드 기반 개발 플랫폼으로, 다양한 기능을 제공합니다. 이 블로그 포스트에서는 Flutter 앱에서 Firebase Crashlytics를 사용하여 실시간 오류 로그를 확인하는 방법에 대해 설명하겠습니다.

Firebase Crashlytics는 앱에서 발생하는 오류를 실시간으로 모니터링하고 기록하는 도구입니다. 앱이 출시된 후에도 오류가 발생하면 신속하게 확인하여 개선할 수 있도록 도와줍니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 로그인하고, 프로젝트를 생성합니다.
2. 프로젝트 설정으로 이동하고, Flutter 앱을 추가합니다.
3. 프로젝트의 Firebase 설정 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 다운로드합니다.

## Flutter 프로젝트 설정

1. Flutter 프로젝트의 `pubspec.yaml` 파일에서 `firebase_crashlytics` 의존성을 추가합니다:

   ```yaml
   dependencies:
     firebase_core: 
     firebase_crashlytics:
   ```

2. 터미널 창에서 다음 명령을 실행하여 모든 종속성을 업데이트합니다:

   ```
   flutter pub get
   ```

3. Flutter 앱의 `main.dart` 파일에서 Firebase를 초기화합니다:

   ```dart
   import 'package:firebase_core/firebase_core.dart';

   void main() async {
     WidgetsFlutterBinding.ensureInitialized(); 
     await Firebase.initializeApp();
     runApp(MyApp());
   }
   ```

## Firebase Crashlytics 통합

1. 앱의 진입 요소(예: `main.dart`)에서 다음 코드를 추가하여 Crashlytics 플러그인을 초기화합니다:

   ```dart
   import 'package:firebase_crashlytics/firebase_crashlytics.dart';

   void main() async {
     WidgetsFlutterBinding.ensureInitialized(); 
     await Firebase.initializeApp();
     FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
     runApp(MyApp());
   }
   ```

2. Crashlytics 기능을 테스트하기 위해 앱에서 인위적으로 오류를 발생시키는 코드를 추가합니다:

   ```dart
   void _testCrash() {
     throw Exception('Test Crash');
   }
   ```

3. 앱의 적절한 위치(예: 버튼 클릭 이벤트)에서 테스트 오류를 발생시키기 위해 위의 `_testCrash()` 함수를 호출합니다.

## 오류 로그 확인하기

1. Firebase 콘솔에서 Firebase Crashlytics로 이동합니다.
2. 앱에서 발생한 실시간 오류, 무시된 오류, 어떤 시점에서 가장 많이 발생한 오류 등을 확인할 수 있습니다.

Firebase Crashlytics를 사용하여 플러터 앱의 실시간 오류 로그를 확인하는 방법에 대해 알아보았습니다. 오류를 신속하게 식별하고 해결하여 앱의 안정성을 향상시키는 데 도움이 됩니다. Firebase Crashlytics를 사용하여 앱의 사용자 경험을 향상시키십시오!

더 자세한 내용은 [Firebase Crashlytics 문서][1]를 참조하세요.

[1]: https://firebase.google.com/docs/crashlytics