---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase ML Kit 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 개발자들이 애플리케이션을 구축하고 운영하기 위한 많은 기능을 제공하는 플랫폼입니다. Firebase ML Kit은 Firebase의 일부로 제공되며, 기계 학습을 사용하여 앱에 AI 기능을 추가할 수 있습니다. 이 기능은 이미지, 비디오 또는 텍스트와 같은 여러 유형의 데이터를 처리하고 분석할 수 있습니다.

Firebase ML Kit의 사용에는 몇 가지 단계가 필요합니다. 먼저 Firebase 콘솔에서 프로젝트를 생성하고 Firebase ML Kit를 활성화해야 합니다. 그런 다음 Flutter 앱에서 Firebase SDK를 설정해야 합니다. 이제 Firebase ML Kit를 사용하여 Flutter 앱에서 이미지 분류를 수행하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 생성 및 설정

Firebase 콘솔에 로그인한 후 프로젝트를 생성합니다. 프로젝트 이름을 지정하고 앱의 패키지 이름을 입력해야 합니다. Firebase가 생성하는 구성 파일을 다운로드하고 프로젝트 설정 페이지에서 Firebase SDK의 구성을 복사합니다.

## Flutter 앱에 Firebase SDK 추가

Flutter 앱에 Firebase를 사용하기 위해 `firebase_core` 패키지를 추가해야 합니다. `pubspec.yaml` 파일을 열어 의존성 섹션에 다음 코드를 추가합니다:

```dart
dependencies:
  firebase_core: ^1.0.0
```

의존성 추가 후 터미널에서 `flutter packages get` 명령어를 실행하여 패키지를 다운로드합니다.

## Firebase ML Kit API 키 가져오기

Firebase ML Kit는 액세스 권한을 관리하기 위해 API 키를 사용합니다. Firebase 콘솔에서 프로젝트 설정 페이지로 이동하여 ML Kit API 키를 생성하고 복사합니다.

## Flutter 앱에 Firebase ML Kit 추가

Flutter 앱에서 Firebase ML Kit를 사용하기 위해 `firebase_ml_vision` 패키지를 추가해야 합니다. `pubspec.yaml` 파일을 열어 의존성 섹션에 다음 코드를 추가합니다:

```dart
dependencies:
  firebase_ml_vision: ^0.11.0
```

의존성 추가 후 터미널에서 `flutter packages get` 명령어를 실행하여 패키지를 다운로드합니다.

## Flutter 앱에서 이미지 분류 수행

이제 Flutter 앱에서 Firebase ML Kit를 사용하여 이미지 분류를 수행할 준비가 되었습니다. 먼저 Firebase 초기화 코드를 작성하여 Firebase SDK를 설정합니다. `main.dart` 파일을 열고 `main` 함수 내에 다음 코드를 추가합니다:

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
}
```

이제 Firebase ML Kit 패키지를 사용하여 이미지 분류를 수행할 수 있습니다. 예를 들어, 앱이 메인 화면에서 사진을 촬영한 후 해당 사진을 Firebase ML Kit로 전송하여 고양이인지 강아지인지 판별해 보겠습니다.

```dart
import 'package:firebase_ml_vision/firebase_ml_vision.dart';

class MyImageClassifier {
  final ImageLabeler _imageLabeler = FirebaseVision.instance.imageLabeler();

  Future<List<ImageLabel>> classifyImage(File imageFile) async {
    final FirebaseVisionImage visionImage = FirebaseVisionImage.fromFile(imageFile);
    final List<ImageLabel> labels = await _imageLabeler.processImage(visionImage);
    return labels;
  }
}
```

이제 `classifyImage` 메소드를 호출하여 이미지를 분류할 수 있습니다. 이 메소드는 이미지 파일을 인자로 받고, 분류 결과를 반환하는 `List<ImageLabel>`을 비동기적으로 반환합니다.

## 결론

이제 Firebase ML Kit를 사용하여 플러터 앱에서 이미지 분류를 수행할 수 있게 되었습니다. Firebase ML Kit는 플러터와 함께 사용하기 매우 간편하며, 다양한 기계 학습 기능을 앱에 추가할 수 있습니다. Flutter에서 Firebase와 Firebase ML Kit를 사용하여 앱을 개발하면 더욱 흥미로운 AI 기능을 구현할 수 있습니다.

## 참고 자료

- [Firebase 공식 문서](https://firebase.google.com/docs)
- [Firebase Core 패키지](https://pub.dev/packages/firebase_core)
- [Firebase ML Vision 패키지](https://pub.dev/packages/firebase_ml_vision)