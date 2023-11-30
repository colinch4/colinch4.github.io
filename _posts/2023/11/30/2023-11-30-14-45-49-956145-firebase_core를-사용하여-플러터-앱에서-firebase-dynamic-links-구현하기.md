---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Dynamic Links 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Dynamic Links는 앱에서 동적으로 생성되는 링크를 통해 사용자를 특정 화면으로 이동시킬 수 있는 기능입니다. 플러터 앱에서 Firebase Dynamic Links를 구현하기 위해서는 `firebase_core` 패키지를 사용해야 합니다. 이번 튜토리얼에서는 `firebase_core` 패키지를 통해 Firebase Dynamic Links를 구현하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Dynamic Links를 사용하기 위해서는 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에 접속하여 프로젝트를 생성하고, 해당 프로젝트에 앱을 추가해야 합니다. 추가한 앱의 패키지 이름은 나중에 사용될 것이므로 정확히 입력해야 합니다.

## 2. `pubspec.yaml` 파일 수정

프로젝트의 `pubspec.yaml` 파일에 `firebase_core` 패키지를 추가해야 합니다. 아래와 같이 `dependencies` 섹션에 `firebase_core` 패키지를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

`dependencies` 섹션에 `firebase_core` 패키지를 추가한 뒤에는 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드 받아야 합니다.

## 3. `main.dart` 파일 수정

이제 `main.dart` 파일을 열고 `firebase_core` 패키지를 초기화하는 코드를 추가해야 합니다. `main()` 함수 내에서 `Firebase.initializeApp()` 메서드를 호출하여 Firebase를 초기화합니다. 이 작업은 앱이 시작될 때 한 번만 수행되어야 합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(); // Firebase 초기화
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Firebase Dynamic Links',
      //...
    );
  }
}
```

## 4. Dynamic Links 처리

이제 Firebase Dynamic Links를 처리하는 코드를 작성해보겠습니다. Dynamic Links를 처리하기 위해서는 `firebase_dynamic_links` 패키지를 사용해야 합니다. 먼저, `pubspec.yaml` 파일에 `firebase_dynamic_links` 패키지를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
  firebase_dynamic_links: ^2.0.0
```

다음으로, 원하는 화면으로 이동할 수 있는 함수를 정의합니다. 예를 들면, `HomePage`로 이동하는 함수를 만들어 보겠습니다.

```dart
void _handleDynamicLink(BuildContext context) async {
  final PendingDynamicLinkData data =
      await FirebaseDynamicLinks.instance.getInitialLink();
  final Uri deepLink = data?.link;

  if (deepLink != null) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => HomePage(), // 이동할 화면
      ),
    );
  }

  FirebaseDynamicLinks.instance.onLink(
    onSuccess: (PendingDynamicLinkData dynamicLink) async {
      final Uri deepLink = dynamicLink?.link;

      if (deepLink != null) {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => HomePage(), // 이동할 화면
          ),
        );
      }
    },
    onError: (OnLinkErrorException e) async {
      print('onLinkError');
      print(e.message);
    },
  );
}
```

위의 코드에서는 `getInitialLink()` 메서드를 통해 초기로드 시 동적 링크를 처리하고, `onLink()` 이벤트를 통해 앱이 실행 중일 때 동적 링크를 처리합니다. 링크를 처리할 페이지로 이동하는 코드는 본인의 앱에 맞게 수정해야 합니다.

## 5. 앱에 Dynamic Link 추가

Firebase 콘솔에서 Dynamic Links를 생성하고, 복사한 링크를 앱에 추가해야 합니다. 앱에서 Dynamic Link를 처리하도록 설정하기 위해서는 `android/app/src/main/AndroidManifest.xml` 파일과 `ios/Runner/Info.plist` 파일에 수정이 필요합니다. Firebase 콘솔에서 제공하는 지침에 따라 해당 파일들을 수정합니다.

## 6. Dynamic Link 테스트

이제 앱을 실행하고 Firebase Dynamic Links를 테스트해 볼 차례입니다. Firebase 콘솔에서 생성한 링크를 웹 브라우저로 접속하면 앱이 실행되고, 해당 페이지로 이동하는 것을 확인할 수 있습니다.

Firebase Dynamic Links를 통해 플러터 앱에서 동적 링크를 구현하는 방법에 대해 알아보았습니다. Firebase Dynamic Links는 앱의 사용자 경험을 향상시키고, 사용자들을 특정 화면으로 이동시킬 때 유용한 기능입니다. Firebase Dynamic Links를 활용하여 앱의 기능을 더욱 확장해보세요!

### 참고 자료

- [FlutterFire - Firebase Core](https://firebase.flutter.dev/docs/core/overview)
- [FlutterFire - Dynamic Links](https://firebase.flutter.dev/docs/dynamic-links/overview)
- [Firebase Dynamic Links 공식 문서](https://firebase.google.com/docs/dynamic-links)