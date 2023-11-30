---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Remote Config 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 플러터 앱 개발에 매우 유용한 클라우드 기반 플랫폼입니다. Firebase Remote Config는 앱의 동적인 설정을 실시간으로 변경할 수 있는 기능을 제공합니다. 이 글에서는 Firebase_core 프로젝트를 설정하고, 플러터 앱에서 Firebase Remote Config를 활용하는 방법에 대해 알아보겠습니다.

## 목차
- [Firebase Core 프로젝트 설정하기](#firebase-core-프로젝트-설정하기)
- [Firebase Remote Config 추가하기](#firebase-remote-config-추가하기)
- [Remote Config 값 가져오기](#remote-config-값-가져오기)
- [Firebase Remote Config 업데이트 감지하기](#firebase-remote-config-업데이트-감지하기)
- [참고 자료](#참고-자료)

## Firebase Core 프로젝트 설정하기

1. Firebase Console로 이동하여 프로젝트를 생성 한다.
2. Firebase SDK 추가를 위해 `firebase_core` 패키지를 `pubspec.yaml`에 추가한다.
   ```yaml
   dependencies:
     flutter:
       sdk: flutter
     firebase_core: ^1.0.0
   ```
3. `firebase_core` 패키지를 임포트한다.
   ```dart
   import 'package:firebase_core/firebase_core.dart';
   ```
4. `main()` 함수에서 `Firebase.initializeApp()`을 호출하여 Firebase Core를 초기화한다.
   ```dart
   void main() async {
     WidgetsFlutterBinding.ensureInitialized();
     await Firebase.initializeApp();
     runApp(MyApp());
   }
   ```

## Firebase Remote Config 추가하기

1. Firebase Console에서 프로젝트를 열고 Remote Config 탭으로 이동한다.
2. 기본 Remote Config 템플릿이 표시되지 않을 경우 '새 원격 구성'을 클릭하여 생성한다.
3. 원격 구성 키와 값을 추가하여 앱의 동적인 설정을 구성한다.

## Remote Config 값 가져오기

1. `firebase_remote_config` 패키지를 `pubspec.yaml`에 추가한다.
   ```yaml
   dependencies:
     flutter:
       sdk: flutter
     firebase_core: ^1.0.0
     firebase_remote_config: ^2.0.0
   ```
2. `firebase_remote_config` 패키지를 임포트한다.
   ```dart
   import 'package:firebase_remote_config/firebase_remote_config.dart';
   ```
3. Remote Config 값 가져오기 위해 `fetchAndActivate()` 메서드를 호출한다.
   ```dart
   final remoteConfig = RemoteConfig.instance;
   await remoteConfig.fetchAndActivate();
   var value = remoteConfig.getString('your_config_key');
   ```
4. 반환된 값으로 필요한 설정을 업데이트한다.

## Firebase Remote Config 업데이트 감지하기

1. Remote Config 업데이트를 받으려면 필요한 타임아웃 시간과 함께 `RemoteConfigSettings` 객체를 설정해야 한다.
   ```dart
   final remoteConfig = RemoteConfig.instance;
   final defaults = <String, dynamic>{'your_config_key': 'default_value'};
   await remoteConfig.setDefaults(defaults);
   remoteConfig.settings = RemoteConfigSettings(
     fetchTimeout: Duration(seconds: 10),
     minimumFetchInterval: Duration(hours: 1),
   );
   ```
2. `fetchAndActivate()`를 호출하여 Remote Config 값을 업데이트한다.
   ```dart
   await remoteConfig.fetchAndActivate();
   ```
3. 앱이 백그라운드로 전환 될 때 백그라운드 상태에서 업데이트를 받기 위해 다음 메서드를 호출한다.
   ```dart
   await remoteConfig.ensureInitialized();
   await remoteConfig.fetchAndActivate();
   ```

이제 플러터 앱에서 Firebase Remote Config를 활용할 수 있습니다.

## 참고 자료
- [Firebase Remote Config 공식 문서](https://firebase.flutter.dev/docs/remote-config/usage/)
- [Firebase Core 공식 문서](https://firebase.flutter.dev/docs/core/usage/)