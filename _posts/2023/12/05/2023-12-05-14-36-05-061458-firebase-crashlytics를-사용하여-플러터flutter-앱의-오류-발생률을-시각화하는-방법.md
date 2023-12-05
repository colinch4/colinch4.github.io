---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 발생률을 시각화하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 Firebase 플랫폼의 핵심 기능 중 하나로서, 앱의 오류 발생과 관련된 다양한 정보를 제공하여 개발자들이 앱의 안정성을 보다 쉽게 관리할 수 있도록 도와줍니다. 이번 블로그 포스트에서는 Flutter 앱에서 Firebase Crashlytics를 사용하여 오류 발생률을 시각화하는 방법에 대해 알아보겠습니다.

## 1. Firebase Crashlytics 설정하기

Firebase Crashlytics를 사용하기 위해선 Firebase 프로젝트에 앱을 추가하고 SDK를 설정해야 합니다. 아래의 단계를 따라 진행해보세요.

1. Firebase 콘솔에 로그인하고, 프로젝트를 선택하세요.

2. 왼쪽 메뉴에서 'Crashlytics'를 선택하세요.

3. '시작하기' 버튼을 클릭하여 Crashlytics를 활성화시킵니다.

4. 해당 페이지에서 Firebase SDK를 추가하는 방법에 대한 안내를 참고하여 Flutter 프로젝트에 Firebase SDK를 설정합니다.

## 2. Crashlytics 플러그인 추가하기

Flutter 앱에서 Crashlytics를 사용하기 위해서는 해당 플러그인을 추가해야 합니다. `flutterfire` 라이브러리를 이용하여 Crashlytics 플러그인을 추가하는 방법은 아래와 같습니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
  firebase_crashlytics: ^2.2.3
```

위의 코드를 `pubspec.yaml` 파일의 `dependencies` 섹션에 추가한 후, 터미널에서 `flutter pub get` 명령어를 사용하여 종속성을 업데이트합니다.

## 3. Crashlytics 초기화하기

앱이 실행되는 시점에 Crashlytics를 초기화해야 합니다. 이를 위해 `main.dart` 파일에 아래의 코드를 추가하세요.

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

위의 코드에서 `Firebase.initializeApp()`는 Firebase를 초기화하는 함수이고, `FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true)`는 Crashlytics 데이터 수집을 활성화합니다. `FlutterError.onError`는 Flutter 앱에서 발생하는 오류를 Crashlytics에 기록하는 함수입니다.

## 4. 테스트하기

위의 단계들을 완료한 후 앱을 실행하고 테스트를 진행해보세요. 테스트 중에 Crashlytics에 기록된 오류는 Firebase 콘솔에서 확인할 수 있습니다.

## 5. 오류 발생률 시각화하기

Firebase 콘솔을 사용하여 앱의 오류 발생률을 시각화할 수 있습니다. 아래의 단계를 따라 오류 발생률을 확인해보세요.

1. Firebase 콘솔에 로그인하고, 프로젝트를 선택하세요.

2. 왼쪽 메뉴에서 'Crashlytics'를 선택하세요.

3. '오류 발생률' 탭으로 이동하세요.

4. 해당 페이지에서는 날짜별, 버전별 등 다양한 기준으로 오류 발생률을 확인할 수 있습니다. 그래프와 표로 데이터를 시각화하여 확인하세요.

Firebase Crashlytics를 사용하여 플러터 앱의 오류 발생률을 쉽게 시각화할 수 있습니다. 개발 중에 발생하는 오류를 적시에 파악하여 앱의 안정성을 향상시키는 데 도움이 되는 이러한 도구를 적극적으로 활용해보세요.

## 참고 자료

- [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)
- [FlutterFire GitHub 저장소](https://github.com/FirebaseExtended/flutterfire)