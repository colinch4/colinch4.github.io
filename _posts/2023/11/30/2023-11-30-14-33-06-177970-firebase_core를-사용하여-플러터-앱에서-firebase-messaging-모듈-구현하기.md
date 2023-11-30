---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Messaging 모듈 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Messaging은 플러터 앱에서 푸시 알림을 구현하는 데 사용되는 모듈입니다. 이 모듈을 사용하면 사용자에게 백그라운드에서 알림을 보낼 수 있으며, 푸시 알림을 받을 때 사용자 지정 로직을 실행할 수 있습니다.

## Firebase 설정 및 프로젝트 생성

1. Firebase 콘솔에 접속하여 프로젝트를 생성합니다.
2. Android 앱 및 iOS 앱을 구성하고 Firebase 설정 파일을 다운로드합니다.

## Flutter 프로젝트 설정

1. `pubspec.yaml` 파일에 `firebase_messaging` 패키지를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_messaging: ^X.X.X # 최신 버전으로 대체
```

2. 필요한 패키지를 가져옵니다:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
```

3. Firebase 초기화를 위해 `main` 함수에서 `Firebase.initializeApp()`를 호출합니다:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 푸시 알림 수신 처리

1. `FirebaseMessaging` 인스턴스를 생성합니다:

```dart
final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;
```

2. 알림 권한을 요청합니다:

```dart
NotificationSettings permission = await _firebaseMessaging.requestPermission(
  alert: true,
  badge: true,
  sound: true,
);
```

3. 알림 권한을 허용한 경우, `onMessage`, `onResume`, `onLaunch` 핸들러를 등록합니다:

```dart
FirebaseMessaging.onMessage.listen((RemoteMessage message) {
  // 앱 실행 중일 때 알림을 수신한 경우 실행할 로직
});

FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
  // 앱이 백그라운드에서 실행 중이었을 때 알림을 수신한 경우 실행할 로직
});

FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
```

4. `onBackgroundMessage` 핸들러를 구현합니다:

```dart
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // 앱이 종료된 후 백그라운드에서 알림을 수신한 경우 실행할 로직
}
```

## 알림 토큰 가져오기

1. 다음과 같이 토큰을 가져올 수 있습니다:

```dart
String? token = await _firebaseMessaging.getToken();
```

## 푸시 알림 데이터 사용하기

1. `onMessage`, `onResume`, `onLaunch` 핸들러에서 `RemoteMessage` 객체를 통해 푸시 알림 데이터에 접근할 수 있습니다:

```dart
FirebaseMessaging.onMessage.listen((RemoteMessage message) {
  String? title = message.notification.title;
  String? body = message.notification.body;
  // 추가 데이터에 접근하기 위해 message.data 사용
});
```

위의 과정을 따라하면 플러터 앱에서 Firebase Messaging 모듈을 구현할 수 있습니다. Firebase Messaging을 통해 푸시 알림을 관리하고, 사용자 정의 로직을 실행하여 사용자에게 알림을 전달할 수 있습니다.

더 자세한 정보는 [Firebase Messaging 문서](https://firebase.flutter.dev/docs/messaging/overview/)를 참고하시기 바랍니다.