---
layout: post
title: "[flutter] 플러터와 클라우드 파이어스토어 CRUD(Create, Read, Update, Delete) 작업"
description: " "
date: 2023-12-15
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱을 개발하다보면 데이터베이스에 대한 CRUD(Create, Read, Update, Delete) 작업이 필요하게 됩니다. 이때, 클라우드 파이어스토어(Cloud Firestore)를 사용하여 데이터를 저장하고 관리할 수 있습니다. 이 포스트에서는 플러터와 클라우드 파이어스토어를 함께 사용하여 CRUD 작업을 수행하는 방법에 대해 알아보겠습니다.

## 1. 클라우드 파이어스토어 설정

먼저, 클라우드 파이어스토어를 프로젝트에 연결해야 합니다. Firebase 콘솔에서 새 프로젝트를 만들고, 앱에 Firebase를 추가하고 구성합니다. 그런 다음, 클라우드 파이어스토어를 활성화하고 필요한 규칙을 설정합니다. 

## 2. 플러터 프로젝트 설정

플러터 앱에서 클라우드 파이어스토어를 사용하려면 `cloud_firestore` 패키지를 `pubspec.yaml` 파일에 추가해야 합니다. 패키지를 추가한 후에는 `flutter pub get` 명령을 사용하여 패키지를 다운로드하고 사용할 수 있도록 설정해야 합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  cloud_firestore: ^2.5.4
```

## 3. CRUD 작업 수행

### 3.1 데이터 생성 (Create)

먼저, 클라우드 파이어스토어에 데이터를 추가해보겠습니다. 아래는 클라우드 파이어스토어에 새로운 문서를 추가하는 예제입니다.

```Dart
import 'package:cloud_firestore/cloud_firestore.dart';

final CollectionReference users = FirebaseFirestore.instance.collection('users');

Future<void> addUser() {
  return users
      .add({
        'name': 'John Doe',
        'age': 30,
      })
      .then((value) => print("User Added"))
      .catchError((error) => print("Failed to add user: $error"));
}
```

### 3.2 데이터 조회 (Read)

다음으로, 클라우드 파이어스토어에서 데이터를 조회하는 방법을 알아보겠습니다. 아래는 클라우드 파이어스토어에서 모든 사용자 데이터를 가져오는 예제입니다.

```Dart
Future<void> getUsers() {
  return users.get().then((QuerySnapshot querySnapshot) => {
        querySnapshot.docs.forEach((doc) {
          print(doc["name"]);
          print(doc["age"]);
        })
      });
}
```

### 3.3 데이터 업데이트 (Update)

데이터를 업데이트하는 예제는 다음과 같습니다.

```Dart
Future<void> updateUser() {
  return users
      .doc('documentId')
      .update({'age': 35})
      .then((value) => print("User Updated"))
      .catchError((error) => print("Failed to update user: $error"));
}
```

### 3.4 데이터 삭제 (Delete)

마지막으로, 클라우드 파이어스토어에서 데이터를 삭제하는 방법에 대해 알아보겠습니다.

```Dart
Future<void> deleteUser() {
  return users
      .doc('documentId')
      .delete()
      .then((value) => print("User Deleted"))
      .catchError((error) => print("Failed to delete user: $error"));
}
```

## 결론

이제 플러터 앱에서 클라우드 파이어스토어를 사용하여 CRUD 작업을 수행하는 방법을 알게 되었습니다. 데이터를 생성, 조회, 업데이트, 삭제하는 기능을 구현하여 앱의 데이터 관리를 보다 효율적으로 할 수 있습니다. 이러한 기능을 활용하여 다양한 앱을 개발해보세요!