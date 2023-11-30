---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Functions 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google이 제공하는 모바일 및 웹 애플리케이션 개발 플랫폼입니다. Firebase에는 다양한 기능이 있지만, 이번에는 Firebase Cloud Functions를 사용하여 플러터 앱에서 서버 사이드 로직을 처리하는 방법을 알아보겠습니다.

Firebase Cloud Functions는 JavaScript로 작성된 서버 사이드 코드를 실행하는 서버리스 컴퓨팅 플랫폼입니다. 이를 사용하여 백그라운드에서 비동기 작업을 수행하거나 외부 API와 통신하는 등의 작업을 수행할 수 있습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에 로그인한 후, 새 프로젝트를 만들고 해당 프로젝트를 선택합니다. 그런 다음 "Cloud Functions"을 활성화합니다.

## 2. Flutter 프로젝트에 Firebase_core 추가하기

Firebase를 Flutter 프로젝트에서 사용하려면 `firebase_core` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 다음 코드를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
```

그런 다음 터미널을 열고 `flutter pub get` 명령을 실행하여 패키지를 다운로드합니다.

## 3. Firebase 프로젝트와 연결하기

Flutter 앱과 Firebase 프로젝트를 연결하기 위해 `main.dart` 파일의 `main()` 함수에서 다음 코드를 추가합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase 초기화를 위해 `Firebase.initializeApp()` 메서드를 사용합니다. 이 메서드는 비동기로 동작하므로 `async`와 `await` 키워드를 사용하여 초기화가 완료될 때까지 기다립니다.

## 4. Firebase Cloud Functions 사용하기

Firebase Cloud Functions를 사용하여 서버 사이드 로직을 실행하려면 `cloud_functions` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 다음 코드를 추가하고 패키지를 다운로드합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
  cloud_functions: ^3.0.1
```

이제 Flutter 코드에서 Firebase Cloud Functions를 사용할 수 있습니다. 예를 들어, 사용자가 특정 버튼을 클릭했을 때 서버의 함수를 호출하도록 할 수 있습니다:

```dart
import 'package:cloud_functions/cloud_functions.dart';

final HttpsCallable callable = FirebaseFunctions.instance.httpsCallable('myFunction');

final results = await callable.call();

print(results.data);
```

`FirebaseFunctions.instance.httpsCallable('myFunction')`를 사용하여 서버의 함수를 가져올 수 있습니다. 그런 다음 `call()` 메서드를 호출하여 서버 함수를 실행하고 결과를 얻을 수 있습니다.

## 5. 결론

이제 Firebase Cloud Functions를 사용하여 플러터 앱에서 서버 사이드 로직을 실행하는 방법을 알아보았습니다. Firebase를 사용하면 클라우드 기반의 강력한 기능을 앱에 쉽게 통합할 수 있습니다.

참고:
- [Firebase 콘솔](https://console.firebase.google.com/)
- [flutterfire/flutterfire repository](https://firebase.flutter.dev/)
- [Cloud Functions for Firebase](https://firebase.google.com/docs/functions)