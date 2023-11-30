---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase AdMob 광고 통합하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 모바일 및 웹 앱 개발 플랫폼으로, Firebase AdMob은 Firebase의 하나의 기능으로서 앱에 광고를 통합할 수 있는 기능을 제공합니다. 플러터(Flutter) 앱에서 Firebase AdMob 광고를 통합하기 위해서는 Firebase Core를 사용하여 Firebase SDK를 프로젝트에 추가해야 합니다.

이번 블로그 포스트에서는 Firebase Core를 사용하여 플러터 앱에서 Firebase AdMob 광고를 통합하는 방법을 알아보겠습니다.

## 목차
- [Firebase 프로젝트 만들기](#firebase-프로젝트-만들기)
- [Flutter 프로젝트에 Firebase Core 추가하기](#flutter-프로젝트에-firebase-core-추가하기)
- [Firebase AdMob 패키지 추가하기](#firebase-admob-패키지-추가하기)
- [Android 앱에 AdMob 광고 단위 추가하기](#android-앱에-admob-광고-단위-추가하기)
- [iOS 앱에 AdMob 광고 단위 추가하기](#ios-앱에-admob-광고-단위-추가하기)
- [플러터 앱에서 AdMob 광고 사용하기](#플러터-앱에서-admob-광고-사용하기)

## Firebase 프로젝트 만들기
Firebase Console(https://console.firebase.google.com/)에 접속하여 새로운 프로젝트를 생성합니다. 프로젝트 이름을 지정하고, 원하는 앱 플랫폼(Android 또는 iOS)을 선택한 후에는 Firebase 프로젝트가 생성됩니다.

## Flutter 프로젝트에 Firebase Core 추가하기
플러터 앱 프로젝트에 Firebase Core를 추가하기 위해서는 `firebase_core` 패키지를 프로젝트에 추가해야 합니다. 프로젝트의 `pubspec.yaml` 파일에서 `dependencies` 섹션에 아래와 같이 `firebase_core` 패키지를 추가해주세요.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

프로젝트 폴더에서 터미널을 실행하고 `flutter pub get` 명령을 입력하여 패키지를 다운로드 받습니다. 이제 Firebase Core를 플러터 앱에 추가할 준비가 완료되었습니다.

## Firebase AdMob 패키지 추가하기
Firebase AdMob을 사용하기 위해서는 `firebase_admob` 패키지를 플러터 앱 프로젝트에 추가해야 합니다. `pubspec.yaml` 파일의 `dependencies` 섹션에 아래와 같이 `firebase_admob` 패키지를 추가해주세요.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
  firebase_admob: ^0.11.2+1
```

패키지 다운로드를 위해 터미널에서 `flutter pub get` 명령을 실행합니다.

## Android 앱에 AdMob 광고 단위 추가하기
Firebase Console로 돌아가서 Firebase 프로젝트의 "광고" 섹션으로 이동합니다. "앱을 추가" 버튼을 클릭하고, Android 패키지 이름을 입력한 후에는 AdMob 광고 단위가 생성됩니다. 생성된 광고 단위의 ID를 메모해두세요.

Flutter 앱의 `AndroidManifest.xml` 파일을 열고 `<application>` 태그 안에 아래의 코드를 추가합니다.

```xml
<meta-data
  android:name="com.google.android.gms.ads.APPLICATION_ID"
  android:value="YOUR_ADMOB_APP_ID"/>
```

위의 `value` 속성에는 메모해둔 AdMob 앱 ID를 입력해야 합니다.

## iOS 앱에 AdMob 광고 단위 추가하기
Firebase Console에서 "앱을 추가" 버튼을 클릭하고, iOS 번들 식별자를 입력한 후에는 AdMob 광고 단위가 생성됩니다. 생성된 광고 단위의 ID를 메모해두세요.

Flutter 앱의 `AppDelegate.swift` 파일을 열고 `didFinishLaunchingWithOptions` 함수 내에 아래의 코드를 추가합니다.

```swift
import Firebase
import GoogleMobileAds

...

GADMobileAds.sharedInstance().start(completionHandler: nil)
FirebaseApp.configure()
```

위의 코드를 추가하기 위해 `import Firebase`와 `import GoogleMobileAds` 문을 추가해야 합니다.

## 플러터 앱에서 AdMob 광고 사용하기
이제 Firebase Core와 Firebase AdMob을 통합하기 위해 필요한 작업들을 마쳤습니다. 플러터 앱의 코드에서 AdMob 광고를 사용할 준비가 되었습니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_admob/firebase_admob.dart';

...

await Firebase.initializeApp();
MobileAds.instance.initialize();

...

BannerAd myBanner = BannerAd(
  adUnitId: '<YOUR_ADMOB_BANNER_AD_UNIT_ID>',
  size: AdSize.banner,
  targetingInfo: MobileAdTargetingInfo(),
  listener: (MobileAdEvent event) {
    print("BannerAd event is $event");
  },
);
myBanner..load()..show();
```

위의 코드에서 `<YOUR_ADMOB_BANNER_AD_UNIT_ID>` 부분을 이전에 메모해둔 AdMob 광고 단위 ID로 대체해주세요. 이제 실행해보면 플러터 앱에서 AdMob 광고를 정상적으로 사용할 수 있습니다.

이제 Firebase Core를 사용하여 플러터 앱에서 Firebase AdMob 광고를 통합하는 방법에 대해 알아보았습니다. Firebase와 AdMob의 강력한 기능을 활용하여 광고 수익을 올려보세요!

## 참고 자료
- Firebase: https://firebase.google.com/
- Flutter: https://flutter.dev/
- Firebase AdMob: https://firebase.google.com/docs/admob
- Flutter packages - firebase_core: https://pub.dev/packages/firebase_core
- Flutter packages - firebase_admob: https://pub.dev/packages/firebase_admob