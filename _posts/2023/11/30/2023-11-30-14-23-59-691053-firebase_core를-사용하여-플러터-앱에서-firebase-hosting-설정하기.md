---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Hosting 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들이 앱 개발을 쉽게 할 수 있도록 다양한 클라우드 기반 서비스를 제공합니다. Firebase Hosting은 Firebase의 한 기능으로, 앱의 정적 파일을 호스팅하고 전 세계적으로 배포할 수 있게 해줍니다. 이번 글에서는 Flutter 앱에서 Firebase Hosting을 설정하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 생성하기

Firebase Hosting을 사용하기 위해 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새 프로젝트를 생성하세요. 프로젝트 이름을 설정하고 필요한 앱 플랫폼을 추가하세요.

## Flutter 프로젝트에 Firebase_core 플러그인 추가하기

Firebase Hosting을 사용하기 위해서는 Flutter 앱에 Firebase_core 플러그인을 추가해야 합니다. `pubspec.yaml` 파일을 열고 아래와 같이 dependencies 섹션에 Firebase_core를 추가하세요.

```dart
dependencies:
  firebase_core: ^1.6.0
```

터미널에서 `flutter pub get` 명령어를 실행하여 Firebase_core 플러그인을 다운로드하고 프로젝트에 적용하세요.

## Firebase 프로젝트 구성 파일 추가하기

Firebase 프로젝트 구성 파일을 Flutter 프로젝트에 추가해야 합니다. Firebase 콘솔에서 프로젝트 설정 페이지로 이동하고, `google-services.json` 파일을 다운로드하세요.

Flutter 프로젝트의 `android/app` 디렉토리에 `google-services.json` 파일을 추가하세요.

## Firebase 초기화하기

Firebase_core 플러그인을 사용하여 Firebase를 초기화해야 합니다. `main.dart` 파일을 열고 Firebase를 초기화하는 코드를 추가하세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## Firebase Hosting 구성하기

Firebase Hosting을 구성하기 위해 Firebase 콘솔로 돌아가세요. 프로젝트 설정 페이지에서 "Hosting" 탭을 선택하세요. "시작하기" 버튼을 클릭하여 Firebase Hosting을 활성화하세요.

Firebase 호스팅 구성 파일(`firebase.json`)을 생성하여 앱의 정적 파일을 호스팅할 위치를 설정하세요. Flutter 프로젝트의 루트 디렉토리에 `firebase.json` 파일을 생성하고 아래와 같이 구성하세요.

```json
{
  "hosting": {
    "public": "build/web",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```

위의 예시에서 `"public"` 속성은 앱의 정적 파일이 위치한 디렉토리를 지정합니다. Flutter 프로젝트에서는 `build/web` 디렉토리가 이에 해당합니다.

## 앱 빌드 및 배포하기

Firebase Hosting 구성이 완료되었습니다. 이제 Flutter 앱을 빌드하고 Firebase Hosting에 배포할 차례입니다. 터미널에서 Flutter 프로젝트의 루트 디렉토리로 이동한 후, 아래 명령어를 실행하세요.

```bash
flutter build web
```

위 명령어를 실행하면 Flutter 앱의 정적 파일이 `build/web` 디렉토리에 생성됩니다.

Firebase 호스팅에 앱을 배포하려면 다음 명령어를 실행하세요.

```bash
firebase deploy --only hosting
```

Firebase CLI를 사용하여 앱을 배포하면 Firebase Hosting에 앱이 갱신되고 전 세계적으로 접근 가능해집니다.

## 결론

이것으로 Firebase_core를 사용하여 Flutter 앱에서 Firebase Hosting을 설정하는 방법을 살펴보았습니다. Firebase Hosting을 통해 앱을 전 세계에 배포하고 사용자들에게 더 나은 앱 환경을 제공할 수 있게 되었습니다. 추가적인 기능과 설정에 대해서는 Firebase 문서를 참고하세요.

#### 참고 문서:

- [Firebase 콘솔](https://console.firebase.google.com/)
- [Firebase_core 패키지](https://pub.dev/packages/firebase_core)
- [Firebase Hosting 문서](https://firebase.google.com/docs/hosting)