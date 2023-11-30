---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Remote Config 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 플러터 앱 개발에 매우 유용한 다양한 서비스를 제공합니다. 그 중 하나인 Firebase Remote Config를 활용하여 플러터 앱에서 동적으로 앱의 동작을 제어하는 방법에 대해 알아보겠습니다.

## Firebase Remote Config란?

Firebase Remote Config는 앱의 동작을 동적으로 변경할 수 있는 서비스입니다. 이를 통해 서버에서 제어되는 구성 값을 설정하고, 앱에서는 이 값을 읽어와서 앱의 동작을 조정할 수 있습니다. Firebase Remote Config를 사용하면 앱의 동작을 변경하거나 최신 정보를 전달하기 위해 앱을 업데이트하지 않고도 변경할 수 있습니다.

## Firebase Remote Config 설정하기

먼저, Firebase Remote Config를 사용하기 위해 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔에서 프로젝트를 생성한 후, 프로젝트의 구성 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 앱 프로젝트에 추가해야 합니다.

Firebase 프로젝트를 만든 후, `pubspec.yaml` 파일에 `firebase_core`와 `firebase_remote_config` 패키지를 추가합니다. 아래는 예시입니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.2.0
  firebase_remote_config: ^2.0.0
```

프로젝트를 업데이트한 후, Firebase 모듈을 초기화해야 합니다. 앱의 진입점인 `main.dart` 파일에서 다음과 같이 Firebase 모듈을 초기화합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

이제 Firebase Remote Config를 사용할 준비가 끝났습니다.

## Firebase Remote Config 사용하기

Firebase Remote Config를 사용하기 위해서는 구성 값을 설정하고 앱에서 이 값을 가져와야 합니다. 먼저, Firebase 콘솔에서 구성 값을 설정해보겠습니다.

1. Firebase 콘솔에 접속하여 프로젝트를 선택합니다.
2. 왼쪽 메뉴에서 'Remote Config'를 선택합니다.
3. 'Add your first parameter'를 클릭하여 구성 값을 추가합니다.
4. Key와 Value를 입력한 후, 'Add parameter'를 클릭하여 구성 값을 저장합니다.

Firebase 콘솔에서 구성 값을 설정한 후, 앱에서 이 값을 가져오겠습니다. `main.dart` 파일에서 앱 초기화 이후 `await Firebase.initializeApp();` 다음에 다음 코드를 추가합니다.

```dart
import 'package:firebase_remote_config/firebase_remote_config.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  
  // Fetch and activate the remote config values
  final RemoteConfig remoteConfig = RemoteConfig.instance;
  await remoteConfig.fetchAndActivate();

  runApp(MyApp());
}
```

위 코드는 Firebase Remote Config에서 구성 값을 가져오고, 활성화하는 과정입니다.

이제 구성 값을 읽어오는 방법에 대해 알아보겠습니다. Remote Config는 Key-Value 형태의 구성 값을 제공합니다. 예를 들어, Key가 'welcome_message'이고 Value가 'Hello, World!'라고 설정된 경우, 다음과 같이 구성 값을 읽어올 수 있습니다.

```dart
final RemoteConfig remoteConfig = RemoteConfig.instance;
String welcomeMessage = remoteConfig.getString('welcome_message');
```

이제 `welcomeMessage` 변수에는 Firebase Remote Config에서 설정한 'Hello, World!'가 할당됩니다.

## 결론

Firebase Remote Config는 앱의 동작을 동적으로 변경하거나 최신 정보를 앱에 전달하는 데 사용할 수 있는 강력한 도구입니다. 위에서 설명한 방법을 따라 Firebase Remote Config를 적용하여 플러터 앱을 더 유연하고 동적으로 만들어보세요.

더 자세한 내용은 [Firebase Remote Config 문서][1]를 참고해주세요.

[1]: https://firebase.google.com/docs/remote-config