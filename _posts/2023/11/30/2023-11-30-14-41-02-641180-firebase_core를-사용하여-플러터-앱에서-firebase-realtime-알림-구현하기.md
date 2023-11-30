---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Realtime 알림 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 앱 개발에 매우 유용한 클라우드 기반 플랫폼입니다. Firebase를 사용하면 앱에 다양한 기능을 추가할 수 있으며, 실시간으로 데이터를 동기화하고 알림을 전송하는 등의 작업을 수행할 수 있습니다. 이번 블로그 포스트에서는 Firebase Core를 사용하여 플러터 앱에서 Firebase Realtime 알림을 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정하기

1. Firebase 콘솔에 접속하여 새 프로젝트를 생성합니다.
2. 생성한 프로젝트를 선택하고 "프로젝트 설정"으로 이동합니다.
3. "프로젝트 설정" 탭에서 "프로젝트 설정" 페이지로 이동합니다.
4. "앱" 섹션에서 "앱 추가" 버튼을 클릭하고, 플러터 앱의 패키지 이름을 입력합니다.
5. 생성된 앱의 "google-services.json" 파일을 다운로드합니다.

## Firebase Core 패키지 추가하기

1. pubspec.yaml 파일을 열고 `firebase_core` 패키지를 추가합니다.

   ```yaml
   dependencies:
     flutter:
       sdk: flutter
     firebase_core: ^1.0.0
   ```

2. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 가져옵니다.

## Firebase Core 초기화하기

1. main.dart 파일을 열고 Firebase Core를 초기화합니다.

   ```dart
   import 'package:firebase_core/firebase_core.dart';

   void main() async {
     WidgetsFlutterBinding.ensureInitialized();
     await Firebase.initializeApp();
     runApp(MyApp());
   }
   ```

## Firebase Realtime 알림 구현하기

Firebase Realtime 알림은 데이터베이스에 신규 데이터가 추가되거나 변경될 때 사용자에게 알림을 보내는 기능입니다. Firebase Core를 초기화한 후에는 Firebase Realtime Database를 사용하여 실시간 알림을 구현할 수 있습니다.

1. Firebase Realtime Database를 사용하기 위해 해당 패키지를 추가합니다.

   ```yaml
   dependencies:
     firebase_database: ^7.0.0
   ```

2. main.dart 파일에 Firebase Realtime Database 관련 코드를 추가합니다.

   ```dart
   import 'package:firebase_database/firebase_database.dart';

   final FirebaseDatabase database = FirebaseDatabase.instance;

   void sendNotification() {
     DatabaseReference ref = database.reference();

     ref.child('notifications').push().set({
       'title': 'New notification',
       'message': 'You have a new notification'
     });
   }
   ```

3. 필요에 따라 플러터 앱에서 알림을 전송하는 작업을 수행합니다. 예를 들어, 버튼을 누를 때마다 알림을 전송하도록 코드를 작성할 수 있습니다.

   ```dart
   RaisedButton(
     child: Text('Send Notification'),
     onPressed: () {
       sendNotification();
     },
   )
   ```

## 결론

Firebase Core를 사용하여 플러터 앱에서 Firebase Realtime 알림을 구현하는 방법에 대해 알아보았습니다. Firebase Realtime Database를 사용하면 앱에서 전달되는 데이터의 변경사항을 감지하고 알림을 보낼 수 있습니다. Firebase의 다양한 기능을 활용하여 앱을 더욱 풍부하고 유용하게 만들어보세요!

참고 문서:
- [Firebase Documentaion](https://firebase.flutter.dev/docs/)
- [Firebase Realtime Database Package](https://pub.dev/packages/firebase_database)