---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Analytics 분석하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google이 제공하는 클라우드 기반 개발 플랫폼으로, 다양한 서비스를 제공합니다. Firebase Analytics는 Firebase의 중요한 기능 중 하나로, 앱의 사용자 동작 및 특성에 대한 다양한 데이터를 수집하고 분석할 수 있습니다. 이 포스트에서는 Flutter 앱에서 Firebase Analytics를 사용하기 위해 `firebase_core` 패키지를 추가하고, 초기 설정을 하는 방법을 알아보겠습니다.

## 1. firebase_core 패키지 추가하기

먼저, Firebase Analytics를 사용하기 위해 `firebase_core` 패키지를 프로젝트에 추가해야 합니다. `pubspec.yaml` 파일을 열고 dependencies 섹션에 다음 코드를 추가합니다:

```yaml
dependencies:
  firebase_core: ^1.4.0
```

이제 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드 받고 프로젝트에 적용합니다.

## 2. Firebase 프로젝트 설정하기

Firebase Console로 이동하여 새로운 Firebase 프로젝트를 생성하고 앱을 추가합니다. 제공된 구성 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 다운로드하고 프로젝트 디렉토리에 추가합니다.

## 3. Firebase 초기화하기

이제 Firebase를 초기화하는 코드를 작성해보겠습니다. 먼저, `main.dart` 파일을 열고 `firebase_core` 패키지를 임포트합니다:

```dart
import 'package:firebase_core/firebase_core.dart';
```

`main()` 함수 안에서 Firebase를 초기화하는 코드를 작성합니다:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

위의 코드는 앱이 시작될 때 `Firebase.initializeApp()` 메서드를 호출하여 Firebase를 초기화합니다. `await` 키워드를 사용하여 비동기로 작업을 수행합니다.

## 4. Firebase Analytics 사용하기

Firebase 초기화가 완료되면, 이제 Firebase Analytics를 사용할 수 있습니다. 예를 들어, 특정 버튼이 클릭되었을 때 해당 이벤트를 Firebase Analytics에 기록하려면 다음과 같은 코드를 사용할 수 있습니다:

```dart
void trackButtonClicked() {
  FirebaseAnalytics().logEvent(
    name: 'button_clicked',
    parameters: {'button_id': 'my_button'},
  );
}
```

위의 코드에서 `logEvent()` 메서드를 사용하여 특정 이벤트를 기록합니다. 이벤트 이름과 매개 변수를 전달할 수 있습니다.

## 마무리

이제 Firebase_core 패키지를 사용하여 플러터 앱에서 Firebase Analytics를 사용하는 방법을 알아보았습니다. Firebase Analytics를 사용하여 앱의 사용자 동작 및 성과를 분석하여 앱의 개선에 도움이 될 수 있습니다. Firebase Console에서 수집된 데이터를 확인하고 분석하여 앱을 최적화하는 데 활용해보세요.

더 자세한 내용은 [firebase_core 패키지 문서](https://pub.dev/documentation/firebase_core/latest/firebase_core/firebase_core-library.html) 및 [FlutterFire 문서](https://firebase.flutter.dev/)를 참조하시기 바랍니다.