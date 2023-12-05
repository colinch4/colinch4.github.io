---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 분석을 위한 실시간 사용자 정의 이벤트 추가하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 Firebase의 일부인 오류 보고 및 분석 도구입니다. 이 도구를 사용하면 앱에서 발생하는 오류를 캡처하고 분석할 수 있습니다. 이번 블로그 포스트에서는 Flutter 앱에서 Firebase Crashlytics를 사용하여 실시간 사용자 정의 이벤트를 추가하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Crashlytics를 사용하려면 먼저 Firebase 프로젝트에서 Crashlytics를 활성화해야 합니다. Firebase 콘솔로 이동하여 프로젝트를 선택하고 Crashlytics 섹션으로 이동합니다. 활성화 버튼을 클릭하여 Crashlytics를 활성화합니다.

## 2. Flutter 앱에 Firebase Crashlytics 추가하기

Firebase Crashlytics는 Firebase의 Flutter 플러그인인 `firebase_crashlytics`를 통해 사용할 수 있습니다. `pubspec.yaml` 파일에 다음 의존성을 추가하세요.

```dart
dependencies:
  firebase_core: "^1.0.0"
  firebase_crashlytics: "^2.2.1"
```

의존성을 추가한 후, 터미널에서 `flutter pub get` 명령을 실행하여 의존성을 설치합니다.

## 3. Firebase 앱 초기화

Firebase Crashlytics를 사용하기 위해 먼저 Flutter 앱을 Firebase에 등록해야 합니다. `main.dart` 파일의 `main` 함수 안에서 다음 코드를 추가하세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(); // Firebase 앱 초기화
  runApp(MyApp());
}
```

`Firebase.initializeApp()`가 앱을 초기화하는 데 사용됩니다.

## 4. Firebase Crashlytics 설정

Firebase Crashlytics를 시작하기 전에 `FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true)`를 호출하여 오류 보고를 켜야 합니다. 이 코드는 보통 `main` 함수 외부에 위치하는 `initCrashlytics` 함수에 추가하는 것이 좋습니다.

```dart
void initCrashlytics() {
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  // 기타 초기화 작업 수행
}
```

`setCrashlyticsCollectionEnabled(true)`를 호출하여 Crashlytics 오류 보고를 활성화합니다.

## 5. 실시간 사용자 정의 이벤트 추가

Firebase Crashlytics를 사용하여 실시간 사용자 정의 이벤트를 추가할 수 있습니다. 예를 들어, 사용자가 특정 화면을 방문했을 때 이벤트를 기록하고 오류 보고에 추가할 수 있습니다.

```dart
void logScreenVisited(String screenName) {
  FirebaseCrashlytics.instance.log('Screen Visited: $screenName');
  FirebaseCrashlytics.instance.setCustomKey('Last Screen Visited', screenName);
}
```

위의 코드에서 `logScreenVisited` 함수는 사용자가 방문한 화면 이름을 기록하고 `setCustomKey`를 사용하여 마지막으로 방문한 화면을 저장합니다.

## 6. Firebase Crashlytics 테스트

이제 Firebase Crashlytics가 설정되었으므로 앱에서 오류를 발생시켜 테스트할 수 있습니다. 예를 들어, 앱의 버튼을 클릭했을 때 예외를 발생시켜보세요.

```dart
void simulateError() {
  throw Exception('Test Crash');
}
```

위의 코드를 호출하여 오류를 발생시킬 수 있습니다. 앱이 충돌하거나 오류가 발생하면 Firebase Crashlytics에 오류 보고서가 생성됩니다.

## 마무리

이제 Firebase Crashlytics를 사용하여 Flutter 앱에서 오류 분석을 위한 실시간 사용자 정의 이벤트를 추가하는 방법을 알게 되었습니다. Firebase Crashlytics의 다양한 기능을 활용하여 앱의 안정성을 개선할 수 있습니다. 좀 더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/crashlytics)를 참조하세요. Happy coding!