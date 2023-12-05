---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류와 충돌에 대한 경고 및 경고 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱에서 발생하는 오류와 충돌에 대한 실시간 경고 및 보고 기능을 제공하는 강력한 도구입니다. 이 블로그 포스트에서는 Firebase Crashlytics를 사용하여 플러터(Flutter) 앱에서 오류와 충돌에 대한 경고를 설정하는 방법을 안내합니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 로그인하고 새 프로젝트를 만듭니다.
2. 프로젝트를 생성한 후 Firebase 프로젝트에 Flutter 앱을 추가합니다. Flutter 앱을 추가하는 방법에 대한 자세한 내용은 Firebase 공식 문서를 참조하세요.

## Crashlytics를 플러터(Flutter) 앱에 통합하기

1. Flutter 프로젝트의 `pubspec.yaml` 파일에 다음 의존성을 추가합니다:
   ```yaml
   dependencies:
     firebase_crashlytics: ^2.4.1
   ```

2. 터미널에서 `flutter packages get` 명령을 실행하여 의존성을 설치합니다.

3. `android/app/build.gradle` 파일을 열고 다음 플러그인을 추가합니다:
   ```gradle
   apply plugin: 'com.google.firebase.crashlytics'
   ```

4. Firebase 콘솔에서 Flutter 앱에 대한 구성 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 다운로드하고 프로젝트의 `android/app` 또는 `ios/Runner` 폴더에 추가합니다.

5. Flutter 앱의 `lib/main.dart` 파일에 다음 코드를 추가하여 Crashlytics를 초기화합니다:

   ```dart
   import 'package:firebase_crashlytics/firebase_crashlytics.dart';

   void main() {
     WidgetsFlutterBinding.ensureInitialized();
     FirebaseCrashlytics.instance
         .setCrashlyticsCollectionEnabled(true); // 앱 충돌 및 오류 보고를 활성화합니다.
     runZonedGuarded<Future<void>>(() async {
       runApp(MyApp());
     }, FirebaseCrashlytics.instance.recordError);
   }
   ```

## Crashlytics 테스트하기

플러터(Flutter) 앱에서 Crashlytics를 테스트해 보려면 다음 절차를 따르세요:

1. 오류를 발생시키는 코드를 추가합니다. 예를 들어, 버튼이 클릭되었을 때 `null` 객체를 참조하는 코드를 추가할 수 있습니다.

   ```dart
   RaisedButton(
     onPressed: () {
       dynamic variable;
       print(variable.toString());
     },
     child: Text('Crash App'),
   )
   ```

2. 앱을 빌드하고 실행합니다. 버튼을 클릭하면 앱이 충돌하고, 충돌이 Firebase Crashlytics에 기록됩니다.

## Firebase 콘솔에서 오류 및 충돌 보고

Firebase 콘솔에서 Crashlytics에서 수집한 오류 및 충돌 보고를 확인할 수 있습니다. 콘솔에서 앱의 통계, 트랜드, 환경 정보 등을 확인할 수 있으며, 보고된 오류 및 충돌에 대한 세부 정보를 살펴볼 수 있습니다.

## 결론

이렇게 Firebase Crashlytics를 사용하여 플러터(Flutter) 앱에서 오류와 충돌에 대한 경고 및 경고 설정을 할 수 있습니다. Firebase Crashlytics를 통해 앱의 안정성을 높이고 사용자에게 향상된 사용 경험을 제공할 수 있습니다.