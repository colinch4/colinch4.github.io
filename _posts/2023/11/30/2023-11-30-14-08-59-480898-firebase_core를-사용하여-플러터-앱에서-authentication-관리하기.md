---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Authentication 관리하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 웹 및 모바일 애플리케이션 개발을 위한 플랫폼으로, 개발자들이 쉽게 데이터베이스, 인증, 스토리지 등을 구축하고 관리할 수 있도록 도와줍니다. 이번에는 Firebase의 `firebase_core` 패키지를 사용하여 플러터 앱에서 인증(Authentication)을 관리하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 생성 및 구성

1. Firebase 콘솔에 접속하여 새로운 프로젝트를 생성합니다.
2. 생성된 프로젝트의 설정 페이지에 들어가서, **앱** 섹션에서 "Android"나 "iOS" 앱을 추가합니다.
3. 각 플랫폼에 대한 패키지 이름과 SHA-1 또는 Bundle Identifier를 입력하고, 각 플랫폼에 대한 구성 파일을 다운로드 받습니다.

## 2. Flutter 프로젝트에 Firebase_core 패키지 추가

1. Flutter 프로젝트의 `pubspec.yaml` 파일을 엽니다.
2. `dependencies` 섹션에 `firebase_core` 패키지를 추가합니다.
   ```yaml
   dependencies:
     firebase_core: ^0.7.0
   ```

3. 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드 받습니다.

## 3. Firebase 인증 설정

1. 프로젝트의 `lib` 폴더에 `firebase_auth.dart` 파일을 생성합니다.
2. 다음 코드를 `firebase_auth.dart` 파일에 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';

class FirebaseAuthService {
  // Firebase 초기화
  static Future<FirebaseApp> initializeFirebase() async {
    return await Firebase.initializeApp();
  }

  // 이메일/비밀번호로 회원가입
  static Future<String> signUpWithEmailAndPassword(
      String email, String password) async {
    try {
      await FirebaseAuth.instance
          .createUserWithEmailAndPassword(email: email, password: password);
      return "회원가입이 완료되었습니다.";
    } catch (e) {
      return e.toString();
    }
  }

  // 이메일/비밀번호로 로그인
  static Future<String> signInWithEmailAndPassword(
      String email, String password) async {
    try {
      await FirebaseAuth.instance
          .signInWithEmailAndPassword(email: email, password: password);
      return "로그인 되었습니다.";
    } catch (e) {
      return e.toString();
    }
  }

  // 로그아웃
  static Future<void> signOut() async {
    await FirebaseAuth.instance.signOut();
  }

  // 로그인 여부 확인
  static bool isSignedIn() {
    return FirebaseAuth.instance.currentUser != null;
  }
}
```

## 4. 인증 기능 사용하기

1. `main.dart` 파일에서 Firebase 초기화 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
// ...

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(); // Firebase 초기화
  runApp(MyApp());
}
```

2. 로그인 페이지를 생성하고, `firebase_auth.dart`에서 정의한 메서드를 호출하여 인증 기능을 사용합니다.

```dart
import 'package:flutter/material.dart';
import 'firebase_auth.dart';

class LoginPage extends StatelessWidget {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('로그인'),
      ),
      body: Column(
        children: [
          TextField(
            controller: _emailController,
            decoration: InputDecoration(
              labelText: '이메일',
            ),
          ),
          TextField(
            controller: _passwordController,
            obscureText: true,
            decoration: InputDecoration(
              labelText: '비밀번호',
            ),
          ),
          ElevatedButton(
            onPressed: () async {
              String email = _emailController.text.trim();
              String password = _passwordController.text.trim();
              String result = await FirebaseAuthService.signInWithEmailAndPassword(
                  email, password); // 로그인
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text(result)),
              );
            },
            child: Text('로그인'),
          ),
        ],
      ),
    );
  }
}
```

이렇게하면 Firebase의 `firebase_core` 패키지를 사용하여 플러터 앱에서 인증을 관리할 수 있습니다. 회원가입, 로그인, 로그아웃 등의 기능을 위해 `firebase_auth` 패키지와 함께 사용할 수 있습니다. Firebase의 다른 기능들도 `firebase_core`와 함께 사용하여 효율적으로 개발할 수 있습니다.

더 자세한 정보는 [Firebase 공식 문서](https://firebase.flutter.dev/)를 참고하시기 바랍니다.