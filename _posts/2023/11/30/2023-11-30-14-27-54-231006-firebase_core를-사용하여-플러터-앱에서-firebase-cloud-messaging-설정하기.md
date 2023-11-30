---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Messaging 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들이 안정적이고 확장 가능한 앱을 빠르게 구축할 수 있는 도구입니다. Firebase의 다양한 기능 중 하나인 Firebase Cloud Messaging(FCM)은 앱으로 푸시 알림을 보내기 위해 사용됩니다. Firebase_core 패키지를 사용하여 플러터 앱에서 FCM 설정을 하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔로 이동하고 프로젝트를 생성합니다.
   - [Firebase 콘솔로 이동하기](https://console.firebase.google.com/)
  
2. 프로젝트 설정에서 안드로이드 앱을 추가합니다.
   - 안드로이드 패키지 이름을 입력하고, 앱에 대한 닉네임을 지정합니다.

3. Firebase 구성 파일을 다운로드하고 `android/app` 폴더에 넣습니다.

4. `android/app/build.gradle` 파일에서 아래의 코드를 추가합니다.
   ```groovy
   apply plugin: 'com.google.gms.google-services'
   ```

5. `android/build.gradle` 파일에서 `dependencies` 섹션에 아래의 코드를 추가합니다.
   ```groovy
   classpath 'com.google.gms:google-services:<버전>'
   ```

6. FCM을 위한 안드로이드 외부 라이브러리를 추가합니다.
   - `android/app/build.gradle` 파일에서 아래의 코드를 추가합니다.
   ```groovy
   implementation platform('com.google.firebase:firebase-bom:<버전>')
   implementation 'com.google.firebase:firebase-messaging'
   ```

## 플러터 앱에서 Firebase_core 설정하기

1. `pubspec.yaml` 파일에 `firebase_core` 패키지를 추가합니다.
   ```yaml
   dependencies:
     firebase_core: ^<버전>
   ```

2. `lib/main.dart` 파일에서 아래의 코드를 추가합니다.
   ```dart
   import 'package:firebase_core/firebase_core.dart';

   void main() async {
     WidgetsFlutterBinding.ensureInitialized();
     await Firebase.initializeApp();
     runApp(MyApp());
   }
   ```

3. FCM을 처리할 수 있는 `FirebaseMessaging` 객체를 초기화합니다.
   - `lib/main.dart` 파일에서 아래의 코드를 추가합니다.
   ```dart
   import 'package:firebase_messaging/firebase_messaging.dart';

   Future<void> main() async {
     WidgetsFlutterBinding.ensureInitialized();
     await Firebase.initializeApp();
     FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
     runApp(MyApp());
   }

   Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
     // 백그라운드에서 수신된 푸시 알림에 대한 처리 코드를 작성합니다.
   }
   ```

4. 푸시 알림 수신을 위한 권한 및 서비스 설정을 수행합니다.
   - 앱의 `AndroidManifest.xml` 파일에 아래의 코드를 추가합니다.
   ```xml
   <manifest>
     <uses-permission android:name="android.permission.INTERNET" />
     <uses-permission android:name="android.permission.WAKE_LOCK" />

     <application>
       <!-- FirebaseMessagingService와 FirebaseMessagingService 클래스를 생성하는 경로를 입력합니다. -->
       <service
         android:name=".firebase.MyFirebaseMessagingService"
         android:exported="false">
         <intent-filter>
           <action android:name="com.google.firebase.MESSAGING_EVENT" />
         </intent-filter>
       </service>
       <service android:name=".firebase.MyFirebaseInstanceIDService">
         <intent-filter>
           <action android:name="com.google.firebase.INSTANCE_ID_EVENT" />
         </intent-filter>
       </service>
     </application>
   </manifest>
   ```

5. FirebaseMessagingService 클래스를 생성하고 알림 수신에 대한 처리 코드를 작성합니다.
   - `lib/firebase/my_firebase_messaging_service.dart` 파일을 생성하고 아래의 코드를 추가합니다.
   ```dart
   import 'package:firebase_messaging/firebase_messaging.dart';

   class MyFirebaseMessagingService extends FirebaseMessagingService {
     @override
     Future<void> onMessage(RemoteMessage message) async {
       // 앱이 실행 중일 때 수신된 푸시 알림에 대한 처리 코드를 작성합니다.
     }

     @override
     Future<void> onBackgroundMessage(RemoteMessage message) async {
       // 백그라운드에서 수신된 푸시 알림에 대한 처리 코드를 작성합니다.
     }

     @override
     Future<void> onMessageOpenedApp(RemoteMessage message) async {
       // 사용자가 알림을 탭했을 때의 처리 코드를 작성합니다.
     }
   }
   ```

6. 앱을 빌드하고 실행하여 Firebase Cloud Messaging을 사용하여 푸시 알림을 받아보세요!

Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Messaging을 설정하는 방법을 살펴보았습니다. Firebase를 사용하여 푸시 알림을 구현하여 사용자에게 다양한 알림을 제공할 수 있습니다. 추가적인 설정 및 기능에 대해서는 Firebase 문서를 참조하시기 바랍니다.

참고 문서: [Firebase Cloud Messaging 공식 문서](https://firebase.flutter.dev/docs/messaging/overview/)