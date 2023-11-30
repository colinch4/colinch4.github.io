---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firestore 데이터베이스 연동하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

이 튜토리얼에서는 Flutter 앱에서 Firestore 데이터베이스를 연동하는 방법에 대해 알아보겠습니다. 본 튜토리얼에서는 Firebase_core 패키지를 사용하여 Firebase의 필수 기능을 설정하고, Firestore 데이터베이스에 데이터를 읽고 쓰는 방법을 소개합니다.

## 목차
- [Firebase_core 패키지 설치](#firebase_core-패키지-설치)
- [Firebase 프로젝트 설정](#firebase-프로젝트-설정)
- [Firestore 연동하기](#firestore-연동하기)
- [Firestore에서 데이터 읽기](#firestore에서-데이터-읽기)
- [Firestore에 데이터 쓰기](#firestore에-데이터-쓰기)

## Firebase_core 패키지 설치

Firebase_core 패키지는 Firebase의 기본 설정과 초기화를 담당합니다. 다음 명령어로 패키지를 설치할 수 있습니다:

```dart
dependencies:
  firebase_core: ^1.0.3
```

패키지를 설치한 후, `pubspec.yaml` 파일을 업데이트하세요. 그 후, Flutter 프로젝트를 다시 빌드하여 의존성을 업데이트하십시오. 

## Firebase 프로젝트 설정

Firebase 콘솔에서 새로운 프로젝트를 생성하고, 앱을 추가하세요.  Firebase SDK 구성 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 다운로드한 뒤, 프로젝트의 `android/app` 또는 `ios/Runner` 디렉토리에 파일을 추가해야 합니다. 이 파일은 Firebase와 앱을 연동하기 위한 필수 파일입니다.

## Firestore 연동하기

Firebase_core 패키지를 사용하여 Firestore를 초기화합니다.

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Firestore',
      home: HomeScreen(),
    );
  }
}
```

## Firestore에서 데이터 읽기

Firestore에서 데이터를 읽고 화면에 표시하는 예제를 살펴보겠습니다.

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Firestore'),
      ),
      body: StreamBuilder(
        stream: FirebaseFirestore.instance
            .collection('users')
            .snapshots(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView.builder(
              itemCount: snapshot.data.docs.length,
              itemBuilder: (context, index) {
                DocumentSnapshot document = snapshot.data.docs[index];
                return ListTile(
                  title: Text(document['name']),
                  subtitle: Text(document['email']),
                );
              },
            );
          } else if (snapshot.hasError) {
            return Text('Error: ${snapshot.error}');
          } else {
            return CircularProgressIndicator();
          }
        },
      ),
    );
  }
}
```

위 예제는 Firestore의 "users" 컬렉션에서 데이터를 실시간으로 읽어와 ListView에 표시합니다.

## Firestore에 데이터 쓰기

Firestore에 데이터를 쓰는 예제를 살펴보겠습니다.

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

class AddUserScreen extends StatelessWidget {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController emailController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Add User'),
      ),
      body: Column(
        children: [
          TextField(
            controller: nameController,
            decoration: InputDecoration(labelText: 'Name'),
          ),
          TextField(
            controller: emailController,
            decoration: InputDecoration(labelText: 'Email'),
          ),
          ElevatedButton(
            onPressed: () {
              FirebaseFirestore.instance.collection('users').doc().set({
                'name': nameController.text,
                'email': emailController.text,
              });
              Navigator.pop(context);
            },
            child: Text('Add'),
          ),
        ],
      ),
    );
  }
}
```

위 예제는 사용자의 이름과 이메일을 입력받아 Firestore의 "users" 컬렉션에 데이터를 쓰는 방법을 보여줍니다.

이제 Firebase_core 패키지를 사용하여 플러터 앱에서 Firestore 데이터베이스를 연동하는 방법을 알게 되었습니다. 다양한 Firestore 기능을 활용하여 앱의 데이터를 효율적으로 관리할 수 있습니다. 추가적인 기능과 설정에 대해서는 Firestore의 공식 문서를 참조하세요.

### 참고 자료
[Firebase Core 패키지](https://pub.dev/packages/firebase_core)\
[Firebase Console](https://console.firebase.google.com)\
[Firestore](https://firebase.flutter.dev/docs/firestore/usage)