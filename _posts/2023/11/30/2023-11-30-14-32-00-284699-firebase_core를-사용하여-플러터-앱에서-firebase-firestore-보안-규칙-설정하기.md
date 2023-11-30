---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Firestore 보안 규칙 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google에서 제공하는 클라우드 기반 개발 플랫폼으로, 다양한 기능을 제공합니다. 이 중 Firebase Firestore는 실시간 데이터베이스로, 플러터 앱에서 데이터를 저장하고 동기화하는 데 사용될 수 있습니다. Firebase Firestore의 보안 규칙은 애플리케이션의 보안성과 데이터의 무결성을 보장하기 위해 설정할 수 있는 중요한 요소입니다.

이 글에서는 플러터 앱에서 Firebase Firestore의 보안 규칙을 설정하는 방법에 대해 알아보겠습니다. 이를 위해 Firebase_core 패키지를 사용하여 Firebase Firestore에 액세스하는 코드 작성하는 방법을 안내합니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 프로젝트를 생성하고 Firebase Firestore를 활성화해야 합니다. Firebase 프로젝트를 생성하려면 다음 단계를 따르세요.

1. Firebase 콘솔(https://console.firebase.google.com)에 로그인합니다.
2. 새 프로젝트를 만들거나 기존 프로젝트를 선택합니다.
3. 프로젝트 이름을 입력하고 프로젝트를 생성합니다.
4. Firebase Firestore를 활성화합니다.

## 2. Firebase_core 패키지 설치

플러터 앱에서 Firebase Firestore를 사용하기 위해 `firebase_core` 패키지를 설치해야 합니다. `pubspec.yaml` 파일을 열고 의존성에 다음 코드를 추가하세요:

```dart
dependencies:
  firebase_core: ^0.8.0
  firebase_auth: ^3.0.1
  cloud_firestore: ^3.1.0
```

의존성을 추가한 후 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치해주세요.

## 3. Firebase 앱 초기화

Firebase를 사용하기 위해 앱을 초기화해야 합니다. `main.dart` 파일을 열고 다음 코드를 추가하세요:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

위의 코드는 Firebase를 초기화하고 앱을 실행하는 데 필요한 작업을 수행합니다.

## 4. Firebase Firestore 보안 규칙 설정

Firestore 보안 규칙은 Firebase 콘솔에서 설정할 수 있습니다. 보안 규칙은 액세스 권한과 데이터 검증 등을 설정할 수 있습니다. 로그인한 상태에서 Firebase 콘솔로 이동하고 "Firestore Database" 탭으로 이동하세요.

보안 규칙을 설정하기 위해 다음과 같은 예제 코드를 참고하세요:

```dart
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read: if isLoggedIn();
      allow write: if isLoggedIn() && isOwner();
      allow delete: if isLoggedIn() && isOwner();
    }
  }
}

function isLoggedIn() {
  return request.auth != null;
}

function isOwner() {
  return request.auth.uid == resource.data.author;
}    
```

위의 코드에서는 `read`, `write`, `delete` 작업에 대한 액세스 권한을 설정합니다. `isLoggedIn()` 함수는 사용자가 로그인한 경우에만 액세스를 허용하고, `isOwner()` 함수는 데이터의 `author` 필드가 현재 사용자의 UID와 일치하는 경우에만 `write` 및 `delete` 액세스를 허용합니다.

## 5. Firestore 데이터 추가, 수정, 삭제

앱에서 Firestore 데이터를 추가, 수정, 삭제하는 방법은 Cloud Firestore 패키지를 사용하여 직접 코드를 작성하는 것입니다. 다음은 데이터를 추가하는 예제입니다:

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

final CollectionReference usersCollection = FirebaseFirestore.instance.collection('users');

Future<void> addUser() {
  return usersCollection
    .add({
      'name': 'John Doe',
      'email': 'johndoe@gmail.com',
    })
    .then((value) => print("User added"))
    .catchError((error) => print("Failed to add user: $error"));
}
```

위의 코드는 `users` 컬렉션에 사용자 정보를 추가합니다. 필요에 따라 데이터를 수정하거나 삭제하는 작업도 이와 비슷한 방식으로 수행할 수 있습니다.

이제 플러터 앱에서 Firebase Firestore 보안 규칙을 설정하는 방법에 대해 알게 되었습니다. Firebase_core 패키지를 사용하여 Firebase Firestore에 액세스하는 코드 작성하는 방법을 학습했습니다. 이를 바탕으로 앱의 보안성과 데이터 무결성을 강화하는데 도움이 되길 바랍니다.