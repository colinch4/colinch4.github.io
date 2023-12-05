---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 대시보드를 실시간으로 구성하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 사용자에게 발생하는 오류와 충돌을 실시간으로 모니터링하고 추적하는 도구입니다. 이 도구를 사용하면 플러터(Flutter) 앱의 오류 대시보드를 손쉽게 구성하고, 신속하게 문제점을 해결할 수 있습니다.

## 1. Firebase 프로젝트 설정

Firebase Crashlytics를 사용하기 위해 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새로운 프로젝트를 생성하고, 해당 프로젝트에서 'Crashlytics'를 활성화해야 합니다.

## 2. Flutter 앱에 Firebase 연동하기

Flutter 앱에서 Firebase Crashlytics를 사용하려면, `firebase_crashlytics` 플러그인을 사용하여 Firebase를 연동해야 합니다. `pubspec.yaml` 파일에 다음과 같이 의존성을 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
  firebase_crashlytics: ^2.1.0
```

의존성을 추가한 다음, `main.dart` 파일에서 Firebase를 초기화합니다:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  runApp(MyApp());
}
```

## 3. 오류 보고 추가하기

Firebase Crashlytics는 앱에서 오류가 발생할 때 해당 오류를 실시간으로 보고합니다. 플러터 앱에서는 `runZonedGuarded` 함수를 사용하여 오류를 캐치하고 Crashlytics에 보고할 수 있습니다.

앱의 진입점인 `main` 함수를 다음과 같이 수정합니다:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  // 오류 보고 추가
  runZonedGuarded<Future<void>>(() async {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
}
```

이제 앱에서 오류가 발생하면 Firebase Crashlytics에 해당 오류가 실시간으로 보고됩니다.

## 4. 사용자 정의 이벤트 보고하기

Firebase Crashlytics는 사용자 정의 이벤트를 보고할 수도 있습니다. 예를 들어, 앱에서 특정 액션을 수행할 때마다 이벤트를 보고하고 싶다면 다음과 같이 작성할 수 있습니다:

```dart
FirebaseCrashlytics.instance.log('사용자 정의 이벤트가 발생했습니다: 특정 액션');
```

## 5. 오류 대시보드 확인하기

Firebase 콘솔에서 Firebase Crashlytics를 열어 오류 대시보드를 확인할 수 있습니다. 오류 대시보드는 앱에서 발생한 오류와 충돌을 실시간으로 모니터링하고, 개별 오류의 스택 트레이스를 확인할 수 있습니다.

Firebase Crashlytics를 통해 실시간으로 오류 대시보드를 확인하고 문제점을 해결하여, 플러터 앱의 안정성을 향상시킬 수 있습니다.

---

참고: 
- [Firebase Crashlytics](https://firebase.google.com/docs/crashlytics)
- [flutterfire/flutterfire:firebase_crashlytics](https://github.com/flutterfire/flutterfire/tree/master/packages/firebase_crashlytics)