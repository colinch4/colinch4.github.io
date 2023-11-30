---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Realtime Database 관리하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자가 앱을 빠르게 개발하고 확장할 수 있는 강력한 클라우드 기반 플랫폼입니다. Firebase Realtime Database는 실시간으로 데이터를 동기화하는 NoSQL 데이터베이스입니다. 플러터 앱에서 Firebase Realtime Database를 사용하여 데이터를 읽고 쓰는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 로그인하고 `프로젝트 만들기` 버튼을 클릭합니다.
2. 프로젝트 이름을 입력하고, 약관에 동의한 뒤 `프로젝트 만들기`를 클릭합니다.
3. 프로젝트가 성공적으로 생성되면, `프로젝트 개요` 페이지로 이동합니다.

## Flutter 앱에 Firebase 추가

1. 플러터 프로젝트 폴더의 `pubspec.yaml` 파일을 엽니다.
2. `dependencies` 섹션에 다음과 같이 Firebase 관련 라이브러리를 추가합니다.

```yaml
firebase_core: ^2.0.0
firebase_database: ^7.0.0
```

3. 터미널에서 `flutter packages get` 명령을 실행하여 패키지를 설치합니다.

## Firebase 앱 구성

1. Firebase 콘솔의 `프로젝트 개요` 페이지에서 Flutter 앱을 추가하기 위해 `앱 추가` 버튼을 클릭합니다.
2. 패키지 이름을 입력하고 앱의 플랫폼을 선택한 뒤 `앱 등록`을 클릭합니다.
3. 생성된 `google-services.json` 파일을 다운로드하여, 프로젝트의 `android/app` 폴더에 추가합니다.

## Firebase_core 초기화

1. `main.dart` 파일을 엽니다.
2. Firebase_core 라이브러리를 import 합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
```

3. `main()` 함수 내부에서 Firebase_core를 초기화합니다.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 데이터 쓰기

1. 데이터를 쓰기 위해 다음 라이브러리를 import 합니다.

```dart
import 'package:firebase_database/firebase_database.dart';
```

2. Firebase Realtime Database에 데이터를 쓰는 예제 코드입니다.

```dart
FirebaseDatabase database = FirebaseDatabase.instance;
DatabaseReference reference = database.reference();

reference.child('users').child('john_doe').set({
  'name': 'John Doe',
  'email': 'john@example.com',
});
```

## 데이터 읽기

1. 데이터를 읽기 위해 다음 라이브러리를 import 합니다.

```dart
import 'package:firebase_database/firebase_database.dart';
```

2. Firebase Realtime Database에서 데이터를 읽는 예제 코드입니다.

```dart
FirebaseDatabase database = FirebaseDatabase.instance;
DatabaseReference reference = database.reference();

reference.child('users').child('john_doe').once().then((DataSnapshot snapshot) {
  print('Name: ${snapshot.value['name']}');
  print('Email: ${snapshot.value['email']}');
});
```

Firebase Realtime Database를 사용하여 플러터 앱에서 데이터를 읽고 쓰는 방법을 알아보았습니다. Firebase Core를 초기화하여 앱에 Firebase를 추가하고, DatabaseReference를 사용하여 데이터를 읽고 쓸 수 있습니다. Firebase Realtime Database는 앱을 실시간으로 업데이트할 수 있고, 데이터를 동기화하여 여러 사용자 간에 실시간으로 공유할 수 있는 강력한 도구입니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs)를 참고하세요.