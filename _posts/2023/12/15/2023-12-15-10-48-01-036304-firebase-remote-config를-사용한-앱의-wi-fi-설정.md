---
layout: post
title: "[flutter] Firebase Remote Config를 사용한 앱의 Wi-Fi 설정"
description: " "
date: 2023-12-15
tags: [flutter]
comments: true
share: true
---

Firebase Remote Config는 Firebase를 사용하는 앱에 쉽게 동적인 설정을 전달할 수 있는 도구입니다. 이 기능을 사용하면 앱의 Wi-Fi 설정과 같은 요소를 앱을 다시 빌드하지 않고도 업데이트할 수 있어 매우 유용합니다. 이 블로그 포스트에서는 Flutter 앱에서 Firebase Remote Config를 사용하여 Wi-Fi 설정을 관리하는 방법에 대해 설명하겠습니다.

## Firebase 프로젝트 설정하기

먼저 Firebase 콘솔에서 새 프로젝트를 생성하고, 해당 프로젝트에 Firebase Remote Config를 활성화합니다. 활성화한 후 Remote Config에 Wi-Fi 관련 설정을 추가합니다. 예를 들어, 'wifi_ssid'와 'wifi_password'와 같은 키-값 쌍을 추가합니다.

```dart
// Wi-Fi 설정 키-값 추가 예시
remoteConfig.setDefaults({
  'wifi_ssid': 'MyWiFi',
  'wifi_password': 'password123',
});
```

## Flutter 프로젝트에 Firebase Remote Config 통합하기

Flutter 앱에서 Firebase Remote Config를 사용하기 위해 `firebase_remote_config` 패키지를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: "^1.0.0"
  firebase_remote_config: "^1.0.0"
```

이후, 앱을 시작할 때 Firebase 앱을 초기화하고 Remote Config를 가져옵니다.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  RemoteConfig remoteConfig = RemoteConfig.instance;
  await remoteConfig.fetchAndActivate();
}
```

## Wi-Fi 설정 사용하기

이제 Remote Config에서 가져온 Wi-Fi 설정을 사용할 수 있습니다.

```dart
String wifiSsid = remoteConfig.getString('wifi_ssid');
String wifiPassword = remoteConfig.getString('wifi_password');

// Wi-Fi 설정 적용 예시
WifiConnection.connect(wifiSsid, wifiPassword);
```

위와 같이 Firebase Remote Config를 사용하여 Flutter 앱의 Wi-Fi 설정을 업데이트하고 적용할 수 있습니다. 이는 앱을 다시 빌드하지 않고도 Wi-Fi 설정을 유동적으로 변경할 수 있는 강력한 방법입니다.

더 많은 Firebase Remote Config에 대한 정보는 [Firebase 문서](https://firebase.google.com/docs/remote-config)를 참고해 주세요.

Happy coding! 😊