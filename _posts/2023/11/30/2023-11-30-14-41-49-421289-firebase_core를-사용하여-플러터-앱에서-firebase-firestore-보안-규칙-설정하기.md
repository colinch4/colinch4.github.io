---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Firestore 보안 규칙 설정하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Firestore는 클라우드 기반의 NoSQL 데이터베이스이며, 다양한 플랫폼에서 사용할 수 있는 Firebase 서비스 중 하나입니다. 이번 블로그에서는 플러터 앱에서 Firebase Firestore 보안 규칙을 설정하는 방법에 대해 알아보겠습니다.

## Firebase 설정

먼저 Firebase 콘솔에서 Firestore를 활성화해야 합니다. Firebase 콘솔로 이동하여 "Firestore" 탭을 선택하고, 데이터베이스를 만들거나 이미 있는 데이터베이스를 선택하세요.

## Firebase_core 패키지 추가

Firebase Firestore를 사용하기 위해서는 Firebase_core 패키지가 필요합니다. `pubspec.yaml` 파일에 Firebase_core 패키지를 추가해주세요.

```dart
dependencies:
  firebase_core: ^1.0.2
```

`pub get` 명령어를 사용하여 패키지를 설치하세요.

## Firebase 앱 초기화

Firebase를 사용하기 위해 앱을 초기화해야 합니다. `main.dart` 파일에서 Firebase 앱을 초기화하는 코드를 추가하세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  
  runApp(MyApp());
}
```

## Firestore 보안 규칙 설정

Firestore 보안 규칙을 설정하기 위해 Firebase 콘솔로 이동하세요. "Firestore" 탭에서 "보안 규칙"을 선택하세요. 이제 규칙 파일을 열어 설정할 수 있습니다.

Firestore 보안 규칙은 Firestore 데이터베이스에 액세스하는 사용자의 권한을 제어합니다. 예를 들어, 특정 사용자 그룹에 대한 읽기 또는 쓰기 권한을 설정할 수 있습니다.

```dart
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // 전체 쓰기 액세스를 금지합니다.
    allow write: if false;
    
    // 인증된 사용자에게만 읽기 액세스를 허용합니다.
    allow read: if request.auth != null;
  }
}
```

위의 예시에서는 모든 쓰기 액세스를 차단하고, 인증된 사용자에게만 읽기 액세스를 허용합니다. 이 예시를 기반으로 필요한 보안 규칙을 설정해주세요.

## 플러터 앱에서 Firestore 액세스

Firebase Firestore 보안 규칙을 설정한 뒤에 플러터 앱에서 Firestore에 액세스할 수 있습니다. `firebase_auth` 패키지를 사용하여 인증된 사용자를 로그인시킨 후, Firestore에 액세스할 수 있습니다.

Firestore에 액세스하기 위해 `cloud_firestore` 패키지를 `pubspec.yaml` 파일에 추가해주세요.

```dart
dependencies:
  cloud_firestore: ^2.5.0
```

`pub get` 명령어를 사용하여 패키지를 설치하세요.

이제 Firestore에 액세스하여 데이터를 읽거나 쓸 수 있습니다.

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

void getData() {
  FirebaseFirestore.instance.collection('users').doc('user1').get()
    .then((DocumentSnapshot documentSnapshot) {
      if (documentSnapshot.exists) {
        print(documentSnapshot.data());
      } else {
        print('Document does not exist');
      }
    })
    .catchError((error) {
      print('Error: $error');
    });
}
```

위의 예시에서는 'users' 컬렉션에서 'user1' 문서를 가져오는 방법을 보여줍니다. 데이터를 읽거나 쓸 때, Firestore 보안 규칙에 맞게 액세스 권한을 확인하세요.

## 마무리

이번 블로그에서는 Firebase_core를 사용하여 플러터 앱에서 Firebase Firestore 보안 규칙을 설정하는 방법을 알아보았습니다. Firestore 보안 규칙을 설정함으로써 데이터베이스의 안전한 액세스를 보장할 수 있습니다. Firebase Firestore를 효율적으로 사용하여 플러터 앱을 개발해보세요!

---

**참고 자료:**

- [Firebase 문서 - Firestore 보안 규칙](https://firebase.google.com/docs/firestore/security/get-started?hl=ko)
- [Firebase 문서 - Firestore 규칙 작성 방법](https://firebase.google.com/docs/firestore/security/rules-conditions?hl=ko)