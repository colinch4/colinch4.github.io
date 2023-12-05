---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 발생 원인을 다른 지표와 실시간으로 연계하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

안녕하세요! 이번에는 Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 발생 원인을 다른 지표와 실시간으로 연계하는 방법에 대해 알아보겠습니다.

Firebase Crashlytics는 Firebase 플랫폼의 일부로, 앱의 오류를 자동으로 수집하고 보고해줌으로써 개발자가 앱의 안정성을 개선할 수 있도록 도와줍니다. Crashlytics를 사용하면 앱이 충돌하거나 예외가 발생할 때 실시간으로 오류 정보를 수집하고, 해당 오류가 발생한 사용자의 디바이스 및 앱 버전 정보 등을 확인할 수 있습니다.

이제 Crashlytics를 플러터 앱에 연동하는 과정을 알아보겠습니다.

## 1. Firebase 프로젝트 설정

먼저 Firebase 프로젝트에서 Crashlytics를 활성화해야 합니다. Firebase 콘솔(https://console.firebase.google.com)에 로그인하여 프로젝트를 선택한 후 다음 단계를 따릅니다.

1. "프로젝트 설정"으로 이동합니다.
2. "통합" 탭에서 "Crashlytics"를 선택합니다.
3. "시작하기" 버튼을 클릭하여 Crashlytics를 활성화합니다.

## 2. Flutter 앱에 Crashlytics 패키지 추가

이제 Flutter 앱에 Crashlytics 패키지를 추가해야 합니다. 이를 위해 `pubspec.yaml` 파일을 열고 `firebase_crashlytics` 패키지를 dependencies에 추가합니다.

```yaml
dependencies:
  firebase_crashlytics: ^2.4.1
```

그리고 패키지를 설치하기 위해 다음 명령어를 실행합니다.

```bash
flutter pub get
```

## 3. Crashlytics 초기화

이제 Crashlytics를 사용하기 위해 앱을 초기화해야 합니다. 이를 위해 앱의 진입점(main 함수)에서 다음과 같이 Crashlytics를 초기화합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  FirebaseCrashlytics.instance.initializeApp();
  runZonedGuarded<Future<void>>(() async {
    // 앱의 나머지 코드 실행
  }, FirebaseCrashlytics.instance.recordError);
}
```

위 코드에서 `recordError`는 Crashlytics가 오류를 자동으로 수집하도록 처리하는 핵심 함수입니다.

## 4. 오류 보고

이제 Crashlytics가 앱의 오류를 실시간으로 보고하도록 설정할 수 있습니다. 예를 들어, 특정 버튼을 클릭할 때 오류가 발생하면 Crashlytics에 오류를 보고하는 코드를 추가할 수 있습니다.

```dart
void _throwError() {
  try {
    throw Exception('예외 발생!');
  } catch (e, s) {
    FirebaseCrashlytics.instance.recordError(e, s);
  }
}
```

위 예제에서는 `_throwError` 함수가 호출될 때 `Exception`을 발생시키고 해당 예외를 Crashlytics에 보고합니다.

## 5. Crashlytics 대시보드에서 오류 확인

Firebase 콘솔에서 Crashlytics 섹션으로 이동하여 앱의 오류 로그를 확인할 수 있습니다. 대시보드에서는 오류 발생 횟수, 사용자 수 등 다양한 지표를 제공하여 앱의 안정성을 파악할 수 있습니다.

오류 발생 시 Crashlytics는 기본적으로 앱이 다시 시작되지 않아도 오류를 수집하고 보고합니다. 또한 자동으로 앱 버전 정보, 디바이스 정보, 스택 트레이스 등을 제공하여 오류의 원인을 파악할 수 있도록 도와줍니다.

이렇게 Firebase Crashlytics를 사용하여 플러터 앱의 오류 발생 원인을 다른 지표와 실시간으로 연계할 수 있습니다. Crashlytics를 통해 앱의 안정성을 개선하고 사용자 경험을 향상시킬 수 있습니다.

더 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics/)를 참조하세요.

반드시 사용자의 환경에 맞게 코딩해야합니다. 코드의 일부가 비활성화 된 경우 해당 부분을 위해 적절한 처리 방식도 고려되어야합니다.