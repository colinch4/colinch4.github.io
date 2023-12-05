---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 발생률과 심각도를 실시간으로 분석하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱에서 발생하는 오류와 충돌을 실시간으로 모니터링하고 분석하는 도구입니다. 이를 통해 개발자는 사용자들이 마주하는 오류를 신속하게 파악하여 앱의 안정성을 향상시킬 수 있습니다. 이번 가이드에서는 플러터(Flutter) 앱에서 Firebase Crashlytics를 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정 및 Crashlytics 추가

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성합니다.
2. 생성한 프로젝트에 앱을 추가하고, Firebase SDK를 프로젝트에 추가합니다. (Firebase 콘솔에서 자동 생성된 google-services.json 파일을 프로젝트 디렉토리에 추가)
3. Firestore, Authentication 등 필요한 Firebase 기능을 활성화합니다.
4. Firebase 콘솔에서 "Crashlytics"를 선택하여 Crashlytics 설정 페이지로 이동합니다.
5. "시작하기" 버튼을 클릭하여 Crashlytics를 활성화합니다.

## 2. Flutter 앱에 Firebase Crashlytics 플러그인 추가

1. pubspec.yaml 파일을 열고 dependencies 섹션에 다음과 같이 Crashlytics 플러그인을 추가합니다:

   ```dart
   dependencies:
     firebase_crashlytics: ^0.4.0+1
   ```

2. 터미널에서 다음 명령을 실행하여 Flutter 패키지를 업데이트합니다:

   ```
   flutter packages get
   ```

## 3. Firebase Crashlytics 초기화와 사용자 정의 오류 리포트

1. main.dart 파일을 열고 다음 코드를 작성합니다. 이 코드는 앱이 시작할 때 Firebase Crashlytics를 초기화합니다.

   ```dart
   import 'package:firebase_crashlytics/firebase_crashlytics.dart';

   void main() {
     WidgetsFlutterBinding.ensureInitialized();
     FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

     runZonedGuarded(() {
       runApp(MyApp());
     }, (error, stack) => FirebaseCrashlytics.instance.recordError(error, stack));
   }
   ```

2. Firebase Crashlytics에 사용자 정의 오류 리포트를 보내려면 다음과 같은 코드를 사용합니다:

   ```dart
   import 'package:firebase_crashlytics/firebase_crashlytics.dart';

   Future<void> reportError(dynamic error, dynamic stackTrace) async {
     await FirebaseCrashlytics.instance.recordError(error, stackTrace);
   }
   
   // 사용 예시
   try {
     // 오류 발생 가능한 코드
   } catch (error, stackTrace) {
     await reportError(error, stackTrace);
   }
   ```

## 4. 앱 릴리즈 빌드에서 Firebase Crashlytics 사용

Firebase Crashlytics를 사용하여 앱의 릴리즈 버전에서 오류를 실시간으로 모니터링하려면 다음 단계를 수행합니다:

1. 터미널에서 다음 명령을 실행하여 앱의 릴리즈 버전을 빌드합니다:

   ```
   flutter build apk --release
   ```

2. 빌드가 완료되면 Firebase 콘솔에서 해당 프로젝트를 선택하고 "품질 > Crashes"를 클릭합니다. 여기에서 앱의 릴리즈 버전에서 발생한 오류를 확인할 수 있습니다.

Firebase Crashlytics를 사용하여 플러터 앱의 오류를 실시간으로 모니터링하고 분석할 수 있습니다. 이를 통해 개발자는 안정성을 향상시키고 사용자들이 경험하는 오류를 빠르게 해결할 수 있습니다.

## 참고 자료
- FlutterFire Crashlytics 문서: [https://firebase.flutter.dev/docs/crashlytics/overview/](https://firebase.flutter.dev/docs/crashlytics/overview/)
- Firebase Crashlytics 문서: [https://firebase.google.com/docs/crashlytics](https://firebase.google.com/docs/crashlytics)