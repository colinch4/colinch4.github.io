---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Remote Config 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Remote Config는 앱의 구성 요소를 동적으로 업데이트할 수 있는 Firebase의 기능입니다. 이 기능을 사용하면 앱 업데이트 없이 앱의 동작을 변경하거나 콘텐츠를 업데이트할 수 있습니다.

이번 튜토리얼에서는 Flutter 앱에서 Firebase Remote Config를 구현하는 방법을 알아보겠습니다. Firebase를 사용하기 위해 `firebase_core` 패키지를 설치하고 설정하는 과정부터 시작해보겠습니다.

## 1. 프로젝트 설정

먼저, `pubspec.yaml` 파일에서 `firebase_core` 패키지를 추가해주세요:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

이후, 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드하세요.

Firebase Remote Config를 사용하기 전에 Firebase 프로젝트를 생성하고 설정해야 합니다. Firebase 콘솔에서 새 프로젝트를 생성하고 필요한 설정을 완료하세요.

## 2. Firebase 초기화

Firebase를 초기화하는 과정에서 `google-services.json` 파일을 프로젝트에 추가해야 합니다. 이 파일은 Firebase 프로젝트의 설정에 대한 정보를 포함하고 있습니다.

Firebase 초기화 코드를 작성하기 전에 `google-services.json` 파일을 프로젝트의 `android/app` 디렉토리에 추가해주세요.

Firebase를 초기화하려면 `main.dart` 파일에서 다음 코드를 추가하세요:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

`Firebase.initializeApp()` 메서드를 호출하여 Firebase를 초기화합니다.

## 3. Firebase Remote Config 사용

Firebase Remote Config를 사용하기 위해 `firebase_remote_config` 패키지도 추가해주세요:

```yaml
dependencies:
  firebase_remote_config: ^2.1.0
```

터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드하세요.

Firebase Remote Config를 사용하기 전에 Remote Config 템플릿과 기본 설정 값을 Firebase 콘솔에서 설정해야 합니다.

Firebase Remote Config를 사용하여 앱에서 동적으로 데이터를 가져오는 예제를 작성해보겠습니다:

```dart
import 'package:firebase_remote_config/firebase_remote_config.dart';

class RemoteConfigService {
  static Future<void> setupRemoteConfig() async {
    final RemoteConfig remoteConfig = RemoteConfig.instance;

    // 기본 설정 값 설정
    final defaults = <String, dynamic>{
      'welcome_message': 'Welcome to our app!',
      'button_text': 'Click me!',
    };
    remoteConfig.setDefaults(defaults);

    try {
      await remoteConfig.fetch(expiration: Duration(hours: 1));
      await remoteConfig.activateFetched();
    } catch (e) {
      print('Error fetching remote config: $e');
    }
  }

  static String get welcomeMessage {
    return RemoteConfig.instance.getString('welcome_message');
  }

  static String get buttonText {
    return RemoteConfig.instance.getString('button_text');
  }
}
```

위의 코드는 `RemoteConfigService`라는 클래스를 정의하고, `setupRemoteConfig()` 메서드를 통해 Firebase Remote Config를 설정하고 초기화합니다.

`fetch()` 메서드를 호출하여 최신의 Remote Config 템플릿을 가져온 다음, `activateFetched()` 메서드를 호출하여 가져온 값을 활성화합니다.

`welcomeMessage`와 `buttonText`와 같은 설정 값을 가져올 때는 `RemoteConfig.instance.getString()` 메서드를 사용합니다.

## 4. Remote Config 값 사용

이제 설정 값을 사용하여 앱의 동작을 변경하거나 콘텐츠를 업데이트할 수 있습니다. 예를 들어, 다음과 같이 환영 메시지와 버튼 텍스트를 표시하는 위젯을 작성해보겠습니다:

```dart
class HomeScreen extends StatelessWidget {
  final String welcomeMessage = RemoteConfigService.welcomeMessage;
  final String buttonText = RemoteConfigService.buttonText;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Remote Config Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(welcomeMessage),
            RaisedButton(
              child: Text(buttonText),
              onPressed: () {
                // 버튼 동작
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

이제 앱을 실행하고 Firebase 콘솔에서 설정 값을 변경하면 앱에 동적으로 업데이트되는 것을 확인할 수 있습니다.

위의 코드는 플러터 앱에서 Firebase Remote Config를 구현하는 방법을 보여주는 예제입니다. Firebase Remote Config를 사용하면 앱을 업데이트하지 않고도 앱의 동작을 변경하거나 콘텐츠를 업데이트할 수 있습니다. Firebase Remote Config의 자세한 내용은 [Firebase 문서](https://firebase.google.com/docs/remote-config)를 참조하세요.