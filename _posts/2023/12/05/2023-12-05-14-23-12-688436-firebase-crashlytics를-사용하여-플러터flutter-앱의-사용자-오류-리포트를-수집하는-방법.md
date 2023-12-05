---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 사용자 오류 리포트를 수집하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 사용자 오류 리포트를 수집하고 실시간으로 분석하여 앱의 안정성을 향상시키는 데 도움을 주는 도구입니다. 이 기능을 사용하여 플러터(Flutter) 앱에서 발생한 오류를 신속하게 식별하고 해결할 수 있습니다.

Firebase Crashlytics를 사용하기 위해 다음 단계를 따라주세요.

## 1. Firebase 프로젝트 설정

Firebase 콘솔(https://console.firebase.google.com/)에 로그인하고 새로운 프로젝트를 생성하세요. 생성된 프로젝트에 앱을 추가하고 Firebase SDK를 다운로드하세요.

## 2. 앱에 Firebase SDK 추가

Flutter 앱에 Firebase SDK를 추가하려면 `pubspec.yaml` 파일에 다음 코드를 추가하세요.

```yaml
dependencies:
  firebase_crashlytics: ^2.2.0
```

패키지를 다운로드하려면 터미널에서 `flutter pub get` 명령을 실행하세요.

## 3. Firebase Crashlytics 초기화

앱을 시작할 때 Firebase Crashlytics를 초기화해야 합니다. 이를 위해 앱의 `main.dart` 파일에 다음 코드를 추가하세요.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp();

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

  // Add your app-specific initialization code here

  runApp(MyApp());
}
```

이 코드는 Firebase를 초기화하고, 앱의 Flutter 오류를 Crashlytics에 기록하는 역할을 합니다.

## 4. Crashlytics 사용

Firebase Crashlytics는 기본적으로 앱에서 발생하는 모든 오류를 자동으로 기록합니다. 또한, 특정 지점에서 명시적으로 오류를 기록할 수도 있습니다. 오류를 기록하려면 다음 코드를 사용하세요.

```dart
try {
  // 오류가 발생할 수 있는 코드
} catch (e, stackTrace) {
  FirebaseCrashlytics.instance.recordError(e, stackTrace);
}
```

위의 코드는 `try-catch` 문으로 오류가 발생할 수 있는 코드를 감싸고, `recordError()` 메서드를 사용하여 오류를 Firebase Crashlytics에 기록합니다. `e`는 발생한 오류 자체이고, `stackTrace`는 해당 오류의 스택 트레이스입니다.

## 5. 오류 리포트 확인

Firebase 콘솔의 Crashlytics 섹션에서 앱에서 발생한 오류 리포트를 확인할 수 있습니다. 이를 통해 각 오류의 발생 빈도, 사용자 정보, 스택 트레이스 등을 확인할 수 있습니다. 이러한 정보를 활용하여 앱의 오류를 분석하고 해결할 수 있습니다.

이제 Firebase Crashlytics를 사용하여 플러터 앱의 사용자 오류 리포트를 수집할 수 있습니다. Firebase Crashlytics를 통해 실시간으로 오류를 파악하고 반응할 수 있으므로, 앱의 안정성을 높이는 데 도움이 됩니다.

더 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참조하세요.