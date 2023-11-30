---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Dynamic Links 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Dynamic Links는 앱 사용자에게 사용자 지정된 링크를 제공하여 앱 내에서 원하는 위치로 이동시킬 수 있는 기능입니다. Flutter 앱에서 Firebase Dynamic Links를 구현하는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 접속하여 프로젝트를 생성합니다.
2. 앱을 추가하고 Flutter 앱의 패키지 이름을 입력합니다.
3. `google-services.json` 파일을 다운로드하여 프로젝트의 `android/app` 디렉터리에 추가합니다.
4. `GoogleService-Info.plist` 파일을 다운로드하여 프로젝트의 `ios/Runner` 디렉터리에 추가합니다.

## Firebase SDK 설정

1. `pubspec.yaml` 파일에 다음 dependency를 추가합니다.
```dart
dependencies:
  firebase_core: ^1.0.1
  firebase_dynamic_links: ^2.0.2
```
2. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드합니다.

## Firebase 초기화

1. `main.dart` 파일의 `main` 함수에서 Firebase를 초기화합니다.
```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## Firebase Dynamic Links 구현

1. Firebase Dynamic Links를 초기화하기 위해 사용자 정의 함수를 추가합니다.
```dart
import 'package:firebase_dynamic_links/firebase_dynamic_links.dart';

Future<void> initDynamicLinks() async {
  final PendingDynamicLinkData? data = await FirebaseDynamicLinks.instance.getInitialLink();

  final Uri? deepLink = data?.link;
  if (deepLink != null) {
    // 앱이 처음으로 열릴 때 받은 딥링크 처리
    // ex) deepLink.path
  }

  FirebaseDynamicLinks.instance.onLink(
    onSuccess: (PendingDynamicLinkData? dynamicLink) async {
      final Uri? deepLink = dynamicLink?.link;
      if (deepLink != null) {
        // 앱이 이미 열린 상태에서 받은 딥링크 처리
        // ex) deepLink.path
      }
    },
    onError: (OnLinkErrorException e) async {
      print('Link Failed: $e');
    }
  );
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await initDynamicLinks(); // Firebase Dynamic Links 초기화
  runApp(MyApp());
}
```

2. 사용자가 원하는 위치에서 Firebase Dynamic Links를 생성하고 공유합니다.
```dart
import 'package:firebase_dynamic_links/firebase_dynamic_links.dart';

final DynamicLinkParameters parameters = DynamicLinkParameters(
  uriPrefix: 'https://your_dynamic_link_domain.page.link',
  link: Uri.parse('your_deep_link'),
  androidParameters: AndroidParameters(
    packageName: 'your_android_package_name',
  ),
  iosParameters: IosParameters(
    bundleId: 'your_ios_bundle_id',
  ),
);

final ShortDynamicLink dynamicUrl = await parameters.buildShortLink();
final Uri shortUrl = dynamicUrl.shortUrl;
```

Firebase Dynamic Links를 생성할 때 `uriPrefix`는 Firebase 콘솔에서 자체 도메인을 설정한 후 얻을 수 있습니다. `link`는 사용자가 원하는 딥링크 주소를 입력하면 됩니다. `androidParameters`와 `iosParameters`는 각 플랫폼에 대한 설정입니다.

## 결론

이제 Flutter 앱에서 Firebase Dynamic Links를 구현하는 방법을 알아보았습니다. Firebase Dynamic Links는 앱 내에서 링크를 통해 사용자의 경험을 개선할 수 있는 강력한 기능입니다. Firebase 콘솔에서 링크의 동작을 설정하고 Flutter 앱에서 Firebase Dynamic Links를 초기화하여 사용자에게 맞춤형 링크를 제공할 수 있습니다.