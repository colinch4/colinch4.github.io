---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Remote Config 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 구글에서 제공하는 범용적인 모바일 백엔드 서비스입니다. Firebase 중 하나인 `Remote Config`를 사용하면 앱 설정의 동적인 업데이트를 쉽게 관리할 수 있습니다. 이번 글에서는 Flutter 앱에서 `Firebase_core` 패키지를 사용하여 `Remote Config`를 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. [Firebase 콘솔](https://console.firebase.google.com/)에 접속하여 프로젝트를 생성합니다.
2. 생성된 프로젝트로 이동하여 "프로젝트 설정"으로 이동합니다.
3. `Android`와 `iOS` 앱을 추가하고, 각각의 패키지명과 앱 스토어 ID를 설정합니다.

## Flutter 프로젝트 설정

1. Flutter 프로젝트의 `pubspec.yaml` 파일에 다음 종속성을 추가합니다:

   ```yaml
   dependencies:
     firebase_core: ^1.10.0
     firebase_remote_config: ^2.2.0
   ```

2. 터미널에서 `flutter pub get` 명령어를 실행하여 종속성을 설치합니다.

3. Firebase 콘솔에서 다운로드 받은 `google-services.json`(Android)와 `GoogleService-Info.plist`(iOS) 파일을 Flutter 프로젝트의 각 플랫폼 디렉터리에 추가합니다.

4. Flutter 앱에서 Firebase 초기화 코드를 추가합니다. `main.dart` 파일의 main 함수에서 다음 코드를 추가합니다:

   ```dart
   import 'package:firebase_core/firebase_core.dart';

   void main() async {
     WidgetsFlutterBinding.ensureInitialized();
     await Firebase.initializeApp();
     runApp(MyApp());
   }
   ```

## Remote Config 사용하기

1. `Remote Config`를 사용하기 위해 Flutter 프로젝트에 `remote_config.dart` 파일을 생성합니다. 다음 코드를 추가합니다:

   ```dart
   import 'package:firebase_remote_config/firebase_remote_config.dart';

   final RemoteConfig remoteConfig = RemoteConfig.instance;
   ```

2. `remote_config.dart` 파일에 다음 함수를 추가하여 `Remote Config`를 초기화합니다:

   ```dart
   Future<void> initializeRemoteConfig() async {
     try {
       await remoteConfig.setConfigSettings(RemoteConfigSettings(
         fetchTimeout: const Duration(seconds: 10),
         minimumFetchInterval: const Duration(hours: 1),
       ));

       await remoteConfig.fetchAndActivate();
     } catch (e) {
       print('Failed to initialize Remote Config: $e');
     }
   }
   ```

   이 코드는 `Remote Config`의 설정을 초기화하고, 캐시된 값이 없을 경우 서버에서 값들을 가져와 적용합니다. `fetchTimeout`은 가져오기 요청의 타임아웃을 설정하고, `minimumFetchInterval`은 서버에서 데이터를 가져오는 최소 시간 간격을 설정합니다.

3. 앱에서 `Remote Config` 값을 사용하려면, `remote_config.dart` 파일에 다음 함수를 추가합니다:

   ```dart
   T getValue<T>(String key, T defaultValue) {
     final value = remoteConfig
         .getValue(key)
         .as<T>(defaultValue: defaultValue);
     return value;
   }
   ```

   이 함수는 주어진 키에 해당하는 `Remote Config` 값을 가져와서 타입을 변환한 후 반환합니다.

4. `initializeRemoteConfig()` 함수를 호출하여 `Remote Config`를 초기화하고, 필요한 곳에서 `getValue()` 함수를 사용하여 값을 가져와 사용할 수 있습니다.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await initializeRemoteConfig();

  // Remote Config 값 가져와 사용하기
  final welcomeMessage = getValue<String>('welcome_message', 'Hello!');
  print(welcomeMessage);

  runApp(MyApp());
}
```

Firebase 콘솔에서 `Remote Config`에 필요한 키와 값을 추가하고, 앱을 실행하여 원격으로 업데이트된 값을 확인할 수 있습니다.

이제 `Firebase_core`를 사용하여 Flutter 앱에서 `Remote Config`를 구현하는 방법에 대해 알아보았습니다. `Remote Config`를 사용하면 앱의 동적인 업데이트를 쉽게 관리할 수 있으며, 사용자에게 최신 정보를 제공하는 데 도움이 됩니다.

더 자세한 내용은 [Firebase_core 문서](https://pub.dev/packages/firebase_core) 및 [Firebase_remote_config 문서](https://pub.dev/packages/firebase_remote_config)를 참고하세요.