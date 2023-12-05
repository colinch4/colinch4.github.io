---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 발생 원인을 다른 지표와 연계하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

## 소개
Firebase Crashlytics는 Firebase의 오류 보고 및 분석 도구로, 플러터 앱에서 발생한 오류를 실시간으로 수집하고 분석할 수 있습니다. 이를 통해 오류 발생 원인을 신속하게 파악하여 개발자들이 오류를 해결할 수 있습니다.

Firebase Crashlytics를 사용하여 플러터 앱의 오류 발생 원인을 다른 지표와 연계하는 방법에 대해 알아보겠습니다.

## 필수 요구사항
- 플러터(Flutter) 프로젝트
- Firebase 프로젝트

## 단계별 가이드

### 단계 1: Firebase Crashlytics 설정
1. Firebase 콘솔로 이동하여 프로젝트를 선택하고 "Crashlytics" 탭으로 이동합니다.
2. Crashlytics를 활성화하고, 앱에 Firebase SDK를 추가합니다.
3. `firebase_core`, `firebase_crashlytics` 플러그인을 `pubspec.yaml` 파일에 추가합니다.
4. `android/app/build.gradle` 파일에서 `defaultConfig` 블록 안에 `multiDexEnabled true`를 추가합니다.

### 단계 2: Crashlytics 초기화
1. Firebase 프로젝트와 연결된 플러터 앱의 `main.dart` 파일을 엽니다.
2. Firebase SDK를 초기화합니다.
```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

### 단계 3: 오류 보고
1. 오류가 발생할 수 있는 부분을 감싸는 코드 블록 안에 다음 코드를 추가하여 오류 보고를 활성화합니다.
```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  runApp(MyApp());
}
```

2. 오류가 발생하는 코드 블록에서 `try-catch` 문으로 오류를 캐치하고 Crashlytics에 보고합니다.
```dart
Future<void> _handleError(Object error, StackTrace stackTrace) async {
  await FirebaseCrashlytics.instance.recordError(error, stackTrace);
}

void doSomethingThatMightThrowError() {
  try {
    // 오류가 발생할 수 있는 코드
  } catch (error, stackTrace) {
    _handleError(error, stackTrace);
  }
}
```

### 단계 4: 오류 데이터 확인
1. Firebase 콘솔로 돌아가서 "Crashlytics" 탭을 선택합니다.
2. 오류 발생 상황을 확인하고, 오류의 원인과 발생 빈도 등의 정보를 확인할 수 있습니다.

## 요약
이렇게 Firebase Crashlytics를 사용하여 플러터 앱의 오류 발생 원인을 다른 지표와 연계할 수 있습니다. 실시간으로 오류를 수집하고, 확인하여 개선을 할 수 있으며, 앱의 안정성을 향상시킬 수 있습니다.

Firebase Crashlytics 문서에서 자세한 내용을 확인할 수 있습니다.

- [Firebase Crashlytics 문서](https://firebase.flutter.dev/docs/crashlytics/overview)