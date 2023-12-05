---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류에 대한 실시간 알림 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

확인된 오류와 문제는 앱의 성능과 사용자 경험에 심각한 영향을 미칠 수 있습니다. Firebase Crashlytics를 사용하면 앱에서 발생하는 오류를 실시간으로 모니터링하고, 효과적으로 해결할 수 있습니다. 이번 글에서는 Flutter 앱에서 Firebase Crashlytics를 설정하여 오류에 대한 실시간 알림을 받는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성하고, Flutter 앱을 추가합니다.
2. Firebase SDK를 Flutter 앱에 추가합니다. `pubspec.yaml` 파일에 다음과 같이 `firebase_crashlytics` 패키지를 추가합니다:

```yaml
dependencies:
  firebase_core: ^1.0.2
  firebase_crashlytics: ^2.5.2
```

3. `main.dart` 파일에서 Firebase를 초기화합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## Crashlytics 설정하기

1. `main.dart`에서 함수나 클래스 바깥에 글로벌 키를 등록합니다:

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

FirebaseCrashlytics crashlytics = FirebaseCrashlytics.instance;
```

2. 앱이 시작되는 `main` 메소드에서 Crashlytics를 초기화합니다:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await runZonedGuarded(() {
    runApp(MyApp());
  }, crashlytics.recordError);
}
```

3. 앱이 발생시키는 예외를 Crashlytics에 기록하기 위해 `runZonedGuarded` 함수를 사용하고, `recordError` 메소드를 설정합니다.

## 오류 및 예외 보고 받기

1. Crashlytics에 사용자 지정 이벤트와 속성을 보고하는 방법은 다양하게 있지만, 가장 일반적인 방법은 예외를 기록하는 것입니다. 앱에서 예외가 발생할 때, Crashlytics에 해당 예외를 기록하도록 구현합니다. 예를 들어:

```dart
try {
  // 예외가 발생할 코드
} catch (e) {
  crashlytics.recordError(e, null);
}
```

2. 선택적으로 원하는 추가 정보를 Crashlytics에 보고할 수 있습니다:

```dart
try {
  // 예외가 발생할 코드
} catch (e, stackTrace) {
  crashlytics.recordError(e, stackTrace, context: 'custom error context');
}
```

3. Firebase 콘솔에서 Crashlytics 섹션으로 가면 앱에서 발생한 오류 및 예외의 실시간 보고를 확인할 수 있습니다.

## 결론

이제 Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류에 대한 실시간 알림 설정하는 방법을 알아보았습니다. Crashlytics를 통해 개발자는 앱에서 발생하는 예외 및 오류를 실시간으로 모니터링할 수 있고, 해당 문제를 빠르게 식별하고 해결할 수 있습니다. Firebase Crashlytics는 앱의 안정성과 사용자 경험 향상에 매우 유용한 도구입니다.

더 자세한 정보는 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참고하세요.