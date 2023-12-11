---
layout: post
title: "[flutter] flutter_localizations 패키지와 Firebase ML Kit 연동 방법"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

이번 포스팅에서는 Flutter 앱에서 다국어 지원을 위해 `flutter_localizations` 패키지를 사용하고, Firebase ML Kit를 통해 이미지 번역 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. flutter_localizations 패키지를 통한 다국어 지원

먼저, `flutter_localizations` 패키지를 사용하여 Flutter 앱에서의 다국어 지원을 구현해보겠습니다.

### 설치

`pubspec.yaml` 파일에 다음과 같이 `flutter_localizations` 패키지를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
```

그런 다음 터미널에서 다음 명령어를 실행하여 패키지를 설치합니다.

```sh
flutter pub get
```

### 사용

다국어 지원을 위해 앱의 `main.dart` 파일에서 다음과 같이 `MaterialApp` 위젯에 `localizationsDelegates`와 `supportedLocales`을 설정합니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      localizationsDelegates: [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: AppLocalizations.supportedLocales,
      home: MyHomePage(),
    );
  }
}
```

## 2. Firebase ML Kit 이미지 번역 연동

이제 Firebase ML Kit를 사용하여 이미지 번역 기능을 구현해보겠습니다.

### 프로젝트 설정

먼저, Firebase 콘솔에서 프로젝트를 생성하고, ML Kit를 활성화합니다. 그런 다음, 해당 프로젝트의 `google-services.json` 파일을 Flutter 프로젝트에 추가합니다.

### ML Kit 플러그인 추가

`pubspec.yaml` 파일에 ML Kit 플러그인을 추가합니다.

```yaml
dependencies:
  firebase_ml_vision: ^0.9.8
```

그런 다음 터미널에서 다음 명령어를 실행하여 패키지를 설치합니다.

```sh
flutter pub get
```

### 이미지 번역 구현

이미지 번역을 위한 코드 예시는 다음과 같습니다.

```dart
import 'package:firebase_ml_vision/firebase_ml_vision.dart';

Future<String> translateImage(MLImage image) async {
  final TextRecognizer recognizer = FirebaseVision.instance.textRecognizer();
  final VisionText visionText = await recognizer.processImage(image);

  // 번역 로직 구현

  return translatedText;
}
```

위 코드에서 ML Kit를 사용하여 이미지에서 텍스트를 추출하고, 추출된 텍스트를 번역하는 로직을 구현할 수 있습니다.

이제 위에서 살펴본 내용을 기반으로 Flutter 앱에서 `flutter_localizations` 패키지를 사용하여 다국어 지원을 하고, Firebase ML Kit를 통해 이미지 번역 기능을 구현해 볼 수 있습니다.

더 자세한 내용은 [Flutter 도큐먼트](https://flutter.dev/docs) 및 [Firebase ML Kit 도큐먼트](https://firebase.google.com/docs/ml-kit)를 참고하시기 바랍니다.