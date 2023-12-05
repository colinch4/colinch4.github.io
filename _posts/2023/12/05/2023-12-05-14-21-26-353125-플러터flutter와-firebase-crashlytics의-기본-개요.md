---
layout: post
title: "[flutter] 플러터(Flutter)와 Firebase Crashlytics의 기본 개요"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

## 개요
플러터(Flutter)는 구글에서 개발한 UI 프레임워크로, 모바일, 웹, 데스크톱 등 다양한 플랫폼에서 동일한 코드로 네이티브 앱을 개발할 수 있습니다. Flutter의 큰 장점 중 하나는 Hot Reload 기능이 있는 것으로, 앱을 수정한 후에 즉시 결과를 확인할 수 있습니다.

Firebase Crashlytics는 Firebase의 서비스 중 하나로, iOS 및 Android 앱에서 앱의 장애 및 충돌에 대한 정보를 실시간으로 수집하여 개발자에게 보고해줍니다. Crashlytics를 사용하면 앱이 충돌할 때 어떤 문제가 발생했는지 정확히 파악하고, 신속하게 대응할 수 있습니다.

이 글에서는 플러터와 Firebase Crashlytics를 함께 사용하는 방법에 대해 소개하고자 합니다.

## 플러터(Flutter)와 Firebase Crashlytics 연동하기
Firebase Crashlytics를 플러터(Flutter) 프로젝트에 연동하는 방법은 다음과 같습니다.

1. 먼저, Firebase 콘솔에 프로젝트를 생성하고 앱을 등록해야 합니다. 필요한 정보를 입력한 후, Firebase 설정 파일을 다운로드 받아 프로젝트의 `android/app` 폴더와 `ios/Runner` 폴더에 추가합니다.

2. 다음으로, 플러터(Flutter) 프로젝트의 `pubspec.yaml` 파일에 다음과 같은 종속성을 추가합니다:

```dart
dependencies:
  firebase_crashlytics: ^2.4.0
```

3. `pubspec.yaml` 파일에 종속성을 추가한 후, 터미널에서 `flutter pub get` 명령어를 사용하여 종속성을 가져옵니다.

4. 플러터(Flutter) 앱의 시작점인 `main` 함수에서 다음과 같이 Firebase를 초기화합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

5. 이제, Crashlytics를 사용할 수 있습니다. 예를 들어, 앱이 충돌한 경우 아래와 같이 `FirebaseCrashlytics.instance.recordFlutterError` 메서드를 호출하여 Crashlytics에 에러를 보고할 수 있습니다:

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

  runApp(MyApp());
}
```

이렇게 플러터(Flutter)와 Firebase Crashlytics를 연동하여 앱의 충돌 정보를 수집하고 분석할 수 있습니다. Firebase 콘솔에서 충돌과 에러에 대한 자세한 정보를 확인할 수 있으며, 추적 정보를 통해 문제를 해결할 수 있습니다.

더 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.flutter.dev/docs/crashlytics/usage)를 참고해주세요.

이상으로 플러터(Flutter)와 Firebase Crashlytics의 기본 개요에 대해 알아보았습니다. 플러터(Flutter)와 Firebase Crashlytics를 함께 사용하여 앱의 안정성을 향상시켜보세요!