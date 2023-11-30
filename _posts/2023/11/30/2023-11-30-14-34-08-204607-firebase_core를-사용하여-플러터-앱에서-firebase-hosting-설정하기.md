---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Hosting 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들이 앱을 더욱 효과적으로 개발할 수 있도록 도와주는 클라우드 기반 플랫폼입니다. Firebase_core는 Firebase 서비스를 사용하기 위한 핵심 패키지로, 플러터 앱에서 Firebase를 설정하고 사용할 수 있게 해줍니다. 이번 글에서는 Firebase_core를 사용하여 플러터 앱을 Firebase Hosting에 배포하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 생성

먼저, Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 "프로젝트 만들기"를 클릭합니다. 프로젝트 이름을 입력하고 원하는 설정을 선택한 뒤 "프로젝트 만들기"를 클릭합니다.

## Firebase 프로젝트 설정

1. Firebase 프로젝트를 생성하면, Firebase 콘솔 대시보드로 이동합니다.
2. "플랫폼 추가"를 클릭하여 플랫폼을 선택합니다. 여기서는 "웹"을 선택합니다.
3. "앱에 Firebase 추가" 단계에서 Firebase SDK 구성 파일을 다운로드합니다.
4. Firebase SDK 구성 파일의 내용을 `web/index.html` 파일에 붙여넣습니다.

## Firebase_core 패키지 추가

Firebase_core 패키지를 사용하여 Firebase 서비스를 플러터 앱에 추가해보겠습니다.

1. `pubspec.yaml` 파일에 아래의 의존성을 추가합니다.

```dart
dependencies:
  firebase_core: ^1.6.0
```

2. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

## Firebase 초기화

Firebase_core 패키지를 사용하여 Firebase를 초기화하고 사용할 준비를 해야합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Firebase.initializeApp();
  
  // Firebase 관련 작업 수행
  
  runApp(MyApp());
}
```

Firebase.initializeApp() 메서드를 호출하여 Firebase를 초기화합니다. await 키워드를 사용하여 비동기적으로 초기화가 완료될 때까지 기다립니다.

## Firebase Hosting 배포

Firebase Hosting에 플러터 앱을 배포하는 방법은 다음과 같습니다.

1. 터미널에서 `flutter build web` 명령어를 실행하여 웹 버전 앱을 빌드합니다.
2. Firebase 프로젝트 디렉토리에서 `firebase login` 명령어를 실행하여 Google 계정으로 로그인합니다.
3. `firebase init` 명령어를 실행하여 Firebase 프로젝트를 초기화합니다. 배포할 앱을 선택한 뒤, Firebase Hosting을 선택합니다.
4. Firebase 백엔드에 플러터 앱을 배포합니다.

## 마무리

이제 Firebase_core를 사용하여 플러터 앱을 Firebase Hosting에 배포할 수 있게 되었습니다. Firebase Hosting은 앱을 빠르고 안정적으로 전 세계적으로 제공할 수 있는 강력한 도구입니다. Firebase를 사용하여 사용자들에게 최고의 앱 경험을 제공해보세요.

더 많은 정보를 원하시면 Firebase 공식 문서를 확인해보십시오: [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup)

## 참고 자료

- [Firebase 콘솔](https://console.firebase.google.com/)
- [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup)
- [Firebase Core 패키지](https://pub.dev/packages/firebase_core)