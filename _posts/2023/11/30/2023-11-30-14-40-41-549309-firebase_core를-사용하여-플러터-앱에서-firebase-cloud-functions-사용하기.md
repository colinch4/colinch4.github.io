---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Functions 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 모바일 앱 개발에 필요한 다양한 서비스를 제공하는 플랫폼입니다. Firebase의 한 가지 유용한 기능은 Firebase Cloud Functions인데, 이를 사용하면 서버 측 로직을 클라우드에서 실행할 수 있습니다. 

이번 블로그에서는 플러터 앱에서 Firebase Cloud Functions를 사용하기 위해 필요한 `firebase_core` 패키지를 소개하겠습니다. 

## 1. `firebase_core` 패키지 추가하기

먼저, Firebase Cloud Functions를 사용하기 위해 `firebase_core` 패키지를 프로젝트에 추가해야 합니다. 

`pubspec.yaml` 파일에 다음과 같이 패키지를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.8.0
```

위와 같이 `firebase_core` 패키지를 추가한 후, 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

## 2. Firebase 설정하기

Firebase Cloud Functions를 사용하기 위해 Firebase 프로젝트를 생성하고, 해당 프로젝트의 설정을 플러터 앱에 추가해야 합니다.

Firebase 콘솔에 접속하여 프로젝트를 생성하고, `google-services.json` 파일을 다운로드합니다.

다운로드한 `google-services.json` 파일을 프로젝트의 `android/app` 디렉터리에 추가합니다.

프로젝트의 `android/app/build.gradle` 파일 최상단에 다음 코드를 추가합니다:

```gradle
apply plugin: 'com.google.gms.google-services'
```

프로젝트의 `android/build.gradle` 파일의 dependencies 블록에 다음 코드를 추가합니다:

```gradle
classpath 'com.google.gms:google-services:4.3.10'
```

## 3. Firebase 초기화하기

Firebase Cloud Functions를 사용하기 위해 앱을 초기화해야 합니다. 

프로젝트의 `main.dart` 파일 상단에 다음 코드를 추가합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

위와 같이 `Firebase.initializeApp()` 메서드를 호출하여 Firebase를 초기화합니다.

## 4. Firebase Cloud Functions 사용하기

이제 Firebase Cloud Functions를 사용할 준비가 되었습니다.

예를 들어, 앱에서 사용자가 로그인을 하면 서버에 로그인 이벤트를 보내고, 서버에서 해당 이벤트에 대한 응답을 받는 기능을 구현하고 싶다고 가정해봅시다.

플러터 앱의 어떤 버튼을 클릭하면 Firebase Cloud Functions를 호출하고 응답을 받을 수 있는 함수를 다음과 같이 작성할 수 있습니다:

```dart
import 'package:cloud_functions/cloud_functions.dart';

Future<void> callLoginFunction() async {
  HttpsCallable loginFunction = FirebaseFunctions.instance.httpsCallable('loginFunction');

  try {
    final results = await loginFunction.call();
    final response = results.data;
    print(response);
  } catch (e) {
    print('Error: $e');
  }
}
```

위 코드에서 `loginFunction`은 Firebase Cloud Functions의 이름을 나타냅니다. 이 함수를 호출하면 서버에서 처리한 결과를 받을 수 있습니다. 

이제 플러터 앱에서 해당 함수를 호출하기 위해 버튼 위젯에 다음과 같이 함수를 연결합니다:

```dart
FlatButton(
  onPressed: () {
    callLoginFunction();
  },
  child: Text('Login'),
),
```

## 마무리

이제 플러터 앱에서 Firebase Cloud Functions를 사용하기 위한 `firebase_core` 패키지의 추가와 Firebase의 초기화 방법을 알아보았습니다. 이를 통해 서버 측 로직을 클라우드에서 실행하는 기능을 효율적으로 구현할 수 있습니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.flutter.dev/)를 참고하시기 바랍니다.