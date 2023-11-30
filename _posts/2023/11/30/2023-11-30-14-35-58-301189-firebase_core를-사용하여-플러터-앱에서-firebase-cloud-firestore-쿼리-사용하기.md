---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Firestore 쿼리 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들이 클라우드 기반 앱 개발에 필요한 여러 서비스와 도구를 제공하는 플랫폼입니다. Firebase Cloud Firestore는 Firebase의 실시간 데이터베이스 서비스 중 하나로, 앱의 데이터를 실시간으로 동기화하고 클라우드에 저장하는 데 사용됩니다. 이번 글에서는 플러터 앱에서 Firebase Cloud Firestore의 쿼리를 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Cloud Firestore를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성하고 설정해야 합니다. [Firebase 콘솔](https://console.firebase.google.com)에 접속하여 새 프로젝트를 생성하고, 앱과 연동하는 과정을 거칩니다. 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup)를 참고하세요.

## 2. Firebase_core 패키지 추가

Flutter 앱에서 Firebase Cloud Firestore를 사용하기 위해서는 `firebase_core` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 아래와 같이 의존성을 추가해주세요.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

의존성을 추가한 후 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드합니다.

## 3. Firebase 초기화

Firebase Cloud Firestore를 사용하기 전에, Flutter 앱에서 Firebase를 초기화해야 합니다. `main.dart` 파일의 `main` 함수에 아래 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase를 초기화하는 위 코드에서는 `Firebase.initializeApp()` 함수를 호출하여 Firebase를 초기화합니다.

## 4. Firestore 쿼리 사용하기

이제 Firebase Cloud Firestore의 쿼리를 사용할 준비가 되었습니다. 아래는 Firestore 컬렉션에서 문서를 필터링하는 예제입니다.

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

void getUsers() {
  FirebaseFirestore.instance.collection('users')
    .where('age', isGreaterThanOrEqualTo: 18)
    .get()
    .then((QuerySnapshot querySnapshot) {
      querySnapshot.docs.forEach((doc) {
         // 문서 처리 로직
      });
    })
    .catchError((error) {
      // 에러 처리 로직
    });
}
```

위 코드에서는 `collection('users')`를 통해 'users' 컬렉션을 선택하고, `where` 절을 사용하여 'age' 필드의 값이 18 이상인 문서들을 필터링합니다. 그리고 `get()` 함수를 사용하여 필터링된 문서들을 가져옵니다. 가져온 문서들은 `QuerySnapshot` 형태로 반환되며, `forEach` 함수를 사용하여 문서를 순회하고 처리할 수 있습니다.

## 5. 쿼리 결과 사용하기

Firestore 쿼리를 사용하여 가져온 문서들의 데이터를 사용할 수 있습니다. 아래는 Firestore 문서에서 필드 값을 읽는 예제입니다.

```dart
String getName(DocumentSnapshot document) {
  return document.data()['name'];
}

int getAge(DocumentSnapshot document) {
  return document.data()['age'] ?? 0; // 필드 값이 null인 경우 0으로 기본값 설정
}
```

위 코드에서는 `data()` 함수를 사용하여 문서의 데이터를 가져온 후, 필드 이름을 통해 필드 값을 읽어옵니다. 필드 값이 null인 경우에 대비하여 기본값을 설정할 수도 있습니다.

## 결론

이제 Firebase Cloud Firestore의 쿼리를 사용하는 방법에 대해 알아보았습니다. Firebase의 다양한 기능을 통해 데이터베이스를 구성하고 관리할 수 있으며, 플러터 앱에서 강력한 데이터 처리를 위해 Firebase를 활용할 수 있습니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/firestore/query-data/queries?hl=ko)를 참고하세요.