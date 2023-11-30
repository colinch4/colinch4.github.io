---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Firestore 쓰기/읽기 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google의 클라우드 기반 플랫폼으로, 플러터 앱을 개발할 때 데이터베이스로 Firebase Firestore를 활용할 수 있습니다. Firebase Core를 사용하여 플러터 앱에서 Firebase Firestore를 쓰기와 읽기를 구현하는 방법을 알아보겠습니다.

## Firebase 설정하기

1. Firebase 콘솔에 접속하여 프로젝트를 생성합니다.
2. 프로젝트 설정에서 `앱 추가` 버튼을 클릭하여 플러터 앱을 추가합니다. 필요한 정보를 입력하고, `패키지 이름`은 `com.example.myapp` 형식으로 입력합니다.
3. `google-services.json` 파일을 다운로드하여 플러터 프로젝트의 `android/app` 폴더에 추가합니다.

## Firebase 및 Firestore 패키지 추가하기

1. `pubspec.yaml` 파일을 열고, dependencies에 아래의 패키지를 추가합니다.
```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.2.1
  cloud_firestore: ^2.2.2
```
2. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 가져옵니다.

## Firebase Core 초기화하기

1. 앱의 메인 파일(`main.dart`)을 열어 `Firebase.initializeApp()`를 호출하여 Firebase Core를 초기화합니다.
```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(); // Firebase Core 초기화
  runApp(MyApp());
}
```

## Firestore 쓰기 구현하기

1. Firestore에 데이터를 쓰는 기능을 추가하기 위해, Firestore 인스턴스를 생성하고 새로운 문서를 추가합니다.
```dart
import 'package:cloud_firestore/cloud_firestore.dart';

void addData() {
  FirebaseFirestore.instance.collection('users').add({
    'name': 'John',
    'age': 25,
  }).then((value) => print('Data added successfully!'))
      .catchError((error) => print('Failed to add data: $error'));
}
```
2. `addData()` 함수를 호출하여 Firestore에 데이터를 추가할 수 있습니다.

## Firestore 읽기 구현하기

1. Firestore에서 데이터를 읽는 기능을 추가하기 위해, Firestore 인스턴스를 사용하여 데이터를 가져옵니다.
```dart
import 'package:cloud_firestore/cloud_firestore.dart';

void getData() {
  FirebaseFirestore.instance.collection('users').get().then((snapshot) {
    snapshot.docs.forEach((doc) {
      print(doc.data());
    });
  }).catchError((error) => print('Failed to get data: $error'));
}
```
2. `getData()` 함수를 호출하여 Firestore에서 데이터를 가져올 수 있습니다.

이제 Firebase Core를 사용하여 플러터 앱에서 Firebase Firestore의 쓰기와 읽기를 구현하는 방법을 알게 되었습니다. Firebase 문서를 참조하여 추가적인 기능을 구현할 수 있습니다.

## 참고 자료
- [Firebase 콘솔](https://console.firebase.google.com)
- [Flutter](https://flutter.dev)
- [Firebase Core](https://pub.dev/packages/firebase_core)
- [Firebase Firestore](https://pub.dev/packages/cloud_firestore)