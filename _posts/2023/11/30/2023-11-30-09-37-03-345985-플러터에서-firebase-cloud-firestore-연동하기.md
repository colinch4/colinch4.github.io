---
layout: post
title: "[flutter] 플러터에서 Firebase Cloud Firestore 연동하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Cloud Firestore는 실시간 데이터베이스 서비스로, 모바일 및 웹 애플리케이션 개발에 매우 유용합니다. 이번 포스트에서는 플러터(Flutter) 프레임워크에서 Firebase Cloud Firestore를 어떻게 연동하는지에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

먼저 Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새 프로젝트를 생성하고, 해당 프로젝트에 원하는 앱을 추가합니다. 구글 서비스 계정 파일을 다운로드하고, 프로젝트 디렉토리의 `android/app` 폴더에 복사합니다.

## 2. Flutter 프로젝트 설정

Flutter 프로젝트에서 Firebase를 사용하기 위해 다음 패키지들을 `pubspec.yaml` 파일에 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
  cloud_firestore: ^2.0.0
```

패키지를 추가한 후, 터미널에서 `flutter pub get` 명령을 실행하여 종속성을 가져옵니다.

## 3. Firebase 초기화

플러터 앱의 `main.dart` 파일에서 Firebase를 초기화합니다. `main` 함수에서 `runApp` 전에 다음 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 4. Firestore 데이터 읽기 및 쓰기

이제 Firestore 데이터베이스를 읽고 쓰기 위해 필요한 코드를 작성해보겠습니다.

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

// 데이터베이스에 데이터 쓰기
void writeData() {
  FirebaseFirestore.instance
      .collection('users')  // 컬렉션 이름
      .doc('1')  // 문서 ID
      .set({
        'name': 'John Doe',
        'age': 30,
      });
}

// 데이터베이스에서 데이터 읽기
void readData() {
  FirebaseFirestore.instance
      .collection('users')
      .doc('1')
      .get()
      .then((DocumentSnapshot documentSnapshot) {
    if (documentSnapshot.exists) {
      print('Name: ${documentSnapshot.data()['name']}');
      print('Age: ${documentSnapshot.data()['age']}');
    } else {
      print('Document does not exist');
    }
  });
}
```

위의 코드는 간단한 예시로, `users` 컬렉션 내에 `1`이라는 ID를 가진 문서에 데이터를 쓰고 읽는 방법을 보여줍니다.

## 마무리

이제 플러터 앱에서 Firebase Cloud Firestore를 성공적으로 연동하였습니다. 이를 활용하여 복잡한 앱의 데이터 관리를 간편하게 수행할 수 있습니다. Firebase Cloud Firestore의 다양한 기능을 살펴보고, 앱의 요구 사항에 맞게 활용해보세요.