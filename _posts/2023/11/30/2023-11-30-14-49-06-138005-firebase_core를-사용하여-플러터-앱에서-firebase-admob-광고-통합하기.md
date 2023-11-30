---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase AdMob 광고 통합하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google의 클라우드 기반 플랫폼으로, 앱 개발자들이 앱을 더 효과적으로 개발하고 운영하는 데 도움을 줍니다. 그 중 Firebase AdMob은 앱에 광고를 통합할 수 있는 기능을 제공합니다. 이번 글에서는 Flutter 앱에서 Firebase_core를 사용하여 Firebase AdMob 광고를 통합하는 방법을 알아보겠습니다.

## Firebase_core 패키지 추가하기

Firebase_core 패키지는 Firebase 서비스를 초기화하는 데 필요한 기능을 제공합니다. 먼저 `pubspec.yaml` 파일에 아래의 의존성을 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.4
```

의존성 추가 후, 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드 합니다.

## Firebase 프로젝트 설정하기

Firebase Console에서 새로운 프로젝트를 생성한 후, Firebase 콘솔의 프로젝트 설정에서 Android 앱을 추가합니다. 패키지 이름, SHA-1 인증서 지문 등의 정보를 입력합니다.
Firebase에서 제공하는 구성 파일(`google-services.json`)을 다운로드한 후, `android/app` 디렉토리에 복사합니다.

## Firebase AdMob 설정하기

Firebase Console에서 AdMob으로 이동하여 앱을 추가합니다. 앱 ID를 생성하고, 애드 유닛을 만듭니다. 이렇게 생성한 앱 ID와 애드 유닛 ID는 나중에 앱에서 사용됩니다.

## Firebase_core 초기화하기

Flutter 앱의 진입점에 Firebase_core를 초기화하는 코드를 작성해야 합니다. 이를 위해 `main.dart` 파일의 `main()` 함수에 아래 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase.initializeApp() 메소드를 호출하여 Firebase_core를 초기화합니다.

## Firebase AdMob 통합하기

Firebase AdMob을 통합하기 위해 다음 단계를 진행해야 합니다.

1. `pubspec.yaml` 파일에 `firebase_admob` 패키지를 추가합니다.
2. AdMob 애드 유닛 ID를 사용하여 앱에 광고 위젯을 추가합니다.

```yaml
dependencies:
  firebase_admob: ^0.11.0+1
```

`pubspec.yaml` 파일의 dependencies에 위의 의존성을 추가한 후, 터미널에서 다시 `flutter pub get` 명령어를 실행하여 패키지를 다운로드 합니다.

```dart
import 'package:firebase_admob/firebase_admob.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    FirebaseAdMob.instance.initialize(appId: 'YOUR_ADMOB_APP_ID');
    return MaterialApp(
      // ...
    );
  }
}
```

`MyApp` 위젯의 `build` 메소드 내에서 `FirebaseAdMob.instance.initialize()`를 호출하여 AdMob을 초기화합니다. `YOUR_ADMOB_APP_ID` 부분에는 생성한 앱 ID를 입력해야 합니다.

```dart
import 'package:firebase_admob/firebase_admob.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Welcome to my app!'),
            SizedBox(height: 20),
            AdWidget(ad: bannerAd),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                InterstitialAd interstitialAd = InterstitialAd(
                  adUnitId: 'YOUR_ADMOB_AD_UNIT_ID',
                  listener: (MobileAdEvent event) {
                    print('InterstitialAd event: $event');
                  },
                );
                interstitialAd.load();
                interstitialAd.show();
              },
              child: Text('Show Interstitial Ad'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위의 코드에서 `AdWidget` 위젯은 광고를 표시하기 위한 위젯입니다. `YOUR_ADMOB_AD_UNIT_ID` 부분에는 생성한 애드 유닛 ID를 입력해야 합니다.

## 결론

이제 Firebase_core를 사용하여 Flutter 앱에 Firebase AdMob 광고를 통합하는 방법을 알아보았습니다. Firebase_core의 초기화와 Firebase AdMob의 통합 단계를 따라하면 앱에 광고를 쉽게 추가할 수 있습니다. Firebase의 다양한 서비스를 활용하여 앱의 기능을 확장해 보세요!

---

참고문서:
- Firebase 공식 문서: https://firebase.google.com/docs/flutter/setup?hl=ko
- Firebase_admob 패키지: https://pub.dev/packages/firebase_admob