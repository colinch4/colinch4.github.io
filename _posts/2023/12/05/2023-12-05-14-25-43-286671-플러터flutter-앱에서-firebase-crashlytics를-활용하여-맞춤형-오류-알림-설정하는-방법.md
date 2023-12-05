---
layout: post
title: "[flutter] 플러터(Flutter) 앱에서 Firebase Crashlytics를 활용하여 맞춤형 오류 알림 설정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 오류를 신속하게 탐지하고 사용자에게 알림을 제공하는 강력한 도구입니다. 이 글에서는 플러터(Flutter) 앱에서 Firebase Crashlytics를 활용하여 맞춤형 오류 알림을 설정하는 방법에 대해 알아보겠습니다.

## 목차
- [Firebase Crashlytics 설정](#firebase-crashlytics-설정)
- [맞춤형 오류 알림 설정](#맞춤형-오류-알림-설정)

## Firebase Crashlytics 설정

1. Firebase 콘솔에 접속하여 프로젝트를 선택하고, "Crashlytics"를 클릭합니다.
2. "Crashlytics" 설정 페이지에서 "시작하기" 버튼을 클릭하여 Crashlytics를 활성화합니다.
3. `pubspec.yaml` 파일에 firebase_crashlytics 라이브러리를 추가합니다.

```yaml
dependencies:
  firebase_crashlytics: ^0.2.4
```

4. `main.dart` 파일의 `main()` 함수에서 Crashlytics를 초기화합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  await Firebase.initializeApp();
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  runZonedGuarded(() {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

5. 앱을 실행하여 Crashlytics를 테스트합니다. 이로써 앱에서 발생한 오류가 Firebase Crashlytics에 기록될 것입니다.

## 맞춤형 오류 알림 설정

Firebase Crashlytics에서 맞춤형 오류 알림을 설정하려면 [Firebase 콘솔](https://console.firebase.google.com/)에서 다음 단계를 수행해야 합니다.

1. Firebase 콘솔에 접속하여 프로젝트를 선택하고, "Crashlytics"를 클릭합니다.
2. "Crashlytics" 설정 페이지에서 "알림" 탭을 클릭합니다.
3. "오류 알림" 섹션에서 원하는 알림 설정을 변경합니다.
   - "자세한 오류 보고서 이메일로 전송" 옵션을 선택하면 선택한 이메일로 오류에 대한 자세한 보고서가 전송됩니다.
   - "앱 업데이트 알림 수신" 옵션을 선택하면 새로운 버전의 앱 업데이트가 출시될 때 알림을 받을 수 있습니다.
   - "대시보드 알림" 옵션을 선택하면 대시보드에서도 알림을 받을 수 있습니다.

이제 앱에서 발생하는 오류에 대한 맞춤형 알림 설정이 완료되었습니다. Firebase Crashlytics는 선택한 설정에 따라 오류 알림을 제공할 것입니다.

더 많은 Firebase Crashlytics 설정 옵션 및 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참고하세요.