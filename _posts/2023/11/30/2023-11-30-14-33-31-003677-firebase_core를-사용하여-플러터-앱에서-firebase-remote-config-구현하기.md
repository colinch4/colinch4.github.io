---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Remote Config 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 앱 개발에 매우 유용한 다양한 기능을 제공하는 플랫폼입니다. Firebase Remote Config는 Firebase의 한 가지 기능으로, 앱의 동작을 동적으로 변경할 수 있게 해줍니다. 이 기능을 사용하면 앱 버전이나 사용자 그룹에 따라 특정 값들을 변경하거나 실험을 할 수 있습니다. 이번 블로그 포스트에서는 Flutter 앱에서 Firebase Remote Config를 구현하는 방법을 살펴보겠습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 프로젝트를 생성하고 Firebase Remote Config를 활성화해야 합니다. Firebase 프로젝트 설정에 대한 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup)를 참고하세요.

## 2. Firebase Core 패키지 추가

Firebase Remote Config를 사용하기 위해서는 `firebase_core` 패키지를 프로젝트에 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같이 의존성을 추가하세요:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.6.0
```

의존성을 추가한 뒤, 패키지를 다운로드하고 업데이트하기 위해 터미널에서 `flutter pub get` 명령을 실행하세요.

## 3. Firebase Remote Config 초기화

Firebase Remote Config를 초기화하기 위해, 앱의 시작 시점에 다음과 같이 `Firebase.initializeApp()` 메서드를 호출해야 합니다. `main()` 함수 안에서 호출되도록 코드를 작성하세요:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  
  runApp(MyApp());
}
```

Firebase 초기화에 성공하면 Firebase Remote Config에 액세스할 수 있게 됩니다.

## 4. Firebase Remote Config 값 가져오기

Firebase Remote Config에서 값을 가져오려면, `FirebaseRemoteConfig` 인스턴스를 생성하고 원하는 키의 값을 가져와서 사용할 수 있습니다. 다음은 `getRemoteConfigValue()` 함수를 사용하여 Remote Config에서 값을 가져오는 예시입니다:

```dart
import 'package:firebase_remote_config/firebase_remote_config.dart';

Future<RemoteConfig> getRemoteConfigValue() async {
  final RemoteConfig remoteConfig = RemoteConfig.instance;

  try {
    // Remote Config 초기화
    await remoteConfig.fetchAndActivate();

    // 원하는 키로 값을 가져오기
    final String welcomeMessage = remoteConfig.getString('welcome_message');
    final int maxItems = remoteConfig.getInt('max_items');

    return remoteConfig;
  } catch (exception) {
    print('Failed to fetch remote config: $exception');
    return null;
  }
}
```

위 코드에서는 `firebase_remote_config` 패키지를 사용하여 `RemoteConfig` 인스턴스를 생성하고, `fetchAndActivate()` 메서드를 사용하여 Remote Config 값을 가져옵니다. 이후에는 `getString()` 또는 `getInt()` 메서드를 사용하여 원하는 키의 값을 가져올 수 있습니다.

## 5. Firebase Remote Config 업데이트 주기 설정

Firebase Remote Config는 앱에서 정기적으로 서버로부터 값을 업데이트할 수 있습니다. 업데이트 주기는 `RemoteConfigSettings`를 사용하여 설정할 수 있으며, 아래와 같이 코드를 작성할 수 있습니다:

```dart
import 'package:firebase_remote_config/firebase_remote_config.dart';

void setRemoteConfigSettings() {
  final RemoteConfig remoteConfig = RemoteConfig.instance;

  final configSettings = RemoteConfigSettings(
    fetchTimeout: const Duration(seconds: 10),
    minimumFetchInterval: const Duration(hours: 1),
  );

  remoteConfig.setConfigSettings(configSettings);
}
```

위 코드에서는 `fetchTimeout` 속성으로 최대 업데이트 시간을 설정하고, `minimumFetchInterval` 속성으로 최소 업데이트 주기를 설정합니다. 이를 통해 Remote Config가 일정 시간마다 업데이트되도록 설정할 수 있습니다.

## 마무리

위의 단계를 따라하면 Flutter 앱에서 Firebase Remote Config를 구현할 수 있습니다. Firebase Remote Config를 사용하면 앱의 동작을 유연하게 변경할 수 있으며, 사용자에게 향상된 경험을 제공할 수 있습니다.

더 자세한 사항은 [Firebase 공식 문서](https://firebase.google.com/docs/remote-config)를 참조하세요.