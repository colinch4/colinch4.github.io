---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Cloud Firestore 쿼리 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들에게 클라우드 기반의 백엔드 서비스를 제공하는 플랫폼입니다. 이 중 Firebase의 Cloud Firestore는 데이터베이스 서비스로서, 실시간 데이터 동기화와 강력한 쿼리 기능을 제공합니다.

이번 글에서는 플러터 앱을 개발하면서 Firebase의 Cloud Firestore를 사용하여 데이터를 읽고 쓰는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정하기

먼저, Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새 프로젝트를 생성한 후, 프로젝트의 설정 페이지에서 Firebase를 사용할 앱에 대한 설정 파일을 다운로드하세요.

## Firebase_core 패키지 추가하기

Firebase의 다양한 서비스를 사용하기 위해선, 먼저 `firebase_core` 패키지를 플러터 앱에 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같이 패키지를 추가하세요:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

패키지 추가 후에는 `pub get` 명령어를 실행하여 패키지를 설치하세요.

## Firebase 연동하기

`firebase_core` 패키지가 추가되었으면, Firebase를 초기화해야 합니다. 이를 위해 `main.dart` 파일에 다음과 같이 코드를 추가하세요:

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

위 코드에서 `await Firebase.initializeApp();`를 통해 Firebase를 초기화해줍니다.

## Cloud Firestore에 데이터 쓰기

데이터를 Cloud Firestore에 쓰기 위해서는 다음과 같이 코드를 작성합니다:

```dart
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void addData() {
  FirebaseFirestore.instance.collection('users').add({
    'name': 'John',
    'age': 30,
    'email': 'john@example.com',
  });
}
```

위 코드는 `users` 컬렉션에 새로운 문서를 추가하는 예시입니다. 문서의 내용으로는 `name`, `age`, `email` 필드가 있습니다.

## Cloud Firestore에서 데이터 읽기

Cloud Firestore에서 데이터를 읽기 위해서는 다음과 같이 코드를 작성합니다:

```dart
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void readData() {
  FirebaseFirestore.instance.collection('users').get().then((querySnapshot) {
    querySnapshot.docs.forEach((doc) {
      print('Name: ${doc.data()['name']}');
      print('Age: ${doc.data()['age']}');
      print('Email: ${doc.data()['email']}');
    });
  });
}
```

위 코드는 `users` 컬렉션의 모든 문서를 가져와서 각 문서의 필드를 출력하는 예시입니다.

Firebase에서 데이터를 읽고 쓰는 방법에 대해 간단히 알아보았습니다. 이 외에도 Firebase의 다양한 기능과 서비스를 플러터 앱에 추가할 수 있으니, 관심이 있다면 Firebase 공식 문서를 참고해보세요.

---

참고 자료:
- Firebase 공식 문서: https://firebase.flutter.dev/
- Flutter 공식 문서: https://flutter.dev/