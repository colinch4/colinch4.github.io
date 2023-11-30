---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Analytics 분석하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 구글에서 제공하는 클라우드 기반 플랫폼으로, 플러터 앱 개발에 많은 도움을 줄 수 있습니다. Firebase Analytics는 앱 사용자의 행동과 이용 패턴을 추적하여 데이터를 수집하고 분석하는 도구입니다. 이번 글에서는 `firebase_core` 패키지를 사용하여 플러터 앱에서 Firebase Analytics를 설정하고 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새로운 프로젝트를 생성해야 합니다. 프로젝트 생성이 완료되면 Firebase Analytics를 활성화해야 합니다.

## 2. flutterfire 패키지 설치

Firebase를 사용하기 위해 `flutterfire` 패키지를 설치해야 합니다. `pubspec.yaml` 파일에 다음과 같이 의존성을 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
  firebase_analytics: ^8.0.0
```

패키지를 설치하기 위해 터미널에서 `flutter pub get` 명령어를 실행합니다.

## 3. Firebase 앱 설정

Firebase 앱을 설정하려면 `main` 함수에서 `Firebase.initializeApp()`를 호출해야 합니다. 예시는 다음과 같습니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  Firebase.initializeApp();
  runApp(MyApp());
}
```

## 4. Firebase Analytics 사용하기

Firebase Analytics를 사용하기 위해 `firebase_analytics` 패키지를 초기화하고 이벤트를 추적할 수 있습니다. 다음은 간단한 예시입니다:

```dart
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:firebase_analytics/observer.dart';

class MyApp extends StatelessWidget {
  final FirebaseAnalytics analytics = FirebaseAnalytics();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      navigatorObservers: [
        FirebaseAnalyticsObserver(analytics: analytics),
      ],
      // 앱 컨텐츠
    );
  }
}

void trackEvent() {
  FirebaseAnalytics().logEvent(
    name: 'button_click',
    parameters: {'button_id': 'my_button'},
  );
}
```

Firebase Analytics를 초기화하고 마지막에 `FirebaseAnalyticsObserver`를 `navigatorObservers`에 등록하여 앱 내에서 페이지 이동에 대한 이벤트를 추적할 수 있습니다. 이벤트를 추적하기 위해서는 `logEvent` 메서드를 사용하면 됩니다.

추가적인 기능 및 세부 설정에 대해서는 Firebase 공식 문서를 참고하시기 바랍니다.

## 참고 자료

- [Firebase 공식 문서](https://firebase.flutter.dev/)
- [flutterfire GitHub 저장소](https://github.com/FirebaseExtended/flutterfire)