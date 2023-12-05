---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 실시간 오류 추적 및 버그 수정하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 Firebase를 통해 제공되는 실시간 오류 추적 도구입니다. 이 도구를 사용하면 플러터(Flutter) 앱에서 발생하는 오류를 실시간으로 모니터링하고, 해당 오류의 원인을 분석하여 버그를 수정할 수 있습니다. 이번 블로그 포스트에서는 Firebase Crashlytics를 사용하여 플러터 앱의 오류를 추적하고 수정하는 방법에 대해 다루겠습니다.

## 1. Firebase Crashlytics 설정하기

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성합니다.
2. 프로젝트 설정 페이지에서 "Crashlytics" 탭을 선택하고, "시작하기"를 클릭합니다.
3. "Firebase SDK 추가" 화면에서 "안드로이드 앱 추가" 버튼을 클릭합니다.
4. 패키지 이름과 앱 닉네임을 입력한 후 "앱 추가하기" 버튼을 클릭합니다.
5. 다음으로 "google-services.json" 파일을 다운로드하여 프로젝트의 "android/app" 폴더에 추가합니다.
6. "android/build.gradle" 파일에서 "firebase-crashlytics" 플러그인을 추가합니다:

```groovy
dependencies {
    // ...
    classpath 'com.google.firebase:firebase-crashlytics-gradle:2.7.0'
    // ...
}
```

7. "android/app/build.gradle" 파일에서 다음과 같이 "apply plugin"에 "com.google.firebase.crashlytics"를 추가합니다:

```groovy
apply plugin: 'com.google.firebase.crashlytics'
```

8. 이제 Crashlytics가 설정되었습니다. 앱을 실행하고 오류를 발생시켜서 Firebase 콘솔에서 확인할 수 있습니다.

## 2. 플러터 앱과 Firebase Crashlytics 연동하기

1. flutterfire 패키지를 사용하여 Firebase Crashlytics를 앱에 연동합니다:

```dart
dependencies:
  firebase_core: ^1.1.1
  firebase_crashlytics: ^2.1.4
```

2. `main.dart` 파일에서 Firebase Crashlytics를 초기화합니다:

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  runApp(MyApp());
}
```

3. 앱에서 오류를 발생시키는 곳에 다음과 같이 Crashlytics를 사용하여 오류를 보고합니다:

```dart
try {
  // 오류가 발생할 수 있는 코드
} catch (error, stackTrace) {
  FirebaseCrashlytics.instance.recordError(error, stackTrace);
}
```

위의 코드에서는 try-catch 문을 사용하여 어떤 부분에서 오류가 발생할 수 있는지 확인하고, 발생한 오류를 Firebase Crashlytics에 보고합니다.

## 3. Firebase 콘솔에서 오류 추적하기

1. Firebase 콘솔에서 프로젝트를 엽니다.
2. "Crashlytics" 탭에서 실시간으로 오류를 모니터링하고, 오류에 대한 자세한 정보를 확인할 수 있습니다.
3. 해당 오류의 상세 정보를 확인하여 원인을 분석하고, 버그를 수정할 수 있습니다.

Crashlytics를 사용하면 플러터 앱의 오류를 실시간으로 추적하여 오류가 발생하는 부분을 파악하고, 더 나은 앱 품질을 제공할 수 있습니다.

참고 자료:
- [플러터(Flutter) 공식 문서](https://flutter.dev/docs)
- [Firebase Crashlytics 공식 문서](https://firebase.google.com/docs/crashlytics?platform=flutter)