---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Dynamic Links 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Dynamic Links는 앱과 웹 사이의 외부 링크를 생성하고 관리하는 데 사용되는 Firebase 서비스입니다. 이 기능을 사용하면 사용자가 특정 링크를 클릭할 때, 앱이 설치되어 있지 않은 경우 구글 플레이 스토어 또는 앱 스토어로 이동하여 앱을 다운로드 할 수 있습니다. 이미 앱이 설치되어 있는 경우에는 해당 링크를 사용하여 앱 내의 특정 화면으로 이동할 수 있습니다.

이번 포스트에서는 Flutter 앱에서 Firebase Dynamic Links를 구현하는 방법을 알아보겠습니다. Firebase Core를 설정하고, Dynamic Links의 생성 및 수신 처리하는 방법에 대해 설명하겠습니다.

## Firebase Core 설정하기

먼저, Firebase Core를 설정해야 합니다. Firebase Core는 Firebase를 사용하기 위해 필요한 기본적인 구성요소입니다. 

1. **pubspec.yaml** 파일에서 firebase_core 패키지를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
```

2. 터미널에서 아래 명령어를 실행하여 변경 사항을 적용합니다.

```bash
flutter pub get
```

3. Firebase Core를 초기화하는 코드를 작성합니다. main() 함수가 있는 **lib/main.dart** 파일을 열고 아래 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  // 앱 시작
  runApp(MyApp());
}
```

Firebase Core는 이제 성공적으로 구성되었습니다.

## Firebase Dynamic Link 생성하기

이제 Firebase Dynamic Link를 생성하는 방법을 알아보겠습니다. 아래 예제 코드를 참고하여 사용자 정의 링크를 생성할 수 있습니다.

```dart
import 'package:firebase_dynamic_links/firebase_dynamic_links.dart';

class DynamicLinkService {
  final FirebaseDynamicLinks _firebaseDynamicLinks = FirebaseDynamicLinks.instance;

  Future<Uri> createDynamicLink() async {
    final DynamicLinkParameters parameters = DynamicLinkParameters(
      uriPrefix: 'https://example.page.link',
      link: Uri.parse('https://www.example.com/'),
      androidParameters: AndroidParameters(
        packageName: 'com.example.app',
      ),
      iosParameters: IosParameters(
        bundleId: 'com.example.app',
      ),
    );

    final ShortDynamicLink shortDynamicLink =
        await parameters.buildShortLink();
    final Uri shortUrl = shortDynamicLink.shortUrl;
    return shortUrl;
  }
}
```

위의 코드에서 `uriPrefix`는 도메인 이름이어야 합니다. Firebase 콘솔에서 프로젝트를 만든 후, [Dynamic Links] 섹션에서 도메인 이름을 구성하고 복사하여 입력해야 합니다.

## Firebase Dynamic Link 수신 처리하기

이제 Firebase Dynamic Link를 수신하는 방법을 알아보겠습니다. 이 기능을 사용하려면 앱이 시작될 때 Firebase Dynamic Link를 처리하는 코드를 작성해야 합니다. 다음은 예제 코드입니다.

```dart
import 'package:firebase_dynamic_links/firebase_dynamic_links.dart';

class DynamicLinkHandler {
  Future handleDynamicLinks() async {
    final PendingDynamicLinkData? data =
        await FirebaseDynamicLinks.instance.getInitialLink();

    final Uri? deepLink = data?.link;

    if (deepLink != null) {
      // Deep link 처리
      // deepLink를 사용하여 앱 내의 특정 화면으로 이동하거나 해당 링크에 대한 추가 동작을 수행합니다.
    }

    FirebaseDynamicLinks.instance.onLink(
        onSuccess: (PendingDynamicLinkData? dynamicLink) async {
      final Uri? deepLink = dynamicLink?.link;

      if (deepLink != null) {
        // Deep link 처리
        // deepLink를 사용하여 앱 내의 특정 화면으로 이동하거나 해당 링크에 대한 추가 동작을 수행합니다.
      }
    }, onError: (OnLinkErrorException e) async {
      print('Dynamic Link Failed: ${e.message}');
    });
  }
}
```

앱이 시작될 때마다 위의 `handleDynamicLinks` 함수를 호출하여 Firebase Dynamic Links를 처리합니다.

## 결론

이번 포스트에서는 Flutter 앱에서 Firebase Core를 설정하고 Firebase Dynamic Links를 생성하고 수신 처리하는 방법에 대해 알아보았습니다. Firebase Dynamic Links를 사용하여 앱과 웹 사이의 외부 링크를 관리할 수 있으며, 사용자 경험을 향상시킬 수 있습니다.

Firebase Dynamic Links의 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/dynamic-links)를 참조하세요.