---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Messaging 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Cloud Messaging (FCM)은 Flutter 앱에서 푸시 알림을 전송하고 수신하는 데 사용되는 강력한 플랫폼입니다. Firebase_core 패키지를 사용하여 플러터 앱에 FCM을 설정하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 로그인하고 새 프로젝트를 생성합니다.
2. Firebase 프로젝트에 Flutter 앱을 추가합니다.
3. `google-services.json` 파일을 다운로드합니다.
4. 플러터 프로젝트의 `android/app` 폴더에 `google-services.json` 파일을 복사합니다.
5. Firebase 콘솔에서 FCM을 설정하고 서버 키를 생성합니다.

## 플러터 프로젝트 설정

1. `pubspec.yaml` 파일에 `firebase_core` 패키지를 추가합니다.
```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.2
```

2. 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드합니다.

3. `main.dart` 파일에서 Firebase_core 패키지를 초기화합니다.
```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

4. Firebase Cloud Messaging을 사용하기 위해 `firebase_messaging` 패키지도 추가하세요.
```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.2
  firebase_messaging: ^11.4.0
```

5. 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드합니다.

6. `main.dart` 파일에서 `firebase_messaging` 패키지를 초기화하고 토큰을 가져옵니다.
```dart
import 'package:firebase_messaging/firebase_messaging.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FirebaseMessaging.instance.getToken();
  runApp(MyApp());
}
```

플러터 앱에서 Firebase Cloud Messaging을 사용하여 푸시 알림을 관리하는 기본적인 설정을 마쳤습니다. Firebase 콘솔에서 알림을 전송하고 푸시 알림을 받을 준비가 되었습니다.

더 많은 FCM 기능을 사용하려면 `firebase_messaging` 패키지의 문서를 참조하세요.

## 참고 자료

- [Firebase 콘솔](https://console.firebase.google.com/)
- [Firebase 설정 가이드](https://firebase.google.com/docs/flutter/setup?platform=android)
- [firebase_messaging 패키지 문서](https://pub.dev/packages/firebase_messaging)