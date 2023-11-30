---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Cloud Storage 사용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google이 개발한 모바일 및 웹 앱 개발을 위한 플랫폼입니다. Firebase Cloud Storage는 Firebase의 기능 중 하나로, 클라우드에서 파일을 저장하고 관리하는 서비스입니다. 이번에는 Flutter 앱에서 Firebase Cloud Storage를 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정하기
Firebase Cloud Storage를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성하고 설정해야 합니다. Firebase 콘솔에 접속하여 새 프로젝트를 생성한 후, Firebase Cloud Storage를 활성화해주세요. Firebase 프로젝트 설정이 완료되면 해당 프로젝트와 연결된 키 파일을 다운로드 받아 안전한 곳에 보관해두세요.

## 2. Flutter 프로젝트에 Firebase_core 추가하기
Firebase Cloud Storage를 사용하기 위해서는 먼저 Firebase Core 패키지인 `firebase_core`를 Flutter 프로젝트에 추가해야 합니다. `pubspec.yaml` 파일에 다음과 같은 의존성을 추가해주세요.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

의존성을 추가한 후, 터미널에서 `flutter pub get` 명령어를 입력하여 패키지를 설치해주세요.

## 3. Firebase 앱 초기화하기
Firebase Cloud Storage를 사용하기 위해서는 Firebase 앱을 초기화해야 합니다. `main.dart` 파일에 다음과 같은 코드를 추가해주세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

`import 'package:firebase_core/firebase_core.dart';`를 통해 `firebase_core` 패키지를 가져온 후, `Firebase.initializeApp()`을 호출하여 Firebase 앱을 초기화해주세요.

## 4. Firebase Cloud Storage 사용하기
이제 Firebase Cloud Storage를 사용할 준비가 되었습니다. 예를 들어, 이미지 파일을 업로드하고 다운로드하는 기능을 추가하고 싶다면 다음과 같은 코드를 사용할 수 있습니다.

```dart
import 'package:firebase_storage/firebase_storage.dart';

final _storage = FirebaseStorage.instance;
File _image;
String _downloadURL;

Future<void> uploadImage() async {
  final String filePath = 'images/my_image.jpg';
  try {
    await _storage.ref(filePath).putFile(_image);
    _downloadURL = await _storage.ref(filePath).getDownloadURL();
  } catch (e) {
    print('Error: $e');
  }
}

Future<void> downloadImage(String downloadURL) async {
  try {
    await _storage.refFromURL(downloadURL).writeToFile(File('path/to/save/image.jpg'));
  } catch (e) {
    print('Error: $e');
  }
}
```

`firebase_storage` 패키지를 가져온 후 `_storage` 변수에 `FirebaseStorage.instance`를 할당합니다. `_image` 변수에 업로드할 이미지 파일을 설정하고, `uploadImage` 함수를 호출하면 해당 이미지 파일이 Cloud Storage에 업로드됩니다. `_downloadURL` 변수에는 업로드한 이미지 파일의 다운로드 URL이 할당됩니다.

`downloadImage` 함수를 호출하면 다운로드할 이미지 URL을 인자로 받고 해당 이미지 파일을 지정된 경로에 다운로드합니다.

## 결론
이제 Flutter 앱에서 Firebase Cloud Storage를 사용하는 방법에 대해 알아보았습니다. Firebase Core를 초기화하고, Firebase Cloud Storage를 사용하여 파일을 업로드 및 다운로드하는 기능을 구현할 수 있습니다. Firebase Cloud Storage의 다양한 기능을 활용하여 앱에 필요한 파일 관리 기능을 구현해보세요.

## 참고 자료
- [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup?platform=android)
- [Firebase Core 패키지](https://pub.dev/packages/firebase_core)
- [Firebase Cloud Storage 패키지](https://pub.dev/packages/firebase_storage)