---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Messaging 모듈 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 모바일 앱 개발에 매우 유용한 클라우드 기반 플랫폼입니다. Firebase Messaging 모듈은 푸시 알림을 통해 사용자에게 메시지를 전달할 수 있는 기능을 제공합니다. 이 기능을 플러터 앱에 추가하기 위해 Firebase_core 라이브러리를 사용하여 Firebase Messaging 모듈을 구현해 보겠습니다.

### Firebase_core 설치하기

프로젝트에 Firebase Messaging을 추가하기 전에, Firebase_core 패키지를 설치해야 합니다. pubspec.yaml 파일에 다음과 같은 의존성을 추가해 주세요:

```yaml
dependencies:
  firebase_core: ^1.0.0
```

의존성을 추가한 후, 터미널에서 다음 명령을 실행하여 패키지를 업데이트해 주세요:

```bash
$ flutter pub get
```

### Firebase 프로젝트 설정하기

Firebase Messaging을 사용하기 위해 Firebase 프로젝트에서 앱을 설정해야 합니다. 다음 단계를 따라 Firebase 프로젝트를 설정해 주세요:

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하세요.
2. 프로젝트를 만들거나 기존 프로젝트를 선택하세요.
3. 앱 설정을 클릭하여 플랫폼(Android or iOS)을 추가하세요.
4. 앱에 대한 패키지 이름 또는 번들 식별자를 입력하세요.
5. google-services.json(Android) 또는 GoogleService-Info.plist(iOS) 파일을 다운로드하고 프로젝트에 추가하세요.

### Firebase Messaging 구현하기

이제 Firebase_core와 Firebase Messaging을 구현할 준비가 되었습니다. 먼저 main.dart 파일에 Firebase_core를 초기화해야 합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase Messaging을 사용하기 위해 푸시 알림을 받는 화면 또는 위젯에 다음 코드를 추가하세요:

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {

  FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;

  @override
  void initState() {
    super.initState();
    _firebaseMessaging.getToken().then((token) {
      print("Firebase Cloud Messaging token: $token");
    });

    FirebaseMessaging.onMessage.listen((message) {
      print("Received message: ${message.notification?.title}");
      // TODO: 푸시 알림을 처리하는 로직 추가
    });

    FirebaseMessaging.onMessageOpenedApp.listen((message) {
      print("Opened app from background message: ${message.notification?.title}");
      // TODO: 푸시 알림을 처리하는 로직 추가
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      // 위젯 내용
    );
  }
}
```

이 코드에서 `_firebaseMessaging.getToken()`은 디바이스의 기기 토큰을 가져오는 코드입니다. 푸시 알림을 처리하는 로직은 `FirebaseMessaging.onMessage`와 `FirebaseMessaging.onMessageOpenedApp` 스트림을 통해 구현됩니다.

### 푸시 알림 처리하기

푸시 알림이 도착할 때마다 `FirebaseMessaging.onMessage` 스트림이 호출되며, 백그라운드에서 앱을 실행 중이면 `FirebaseMessaging.onMessageOpenedApp` 스트림이 호출됩니다. 이 스트림을 사용하여 푸시 알림을 처리하려면 원하는 로직을 추가하면 됩니다. 예를 들어, 알림을 표시하거나 특정 화면으로 이동하는 등의 동작을 수행할 수 있습니다.

### 결론

이제 Firebase Messaging이 플러터 앱에서 작동하도록 구현할 수 있습니다. Firebase_core를 사용하여 Firebase 프로젝트를 초기화하고, Firebase Messaging 모듈을 사용하여 푸시 알림을 처리할 수 있습니다. Firebase Messaging의 다양한 기능과 옵션을 활용하여 사용자에게 효과적인 알림을 제공할 수 있습니다. 더 많은 정보를 원하시면 [Firebase 공식 문서](https://firebase.flutter.dev/docs/messaging/overview)를 참조하세요.