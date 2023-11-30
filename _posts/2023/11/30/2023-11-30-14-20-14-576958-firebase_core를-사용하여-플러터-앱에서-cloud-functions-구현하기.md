---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Cloud Functions 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 백엔드 인프라를 개발자들에게 제공하는 플랫폼으로, 배포 관리, 데이터베이스, 인증, 저장소 등 다양한 기능을 제공합니다. Cloud Functions는 이 Firebase 플랫폼 내에서 서버리스 방식으로 동작하는 함수를 개발하고 배포할 수 있는 기능입니다. 이번 튜토리얼에서는 Flutter 앱에서 Cloud Functions를 구현하는 방법을 알아보겠습니다.

## Step 1: Firebase 프로젝트 생성하기
1. Firebase 콘솔에 로그인하고, 프로젝트를 생성합니다.
2. 생성된 프로젝트에 Flutter 앱을 추가합니다.

## Step 2: Cloud Functions 설정하기
1. Firebase 콘솔에서 "Functions" 메뉴로 이동합니다.
2. "시작하기" 버튼을 클릭하여 Cloud Functions를 활성화합니다.

## Step 3: Flutter 프로젝트 설정하기
1. Flutter 프로젝트의 `pubspec.yaml` 파일에 `firebase_core` 패키지를 추가합니다.
   ```yaml
   dependencies:
     firebase_core: ^1.0.0
   ```
2. 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 가져옵니다.

## Step 4: Firebase 초기화하기
1. Flutter 앱의 `main.dart` 파일에 Firebase를 초기화하는 코드를 추가합니다.
   ```dart
   import 'package:firebase_core/firebase_core.dart';

   Future<void> main() async {
     WidgetsFlutterBinding.ensureInitialized();
     await Firebase.initializeApp();
     runApp(MyApp());
   }
   ```

## Step 5: Cloud Functions 사용하기
1. Flutter 앱에서 Cloud Functions를 사용하여 데이터를 가져오는 예제를 살펴보겠습니다.
   ```dart
   import 'package:firebase_functions/firebase_functions.dart';

   void fetchDataFromFunction() {
     final HttpsCallable callable = FirebaseFunctions.instance.httpsCallable('getData');
     callable.call().then((result) {
       // 데이터를 가져온 후에 할 작업들을 정의합니다.
       print(result.data);
     });
   }
   ```

## Step 6: Cloud Functions 배포하기
1. Firebase 콘솔에서 "Functions" 메뉴로 이동합니다.
2. 개발한 Cloud Functions를 배포하기 위해 `firebase deploy --only functions` 명령을 실행합니다.

이제 Flutter 앱에서 Cloud Functions를 사용하여 데이터를 가져오는 기능을 구현할 수 있습니다. Firebase와 Cloud Functions를 사용하면 플러터 앱의 백엔드 로직을 더욱 간단하게 개발할 수 있습니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/functions)를 참고하세요.