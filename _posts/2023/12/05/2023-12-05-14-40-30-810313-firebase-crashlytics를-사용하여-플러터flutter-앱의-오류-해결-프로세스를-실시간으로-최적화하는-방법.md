---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 해결 프로세스를 실시간으로 최적화하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

앱 개발 과정에서 발생하는 오류는 사용자 경험에 악영향을 미치고 앱의 평판을 훼손할 수 있습니다. 오류 해결은 앱 개발자에게 매우 중요한 과제입니다. Firebase Crashlytics는 앱 안에서 발생하는 크래시와 오류를 실시간으로 모니터링하고 보고서를 제공하여 앱의 안정성을 향상시킬 수 있는 강력한 도구입니다. 이번 포스트에서는 Flutter 앱에서 Firebase Crashlytics를 사용하여 앱의 오류 해결 프로세스를 실시간으로 최적화하는 방법을 살펴보겠습니다.

## 목차
- [Firebase Crashlytics 설정](#firebase-crashlytics-설정)
- [앱에 Crashlytics SDK 추가](#앱에-crashlytics-sdk-추가)
- [오류 및 크래시 보고서 확인](#오류-및-크래시-보고서-확인)
- [사용자 정의 이벤트 및 로그 추가](#사용자-정의-이벤트-및-로그-추가)
- [오류 수정 및 앱 안정성 향상](#오류-수정-및-앱-안정성-향상)

### Firebase Crashlytics 설정

Firebase Crashlytics를 사용하려면 먼저 Firebase 프로젝트를 생성하고 해당 프로젝트에서 Crashlytics를 활성화해야 합니다. Firebase 콘솔에 로그인한 후, 프로젝트를 선택하고 "Crashlytics"로 이동합니다. "시작하기" 버튼을 클릭하여 Crashlytics 작업을 설정합니다.

### 앱에 Crashlytics SDK 추가

Flutter 앱에 Crashlytics SDK를 추가해야 합니다. `firebase_crashlytics` 패키지를 사용하여 Flutter 프로젝트에 Crashlytics를 통합할 수 있습니다. `pubspec.yaml` 파일에 아래의 의존성을 추가합니다.

```dart
dependencies:
  firebase_core: ^1.10.0
  firebase_crashlytics: ^2.2.3
```

의존성을 추가한 후, `pub get` 명령을 실행하여 패키지를 다운로드 및 설치합니다.

```bash
$ flutter pub get
```

이제 `main.dart` 파일에 Crashlytics를 초기화하는 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  if (kDebugMode) {
    // Debug 모드에서는 Crashlytics를 비활성화합니다.
    await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(false);
  } else {
    // Release 모드에서는 Crashlytics를 활성화합니다.
    await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  }

  runApp(MyApp());
}
```

### 오류 및 크래시 보고서 확인

Firebase Crashlytics가 작동하는지 확인하기 위해 앱에서 테스트 크래시를 발생시켜 봅니다. 예를 들어, 앱의 초기화 단계에서 다음과 같이 크래시를 발생시킬 수 있습니다.

```dart
void main() {
  WidgetsFlutterBinding.ensureInitialized();
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;

  throw Exception('Testing Crash');
  runApp(MyApp());
}
```

앱이 크래시가 발생하면, Firebase Crashlytics의 대시보드에서 해당 크래시를 확인할 수 있습니다. 대시보드에서는 크래시가 발생한 앱의 사용자 정보, 기기 정보, 스택 트레이스 등 자세한 정보를 확인할 수 있습니다.

### 사용자 정의 이벤트 및 로그 추가

Firebase Crashlytics를 사용하여 사용자 정의 이벤트 및 로그를 추가할 수도 있습니다. 예를 들어, 특정 화면에서 버튼이 클릭되었다는 정보를 로깅하고 싶다면 다음과 같이 코드를 작성할 수 있습니다.

```dart
void onButtonClicked() {
  FirebaseCrashlytics.instance.log('Button is clicked');
  FirebaseCrashlytics.instance.setCustomKey('button_clicked', true);

  // 이곳에서 버튼 클릭 관련 작업을 수행합니다.
}
```

Firebase Crashlytics는 이벤트 및 로그를 수집하고 기록하여 앱의 오류 해결에 도움을 줄 수 있습니다.

### 오류 수정 및 앱 안정성 향상

Firebase Crashlytics의 대시보드를 통해 발생한 오류와 크래시를 분석하고 해결할 수 있습니다. 반복적으로 발생하는 오류를 확인하고 해당 오류가 발생하는 상황을 재현하는 것이 중요합니다. 오류가 발생할 때마다 Crashlytics는 실시간으로 알림을 제공하여 빠른 대응을 할 수 있도록 도와줍니다. 오류를 수정하고 업데이트된 버전을 배포하면 사용자들이 안정적인 앱을 경험할 수 있게 됩니다.

여기까지 Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 해결 프로세스를 실시간으로 최적화하는 방법을 살펴보았습니다. Firebase Crashlytics는 강력한 도구로 앱의 안정성을 향상시키고 사용자의 만족도를 높일 수 있습니다.