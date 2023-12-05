---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 대시보드를 구성하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 Firebase의 솔루션 중 하나로, 앱의 오류를 실시간으로 모니터링하여 사용자에게 안정적인 앱을 제공하는 데 도움을 줍니다. 이 글에서는 Flutter 앱에서 Firebase Crashlytics를 사용하여 오류 대시보드를 구성하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Crashlytics를 사용하려면 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에 로그인한 다음 프로젝트를 생성하고, 앱을 추가해야 합니다.

## 2. Flutter 프로젝트에 Firebase 추가

Flutter 프로젝트에 Firebase를 추가해야 합니다. FlutterFire는 Flutter 앱에서 Firebase 서비스를 사용할 수 있도록 도와주는 플러그인입니다. FlutterFire를 사용하여 Firebase Crashlytics를 추가할 수 있습니다.

```dart
dependencies:
  firebase_core: ^0.7.0
  firebase_crashlytics: ^2.1.0
```
  

## 3. Firebase Crashlytics 초기화

Firebase Crashlytics를 사용하기 위해 앱 초기화 과정을 수행해야 합니다. `main()` 함수에서 Firebase 초기화를 수행하는 것이 좋습니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  
  runApp(MyApp());
}
```

## 4. 오류 발생 시 Crashlytics에 보고

앱에서 오류가 발생했을 때 Crashlytics에 보고해야 합니다. Flutter에서는 `catchError()`를 사용하여 감싸인 구문에서 오류를 잡을 수 있습니다. 

```dart
try {
  // 오류가 발생할 수 있는 코드
} catch (error, stackTrace) {
  FirebaseCrashlytics.instance.recordError(error, stackTrace);
}
```

## 5. 테스트 및 실시간 오류 모니터링

Firebase Crashlytics를 사용하여 설정한 앱에서 오류가 발생하는지 테스트해보세요. 오류가 발생하면 Firebase 콘솔의 Crashlytics 섹션에서 실시간으로 오류 보고서를 모니터링할 수 있습니다.

## 결론

Firebase Crashlytics는 플러터(Flutter) 앱의 안정성을 높이기 위해 유용한 도구입니다. 이 글에서는 Firebase 프로젝트 설정, Flutter 프로젝트에 Firebase 추가, Firebase Crashlytics 초기화, 오류 발생 시 Crashlytics에 보고하는 방법에 대해 알아보았습니다. Firebase Crashlytics를 사용하여 앱의 오류 대시보드를 구성하면 사용자에게 안정적인 앱 환경을 제공할 수 있습니다.

참고: [Firebase 공식 문서 - Flutter에서 Crashlytics 시작하기](https://firebase.google.com/docs/crashlytics/get-started?platform=flutter)