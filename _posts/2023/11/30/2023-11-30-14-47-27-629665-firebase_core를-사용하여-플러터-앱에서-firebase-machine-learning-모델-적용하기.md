---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Machine Learning 모델 적용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google의 클라우드 기반 통합 개발 플랫폼으로, 앱 개발자들이 앱을 더욱 효과적으로 개발하고 운영할 수 있도록 도와줍니다. Firebase에는 여러가지 기능들이 포함되어 있는데, 그 중 Firebase Machine Learning은 앱에 머신러닝 기반의 기능을 쉽게 적용할 수 있는 기능입니다.

여기서는 Flutter 앱에서 Firebase Machine Learning 모델을 적용하는 방법을 알아보겠습니다. Firebase_core 패키지를 사용하여 Firebase를 초기화하고, Firebase Machine Learning 모델을 로드하여 앱에서 사용하는 방법을 다룰 것입니다.

## 1. Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새 프로젝트를 만듭니다.
2. 프로젝트 설정에서 "프로젝트 설정"을 선택하고, Android 앱을 추가합니다.
3. 패키지 이름과 SHA-1 인증서 지문을 입력하고, 앱을 등록합니다.
4. 구성 파일(google-services.json)을 다운로드하여 안드로이드 앱의 `android/app` 폴더에 추가합니다.

## 2. 프로젝트에 Firebase_core 패키지 추가

1. `pubspec.yaml` 파일에 아래와 같이 `firebase_core` 패키지를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

2. 패키지를 적용하기 위해 터미널에서 `flutter pub get` 명령어를 실행합니다.

## 3. Firebase 초기화

1. Firebase 초기화는 앱이 시작될 때 수행되어야 합니다. 앱의 `main.dart` 파일에서 `main` 함수를 수정하여 Firebase를 초기화합니다:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## 4. Firebase Machine Learning 모델 적용

Firebase Machine Learning은 클라이언트 측에서 모델을 로드할 수 있도록 지원합니다. 예를 들어, 간단한 이미지 분류 앱을 만들어보겠습니다.

1. Firebase 콘솔에서 "ML Kit"을 선택하고 "모델 콘솔"로 이동합니다.
2. "새 모델"을 선택하고, 모델을 업로드하거나 Firebase에서 제공하는 사전 훈련된 모델을 사용합니다.
3. 모델을 업로드하면 모델 ID가 생성됩니다.

```dart
import 'package:firebase_ml_custom/firebase_ml_custom.dart';

FirebaseModelManager modelManager = FirebaseModelManager.instance;

// 모델 로드 및 사용 예시
FirebaseModelInterpreterInterpreter firebaseInterpreter;
FirebaseModelManagerDownloadConditions downloadConditions =
  FirebaseModelManagerDownloadConditions(
    androidRequireWifi: true,
    androidRequireDeviceIdle: true,
);

void loadModel() async {
  FirebaseModelManager.modelManager().registerCloudModelSource(
    FirebaseCloudModelSource.Builder(modelName).build(),
  );

  final conditions = FirebaseModelManagerDownloadConditions();
  conditions?.androidRequireWifi = true;

  FirebaseModelManager.modelManager().downloadCloudModelIfNeeded(
    FirebaseCloudModelSource.Builder(modelName).build(),
    conditions: downloadConditions,
  );

  FirebaseModelInterpreterOptions options = FirebaseModelInterpreterOptionsBuilder(
    FirebaseModelManager.modelManager().cloudModelSourceByName(modelName),
  ).build();

  firebaseInterpreter = FirebaseModelInterpreter.getInstance(options);
}

void classifyImage() async {
  FirebaseModelInputOutputOptions inputOutputOptions =
    FirebaseModelInputOutputOptionsBuilder()
        .setInputFormat(0, FirebaseModelDataType.FLOAT32, List<int>.from([1, inputSize, inputSize, 3]))
        .setOutputFormat(0, FirebaseModelDataType.FLOAT32, List<int>.from([1, outputSize]))
        .build();

  String imagePath = "path/to/image.jpg";
  FirebaseModelInputOutputOptions interpreterResult =
    FirebaseModelInterpreter.run(
      firebaseInterpreter,
      <String, dynamic>{
        'data': _preprocessImage(imagePath),
      },
      inputOutputOptions,
    );

  final List response = interpreterResult.getOutput<List>(0);
  // 분류 결과 사용
}

Uint8List _preprocessImage(String imagePath) {
  // 이미지 전처리 작업 수행
  // 예시: 이미지를 모델 입력 형식으로 변환하여 반환
}
```

위의 예제에서는 FirebaseModelInterpreter 객체를 생성하여 Firebase로부터 모델을 로드하고, 이미지 분류를 위한 전처리 작업 및 결과를 가져오는 방법을 보여줍니다.

Firebase와 Flutter를 통합하여 앱에 머신러닝 기능을 추가하는 방법을 알아보았습니다. 위의 단계대로 따라하면 Firebase Machine Learning 모델을 효과적으로 적용할 수 있을 것입니다.

더 많은 정보를 원하시면 [Firebase 공식 문서](https://firebase.google.com/docs/ml-kit/)를 참조하십시오.