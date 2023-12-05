---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 앱 충돌 여부에 대한 실시간 경고 및 알림 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 충돌 여부를 실시간으로 모니터링하고 디버깅 정보를 제공해주는 도구입니다. 이 튜토리얼에서는 Flutter 앱에서 Firebase Crashlytics를 설정하는 방법에 대해 알아보겠습니다.

## 목차

1. Firebase 프로젝트 설정
2. 앱에 Firebase 추가
3. Firebase Crashlytics 패키지 추가
4. 앱 충돌 정보 수집 설정
5. 알림 설정

## 1. Firebase 프로젝트 설정

Firebase Crashlytics를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔(https://console.firebase.google.com)에 접속하여 새 프로젝트를 생성하고 프로젝트 설정을 완료하세요.

## 2. 앱에 Firebase 추가

Firebase 콘솔에서 프로젝트를 생성한 후, Flutter 앱에 Firebase를 추가해야 합니다. Flutter 앱에 Firebase를 추가하기 위해 `firebase_core` 패키지를 사용합니다.

먼저 `pubspec.yaml` 파일에 다음과 같이 `firebase_core` 패키지를 추가하세요:

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
```

추가한 후 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치하세요.

## 3. Firebase Crashlytics 패키지 추가

Firebase 콘솔에서 프로젝트를 생성한 후, Firebase Crashlytics 패키지를 추가해야 합니다. Flutter 앱에 Firebase Crashlytics 패키지를 추가하기 위해 `firebase_crashlytics` 패키지를 사용합니다.

먼저 `pubspec.yaml` 파일에 다음과 같이 `firebase_crashlytics` 패키지를 추가하세요:

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
  firebase_crashlytics: ^2.1.1
```

추가한 후 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치하세요.

## 4. 앱 충돌 정보 수집 설정

Firebase Crashlytics를 사용하기 위해서는 앱의 충돌 정보 수집을 활성화해야 합니다. 앱이 시작될 때 Firebase와 통신하여 충돌 정보를 전송하도록 설정할 수 있습니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  
  runZonedGuarded<Future<void>>(() async {
    runApp(MyApp());
  }, (error, stackTrace) async {
    await FirebaseCrashlytics.instance.recordError(error, stackTrace);
  });
}
```

위 코드에서 `setCrashlyticsCollectionEnabled(true)`를 호출하여 충돌 정보 수집을 활성화시킬 수 있습니다. 또한, `runZonedGuarded` 함수를 사용하여 앱 내에서 발생하는 모든 예외를 기록하도록 설정합니다.

## 5. 알림 설정

Firebase Crashlytics는 앱이 충돌되면 실시간 경고 및 알림을 제공합니다. 알림을 설정하려면 Firebase 콘솔로 이동하여 알림 설정을 변경해야 합니다.

Firebase 콘솔에서 프로젝트를 선택하고 Crashlytics 섹션으로 이동하세요. 알림 탭에서 포함 또는 제외할 이메일 주소를 추가하고 알림을 설정하세요.

이제 Firebase Crashlytics를 사용하여 앱의 앱 충돌 여부에 대한 실시간 경고와 알림을 설정할 수 있습니다. 앱이 충돌되었을 때 Firebase 콘솔에서 제공되는 디버깅 정보를 확인하고, 문제를 신속하게 해결할 수 있습니다.

## 참고 자료

- [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)
- [Flutter Firebase Crashlytics 패키지](https://pub.dev/packages/firebase_crashlytics)