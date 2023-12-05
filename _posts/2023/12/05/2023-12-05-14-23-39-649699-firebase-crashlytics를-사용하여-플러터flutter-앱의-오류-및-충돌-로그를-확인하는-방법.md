---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 및 충돌 로그를 확인하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 Firebase의 앱 분석 도구 중 하나로, 모바일 앱의 오류 및 충돌 로그를 실시간으로 모니터링하고 기록하는 기능을 제공합니다. 이 기능을 사용하면 개발자는 앱의 안정성을 유지하고 사용자 경험을 향상시킬 수 있습니다. 이제 Flutter 앱에서 Firebase Crashlytics를 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Console에 로그인하고, 프로젝트를 생성하거나 기존 프로젝트를 선택합니다. 프로젝트 설정에서 "Crashlytics"를 활성화해줍니다.

## 2. Flutter 앱에 Firebase 추가

Flutter 프로젝트의 `pubspec.yaml` 파일에서 `firebase_crashlytics` 패키지를 추가합니다.

```dart
dependencies:
  firebase_core: ^1.0.0
  firebase_crashlytics: ^2.4.0
```

그리고 `pub get`를 실행하여 패키지를 설치합니다.

## 3. Firebase 초기화

Firebase Crashlytics를 사용하기 위해 먼저 Firebase를 초기화해야 합니다. `main` 함수에서 다음과 같이 초기화 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  // ...
}
```

## 4. Crashlytics 초기화

Firebase 초기화 후, 앱의 첫 번째 화면인 `MaterialApp` 위젯의 `home` 속성에서 `Crashlytics.instance.initializeApp()`을 호출하여 Crashlytics를 초기화합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // ...
    return MaterialApp(
      home: Builder(
        builder: (context) {
          Crashlytics.instance.initializeApp();
          // ...
        },
      ),
    );
  }
}
```

## 5. 오류 및 충돌 기록하기

Flutter 앱에서 오류 및 충돌을 기록하려면 `try-catch` 블록으로 감싸고 `Crashlytics.instance.recordError` 메서드를 호출하면 됩니다. 예를 들어, 다음과 같이 코드를 작성할 수 있습니다.

```dart
try {
  // 오류가 발생할 수 있는 코드
} catch (error, stackTrace) {
  Crashlytics.instance.recordError(error, stackTrace);
}
```

## 6. 로그 추가하기

Crashlytics에 로그를 추가하여 디버깅을 도와줄 수도 있습니다. `Crashlytics.instance.log` 메서드를 사용하여 로그를 추가할 수 있습니다. 예를 들어, 다음과 같이 코드를 작성할 수 있습니다.

```dart
Crashlytics.instance.log('This is a log message');
```

## 7. 사용자 지정 데이터 추가하기

추가적인 디버그 정보를 제공하기 위해, 사용자 지정 데이터를 Crashlytics에 추가할 수도 있습니다. `Crashlytics.instance.setCustomKey` 메서드를 사용하여 데이터를 추가합니다. 예를 들어, 다음과 같이 코드를 작성할 수 있습니다.

```dart
Crashlytics.instance.setCustomKey('user_id', '12345');
Crashlytics.instance.setCustomKey('username', 'john123');
```

## 8. 테스트 및 배포

Firebase Crashlytics가 작동하는지 확인하기 위해 앱을 테스트합니다. 오류 및 충돌이 발생하면 Firebase Console에서 해당 로그를 확인할 수 있습니다. 앱을 배포하기 전에도 충분한 테스트를 수행하여 오류와 충돌을 방지할 수 있습니다.

이제 Firebase Crashlytics를 사용하여 플러터 앱의 오류 및 충돌 로그를 확인하는 방법에 대해 알게 되었을 것입니다. 이 도구를 사용하여 앱의 안정성을 유지하고 사용자 경험을 향상시킬 수 있습니다.

더 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참조하세요.