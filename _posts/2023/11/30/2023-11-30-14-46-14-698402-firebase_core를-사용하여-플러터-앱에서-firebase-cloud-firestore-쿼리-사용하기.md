---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Firestore 쿼리 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 모바일 및 웹 애플리케이션에서 데이터를 저장, 조회 및 실시간으로 동기화하기위한 클라우드 기반 서비스를 제공하는 Google의 개발 플랫폼입니다. Firebase의 중요한 기능 중 하나인 Cloud Firestore는 NoSQL 데이터베이스이며, 사용자가 실시간으로 데이터를 읽고 쓸 수 있습니다.

이 튜토리얼에서는 플러터 앱에서 Firebase Core를 사용하여 Firebase Cloud Firestore에 저장된 데이터를 조회하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase를 사용하기 위해서는 먼저 Firebase 프로젝트를 설정해야합니다. Firebase 콘솔에 로그인한 후, 새 프로젝트를 생성하고 해당 프로젝트에 Firebase Cloud Firestore를 추가해야합니다. Firebase 프로젝트에 대한 자세한 설정은 [Firebase 문서](https://firebase.google.com/docs/flutter/setup?hl=ko)를 참조하세요.

## 2. 플러터 프로젝트 설정

플러터 앱에서 Firebase를 사용하려면 `firebase_core` 패키지를 사용하여 Firebase를 초기화해야합니다. `pubspec.yaml` 파일에 `firebase_core` 패키지를 추가하고, 패키지를 가져와서 Firebase를 초기화합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Firebase.initializeApp();
  
  runApp(MyApp());
}
```

## 3. Firebase Cloud Firestore 연결

Firebase Cloud Firestore에 연결하기 위해 `cloud_firestore` 패키지를 추가해야합니다. `pubspec.yaml` 파일에 `cloud_firestore` 패키지를 추가하고, 패키지를 가져와서 Firestore 인스턴스를 만듭니다.

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

final FirebaseFirestore firestore = FirebaseFirestore.instance;
```

## 4. Firestore 쿼리 실행하기

Firestore에서 데이터를 조회하기 위해 `Query`를 생성하고, 해당 쿼리를 실행하여 데이터를 가져올 수 있습니다. 예를 들어, `users` 컬렉션에서 모든 사용자를 가져오는 쿼리를 실행하는 방법은 다음과 같습니다.

```dart
QuerySnapshot usersSnapshot = await firestore.collection('users').get();
List<DocumentSnapshot> usersDocuments = usersSnapshot.docs;

usersDocuments.forEach((userDocument) {
  print(userDocument.data());
  // 또는
  print(userDocument.get('name'));
});
```

위 코드는 `users` 컬렉션에서 모든 사용자 데이터를 가져오고, 각 사용자의 이름을 콘솔에 출력합니다.

## 5. Firestore 실시간 업데이트 처리하기

Firestore에서 데이터를 실시간으로 감지하려면 `Stream`을 사용하여 업데이트를 수신할 수 있습니다. 예를 들어, `users` 컬렉션에서 사용자가 추가 또는 업데이트 될 때마다 데이터를 가져오는 방법은 다음과 같습니다.

```dart
Stream<QuerySnapshot> usersStream =
    firestore.collection('users').snapshots();

usersStream.listen((usersSnapshot) {
  List<DocumentSnapshot> usersDocuments = usersSnapshot.docs;
  
  usersDocuments.forEach((userDocument) {
    print(userDocument.data());
    // 또는
    print(userDocument.get('name'));
  });
});
```

위 코드는 `users` 컬렉션에서 사용자 데이터를 실시간으로 가져오고, 매번 데이터가 추가 또는 업데이트 될 때마다 해당 데이터를 콘솔에 출력합니다.

이제 플러터 앱에서 Firebase Cloud Firestore 쿼리를 사용하는 방법을 알게되었습니다. Firebase Cloud Firestore의 다양한 쿼리 옵션을 사용하여 데이터를 조작하고 손쉽게 활용할 수 있습니다.

더 많은 Firebase와 플러터 관련 정보는 [Firebase 플러터 문서](https://firebase.flutter.dev/)를 참조하세요.