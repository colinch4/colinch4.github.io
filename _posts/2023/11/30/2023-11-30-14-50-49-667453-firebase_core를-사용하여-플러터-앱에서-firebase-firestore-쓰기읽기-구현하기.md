---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Firestore 쓰기/읽기 구현하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 구글의 벡엔드 클라우드 서비스 플랫폼으로, Firestore는 Firebase의 NoSQL 데이터베이스입니다. 이번 포스트에서는 Flutter 앱에서 Firebase Firestore를 사용하여 데이터를 쓰고 읽는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

먼저, Firebase 프로젝트를 생성하고 앱을 추가해야 합니다. Firebase 콘솔에서 새 프로젝트를 생성하고, "프로젝트 설정" 페이지에서 android 앱과 iOS 앱을 추가합니다. 이 과정에서는 각 플랫폼의 패키지 이름과 SHA-1 인증서 지문을 제공해야 합니다.

Firebase 콘솔에서 생성한 프로젝트에 연결하기 위해 Flutter 프로젝트의 `pubspec.yaml` 파일에 `firebase_core`와 `cloud_firestore` 패키지를 추가해 주세요. 패키지를 추가하려면 `dependencies` 섹션에 다음과 같이 추가하면 됩니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.6.0
  cloud_firestore: ^3.1.0
```

의존성을 추가한 후, 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드하세요.

## Firebase 인증 설정

Firebase 프로젝트의 인증 설정을 구성해야 합니다. 이를 위해 Firebase 콘솔에서 "Authentication" 섹션으로 이동하고, "Sign-in method" 탭에서 "Anonymous"를 활성화하세요. 이렇게 하면 앱 사용자가 익명으로 인증됩니다.

## Firebase 초기화

Firestore에 액세스하려면 Firebase를 초기화해야 합니다. 프로젝트의 `main.dart` 파일을 열고 다음 코드 스니펫을 추가하세요:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runApp(MyApp());
}
```

`Firebase.initializeApp()` 메서드가 Firebase를 초기화하는 역할을 합니다. `main()` 함수를 `async`로 작성하려면 `await Firebase.initializeApp()`을 호출하기 전에 `WidgetsFlutterBinding.ensureInitialized()`를 호출해야 합니다.

## Firestore 쓰기

Firestore에 데이터를 쓰려면 FirebaseFirestore 인스턴스를 사용해야 합니다. Firestore에 데이터를 추가하려면 `collection()` 및 `add()` 메서드를 사용해야 합니다. 예를 들어, "users" 컬렉션에 사용자를 추가하는 코드를 작성해 보겠습니다:

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

void addUser() async {
  final CollectionReference users = FirebaseFirestore.instance.collection('users');

  await users.add({
    'name': 'John',
    'age': 25,
  });
}
```

Firestore에서 데이터를 쓸 때는 비동기 함수로 작성해야 하므로 `async`와 `await` 키워드를 사용했습니다. `users.add()` 메서드를 호출하여 데이터를 추가하고, 사용자 이름과 나이를 맵 형태로 전달했습니다.

## Firestore 읽기

Firestore에서 데이터를 읽으려면 `collection()` 및 `get()` 메서드를 사용해야 합니다. 예를 들어, "users" 컬렉션의 모든 사용자를 가져오는 코드를 작성해 보겠습니다:

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

void getUsers() async {
  final CollectionReference users = FirebaseFirestore.instance.collection('users');

  final QuerySnapshot snapshot = await users.get();
  
  for (final DocumentSnapshot doc in snapshot.docs) {
    print("Name: ${doc.data()['name']}");
    print("Age: ${doc.data()['age']}");
  }
}
```

Firestore에서 데이터를 가져올 때도 비동기 함수로 작성해야 하므로 `async`와 `await` 키워드를 사용했습니다. `users.get()` 메서드를 호출하여 데이터를 가져오고, `snapshot.docs`를 사용하여 모든 문서를 반복하고 이름과 나이를 출력했습니다.

## 마무리

이런 식으로 Flutter 앱에서 Firebase Firestore에 데이터를 쓰고 읽을 수 있습니다. Firebase에서 제공하는 다양한 기능을 사용하여 더 많은 작업을 수행할 수 있습니다. Firebase 문서와 플러터 패키지 문서를 참조하여 더 자세한 내용을 알아보시기 바랍니다.

참고 자료:
- [Firebase 공식 문서](https://firebase.flutter.dev/)
- [FlutterFire GitHub 저장소](https://github.com/FirebaseExtended/flutterfire)