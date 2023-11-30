---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Hosting 배포하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google이 제공하는 서비스로, 앱의 백엔드 인프라스트럭처를 구축하고 관리하는 데 도움을 줍니다. Firebase를 사용하여 앱을 개발하면 데이터베이스, 인증, 애널리틱스, 클라우드 메시징 등의 기능을 쉽게 구현할 수 있습니다. 

Firebase Hosting은 Firebase의 한 서비스로, 정적 웹 페이지를 호스팅하는 데 사용됩니다. Flutter 앱을 개발하고 Firebase를 사용하여 호스팅하려면 다음 단계를 따르세요.

## Firebase 프로젝트 설정

1. [Firebase 콘솔](https://console.firebase.google.com/)에 로그인하고, 새 프로젝트를 생성합니다.
2. 프로젝트의 이름을 입력하고, 동의하고 계속 버튼을 클릭합니다.
3. Firebase 콘솔에 프로젝트가 생성되면, 앱을 추가해야 합니다. Flutter 앱을 추가하려면 "Android"와 "iOS"를 클릭하고, 각 플랫폼에 대한 정보를 입력하세요.

## Firebase Flutter 패키지 추가

1. 개발하고 있는 플러터 앱의 `pubspec.yaml` 파일을 엽니다.
2. `dependencies` 부분에 아래 코드를 추가합니다.

```dart
dependencies:
  firebase_core: ^1.0.2
```

3. 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드합니다.

## Firebase 초기화

1. `main.dart` 파일에서 Firebase를 초기화하기 위해 `Firebase.initializeApp()` 메서드를 호출합니다. 이 메서드를 호출할 위치는 중요하지 않으며, 일반적으로 `void main()` 함수나 `runApp()` 함수 전에 호출합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## Firebase Hosting 구성 파일 생성

1. 앱 루트 디렉토리에 `firebase.json` 파일을 생성합니다.
2. 아래 코드를 `firebase.json` 파일에 추가합니다.

```json
{
  "hosting": {
    "public": "build/web",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

## 앱 빌드 및 배포

1. 터미널에서 아래 명령을 실행하여 앱을 빌드합니다.

```bash
flutter build web
```

2. 빌드가 완료되면, Firebase에 앱을 배포합니다.

```bash
firebase init
firebase deploy --only hosting
```

Firebase 콘솔에서 호스팅 URL을 확인할 수 있으며, 이 URL을 통해 앱에 접속할 수 있습니다.

이제 플러터 앱을 Firebase Hosting으로 배포할 수 있는 방법을 알게 되었습니다. Firebase를 사용하여 앱을 보다 강력하게 만들고 사용자들에게 앱을 보여줄 수 있습니다. 참고로, Firebase Hosting은 정적 웹 페이지를 호스팅하므로, 웹 기능을 추가해야 하는 경우에만 사용하는 것이 좋습니다.

더 많은 Firebase 기능을 알아보려면, [Firebase 문서](https://firebase.google.com/docs)를 참고하세요.