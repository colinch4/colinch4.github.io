---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 및 충돌을 모니터링하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱을 개발하고 배포할 때 오류 및 충돌이 발생할 수 있습니다. 이러한 문제를 신속하게 감지하고 해결하기 위해 Firebase Crashlytics를 사용할 수 있습니다. Firebase Crashlytics는 앱의 실시간 오류 및 충돌 데이터를 수집하여 개발자에게 보고해주는 도구입니다. 이번 포스트에서는 Flutter 앱에서 Firebase Crashlytics를 사용하여 오류 및 충돌을 모니터링하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 생성

Firebase Crashlytics를 사용하기 위해 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔에 접속하여 새 프로젝트를 만들고, 앱을 추가합니다. 앱을 추가할 때는 Flutter 프로젝트의 패키지명을 입력해야 합니다.

## 2. Firebase Flutter 패키지 추가

Flutter 프로젝트에서 Firebase Crashlytics를 사용하기 위해 필요한 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 아래의 의존성을 추가합니다.

```dart
dependencies:
  firebase_crashlytics: ^0.6.0
```

의존성을 추가한 후 터미널을 열고 `flutter packages get` 명령어를 실행하여 패키지를 다운로드 받습니다.

## 3. Firebase Crashlytics 초기화

Flutter 앱의 진입점인 `main.dart` 파일에서 Firebase Crashlytics를 초기화해야 합니다. `main()` 함수의 첫 줄에 아래의 코드를 추가합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  // ...
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  runZonedGuarded<Future<void>>(() async {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

위 코드는 앱이 오류 또는 예외를 처리할 때마다 Firebase Crashlytics에 보고하는 설정을 하는 코드입니다.

## 4. 오류 및 충돌 보고

Firebase Crashlytics를 초기화한 후 앱이 실행될 때마다 발생하는 오류와 충돌을 Firebase에 보고할 수 있습니다. 오류 또는 예외가 발생하는 위치에서 아래의 코드를 사용하여 Firebase Crashlytics에 보고합니다.

```dart
FirebaseCrashlytics.instance.log('오류 메시지');
FirebaseCrashlytics.instance.recordError(exception, stackTrace);
```

`log()` 메소드는 오류 메시지를 기록하고, `recordError()` 메소드는 예외와 스택 트레이스를 기록합니다.

## 5. Firebase 콘솔에서 오류 및 충돌 확인

앱을 테스트하고 배포한 후 Firebase 콘솔에서 오류 및 충돌을 확인할 수 있습니다. Firebase 콘솔에서 오류 및 충돌 섹션으로 이동하여 발생한 오류와 충돌에 대한 자세한 정보를 확인할 수 있습니다. 또한 앱 버전, 디바이스 정보 등의 추가 정보를 확인할 수 있습니다.

이제 Flutter 앱에서 Firebase Crashlytics를 사용하여 오류 및 충돌을 신속하게 모니터링할 수 있습니다. Firebase Crashlytics를 활용하여 앱의 안정성을 높이고 사용자 경험을 향상시켜보세요.

참고: [Firebase Crashlytics 문서](https://firebase.flutter.dev/docs/crashlytics/overview)