---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Predictions API 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google의 모든 개발자 도구와 서비스를 통합하는 플랫폼으로, Firebase의 Predictions API를 사용하면 사용자 동작 및 패턴을 예측하여 개인화된 앱 경험을 제공할 수 있습니다. 이번 포스트에서는 Flutter 앱에서 Firebase의 Predictions API를 활용하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하고 프로젝트를 생성합니다.
2. 앱을 추가하고, Flutter 앱의 패키지 이름을 입력합니다.
3. Firebase 설정 파일(`google-services.json`)을 다운로드하고, 프로젝트의 `android/app` 디렉토리에 추가합니다.

## 프로젝트에 필요한 패키지 추가하기

`pubspec.yaml` 파일에 아래의 의존성을 추가합니다.

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^0.8.0
  firebase_ml_custom: ^0.1.2
```

의존성을 추가한 후, `flutter pub get` 명령어를 실행하여 패키지를 가져옵니다.

## Firebase_core 초기화하기

Firebase_core 패키지를 사용하여 Firebase를 초기화합니다. 앱이 시작될 때 Firebase 설정을 로드하고 Firebase 서비스에 연결됩니다.

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 모델 가져오기

Firebase Predictions API는 Firebase ML Custom 모델을 사용합니다. 먼저, Firebase 콘솔에서 ML 모델을 업로드하고 모델 이름(예: `my_model`)을 확인하세요.

## Predictions API 호출하기

```dart
import 'package:firebase_ml_custom/firebase_ml_custom.dart';

Future<void> makePrediction() async {
  final FirebaseModelManager modelManager = FirebaseModelManager.instance;
  final FirebaseModelDetails modelDetails = await modelManager.downloadRemoteModelIfNeeded('my_model');

  final inputs = {'input': 'some_input_data'};
  final customModelInput = FirebaseCustomRemoteModelInput(remoteModelName: 'my_model', inputTensorMap: inputs);

  final options = FirebaseCustomRemoteModelOptions(firebaseModelOptions: FirebaseModelDownloadConditions());
  final FirebaseModelInterpreter modelInterpreter = FirebaseModelInterpreter.instance;

  final List<FirebaseCustomRemoteModelOutput> results = await modelInterpreter.runRemoteModel(customModelInput, options);

  // 결과 처리하기
  for (final output in results) {
    final outputData = output.outputTensorMap['output'];
    final outputResult = outputData.data;
    // 결과를 사용하여 앱 작업 수행
  }
}
```

Firebase Predictions API를 호출하려면 FirebaseModelManager, FirebaseCustomRemoteModelInput, FirebaseCustomRemoteModelOptions, FirebaseModelInterpreter 등의 클래스를 사용해야 합니다. 위의 코드 예제에서 `makePrediction` 함수는 모델을 다운로드하고, 입력을 설정하고, 결과를 얻는 과정을 보여줍니다.

이제 Flutter 앱에서 Firebase의 Predictions API를 활용할 수 있습니다. Firebase Predictions API를 사용하면 사용자의 동작 및 패턴을 예측하여 개인화된 앱 경험을 제공할 수 있습니다. 더 자세한 내용은 [Firebase Predictions API 문서](https://firebase.google.com/docs/predictions)를 참고하세요.

## 참고 자료
- [Firebase 공식 문서 - Flutter용 Firebase 설치](https://firebase.google.com/docs/flutter/setup?platform=android)
- [Firebase 공식 문서 - Predictions API 개요](https://firebase.google.com/docs/predictions)