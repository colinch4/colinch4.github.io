---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Hosting 배포하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 클라우드 기반 개발 플랫폼으로, 다양한 기능을 제공합니다. 그 중 Firebase Hosting은 정적 웹사이트를 호스팅하고 배포하는 서비스입니다. Flutter 앱에서 Firebase Hosting을 사용하여 앱을 배포하려면 `firebase_core` 패키지를 사용해야 합니다.

## 1. Firebase 프로젝트 설정

Firebase Hosting을 사용하기 위해 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔에 접속하여 새 프로젝트를 만들고, Firebase SDK 설정을 진행합니다.

Firebase SDK 설정 중 `firebase_core`를 추가해야 합니다. `pubspec.yaml` 파일에 다음 코드를 추가하세요.

```yaml
dependencies:
  flutter:
    sdk: flutter

  firebase_core: ^1.0.2
```

## 2. Firebase 앱 초기화

Firebase 초기화는 앱의 진입 지점에서 수행되어야 합니다. 보통 `main.dart` 파일에서 `main` 함수 내에 Firebase 앱을 초기화합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(); // Firebase 초기화

  runApp(MyApp());
}
```

위 코드에서 `await Firebase.initializeApp();`을 통해 Firebase를 초기화하고, 앱이 시작될 때 Firebase와의 연결을 수립합니다.

## 3. Firebase Hosting 배포

Firebase 프로젝트와 앱이 준비되었다면, Firebase Hosting 배포를 위해 몇 가지 단계를 거쳐야 합니다.

### 3.1. Firebase CLI 설치

Firebase CLI를 사용하여 배포를 진행합니다. Node.js가 설치되어 있어야 합니다. npm을 통해 Firebase CLI를 설치하세요.

```
$ npm install -g firebase-tools
```

### 3.2. Firebase CLI 로그인

Firebase CLI를 사용하기 위해 로그인해야 합니다. 터미널에서 다음 명령어를 실행하세요.

```
$ firebase login
```

로그인이 완료되면 Gmail 계정으로 인증됩니다.

### 3.3. Firebase 프로젝트 초기화

Firebase 프로젝트를 초기화해야 Firebase Hosting을 사용할 수 있습니다. 프로젝트 루트 경로에 접근하고 다음 명령어를 실행하세요.

```
$ firebase init
```

위 명령어를 실행하면 Firebase CLI가 초기화 설정을 위한 몇 가지 질문을 할 것입니다. Hosting을 선택하고, 기본 설정의 대부분을 사용하면 됩니다.

### 3.4. 앱 빌드

클라이언트 앱을 Firebase Hosting에 배포하기 전에 먼저 앱을 빌드해야 합니다. 터미널에서 다음 명령어를 실행하세요.

```
$ flutter build web
```

위 명령어를 실행하면 `web` 폴더에 앱의 정적 파일이 생성됩니다.

### 3.5. 앱 배포

앱 빌드가 완료되었으면 이제 Firebase 프로젝트에 앱을 배포할 준비가 되었습니다. 터미널에서 다음 명령어를 실행하세요.

```
$ firebase deploy
```

위 명령어를 실행하면 Firebase CLI가 `web` 폴더 내의 파일을 Firebase Hosting에 업로드하고 배포합니다.

## 마치며

이제 Flutter 앱을 Firebase Hosting에 배포하는 방법을 알게 되었습니다. Firebase Hosting은 간편하고 확장 가능한 서비스이며, 효율적인 앱 배포를 제공합니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup?platform=web)를 참고하시기 바랍니다.