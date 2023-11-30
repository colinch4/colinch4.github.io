---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Realtime Database 관리하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 구글에서 제공하는 클라우드 기반의 개발 플랫폼으로, 다양한 기능과 서비스를 제공합니다. Firebase를 사용하여 플러터(Flutter) 앱에서 실시간 데이터베이스를 관리하는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

Firebase를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔(https://console.firebase.google.com)에 접속하여 프로젝트를 생성한 후, 해당 프로젝트의 설정 페이지에서 "프로젝트의 앱 추가"를 선택하여 플러터 앱을 등록합니다. 이 때, Firebase에서 생성한 앱의 패키지명과 앱 아이콘을 입력해야 합니다.

Firebase 콘솔에서는 Firebase Realtime Database를 활성화해야 합니다. 데이터베이스의 규칙을 설정하고 데이터를 관리하기 위한 권한을 부여할 수 있습니다.

## 플러터 프로젝트 설정

플러터 프로젝트에 Firebase Core를 사용하려면 `firebase_core` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같이 패키지를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.3.0
```

패키지를 추가한 후, 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

Firebase Core를 초기화하기 위해 `main.dart` 파일에서 다음과 같이 코드를 추가합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

`Firebase.initializeApp()` 메소드를 호출하여 Firebase Core를 초기화합니다. `await` 키워드를 사용해 비동기로 처리되도록 해야 합니다.

## Firebase Realtime Database 사용하기

Firebase Realtime Database는 실시간으로 동기화되는 JSON 트리로 데이터를 저장 및 동기화할 수 있는 NoSQL 데이터베이스입니다.

Firebase Realtime Database를 사용하려면 `firebase_database` 패키지를 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같이 패키지를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.3.0
  firebase_database: ^8.0.0
```

패키지를 추가한 후, 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

Firebase Realtime Database를 초기화하여 인스턴스를 생성하고 데이터를 읽고 쓸 수 있습니다. 다음은 Realtime Database에 데이터를 쓰고 읽는 예제입니다:

```dart
import 'package:firebase_database/firebase_database.dart';

void main() {
  final databaseReference = FirebaseDatabase.instance.reference();

  // 데이터 쓰기
  databaseReference.child('message').set({
    'title': 'Hello, Flutter!',
    'body': 'Firebase Realtime Database'
  });

  // 데이터 읽기
  databaseReference.child('message').once().then((DataSnapshot snapshot) {
    print('Title: ${snapshot.value['title']}');
    print('Body: ${snapshot.value['body']}');
  });
}
```

위의 예제에서는 `FirebaseDatabase.instance.reference()`를 사용하여 데이터베이스 객체의 참조를 얻고, 참조를 통해 데이터를 쓰고 읽을 수 있습니다. 데이터를 읽을 때는 `once()` 메소드를 사용하여 한 번만 데이터를 읽도록 합니다.

## 규칙 설정

Firebase Realtime Database에서는 데이터베이스의 규칙을 설정하여 데이터의 읽기 및 쓰기 권한을 제어할 수 있습니다. Firebase 콘솔에서 규칙을 설정할 수 있으며, 다음은 예시 규칙입니다:

```json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

위의 예시 규칙은 사용자가 인증된 경우에만 데이터의 읽기 및 쓰기가 허용되도록 설정합니다. 필요에 따라 규칙을 수정하여 보안과 데이터의 액세스 제어를 강화할 수 있습니다.

## 결론

이번 글에서는 Firebase Core를 사용하여 플러터 앱에서 Firebase Realtime Database를 관리하는 방법을 알아보았습니다. Firebase를 사용하면 빠르고 실시간으로 데이터를 저장하고 동기화할 수 있으며, 권한 설정을 통해 데이터의 보안을 강화할 수 있습니다. Firebase의 다른 기능과 서비스를 활용하여 더욱 강력하고 다양한 앱을 개발할 수 있습니다.

더 자세한 내용을 알아보려면 [Firebase 공식 문서](https://firebase.google.com/docs)를 참고하시기 바랍니다.