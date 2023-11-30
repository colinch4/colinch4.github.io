---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Hosting 배포하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 클라우드 기반의 백엔드 서비스로, 데이터베이스, 인증, 스토리지, 호스팅 등 다양한 기능을 제공합니다. Firebase를 사용하여 플러터 앱을 개발한 뒤, Firebase Hosting을 통해 앱을 배포하고 싶다면 firebase_core를 사용해야 합니다.

## 1. Firebase 프로젝트 생성하기

Firebase Hosting을 사용하기 위해서는 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성하세요. 프로젝트 이름을 입력한 후, Firebase 앱을 추가합니다.

## 2. Firebase_core 패키지 추가하기

Firebase_core 패키지는 Firebase 서비스를 초기화하는 데 필요한 코드를 제공합니다. pubspec.yaml 파일에 firebase_core 패키지를 추가해주세요.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.3.0
```

패키지를 추가한 뒤, `flutter pub get` 명령어를 실행하여 패키지를 다운로드합니다.

## 3. Firebase 앱 초기화하기

Firebase 앱을 초기화하기 위해 main.dart 파일을 열고 다음과 같이 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase.initializeApp() 메서드를 사용하여 Firebase 앱을 초기화합니다. 이때 앱에 필요한 인증 정보는 Firebase 콘솔에서 제공하는 google-services.json 파일을 프로젝트의 android/app 폴더에 추가해야 합니다.

## 4. Firebase Hosting 설정하기

Firebase 콘솔에서 Hosting으로 이동하여 원하는 도메인을 설정합니다. 도메인을 설정한 후, Firebase CLI를 사용하여 배포를 진행합니다.

Firebase CLI를 설치하려면 다음 명령어를 터미널에 입력하세요.

```bash
npm install -g firebase-tools
```

프로젝트 폴더에서 다음 명령어를 실행하여 Firebase CLI에 로그인합니다.

```bash
firebase login
```

로그인이 완료되면 다음 명령어를 실행하여 Firebase 프로젝트와 연결합니다.

```bash
firebase init
```

Firebase 초기화 명령어를 실행하면 설정할 사항들을 선택할 수 있는 메뉴가 나타납니다. Hosting에 체크하고, Public Directory를 "build"로 설정하세요.

마지막으로 다음 명령어를 실행하여 앱을 배포합니다.

```bash
firebase deploy
```

Firebase Hosting에 정상적으로 배포되면, 앱의 도메인으로 접속하여 앱을 확인할 수 있습니다.

이제 Firebase_core를 사용하여 플러터 앱을 개발하고, Firebase Hosting을 통해 앱을 배포할 수 있습니다. Firebase를 사용하면 플러터 앱의 백엔드 구축 및 호스팅이 간단하고 효율적으로 이루어집니다.