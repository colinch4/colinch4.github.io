---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Cloud Storage 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

## 소개
Firebase는 Google이 제공하는 개발 플랫폼으로, 다양한 서비스와 기능을 제공합니다. 그 중 하나인 Firebase Cloud Storage는 앱에서 파일을 저장하고 검색할 수 있는 클라우드 스토리지 서비스입니다. 이번에는 플러터 앱에서 Firebase Cloud Storage를 사용하는 방법에 대해 알아보겠습니다.

## 선행 작업
Firebase Cloud Storage를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성하고 Firebase Core 패키지를 설치해야 합니다. Firebase 프로젝트를 생성하는 방법은 Firebase 콘솔에서 쉽게 수행할 수 있습니다. 또한 Firebase Core 패키지는 `pubspec.yaml` 파일에 추가하여 설치할 수 있습니다.

## Firebase Core 설정
Firebase Core는 Firebase 프로젝트의 초기화에 사용되는 패키지입니다. 다음과 같이 `pubspec.yaml` 파일에 Firebase Core 패키지를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.11.0
```

이후 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

## Cloud Storage 연결
Firebase Core를 사용하여 Firebase Cloud Storage에 연결하는 방법은 간단합니다. 다음과 같이 Firebase Core를 초기화하고 Cloud Storage 인스턴스를 가져오는 코드를 작성합니다.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_storage/firebase_storage.dart';

class MyStorageService {
  FirebaseStorage _storageInstance;

  Future<void> initialize() async {
    await Firebase.initializeApp();
    _storageInstance = FirebaseStorage.instance;
  }
}
```

위 코드에서 `initialize()` 메소드를 호출하여 Firebase Core를 초기화합니다. 이후 `_storageInstance` 변수를 사용하여 Firebase Cloud Storage 인스턴스에 접근할 수 있습니다.

## 파일 업로드
Firebase Cloud Storage를 사용하여 파일을 업로드하는 방법은 다음과 같습니다.

```dart
import 'dart:io';
import 'package:firebase_storage/firebase_storage.dart';

class MyStorageService {
  FirebaseStorage _storageInstance;

  Future<String> uploadFile(String filePath) async {
    File file = File(filePath);
    String fileName = file.path.split('/').last;
    Reference ref = _storageInstance.ref().child(fileName);
    UploadTask uploadTask = ref.putFile(file);
    TaskSnapshot snapshot = await uploadTask;
    String downloadUrl = await snapshot.ref.getDownloadURL();
  
    return downloadUrl;
  }
}
```

위 코드에서 `uploadFile()` 메소드는 로컬 파일의 경로를 인자로 받아서 해당 파일을 Firebase Cloud Storage에 업로드합니다. 업로드된 파일의 다운로드 URL을 반환합니다.

## 파일 다운로드
Firebase Cloud Storage에서 파일을 다운로드하는 방법은 다음과 같습니다.

```dart
import 'package:firebase_storage/firebase_storage.dart';

class MyStorageService {
  FirebaseStorage _storageInstance;

  Future<void> downloadFile(String fileName) async {
    Reference ref = _storageInstance.ref().child(fileName);
    String filePath = '/path/to/save/file.jpg';
    File file = File(filePath);
    await ref.getFile(file);
  }
}
```

위 코드에서 `downloadFile()` 메소드는 다운로드할 파일의 이름을 인자로 받아서 해당 파일을 Firebase Cloud Storage에서 다운로드하여 로컬 파일 시스템에 저장합니다.

## 결론
이제 Firebase Core와 Firebase Cloud Storage를 사용하여 플러터 앱에서 파일을 업로드하고 다운로드할 수 있습니다. Firebase Cloud Storage의 다양한 기능을 활용하여 앱에 파일 관리 기능을 추가해 보세요.

## 참고 자료
- [Firebase 콘솔](https://console.firebase.google.com/)
- [Firebase Core 패키지](https://pub.dev/packages/firebase_core)
- [Firebase Storage 패키지](https://pub.dev/packages/firebase_storage)