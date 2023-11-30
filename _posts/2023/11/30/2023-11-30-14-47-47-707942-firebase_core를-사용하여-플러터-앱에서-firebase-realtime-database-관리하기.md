---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Realtime Database 관리하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

## 개요
Firebase는 개발자들이 쉽게 앱에 백엔드 기능을 추가할 수 있는 도구들을 제공하는 Google의 플랫폼입니다. Firebase Realtime Database는 실시간 데이터베이스를 제공하여 앱과 백엔드 간의 실시간 데이터 동기화를 가능하게 합니다. 이번 포스트에서는 플러터 앱에서 Firebase Core를 사용하여 Firebase Realtime Database를 관리하는 방법에 대해 알아보겠습니다.

## Firebase Core 설정하기
Firebase를 사용하기 위해서는 먼저 Firebase Core를 앱에 추가해야 합니다. `pubspec.yaml` 파일에 다음 의존성을 추가해주세요.

```yaml
dependencies:
  firebase_core: ^1.3.0
```

의존성 추가 후, `pub get` 명령어를 실행하여 의존성을 다운로드 받아주세요.

## Firebase 프로젝트 설정하기
Firebase Console에서 Firebase 프로젝트를 생성하고, 프로젝트에 Firebase Realtime Database를 추가해주세요. 

Firebase 프로젝트의 설정 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 다운로드하여 프로젝트 디렉토리에 추가해주세요.

## Firebase Core 초기화하기
Firebase Core를 사용하기 위해 애플리케이션을 초기화해야 합니다. `main.dart` 파일에서 다음과 같이 Firebase Core를 초기화할 수 있습니다.

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  
  runApp(MyApp());
}
```

Firebase.initializeApp() 함수를 호출하여 Firebase Core를 초기화합니다.

## 데이터 읽기 및 쓰기
Firebase Realtime Database에서 데이터를 읽거나 쓰기 위해서는 DatabaseReference 개체를 사용해야 합니다. DatabaseReference는 Database의 특정 위치를 가리키는 참조입니다.

Firebase Database를 사용하여 데이터를 읽어오는 예제는 다음과 같습니다.

```dart
import 'package:firebase_database/firebase_database.dart';

void readData() {
  DatabaseReference dbRef = FirebaseDatabase.instance.reference();
  
  dbRef.child('users').once().then((DataSnapshot snapshot) {
    Map<dynamic, dynamic> values = snapshot.value;
    values.forEach((key, values) {
      print('User: $key, Name: ${values['name']}, Age: ${values['age']}');
    });
  });
}
```

Firebase Database에 데이터를 쓰는 예제는 다음과 같습니다.

```dart
import 'package:firebase_database/firebase_database.dart';

void writeData() {
  DatabaseReference dbRef = FirebaseDatabase.instance.reference();
  
  dbRef.child('users').push().set({
    'name': 'John Doe',
    'age': 25,
  });
}
```

## 결론
이번 포스트에서는 Flutter 앱에서 Firebase Core를 사용하여 Firebase Realtime Database를 관리하는 방법에 대해 알아보았습니다. Firebase Core를 초기화한 뒤 DatabaseReference를 사용하여 데이터를 읽고 쓸 수 있습니다. Firebase를 사용하면서 추가적인 기능들을 사용하고 싶다면 Firebase에서 제공하는 공식 문서를 참고하시기 바랍니다.

## 참고 자료
- [Firebase Core - Flutter Package](https://pub.dev/packages/firebase_core)
- [Firebase Realtime Database - Flutter Package](https://pub.dev/packages/firebase_database)
- [Firebase Documentation](https://firebase.google.com/docs)