---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Cloud Firestore 규칙 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 앱 개발에 매우 유용한 클라우드 기반 플랫폼입니다. Cloud Firestore는 Firebase의 NoSQL 데이터베이스로, 실시간 데이터 동기화와 강력한 쿼리 기능을 제공합니다. Firestore 데이터베이스에 액세스하고 조작하기 위해서는 보안을 유지하기 위해 규칙을 설정해야 합니다.

이 글에서는 플러터 앱에서 Firebase의 Cloud Firestore 규칙을 설정하는 방법에 대해 알아보겠습니다. Firebase_core 패키지를 사용하여 앱에 Firebase를 통합하고, 액세스 권한 제어를 위한 Firestore 규칙을 설정하는 방법을 설명합니다.

## 1. Firebase 프로젝트 생성 및 설정

Firebase 콘솔에 로그인하고, 새 프로젝트를 생성합니다. 프로젝트 이름을 지정하고, 해당 프로젝트를 선택합니다. 프로젝트 설정에서 앱 추가를 선택하고, Flutter 앱을 추가합니다.

앱 추가 단계에서, 패키지 이름을 입력하고, 별칭과 SHA 인증서 지문을 등록합니다. 이 정보는 Firebase와 앱이 상호작용하는 데 필요합니다. 설정이 완료되면, Firebase 콘솔에서 제공되는 `google-services.json` 파일을 다운로드합니다.

## 2. Flutter 앱에 Firebase_core 패키지 추가

플러터 프로젝트의 `pubspec.yaml` 파일을 열고, `firebase_core` 패키지를 추가합니다. 버전에는 Flutter 프로젝트의 최신 버전을 사용해야 합니다.

```dart
dependencies:
  flutter:
    sdk: flutter

  firebase_core: ^1.0.0
```

`pubspec.yaml` 파일을 저장하고, 패키지를 다운로드하기 위해 터미널에서 `flutter pub get` 명령어를 실행합니다.

## 3. Firebase 초기화 및 규칙 설정

`main.dart` 파일을 열고, Firebase 초기화를 위한 코드를 추가합니다. `initializeApp()` 메서드를 호출하여 Firebase를 초기화합니다.

```dart
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';

void main() async {
  // Firebase 초기화
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runApp(MyApp());
}
```

Firebase 초기화가 성공적으로 이루어지면, `FirebaseFirestore.instance`를 사용하여 Firestore 인스턴스에 액세스할 수 있습니다. Firestore 규칙을 설정하기 위해, `FirebaseFirestore.instance.settings` 메서드를 사용합니다. `host`, `sslEnabled`, `persistenceEnabled` 등의 옵션을 설정할 수 있습니다.

이제 Firestore 규칙을 설정해보겠습니다. Firebase 콘솔에서 프로젝트 설정으로 이동한 다음, `Cloud Firestore` 섹션으로 이동합니다. `규칙` 탭을 선택합니다. 원하는 규칙을 작성한 다음, 변경 내용을 저장합니다.

## 4. 플러터 앱에서 Firestore 액세스

이제 Firebase와 Firestore를 사용하여 플러터 앱에서 데이터를 읽고 쓸 수 있습니다. `collection`과 `document` 메서드를 사용하여 Firestore의 컬렉션과 문서에 액세스합니다.

```dart
import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class MyHomePage extends StatelessWidget {
  final firestoreInstance = FirebaseFirestore.instance;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Firestore Example'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: () {
                firestoreInstance.collection("users").get().then((querySnapshot) {
                  querySnapshot.docs.forEach((result) {
                    print(result.data());
                  });
                });
              },
              child: Text('Read Firestore'),
            ),
            ElevatedButton(
              onPressed: () {
                firestoreInstance.collection("users").add({
                  "name": "John Doe",
                  "age": 30,
                }).then((value) {
                  print(value.id);
                });
              },
              child: Text('Write Firestore'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위의 예제는 Firestore에서 데이터를 읽고 쓰는 간단한 플러터 앱의 일부입니다. 코드에서는 `users` 컬렉션에서 데이터를 읽고, 새 문서를 작성하는 방법을 보여줍니다.

이제 Firestore 데이터베이스에 대한 규칙이 설정되며, 플러터 앱에서 데이터를 보안적으로 액세스할 수 있습니다.

## 결론

Firebase_core를 사용하여 플러터 앱에서 Cloud Firestore 규칙을 설정하는 방법에 대해 알아보았습니다. Firebase 초기화 및 Firestore 데이터 액세스를 위한 패키지 설정, Firestore 규칙 설정, 그리고 Firestore 데이터 읽기 및 쓰기를 위한 플러터 코드 작성 방법을 배웠습니다. 이를 통해 플러터 앱에서 Firebase와 Firestore를 사용하여 안전하게 데이터를 관리할 수 있습니다.

더 자세한 내용은 다음 링크를 참조하세요.
- [Firebase 공식 문서](https://firebase.flutter.dev/)
- [Firestore 공식 문서](https://firebase.google.com/docs/firestore)