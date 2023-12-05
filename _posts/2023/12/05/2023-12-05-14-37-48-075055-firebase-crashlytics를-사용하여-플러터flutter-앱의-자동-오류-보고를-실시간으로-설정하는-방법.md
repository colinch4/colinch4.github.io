---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 자동 오류 보고를 실시간으로 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 오류 및 충돌을 실시간으로 모니터링하고 보고하는 데 사용할 수 있는 강력한 도구입니다. 이 블로그에서는 Flutter 앱에서 Firebase Crashlytics를 설정하여 자동 오류 보고를 활성화하는 방법을 다루겠습니다.

## 1. Firebase 프로젝트 생성

Firebase Crashlytics를 사용하기 위해 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔에 로그인한 후, 새 프로젝트를 만들고 해당 프로젝트에 앱을 추가합니다.

## 2. Flutter 프로젝트에 Firebase 추가

Flutter 프로젝트에 Firebase를 추가해야 합니다. FlutterFire를 사용하여 Firebase를 플러터 앱에 통합할 수 있습니다. 터미널에서 다음 명령을 실행하여 FlutterFire를 설치하세요:

```
flutter pub add firebase_core
```

또한 Crashlytics 패키지를 추가하기 위해 다음 명령을 실행하세요:

```
flutter pub add firebase_crashlytics
```

## 3. Firebase 프로젝트와 플러터 앱 연결

Firebase 프로젝트와 플러터 앱을 연결해야 합니다. Firebase 콘솔에서 어플리케이션에 대한 Google 서비스 정보 파일(`google-services.json`)을 다운로드한 후, 해당 파일을 Flutter 프로젝트의 `android/app` 폴더에 추가하세요.

또한, iOS에서도 Firebase와 앱을 연결하려면 Firebase 콘솔에서 앱을 추가하고, `GoogleService-Info.plist` 파일을 다운로드하여 Flutter 프로젝트의 `ios/Runner` 폴더에 추가해야 합니다.

## 4. Crashlytics 플러그인 초기화

플러터 앱의 `main.dart` 파일에서 Firebase Crashlytics 플러그인을 초기화해야 합니다. 다음과 같이 `main` 함수 안에 다음 코드를 추가하세요:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  runZonedGuarded<Future<void>>(() async {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

## 5. 오류 보고 테스트

Firebase Crashlytics가 올바르게 설정되었는지 확인하기 위해 앱에서 오류를 발생시켜 보겠습니다. 예를 들어, 버튼을 클릭할 때 앱이 충돌하도록 설정합니다.

```dart
RaisedButton(
  onPressed: () {
    throw Exception('Manual Crash');
  },
  child: Text('Crash App'),
),
```

앱을 실행하고 버튼을 클릭하면 Crashlytics 대시보드에 자동으로 오류가 기록되는 것을 확인할 수 있습니다.

## 결론

Firebase Crashlytics를 사용하여 플러터 앱의 자동 오류 보고를 실시간으로 설정하는 방법을 알아보았습니다. Flutter 앱의 안정성을 향상시키고 사용자들의 문제를 더 빠르게 해결하기 위해 Firebase Crashlytics를 적극적으로 활용해 보세요!

## 참고 자료
- [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)
- [Firebase FlutterFire 문서](https://firebase.flutter.dev/)