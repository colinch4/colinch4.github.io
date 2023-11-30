---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Hosting 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 클라우드 기반의 플랫폼으로, 다양한 기능을 제공하여 개발자들이 앱을 보다 쉽게 구축하고 관리할 수 있게 해줍니다. Firebase Hosting은 Firebase의 한 기능으로, 정적인 웹 콘텐츠를 호스팅할 수 있는 서비스입니다. 이번 포스트에서는 플러터 앱에서 Firebase Hosting을 설정하는 방법에 대해 알아보겠습니다.

## 필요한 사전 작업

Firebase Hosting을 사용하기 위해 다음 사전 작업이 필요합니다:

1. Firebase 프로젝트 생성: [Firebase 콘솔](https://console.firebase.google.com/)에서 새 프로젝트를 생성합니다.
2. Flutter 프로젝트 설정: Firebase 프로젝트와 연동할 Flutter 프로젝트를 생성합니다.
3. FlutterFire 설치: `firebase_core` 플러그인을 추가하여 Flutter 앱에서 Firebase를 초기화 할 수 있게 합니다.

## Firebase 프로젝트와 Flutter 앱 연동

Firebase 프로젝트와 Flutter 앱을 연동하는 방법은 다음과 같습니다:

1. Firebase 프로젝트의 `google-services.json` 파일을 다운로드합니다.
2. Flutter 프로젝트의 `android/app` 디렉토리에 `google-services.json` 파일을 복사합니다.
3. `pubspec.yaml` 파일에서 `firebase_core` 플러그인을 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
```

4. Flutter 앱의 `main.dart` 파일에서 Firebase를 초기화합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## Firebase Hosting 세팅

Firebase 프로젝트와 Flutter 앱이 성공적으로 연동되면, Firebase Hosting을 설정할 수 있습니다.

1. Firebase 콘솔에서 Hosting 탭으로 이동합니다.
2. Firebase Hosting 시작하기를 선택합니다.
3. 사용 가능한 도메인을 선택하고, 앱의 웹 콘텐츠를 업로드하기 위한 디렉토리 경로를 설정합니다.
4. Firebase CLI를 설치한 뒤, 터미널에서 다음 명령어를 실행하여 Firebase Hosting을 배포합니다.

```bash
$ firebase deploy --only hosting
```

5. 배포가 완료되면, 제공된 웹 호스팅 URL을 통해 앱에 접속할 수 있습니다.

Firebase Hosting을 사용하여 플러터 앱을 호스팅하려면 위의 단계를 따르면 됩니다. Firebase는 강력한 호스팅 서비스이며, 앱의 정적인 콘텐츠를 쉽게 배포하고 관리할 수 있게 도와줍니다. 추가적인 세부 설정은 Firebase 콘솔에서 수행할 수 있으며, Firebase 문서에서 자세한 내용을 확인할 수 있습니다.

참고: [Firebase 공식 문서](https://firebase.google.com/docs/hosting)