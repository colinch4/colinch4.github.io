---
layout: post
title: "[flutter] 플러터에서 Firebase Realtime Database 연동하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---
Firebase는 Google에서 제공하는 클라우드 기반 플랫폼으로, 실시간 데이터베이스를 비롯한 다양한 기능을 제공합니다. 이번 포스트에서는 플러터(Flutter)에서 Firebase Realtime Database를 연동하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정 및 구성
Firebase Realtime Database를 사용하기 위해서는 먼저 Firebase 프로젝트를 설정해야 합니다. Firebase 콘솔에 접속하여 프로젝트를 생성하고, Firebase SDK를 다운로드 받아 프로젝트에 추가합니다.

## 2. 플러터 프로젝트에 Firebase 패키지 추가
플러터 프로젝트에서 Firebase Realtime Database를 사용하기 위해 `firebase_database` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같이 의존성을 추가합니다.

```dart
dependencies:
  firebase_database: ^7.0.0
```

의존성을 추가한 후 터미널에서 `flutter packages get` 명령어를 실행하여 패키지를 다운로드 받습니다.

## 3. Firebase 초기화 및 데이터 읽기/쓰기
Firebase 패키지를 추가한 후, 플러터 앱에서 Firebase를 초기화하고 데이터를 읽거나 쓸 수 있습니다. 다음은 Firebase Realtime Database에 데이터를 쓰고 읽는 간단한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:firebase_database/firebase_database.dart';

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final databaseReference = FirebaseDatabase.instance.reference();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Firebase Realtime Database"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              child: Text("Write Data"),
              onPressed: () {
                databaseReference.child('message').set("Hello, Flutter!");
              },
            ),
            SizedBox(height: 16),
            ElevatedButton(
              child: Text("Read Data"),
              onPressed: () {
                databaseReference.child('message').once().then((DataSnapshot snapshot) {
                  showDialog(
                    context: context,
                    builder: (BuildContext context) {
                      return AlertDialog(
                        title: Text("Message"),
                        content: Text(snapshot.value),
                      );
                    },
                  );
                });
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

위의 코드에서 `databaseReference`는 Firebase Realtime Database의 루트 참조를 가리키는 객체입니다. `onPressed` 이벤트 핸들러에서 해당 참조를 사용하여 데이터를 읽거나 쓸 수 있습니다.

## 4. 플러터 앱 실행 및 Firebase Realtime Database 확인
위의 예시 코드를 실행하면 플러터 앱에서 "Write Data" 버튼을 눌렀을 때 'message'라는 키에 "Hello, Flutter!"라는 값이 쓰여지고, "Read Data" 버튼을 눌렀을 때 해당 데이터를 다이얼로그로 확인할 수 있습니다. 실제 Firebase 콘솔에서도 변경된 데이터를 확인할 수 있습니다.

이처럼 플러터에서 Firebase Realtime Database를 연동하여 실시간으로 데이터를 읽고 쓸 수 있습니다. 이를 활용하여 다양한 앱 개발 가능성을 가질 수 있습니다.

더 자세한 내용은 [Firebase Realtime Database 설명서](https://firebase.flutter.dev/docs/database/overview/)를 참고하시기 바랍니다.