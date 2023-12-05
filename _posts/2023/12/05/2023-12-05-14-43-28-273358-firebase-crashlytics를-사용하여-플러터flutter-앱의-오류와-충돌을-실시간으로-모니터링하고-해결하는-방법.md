---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류와 충돌을 실시간으로 모니터링하고 해결하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱에 대한 오류 및 충돌을 실시간으로 모니터링하고 이를 해결하는 훌륭한 도구입니다. 이 기능을 사용하면 앱의 안정성을 향상시키고 사용자들이 겪는 문제점을 신속하게 해결할 수 있습니다. 이번 블로그 포스트에서는 Flutter 프로젝트에서 Firebase Crashlytics를 통해 오류 및 충돌을 모니터링하는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

먼저, Firebase Crashlytics를 사용하려면 Firebase 프로젝트에 앱을 추가해야 합니다. Firebase 콘솔에서 프로젝트를 생성하고, 앱을 추가하는 단계를 따라야 합니다. Firebase SDK와 Crashlytics를 추가하는 방법은 [Firebase 문서](https://firebase.google.com/docs/flutter/setup)에서 자세히 설명되어 있습니다.

## Crashlytics SDK 추가

앱에 Firebase SDK를 추가한 후, 이제 Crashlytics SDK를 추가해야 합니다. `pubspec.yaml` 파일을 열고 dependencies 섹션에 다음과 같이 Crashlytics 의존성을 추가합니다.

```yaml
dependencies:
  firebase_crashlytics: ^2.1.0
```

의존성을 추가한 후, 터미널에서 `flutter pub get` 명령어를 실행하여 의존성을 설치합니다.

## Crashlytics 초기화

앱에서 Crashlytics를 사용하기 위해 `main()` 함수에서 다음과 같이 초기화해야 합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

  runApp(MyApp());
}
```

Crashlytics를 초기화하는 데에는 Firebase SDK를 초기화하는 `Firebase.initializeApp()`을 호출하는 것이 중요합니다.

## 오류 및 충돌 보고

이제 Crashlytics가 초기화되었으므로 오류 및 충돌 보고를 설정할 수 있습니다. 예를 들어, 앱 내부에서 예외가 발생했을 때 Crashlytics에 보고하는 코드를 추가해보겠습니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

  runApp(MyApp());
}

void someFunction() {
  try {
    // 예외 발생 가능성이 있는 코드
  } catch (error, stackTrace) {
    FirebaseCrashlytics.instance.setCustomKey('error_message', error.toString());
    FirebaseCrashlytics.instance.recordError(error, stackTrace);
  }
}
```

위의 예제에서 `someFunction()` 함수는 예외가 발생할 가능성이 있는 코드를 포함하고 있습니다. 예외가 발생하면 `FirebaseCrashlytics.instance.recordError()`를 호출하여 Crashlytics에 오류를 보고합니다. 추가로 `FirebaseCrashlytics.instance.setCustomKey()`를 사용하여 사용자 정의 데이터를 추가로 기록할 수도 있습니다.

## Crashlytics 데이터 확인

오류 및 충돌이 발생하면 해당 데이터는 Firebase 콘솔에서 확인할 수 있습니다. Firebase 콘솔에서 프로젝트를 선택한 후, 왼쪽의 "Crashlytics" 탭을 선택하여 오류 및 충돌 데이터를 확인할 수 있습니다. 여기에서 앱의 안정성에 관련된 정보를 확인하고, 문제점을 분석하고 해결할 수 있습니다.

## 결론

이제 Firebase Crashlytics를 사용하여 플러터 앱의 오류 및 충돌을 실시간으로 모니터링하고 해결하는 방법을 알아보았습니다. 이를 통해 앱의 안정성을 향상시키고 사용자 경험을 개선할 수 있습니다. Firebase 문서 및 Crashlytics 문서를 참조하여 더 자세한 내용을 학습하고 실제 프로젝트에 도입해보세요!

참고 자료:
- [Firebase 문서 - Flutter 앱에 Firebase 추가](https://firebase.google.com/docs/flutter/setup)
- [Firebase 구글 그룹 - Flutter에서 중대한 오류를 처리하는 방법](https://groups.google.com/g/firebase-talk/c/beQ7Q0j0mi8?pli=1)
- [FlutterFire GitHub 저장소 - Firebase Crashlytics](https://github.com/FirebaseExtended/flutterfire/tree/master/packages/firebase_crashlytics)