---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Crashlytics 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 모바일 개발 플랫폼입니다. Firebase는 다양한 기능을 제공하며, 이 중 Crashlytics는 앱의 크래시 리포팅과 분석을 제공하는 도구입니다. 이 글에서는 플러터(Flutter) 앱에서 Firebase_core를 사용하여 Crashlytics를 활용하는 방법을 소개하겠습니다.

## 전제 조건
- Firebase 프로젝트가 설정되어 있어야 합니다. Firebase 콘솔에서 프로젝트를 생성하고, 앱을 등록하여 google-services.json 파일을 다운로드해야 합니다.
- Flutter 프로젝트가 설정되어 있어야 합니다. Flutter 컴포넌트를 사용하여 앱을 개발할 수 있는 환경이어야 합니다.

## Firebase_core 패키지 추가

먼저, `firebase_core` 패키지를 추가해야 합니다. 이 패키지는 Firebase를 플러터 앱에서 사용하기 위해 필요한 핵심 패키지입니다. `pubspec.yaml` 파일에서 dependencies 섹션에 `firebase_core` 패키지를 추가해주세요.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.3
```

`pubspec.yaml` 파일을 수정한 후, 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 설치해주세요.

## Firebase 초기화

이제 Firebase_core를 사용하여 Firebase를 초기화해야 합니다. 이는 앱이 실행될 때 한 번만 수행하면 됩니다. Firebase를 초기화하는 코드는 `main.dart` 파일에 추가해주세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase를 초기화하려면 `Firebase.initializeApp()` 함수를 호출해야 합니다. `await` 키워드는 비동기 함수로, Firebase 초기화가 완료될 때까지 앱이 대기하도록 합니다.

## Crashlytics 설정

Firebase의 Crashlytics를 사용하기 위해서는 `firebase_crashlytics` 패키지도 추가해야 합니다. `pubspec.yaml` 파일에서 dependencies 섹션에 `firebase_crashlytics` 패키지를 추가해주세요.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.3
  firebase_crashlytics: ^2.1.1
```

패키지를 추가한 후, 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 설치해주세요.

### 앱에 Crashlytics 초기화

Crashlytics를 사용하기 위해서는 앱에서 Crashlytics를 초기화해야 합니다. 일반적으로 앱이 초기화될 때 수행하면 됩니다. `main.dart` 파일에서 Firebase 초기화 코드 바로 다음에 Crashlytics 초기화 코드를 추가해주세요.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';
import 'package:flutter/foundation.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(!kDebugMode);
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  runApp(MyApp());
}
```

`setCrashlyticsCollectionEnabled()` 함수를 사용하여 개발 중에는 디버그 모드에서는 Crashlytics 수집을 비활성화할 수 있습니다. `recordFlutterError` 함수는 Flutter의 에러를 Crashlytics에 기록해줍니다.

### 앱에서 Crashlytics 사용

이제 앱에서 Crashlytics를 사용할 준비가 되었습니다. Crashlytics에서는 특정 이벤트가 발생했을 때 로그를 기록하고, 예외를 기록하고, 사용자 지정 키와 값 데이터를 기록하는 등의 기능을 제공합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void myFunction() {
  try {
    // 코드 실행 중에 예외가 발생할 수 있는 부분
  } catch (e, stackTrace) {
    FirebaseCrashlytics.instance.recordError(e, stackTrace);
  }
  
  FirebaseCrashlytics.instance.log('myFunction called');
  FirebaseCrashlytics.instance.setCustomKey('myCustomKey', 'myCustomValue');
}
```

위의 예제에서는 `myFunction()`이라는 함수에서 예외가 발생할 수 있는 부분을 `try-catch` 문으로 감싸고, `recordError()` 함수를 사용하여 발생한 예외를 Crashlytics에 기록합니다. `log()` 함수는 중요한 이벤트를 로그로 기록하고, `setCustomKey()` 함수는 사용자 지정 데이터를 기록할 수 있습니다.

## 결론

이제 Firebase_core를 사용하여 플러터(Flutter) 앱에서 Crashlytics를 활용하는 방법을 알아보았습니다. Firebase의 다양한 기능을 활용하여 앱의 성능 모니터링과 크래시 리포팅을 간편하게 수행할 수 있습니다.