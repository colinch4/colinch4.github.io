---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Messaging 모듈 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Messaging은 Firebase의 메시징 서비스를 사용하여 푸시 알림을 플러터 앱에 통합하는 기능을 제공합니다. 이 글에서는 Firebase_core 패키지를 사용하여 플러터 앱에서 Firebase Messaging 모듈을 구현하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Console에서 새로운 프로젝트를 생성하고, 필요한 설정을 완료해야합니다. Firebase Console에서 앱 추가 작업을 수행하고, `google-services.json` 파일을 받아와 프로젝트의 `android/app` 디렉토리에 추가합니다.

## 2. Firebase_core 패키지 추가

우선, `pubspec.yaml` 파일에 Firebase 관련 패키지를 추가해야합니다. `firebase_core` 패키지를 아래와 같이 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

패키지를 추가한 후, 터미널에서 `flutter packages get` 명령을 실행하여 패키지를 다운로드하고 의존성을 해결합니다.

## 3. Android 설정

Firebase Messaging 모듈을 구현하기 위해서는 Android 앱에 몇 가지 추가적인 설정이 필요합니다.

1. `android/app/build.gradle` 파일에서 `defaultConfig` 섹션에 다음 코드를 추가합니다.

```gradle
defaultConfig {
  // ...
  manifestPlaceholders = [
    'appPackageName': '$applicationId',
  ]
}
```

2. `android/build.gradle` 파일에 다음 플러그인을 추가합니다.

```gradle
dependencies {
  // ...
  classpath 'com.google.gms:google-services:4.3.10'
}
```

3. `android/app` 디렉토리에 `google-services.json` 파일을 추가합니다.

4. `android/app/src/main/AndroidManifest.xml` 파일에 다음 코드를 추가합니다.

```xml
<manifest>
  <!-- ... -->

  <uses-permission android:name="android.permission.INTERNET" />

  <application>
    <!-- ... -->

    <service
        android:name="io.flutter.plugins.firebasemessaging.FlutterFirebaseMessagingBackgroundService"
        android:exported="false"
        android:permission="android.permission.BIND_JOB_SERVICE">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

## 4. Firebase Messaging 설정

Firebase Messaging 모듈을 구현하기 위해 `main.dart` 파일을 엽니다.

1. 필요한 패키지를 임포트합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
```

2. Firebase 초기화를 위한 `main` 함수에 다음 코드를 추가합니다.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

3. Firebase Messaging 구성을 위해 앱의 진입점에 다음 코드를 추가합니다.

```dart
class MyApp extends StatelessWidget {
  // ...

  @override
  Widget build(BuildContext context) {
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

    // ...

    return MaterialApp(
      // ...
    );
  }
}

Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp();
  print('Handling a background message: ${message.messageId}');
}
```

4. 필요한 푸시 알림 권한을 추가합니다. `AndroidManifest.xml` 파일의 `<application>` 태그 안에 다음 코드를 추가합니다.

```xml
<meta-data
    android:name="com.google.firebase.messaging.default_notification_channel_id"
    android:value="default_notification_channel_id" />
```

Firebase Messaging 모듈을 사용하여 앱에서 푸시 알림을 수신할 준비가 끝났습니다. 이제 앱에서 알림 표시 및 처리 로직을 추가할 수 있습니다.

## 5. 알림 처리

Firebase Messaging 모듈을 통해 수신한 푸시 알림을 처리하기 위해 `main.dart` 파일의 `MyApp` 위젯 클래스에 다음 코드를 추가합니다.

```dart
class MyApp extends StatelessWidget {
  // ...

  @override
  Widget build(BuildContext context) {
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      RemoteNotification notification = message.notification;
      AndroidNotification android = message.notification?.android;
      if (notification != null && android != null) {
        // 푸시 알림을 표시하기 위해 알림 창을 엽니다.
        showDialog(
          context: context,
          builder: (BuildContext context) => AlertDialog(
            title: Text(notification.title),
            content: Text(notification.body),
          ),
        );
      }
    });

    // ...
  }
}
```

위의 코드는 앱이 포그라운드에서 실행되는 동안 푸시 알림을 수신할 때마다 알림을 표시하는 AlertDialog를 띄웁니다. 앱이 백그라운드에서 실행되는 동안에는 `_firebaseMessagingBackgroundHandler` 함수가 호출되며, 필요한 로직을 추가하여 원하는 동작을 수행할 수 있습니다.

Firebase Messaging 모듈을 사용하여 플러터 앱에서 푸시 알림을 통합하는 방법에 대해 소개했습니다. Firebase Console에서 앱에 대한 메시지를 보내면 앱에서 푸시 알림을 수신하고 처리하는 로직을 구현할 수 있습니다.

더 자세한 내용은 [Firebase Messaging](https://firebase.flutter.dev/docs/messaging/overview/) 문서를 참고하시기 바랍니다.