---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 자동 오류 보고 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

만약 플러터(Flutter)로 개발한 앱을 출시하고 있다면, 앱의 안정성을 유지하고 사용자들로부터 발생하는 오류를 신속하게 파악해야 합니다. Firebase Crashlytics를 사용하면 앱이 발생하는 오류를 자동으로 보고하여 문제를 해결할 수 있습니다. 이번 블로그 포스트에서는 플러터 앱에 Firebase Crashlytics를 설정하는 방법을 알아보겠습니다.

## 전제 조건

이 튜토리얼을 진행하기 전에 다음 사항들이 필요합니다:

1. Flutter SDK가 설치되어 있어야 합니다. Flutter SDK 설치 방법에 대해서는 [공식 플러터 홈페이지](https://flutter.dev/docs/get-started/install)를 참고하세요.
2. Firebase 프로젝트가 생성되어 있어야 합니다. Firebase 프로젝트 생성 방법에 대해서는 [Firebase 콘솔](https://console.firebase.google.com/)을 이용하여 새로운 프로젝트를 생성하는 방법을 참고하세요.

## 1. Firebase 프로젝트에 앱 추가하기

1. Firebase 콘솔에 로그인하고 프로젝트 대시보드로 이동합니다.
2. **프로젝트 설정**으로 이동하여 **앱 추가**를 클릭합니다.
3. Flutter 앱을 추가하기 위해 **Android** 아이콘을 클릭합니다.
4. 패키지 이름을 입력하고 **앱 등록**을 클릭합니다.

## 2. 안드로이드 앱에 Firebase SDK 추가하기

1. Flutter 프로젝트의 `android/app/build.gradle` 파일을 열고 `dependencies` 섹션에 다음 코드를 추가합니다:

   ```java
   implementation 'com.google.firebase:firebase-crashlytics:17.3.0'
   ```

2. `android/build.gradle` 파일에 다음 코드를 추가합니다:

   ```java
   repositories {
       // ...
       maven {
           url 'https://dl.google.com/firebase/sdk/maven'
       }
   }
   ```

3. Firebase 프로젝트를 개별로 설정하기 위해 `android/app/src/main/AndroidManifest.xml` 파일을 열고 다음 코드를 추가합니다:

   ```xml
   <meta-data
       android:name="firebase_crashlytics_collection_enabled"
       android:value="true" />
   ```

   이 코드를 추가함으로써 Firebase Crashlytics가 오류 보고를 수집하도록 설정됩니다.

4. Firebase 설정 파일 (`google-services.json`)을 다운로드하여 `android/app` 디렉토리에 추가합니다.

## 3. Flutter 앱에 Firebase Crashlytics 플러그인 추가하기

1. `pubspec.yaml` 파일을 열고 `firebase_crashlytics` 플러그인을 추가합니다:

   ```yaml
   dependencies:
     flutter:
       sdk: flutter
     firebase_crashlytics: ^0.1.3
   ```

2. 터미널에서 `flutter packages get` 명령어를 실행하여 플러그인을 설치합니다.

3. Firebase Crashlytics를 사용하기 위해 앱의 진입점 코드에 다음 코드를 추가합니다:

   ```dart
   import 'package:firebase_crashlytics/firebase_crashlytics.dart';

   Future<void> main() async {
     WidgetsFlutterBinding.ensureInitialized();
   
     await Firebase.initializeApp();
     FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
     FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
   
     runApp(MyApp());
   }
   ```

만약 앱에서 발생하는 오류를 트리거하려면, `FlutterError`를 사용하여 오류를 생성하도록 코드를 추가할 수 있습니다.

## 4. 앱 빌드 및 테스트

1. Flutter 프로젝트의 루트 폴더에서 터미널을 열고 다음 명령어를 실행하여 앱을 빌드합니다:

   ```
   flutter build apk --release
   ```

2. 생성된 apk 파일을 기기에 설치하고 앱을 실행합니다.

3. 앱에서 오류를 트리거하여 Firebase Crashlytics로 오류 보고가 전송되는지 확인합니다.

Firebase Crashlytics를 사용하여 플러터 앱의 자동 오류 보고 설정이 성공적으로 완료되었습니다. Firebase 콘솔에서 오류 보고를 확인하여 개발 과정에서 발생할 수 있는 문제를 신속하게 파악하고 해결할 수 있습니다.