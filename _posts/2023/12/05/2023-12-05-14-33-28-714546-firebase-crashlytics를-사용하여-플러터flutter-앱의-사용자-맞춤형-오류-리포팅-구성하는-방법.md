---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 사용자 맞춤형 오류 리포팅 구성하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 플러터(Flutter) 앱의 오류를 감지하고 리포팅하는 데 사용되는 강력한 도구입니다. 이 문서에서는 Firebase Crashlytics를 사용하여 플러터 앱의 사용자 맞춤형 오류 리포팅을 구성하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Crashlytics를 사용하기 위해 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔(https://console.firebase.google.com)에 로그인한 후, 새 프로젝트를 만들거나 기존 프로젝트를 선택합니다.

## 2. Firebase Crashlytics SDK 추가

Firebase Crashlytics를 사용하려면 먼저 Flutter 프로젝트에 Firebase Crashlytics SDK를 추가해야 합니다. `pubspec.yaml` 파일에 다음 종속성을 추가하세요.

```yaml
dependencies:
  firebase_crashlytics: ^2.2.3
```

SDK를 추가한 후, 터미널에서 `flutter pub get` 명령을 실행하여 종속성을 다운로드합니다.

## 3. Firebase 프로젝트와 앱 연결

Firebase 프로젝트와 플러터 앱을 연결해야 합니다. Firebase 콘솔에서 프로젝트 설정을 열고, 앱 설정을 클릭합니다. "앱을 추가하세요" 버튼을 클릭하여 플러터 앱을 추가합니다. 패키지 이름과 안드로이드 앱의 디버그/릴리즈 서명 인증서 SHA-1 지문을 입력하세요.

## 4. Crashlytics 설정

Firebase Crashlytics를 시작하기 전에 앱의 `main.dart` 파일에 다음 코드를 추가하여 Crashlytics를 초기화해야 합니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Firebase.initializeApp();
  
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  
  runApp(MyApp());
}
```

위 코드에서 `Firebase.initializeApp()`을 호출하여 Firebase를 초기화하고, `FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true)`를 사용하여 Crashlytics 데이터 수집을 활성화합니다.

## 5. 사용자 정의 오류 리포팅

Firebase Crashlytics를 사용하여 사용자 정의 오류 리포팅을 추가할 수 있습니다. 예를 들어, 사용자가 특정 버튼을 클릭했을 때 오류를 리포트하고 싶다면 아래와 같이 코드를 작성할 수 있습니다.

```dart
try {
  // 버튼 클릭 시 동작하는 코드
} catch (e, s) {
  FirebaseCrashlytics.instance.recordError(e, s);
}
```

위 코드에서 `FirebaseCrashlytics.instance.recordError(e, s)`를 사용하여 오류를 리포트합니다. `e`는 오류 객체이고, `s`는 오류 발생 위치 정보인 스택 트레이스입니다.

## 결론

이제 Firebase Crashlytics를 사용하여 플러터 앱에 사용자 맞춤형 오류 리포팅을 구성할 수 있습니다. Firebase Crashlytics의 강력한 기능을 적극 활용하여 앱의 안정성을 향상시키고 사용자 경험을 개선해보세요.

## 참고 자료

- Firebase Crashlytics 공식 문서: https://firebase.google.com/docs/crashlytics
- Firebase Flutter 패키지: https://pub.dev/packages/firebase_crashlytics