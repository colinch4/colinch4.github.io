---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Messaging 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Cloud Messaging(FCM)은 Firebase 푸시 알림 서비스로, 플러터 앱에서 사용자에게 푸시 알림을 보낼 수 있습니다. Firebase core를 사용하여 플러터 앱에 FCM을 설정하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 생성

Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새 프로젝트를 생성합니다. 프로젝트 이름을 입력하고 생성합니다.

## 2. Flutter 프로젝트에 Firebase 추가

플러터 프로젝트의 pubspec.yaml 파일에 다음 의존성을 추가합니다:

```dart
dependencies:
  firebase_core: ^1.0.0
  firebase_messaging: ^10.0.0
```

의존성을 추가한 후에는 `flutter pub get` 명령어를 실행하여 의존성을 다운로드합니다.

## 3. Firebase 구성 파일 추가

Firebase 콘솔에서 프로젝트 설정으로 이동한 후, 안드로이드 및 iOS 앱을 추가합니다. 안드로이드 패키지 이름과 iOS 번들 식별자를 입력합니다. 이과정에서 발급되는 google-services.json(Android) 및 GoogleService-Info.plist(iOS) 파일을 다운로드합니다.

다운로드한 파일을 아래와 같이 프로젝트의 디렉토리에 추가합니다:

- Android: `android/app/google-services.json`
- iOS: `ios/Runner/GoogleService-Info.plist`

## 4. 플러터 앱에서 Firebase 초기화

main.dart 파일에 Firebase를 초기화하는 코드를 추가합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 5. 푸시 알림 받기

Firebase Messaging 패키지를 사용하여 푸시 알림을 받을 준비를 합니다. main.dart 파일에 Firebase Messaging을 초기화하는 코드를 추가합니다:

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

class FirebaseMessagingService {
  static final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;

  static Future<String> getToken() async {
    String? token = await _firebaseMessaging.getToken();
    return token ?? '';
  }
 
  static Future<void> initialize() async {
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
    FirebaseMessaging.onMessage.listen(_firebaseMessagingOnMessage);
    FirebaseMessaging.onMessageOpenedApp.listen(_firebaseMessagingOnMessageOpenedApp);
  }

  static Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
    print('Handling a background message: ${message.notification?.title}');
  }

  static Future<void> _firebaseMessagingOnMessage(RemoteMessage message) async {
    print('Received message: ${message.notification?.title}');
  }

  static Future<void> _firebaseMessagingOnMessageOpenedApp(RemoteMessage message) async {
    print('Opened message: ${message.notification?.title}');
  }
}
```

FirebaseMessagingService 클래스는 Firebase Messaging을 초기화하고 푸시 알림을 처리하는 코드입니다.

## 6. 기기 토큰 가져오기

FirebaseMessagingService.getToken() 메서드를 호출하여 푸시 알림을 보낼 때 필요한 기기 토큰을 가져올 수 있습니다:

```dart
String token = await FirebaseMessagingService.getToken();
```

## 결론

이제 Firebase core를 사용하여 플러터 앱에서 Firebase Cloud Messaging을 설정하는 방법에 대해 알아보았습니다. FCM을 통해 플러터 앱에서 사용자에게 푸시 알림을 보낼 수 있게 되었습니다.

더 자세한 내용은 [Firebase Cloud Messaging 문서](https://firebase.flutter.dev/docs/messaging/overview)를 참조하시기 바랍니다.