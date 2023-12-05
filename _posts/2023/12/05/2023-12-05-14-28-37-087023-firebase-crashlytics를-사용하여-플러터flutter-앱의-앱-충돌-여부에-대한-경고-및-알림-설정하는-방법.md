---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 앱 충돌 여부에 대한 경고 및 알림 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱에서 발생하는 크래시를 실시간으로 모니터링하고, 디버깅 정보를 제공하여 앱의 안정성을 향상시킬 수 있는 매우 유용한 도구입니다. 이 글에서는 Flutter 앱에서 Crashlytics를 설정하여 앱의 충돌 상황에 대한 경고 및 알림을 받는 방법에 대해 알아보겠습니다.

## 목차
1. 필요한 준비물
2. Firebase 프로젝트 설정
3. Flutter 앱에 Firebase Crashlytics 추가
4. 앱 충돌 모니터링과 경고 설정
5. 알림 설정

## 필요한 준비물

- Firebase 계정
- Flutter 개발환경

## Firebase 프로젝트 설정

1. Firebase 콘솔에 접속하여 새로운 프로젝트를 생성합니다.
2. 프로젝트 설정 페이지에서 `Crashlytics`를 활성화합니다.

## Flutter 앱에 Firebase Crashlytics 추가

1. `pubspec.yaml` 파일에 `firebase_crashlytics` 의존성을 추가합니다.

```dart
dependencies:
  firebase_core: ^1.7.0
  firebase_crashlytics: ^2.6.0
```

2. Flutter 프로젝트를 업데이트합니다.

```bash
flutter pub get
```

## 앱 충돌 모니터링과 경고 설정

1. `main.dart` 파일에 Crashlytics를 초기화하는 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
}
```

2. 앱이 충돌할때 Crashlytics에 알림을 보내도록 설정합니다. `main.dart` 파일에 다음 코드를 추가합니다.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Firebase.initializeApp();
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  
  runZonedGuarded(() {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

## 알림 설정

Crashlytics는 기본적으로 앱이 충돌하면 알림을 보내지만, 사용자 정의 알림을 설정할 수도 있습니다. 알림은 Firebase 콘솔에서 설정할 수 있습니다.

1. Firebase 콘솔에서 `Crashlytics` 탭으로 이동합니다.
2. `사용자 정의 알림` 섹션에서 알림 설정을 원하는 대로 구성합니다.
3. 변경 사항을 저장합니다.

이제 앱이 충돌할 때마다 경고와 알림을 받을 수 있습니다.

> 본 포스트는 [Firebase Crashlytics 문서](https://firebase.flutter.dev/docs/crashlytics/overview/)를 참고하여 작성되었습니다.