---
layout: post
title: "[flutter] 플러터(Flutter) 앱에서 Firebase Crashlytics를 사용하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들에게 앱 개발 및 운영에 필요한 다양한 기능을 제공하는 플랫폼입니다. Firebase Crashlytics는 앱의 충돌 정보를 실시간으로 수집하고 분석하여 개발자에게 앱의 크래시 로그와 전반적인 성능 상태에 대한 통찰력을 제공해줍니다. 플러터(Flutter) 앱에서 Firebase Crashlytics를 사용하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성하고, 해당 프로젝트에 앱을 추가합니다.

2. Flutter 프로젝트의 `pubspec.yaml` 파일에 `firebase_crashlytics` 패키지를 추가합니다. 패키지를 추가한 후 `flutter packages get` 명령어를 실행하여 패키지를 다운로드합니다.

3. Firebase 콘솔에서 앱 설정 페이지로 들어가서 'GoogleService-Info.plist' 파일(iOS) 또는 'google-services.json' 파일(Android)을 다운로드합니다. 이 파일은 Firebase Crashlytics와 앱을 연결하는 데 필요합니다. 파일을 프로젝트 디렉토리에 추가합니다.

4.  Firebase 콘솔에서 '프로젝트 설정' 페이지로 이동하여 'Crashlytics'를 활성화합니다.

## iOS 설정

1. 터미널에서 Flutter 프로젝트 디렉토리로 이동한 뒤, 다음 명령어를 실행하여 Firebase Crashlytics에 앱을 연결합니다.

   ```
   flutter firebase configure
   ```

2. iOS 디렉토리로 이동한 뒤, `Runner.xcworkspace` 파일을 엽니다.

3. Firebase 콘솔에서 다운로드 받은 'GoogleService-Info.plist' 파일을 Xcode 프로젝트에 추가합니다. 

4. 'AppDelegate.swift' 파일을 열고 `import Firebase`와 `import FirebaseCrashlytics`를 추가합니다.

5. `didFinishLaunchingWithOptions` 메서드에 다음 코드를 추가합니다.

   ```swift
   FirebaseApp.configure()
   Crashlytics.crashlytics().setCrashlyticsCollectionEnabled(true)
   ```

6. `applicationDidFinishLaunching` 메서드에 다음 코드를 추가합니다.

   ```swift
   Fabric.with([Crashlytics.crashlytics()])
   ```

7. 앱을 빌드하고 실행합니다. 앱이 충돌하면 Firebase Crashlytics에 충돌 정보가 전송되어야 합니다.

## Android 설정

1. 터미널에서 Flutter 프로젝트 디렉토리로 이동한 뒤, 다음 명령어를 실행하여 Firebase Crashlytics에 앱을 연결합니다.

   ```
   flutter firebase configure
   ```

2. Android Studio에서 Flutter 프로젝트를 엽니다.

3. Firebase 콘솔에서 다운로드 받은 'google-services.json' 파일을 `android/app` 디렉토리에 추가합니다.

4. `android/build.gradle` 파일을 열고 `dependencies` 블록에 다음 코드를 추가합니다.

   ```groovy
   // Firebase Crashlytics
   classpath 'com.google.firebase:firebase-crashlytics-gradle:2.7.1'
   ```

5. `android/app/build.gradle` 파일을 열고 맨 아래에 다음 코드를 추가합니다.

   ```groovy
   apply plugin: 'com.google.firebase.crashlytics'
   ```

6. 앱을 빌드하고 실행합니다. 앱이 충돌하면 Firebase Crashlytics에 충돌 정보가 전송되어야 합니다.

## Firebase Crashlytics 테스트

Firebase Crashlytics를 테스트하기 위해 앱에 명시적으로 크래시를 발생시켜봅시다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() {
  runZonedGuarded(() {
    runApp(MyApp());
  }, (error, stackTrace) {
    FirebaseCrashlytics.instance.recordError(error, stackTrace);
  });
}
```

위 코드는 앱의 `main()` 함수에 `runZonedGuarded`를 사용하여 앱이 충돌하면 Firebase Crashlytics에 오류를 기록하도록 설정합니다.

위와 같이 설정하고 앱을 실행하면 크래시가 발생할 때마다 Firebase Crashlytics에 오류가 기록됩니다.

## 결론

이제 플러터(Flutter) 앱에서 Firebase Crashlytics를 사용하는 방법에 대해 알아보았습니다. Firebase Crashlytics를 사용하면 앱의 크래시 정보를 실시간으로 수집하여 앱의 안정성을 향상시킬 수 있습니다. Firebase 콘솔을 통해 앱의 성능과 크래시 로그를 실시간으로 모니터링할 수 있으니, 앱의 개발과 운영에 활용해 보시기 바랍니다.

## 참고자료

- [Firebase Documentation](https://firebase.google.com/docs/crashlytics)
- [Flutter Firebase Crashlytics GitHub](https://github.com/FirebaseExtended/flutterfire/blob/master/packages/firebase_crashlytics/firebase_crashlytics/lib/firebase_crashlytics.dart)