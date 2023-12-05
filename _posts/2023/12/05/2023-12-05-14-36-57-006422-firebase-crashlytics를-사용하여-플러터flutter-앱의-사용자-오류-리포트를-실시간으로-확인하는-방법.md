---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 사용자 오류 리포트를 실시간으로 확인하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 사용자 오류 리포트를 수집하고 실시간으로 확인할 수 있는 강력한 도구입니다. 이 기능은 Firebase의 일부로 제공되며, Firebase 프로젝트에 추가하여 사용할 수 있습니다.

## Firebase Crashlytics 설정

1. Firebase 콘솔에 로그인하고, 프로젝트를 선택합니다.
2. 왼쪽 메뉴에서 "Crashlytics"를 선택합니다.
3. "시작하기"를 클릭하고, 개발자 약관에 동의합니다.
4. Crashlytics SDK를 프로젝트에 추가하기 위해 안내에 따라 진행합니다.

## 플러터(Flutter) 앱에 Firebase 추가

1. Flutter 앱의 `pubspec.yaml` 파일을 열고, `firebase_crashlytics` 패키지를 추가합니다:

```yaml
dependencies:
  firebase_crashlytics: ^2.5.2
```

2. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

3. `main.dart` 파일을 열고, 앱을 초기화 하는 부분에 다음 코드를 추가합니다:

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp();
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);

  runZonedGuarded<Future<void>>(
    () async {
      runApp(MyApp());
    },
    (error, stackTrace) async {
      await FirebaseCrashlytics.instance.recordError(error, stackTrace);
    },
  );
}
```

위 코드는 `FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true)`를 통해 Crashlytics 수집을 활성화하며, `runZonedGuarded`를 사용하여 앱 내의 발생하는 모든 오류를 Crashlytics에 기록합니다.

## 실시간 오류 리포트 확인

Firebase 콘솔에서 Crashlytics 섹션으로 이동하여 실시간으로 앱의 사용자 오류 리포트를 확인할 수 있습니다. 여기에서는 앱의 오류 발생 횟수, 사용자 수 등 다양한 정보를 확인할 수 있습니다.

## 정리

Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 사용자 오류 리포트를 실시간으로 확인하는 방법에 대해 알아보았습니다. Crashlytics는 앱의 안정성과 품질을 향상시키는 데 매우 유용한 도구입니다. 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/crashlytics)를 참조하시기 바랍니다.