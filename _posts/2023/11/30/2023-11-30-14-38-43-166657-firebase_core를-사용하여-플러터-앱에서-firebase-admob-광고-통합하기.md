---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase AdMob 광고 통합하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

안녕하세요! 이번에는 Firebase Core를 사용하여 플러터 앱에서 Firebase AdMob 광고를 통합하는 방법에 대해 알아보겠습니다. 

## Firebase Core 설정하기

Firebase를 사용하기 위해선 먼저 Firebase Core를 설정해야 합니다. Firebase Core는 Firebase의 기본적인 기능을 사용할 수 있도록 해주는 라이브러리입니다. 

1. `pubspec.yaml` 파일을 열고 `firebase_core` 패키지를 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
```

2. 터미널에서 `flutter pub get` 명령어를 실행해 패키지를 다운로드합니다.

3. Firebase 프로젝트를 생성하고 `google-services.json` 파일을 다운로드합니다. 

4. 다운로드한 `google-services.json` 파일을 프로젝트의 `android/app` 폴더에 추가합니다.

5. `main.dart` 파일을 열고 다음 코드를 추가하여 Firebase Core를 초기화합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase Core 설정이 완료되었습니다!

## Firebase AdMob 통합하기

이제 Firebase Core를 사용하여 Firebase AdMob 광고를 통합해보겠습니다.

1. `pubspec.yaml` 파일을 열고 `firebase_admob` 패키지를 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_admob: ^0.11.0+1
```

2. 터미널에서 `flutter pub get` 명령어를 실행해 패키지를 다운로드합니다.

3. Firebase AdMob를 초기화하기 위해 `AndroidManifest.xml` 파일을 열고 다음 코드를 추가합니다.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.myapp">

    <application
        <!-- ... -->
        <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="YOUR_ADMOB_APP_ID"/>
        <!-- ... -->
```

위 코드에서 `YOUR_ADMOB_APP_ID` 부분에 본인의 AdMob 앱 ID를 입력합니다. AdMob 앱 ID는 AdMob 계정을 생성하고 앱을 등록한 후에 얻을 수 있습니다.

4. 이제 앱에서 광고를 표시할 위젯의 코드를 수정합니다. 예를 들어, `MyApp` 위젯에 광고를 추가하려면 다음과 같이 코드를 수정할 수 있습니다.

```dart
import 'package:firebase_admob/firebase_admob.dart';

class MyApp extends StatelessWidget {
  // ...

  @override
  Widget build(BuildContext context) {
    // ...
    return MaterialApp(
      // ...
      home: Scaffold(
        // ...
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                '플러터 앱',
              ),
              SizedBox(height: 20),
              AdWidget(ad: BannerAd(
                adUnitId: BannerAd.testAdUnitId, // 테스트용 광고 ID
                size: AdSize.banner,
              )),
            ],
          ),
        ),
      ),
    );
  }
}
```

위 코드에서 `BannerAd.testAdUnitId`는 테스트 광고를 보여주는 광고 ID이므로 앱을 배포하기 전에 본인의 AdUnit ID로 바꿔야 합니다.

Firebase AdMob 광고 통합이 완료되었습니다!

이제 Firebase Core를 사용하여 플러터 앱에서 Firebase AdMob 광고를 통합하는 방법에 대해 알아보았습니다. Firebase Core를 설정한 후에 Firebase AdMob 패키지를 추가하여 원하는 광고 형식을 앱에 통합할 수 있습니다. 자세한 내용은 [Firebase AdMob 문서](https://firebase.google.com/docs/admob)를 참고하시기 바랍니다.

Happy coding!