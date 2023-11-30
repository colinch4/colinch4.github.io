---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Firestore 쓰기/읽기 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

이번에는 Flutter 앱에서 Firebase Firestore를 사용하여 데이터를 쓰고 읽는 방법에 대해 소개하겠습니다. Firebase Firestore는 실시간 데이터 동기화를 제공하는 NoSQL 데이터베이스입니다. Firebase Firestore를 사용하면 플러터 앱에서 간단하게 데이터를 저장하고 검색할 수 있습니다.

## 1. Firebase 설정하기
먼저, Firebase Console에서 프로젝트를 생성하고 Firebase Firestore를 활성화해야 합니다. Firebase Console에서 프로젝트를 생성한 후, "프로젝트 설정"으로 이동하여 "Firebase SDK 스니펫"을 다운로드하고 `google-services.json` 파일을 프로젝트의 `android/app` 폴더에 추가합니다. 

## 2. firebase_core 패키지 추가하기
Firebase Firestore를 사용하기 위해 firebase_core 패키지를 추가해야 합니다. `pubspec.yaml` 파일의 dependencies 섹션에 다음과 같은 코드를 추가합니다:

```yaml
dependencies:
  firebase_core: ^1.0.1
```

## 3. firebase_firestore 패키지 추가하기
Firebase Firestore를 사용하기 위해 `firebase_firestore` 패키지를 추가합니다. `pubspec.yaml` 파일의 dependencies 섹션에 다음과 같은 코드를 추가합니다:

```yaml
dependencies:
  firebase_firestore: ^2.5.4
```

## 4. Firebase.initializeApp() 호출하기
Firebase Firestore를 사용하기 전에 `Firebase.initializeApp()`을 호출해야 합니다. 이를 위해 앱의 시작점인 `main()` 함수에서 `await Firebase.initializeApp();`을 호출합니다. 

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 5. Firestore 데이터 쓰기
Firestore에 데이터를 쓰려면 `FirebaseFirestore.instance.collection('collectionName').doc('docName').set(data);` 메서드를 사용합니다. `collectionName`은 컬렉션의 이름, `docName`은 문서의 이름, `data`는 저장할 데이터를 의미합니다.

```dart
import 'package:firebase_firestore/firebase_firestore.dart';

void writeData() {
  FirebaseFirestore.instance
    .collection('users')
    .doc('1')
    .set({
      'name': 'John',
      'age': 30,
      'email': 'john@example.com',
    })
    .then((value) => print("Data has been written successfully!"))
    .catchError((error) => print("Failed to write data: $error"));
}
```

## 6. Firestore 데이터 읽기
Firestore에서 데이터를 읽으려면 `FirebaseFirestore.instance.collection('collectionName').doc('docName').get();` 메서드를 사용합니다.

```dart
import 'package:firebase_firestore/firebase_firestore.dart';

void readData() {
  FirebaseFirestore.instance
    .collection('users')
    .doc('1')
    .get()
    .then((DocumentSnapshot documentSnapshot) {
      if (documentSnapshot.exists) {
        print('Document data: ${documentSnapshot.data()}');
      } else {
        print('Document does not exist on the database');
      }
    })
    .catchError((error) => print("Failed to read data: $error"));
}
```

위의 코드에서 `doc('1')`에서 '1'은 문서의 이름을 나타냅니다. 필요에 따라 동적으로 문서 이름을 변경할 수 있습니다.

## 마무리
이제 Firebase Firestore를 사용하여 플러터 앱에서 데이터를 쓰고 읽을 수 있습니다. Firestore의 다양한 기능을 활용하여 앱에 맞게 데이터를 구성하고 활용해 보세요.

더 많은 자세한 내용은 [Firebase 공식 문서](https://firebase.flutter.dev/)를 참조하세요.