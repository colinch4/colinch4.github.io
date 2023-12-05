---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 맞춤형 오류 탐지 및 예방하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

안녕하세요! 오늘은 Firebase Crashlytics를 사용하여 플러터(Flutter) 애플리케이션에서의 맞춤형 오류 탐지와 예방 방법에 대해 알아보겠습니다.

Firebase Crashlytics는 Firebase의 일부인 크래시 보고 도구로, 앱의 충돌과 다운시 문제를 실시간으로 모니터링하고 기록합니다. 이를 통해 앱의 안정성을 개선하고 사용자 경험을 향상시킬 수 있습니다.

## 1. Firebase 설정

Firebase Crashlytics를 사용하려면 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성하고, Firebase SDK를 프로젝트에 추가합니다. Firebase SDK를 추가하는 방법은 Firebase 콘솔에서 자세히 안내되어 있습니다.

## 2. Android 설정

### 2.1. Firebase SDK 추가

build.gradle 파일에 Firebase Crashlytics SDK를 추가해야 합니다. 다음 코드를 `android/app/build.gradle` 파일의 `dependencies` 섹션에 추가하세요.

```gradle
implementation 'com.google.firebase:firebase-crashlytics'
```

### 2.2. Crashlytics 초기화

Crashlytics를 사용하기 위해 애플리케이션의 `main.dart` 파일에 다음과 같이 코드를 추가하세요.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() {
  // Add the following line before `runApp`
  WidgetsFlutterBinding.ensureInitialized();
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  
  // Add the following line after `runApp`
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  runApp(MyApp());
}
```

위 코드를 추가하면 앱이 시작될 때 Firebase Crashlytics가 초기화됩니다.

## 3. Crashlytics 사용

Crashlytics를 사용하여 앱에서 오류를 탐지하고 보고할 수 있습니다.

### 3.1. 명시적 사용자 식별

Crashlytics는 사용자의 오류를 추적하여 보고할 수 있습니다. 사용자 식별 정보를 Crashlytics에 연결하려면 다음과 같이 코드를 작성하세요.

```dart
FirebaseCrashlytics.instance.setUserIdentifier("user123");
FirebaseCrashlytics.instance.setUserName("John Doe");
FirebaseCrashlytics.instance.setUserEmail("john.doe@example.com");
```

### 3.2. 예외 보고

앱에서 예외가 발생하는 경우, Crashlytics를 사용하여 예외 정보를 보고할 수 있습니다. 다음 코드를 추가하여 예외를 보고하세요.

```dart
try {
  // 예외 발생 가능한 코드
} catch (e, stackTrace) {
  FirebaseCrashlytics.instance.recordError(e, stackTrace);
}
```

위 코드는 예외가 발생할 경우, Crashlytics에 예외 정보를 보고합니다.

### 3.3. 비동기 예외 보고

비동기 코드에서 예외가 발생하는 경우, Catch 구문으로 예외를 잡을 수 없습니다. 이러한 경우, Crashlytics에 예외를 보고하기 위해 다음 코드를 사용하세요.

```dart
Future<void> myAsyncFunction() async {
  try {
    // 비동기 코드
  } catch (e, stackTrace) {
    await FirebaseCrashlytics.instance.recordError(e, stackTrace);
  }
}
```

## 4. Crashlytics 테스트

Crashlytics를 사용한 앱의 오류 보고 기능을 테스트해보려면, 다음과 같이 앱에서 의도적으로 오류를 발생시켜 보세요.

```dart
try {
  throw Exception('This is a test crash');
} catch (e, stackTrace) {
  FirebaseCrashlytics.instance.recordError(e, stackTrace);
}
```

위 코드는 의도적으로 예외를 발생시키고, Crashlytics에 오류를 보고합니다. Firebase 콘솔에서 오류 보고서를 확인할 수 있습니다.

Firebase Crashlytics를 사용하여 맞춤형 오류 탐지와 예방 기능을 플러터(Flutter) 앱에 추가하는 방법을 살펴보았습니다. 이를 통해 앱의 안정성을 개선하고 사용자에게 더 나은 경험을 제공할 수 있습니다.

더 많은 세부 사항과 기능에 대해서는 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참고하세요.

감사합니다!