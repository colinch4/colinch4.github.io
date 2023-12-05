---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 발생률과 심각도를 분석하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)로 개발된 앱을 출시하고 운영하는 과정에서 앱의 안정성과 사용자 경험을 보장하기 위해서는 오류와 크래시를 신속하게 식별하고 수정해야 합니다. Firebase Crashlytics는 플러터 앱에서 오류를 추적하고 심각도를 파악하여 이러한 문제를 해결하는 데 도움을 주는 강력한 도구입니다.

## Firebase Crashlytics란?

Firebase Crashlytics는 Firebase의 하나의 기능으로 앱에서 발생한 오류들을 실시간으로 추적하고 분석하여 개발자에게 알려줍니다. 오류 발생 시 디바이스와 사용자의 정보, 오류 발생 위치 등 자세한 로그를 제공하여 개발자가 문제를 해결할 수 있도록 도와줍니다.

## Firebase 프로젝트에 Crashlytics 추가하기

Firebase Crashlytics를 사용하기 위해서는 먼저 Firebase 프로젝트에 Crashlytics를 추가해야 합니다. Firebase 콘솔에서 해당 프로젝트를 선택한 후, "개발" 탭에서 "Crashlytics"를 클릭하여 Crashlytics를 활성화하면 됩니다.

## 플러터(Flutter) 프로젝트에 Firebase Crashlytics 통합하기

1. `pubspec.yaml` 파일에 `firebase_crashlytics` 의존성을 추가합니다:
```dart
dependencies:
  firebase_crashlytics: ^0.5.3
```

2. `main.dart` 파일에서 Firebase Crashlytics를 초기화합니다. `runApp()` 전에 다음 코드를 추가합니다:
```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  // Crashlytics 초기화
  FirebaseCrashlytics.instance.crash();
  runZonedGuarded(() {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

3. 오류 및 예외 발생 시 Crashlytics에 보고하는 코드를 추가합니다. 예를 들어, 특정 버튼이 클릭되었을 때 오류 발생을 로깅하고 Crashlytics에 보고하는 코드를 추가할 수 있습니다:
```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

RaisedButton(
  child: Text('버튼'),
  onPressed: () {
    try {
      // 오류 발생 시도
      throw Exception("버튼 클릭 오류");
    } catch (e, s) {
      // 오류 로깅 후 Crashlytics에 보고
      FirebaseCrashlytics.instance.recordError(e, s);
    }
  },
),
```

실제 앱에서는 오류 발생 조건을 파악하여 로깅할 수 있도록 조건문 등을 활용해야 합니다.

## Crashlytics 로그 및 분석

Firebase 콘솔에서 Crashlytics를 열어 앱의 오류 통계 및 상세 정보를 확인할 수 있습니다. Crashlytics 대시보드에서는 간단한 통계 정보뿐만 아니라 오류 발생 위치, 오류 타입, 디바이스 정보 등의 자세한 내용을 제공합니다. 이를 통해 개발자는 앱의 오류 발생률과 심각도를 파악하고, 가장 심각한 오류를 해결하기 위한 우선순위를 정할 수 있습니다.

## 요약

Firebase Crashlytics를 통해 플러터 앱의 오류 발생률과 심각도를 신속하게 분석할 수 있으며, 이를 통해 개발자는 앱의 안정성을 향상시킬 수 있습니다. Crashlytics를 Firebase 프로젝트에 추가한 후, 플러터 프로젝트에서 초기화하고 오류를 로깅하여 Crashlytics에 보고하는 코드를 추가하면 됩니다. Firebase 콘솔에서 Crashlytics 대시보드를 통해 앱의 오류 통계와 분석 정보를 확인할 수 있습니다.

더 많은 정보를 원하신다면, [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참조하세요.