---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션 내 회원 가입 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

1. **의존성 추가**: 
   먼저, Flutter 프로젝트의 `pubspec.yaml` 파일에 다음과 같이 `flutter_spinkit` 패키지를 추가합니다. 

   ```yaml
   dependencies:
     flutter_spinkit: ^5.0.0
   ```

2. **패키지 가져오기**:
   그런 다음, 해당 패키지를 가져와야 합니다.

   ```dart
   import 'package:flutter_spinkit/flutter_spinkit.dart';
   ```

3. **CircularProgressIndicator 표시**:
   이제 CircularProgressIndicator를 사용하여 회원 가입 상태를 표시할 수 있습니다. 예를 들어, 회원 가입 버튼을 눌렀을 때 CircularProgressIndicator를 표시하고, 회원 가입이 완료되면 CircularProgressIndicator를 숨기는 방법은 다음과 같습니다.

   ```dart
   bool _isSigningUp = false;

   Widget build(BuildContext context) {
     return _isSigningUp
         ? SpinKitCircle(color: Colors.blue)  // 회원가입 진행 중에만 표시
         : ElevatedButton(
             onPressed: () async {
               setState(() {
                 _isSigningUp = true;  // 회원 가입 시작 시 CircularProgressIndicator 표시
               });
               // 회원 가입 로직 수행
               await _signUp();
               setState(() {
                 _isSigningUp = false; // 회원 가입 완료 시 CircularProgressIndicator 숨김
               });
             },
             child: Text('회원 가입'),
           );
   }
   ```

위의 예제에서 `SpinKitCircle`는 회원 가입이 진행 중일 때 표시되는 CircularProgressIndicator입니다. `_isSigningUp` 변수는 현재 회원 가입 상태를 나타내며, 회원 가입 버튼을 눌렀을 때 `true`로 설정되어 CircularProgressIndicator가 표시됩니다. 회원 가입이 완료되면 다시 `false`로 설정되어 CircularProgressIndicator가 숨겨집니다.

이와 같이 CircularProgressIndicator를 활용하여 애플리케이션 내 회원 가입 상태를 표시할 수 있습니다.