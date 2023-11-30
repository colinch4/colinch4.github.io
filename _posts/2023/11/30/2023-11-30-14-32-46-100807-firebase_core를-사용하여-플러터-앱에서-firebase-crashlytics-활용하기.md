---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Crashlytics 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

## 목차
- [Firebase_core란?](#firebase_core란)
- [Firebase Crashlytics란?](#firebase-crashlytics란)
- [Firebase_core 및 Firebase Crashlytics 설정](#firebase_core-및-firebase-crashlytics-설정)
- [Firebase Crashlytics로 앱의 충돌 정보 수집하기](#firebase-crashlytics로-앱의-충돌-정보-수집하기)
- [결론](#결론)

## Firebase_core란?
Firebase_core는 Google Firebase의 Flutter 패키지 중 하나로, Firebase 서비스를 사용하기 위한 기본적인 설정과 초기화를 담당합니다. 따라서, Firebase_core를 플러터 앱에 추가하지 않으면 Firebase 서비스를 사용할 수 없습니다.

## Firebase Crashlytics란?
Firebase Crashlytics는 Firebase에서 제공하는 앱 충돌 모니터링 및 리포팅 도구입니다. 이 도구를 사용하면 앱이 실행 중에 발생하는 예외 및 충돌 정보를 실시간으로 수집하고 분석할 수 있습니다. 이를 통해 앱의 안정성을 향상시키고 사용자에게 더 나은 사용 경험을 제공할 수 있습니다.

## Firebase_core 및 Firebase Crashlytics 설정
1. 프로젝트에 Firebase 설정 추가: Firebase 콘솔에 접속하여 새 프로젝트를 만들고, Firebase 설정 파일을 다운로드하여 프로젝트에 추가합니다. 이 파일은 `android/app` 및 `ios/Runner` 폴더에 저장되어야 합니다.
2. `pubspec.yaml` 파일에 Firebase_core 추가: `pubspec.yaml` 파일에 `firebase_core` 패키지를 추가합니다. 예시 코드는 아래와 같습니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

3. 앱 초기화: 앱의 진입점인 `main.dart` 파일에서 Firebase_core를 초기화합니다. 아래는 예시 코드입니다.

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

4. Android 설정 추가: `android/app/build.gradle` 파일에 다음 코드를 추가합니다.

```groovy
apply plugin: 'com.google.gms.google-services'
```

5. iOS 설정 추가: Xcode에서 `GoogleService-Info.plist` 파일을 프로젝트에 추가합니다. 이 파일은 Firebase에서 다운로드한 파일입니다. 추가 후에는 Xcode에서 파일을 선택하고, target의 build phases에서 `Copy Bundle Resources` 옵션을 확인해야 합니다.

## Firebase Crashlytics로 앱의 충돌 정보 수집하기
Firebase Crashlytics를 사용하여 앱의 충돌 정보를 수집하는 방법은 다음과 같습니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() {
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

  runZonedGuarded(() {
    // 앱 실행코드
  }, (error, stackTrace) {
    FirebaseCrashlytics.instance.recordError(error, stackTrace);
  });
}
```

위 코드에서 `recordFlutterError` 메소드는 Flutter에서 발생하는 모든 예외를 Firebase Crashlytics에 기록합니다. `runZonedGuarded`는 Flutter 앱 내에서 비동기 및 백그라운드 스레드에서 발생하는 예외를 처리할 수 있게 해줍니다.

## 결론
Firebase_core를 사용하여 플러터 앱에서 Firebase Crashlytics를 활용하는 방법에 대해 알아보았습니다. Firebase Crashlytics는 앱의 충돌 정보를 실시간으로 수집하고 분석하여 앱의 안정성을 향상시킬 수 있는 강력한 도구입니다. Firebase_core를 통해 Firebase 서비스를 초기화한 다음, Firebase Crashlytics를 사용하여 앱의 충돌 정보를 수집하는 방법을 적용해보세요.