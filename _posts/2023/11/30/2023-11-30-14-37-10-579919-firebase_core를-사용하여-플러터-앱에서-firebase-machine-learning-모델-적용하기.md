---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Machine Learning 모델 적용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

## 개요
Firebase는 Google의 제공하는 개발 플랫폼으로, 다양한 기능과 서비스를 제공합니다. Firebase Machine Learning은 Firebase의 일부로, 기계 학습 모델을 구축하고 배포하기 위한 도구와 서비스를 제공합니다. 이번 블로그 포스트에서는 Firebase_core 패키지를 사용하여 플러터 앱에서 Firebase Machine Learning 모델을 적용하는 방법을 알아보겠습니다.

## 필수 사항
- Flutter 개발 환경이 설정되어 있어야 합니다.
- Firebase 프로젝트 및 Firebase Machine Learning 모델이 생성되어 있어야 합니다.

## Firebase 프로젝트 설정
Firebase 프로젝트에 Firebase Machine Learning 모델을 추가해야 합니다. Firebase 콘솔로 이동하여 "ML Kit" 섹션에서 "모델 관리"를 선택한 후, 모델을 추가합니다. 필요한 패키지(Integration)를 선택한 다음, "다음"을 클릭하여 모델 생성을 완료합니다.

## Firebase_core 패키지 추가
Firebase_core 패키지는 Firebase를 플러터 앱에 통합하는 데 사용됩니다. `pubspec.yaml` 파일에 다음과 같은 의존성을 추가하여 Firebase_core 패키지를 사용할 수 있습니다.

```dart
dependencies:
  firebase_core: ^1.0.4
```

의존성을 추가한 후 `flutter pub get` 명령어를 실행하여 패키지를 설치합니다.

## Firebase 초기화하기
Firebase_core 패키지는 앱 내에서 Firebase를 초기화하는 데 사용됩니다. Firebase 초기화를 위해 `main.dart` 파일을 열고 다음 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  await Firebase.initializeApp();

  runApp(MyApp());
}
```

Firebase 초기화를 위해 `Firebase.initializeApp()`를 호출하고 `await` 키워드를 사용하여 초기화가 완료될 때까지 대기합니다.

## Firebase Machine Learning 모델 사용하기
Firebase Machine Learning 모델을 사용하려면 `firebase_ml_custom.dart` 파일을 생성하고 다음의 코드를 추가합니다.

```dart
import 'package:firebase_ml_custom/firebase_ml_custom.dart';

class FirebaseMLModel {
  final FirebaseCustomRemoteModel remoteModel;

  FirebaseMLModel() : remoteModel = FirebaseCustomRemoteModel('your_model_name');

  Future<List<String>> classifyImage(String imagePath) async {
    final inputs = FirebaseModelInputs()
      ..addInput(FirebaseModelInput(outputName: 'predict_image', inputBytes: await imageToByteArray(imagePath)));

    final options = FirebaseModelOptions(
      remoteModelName: 'your_model_name',
      maxResults: 3,
    );

    final results = await FirebaseModelManager.instance.runRemoteModel(inputs, options);

    final List<PredictedClass> predictedClasses = results.map((result) => result.label).toList();

    return predictedClasses;
  }

  Future<List<double>> imageToByteArray(String imagePath) async {
    // 이미지를 바이트 배열로 변환하는 로직 작성하기
  }
}
```

위의 코드에서 `FirebaseCustomRemoteModel` 클래스는 Firebase Machine Learning 모델을 나타내며, `remoteModel` 필드를 통해 모델을 초기화합니다. 

`classifyImage` 메소드는 이미지를 입력받아 모델을 실행하고 결과를 반환합니다. `imageToByteArray` 메소드는 이미지를 바이트 배열로 변환하는 로직을 작성하면 됩니다.

## 결과 표시하기
앱에서 Firebase Machine Learning 모델을 사용하는 방법은 매우 다양하며, UI에 따라 다를 수 있습니다. 위에서 작성한 `FirebaseMLModel` 클래스를 통해 모델을 호출하고 결과를 받아온 다음, 적절한 방법으로 결과를 표시할 수 있습니다.

```dart
final model = FirebaseMLModel();
final results = await model.classifyImage('image_path.jpg');
```

위의 코드를 사용하여 Firebase Machine Learning 모델을 호출하고, `results` 변수에 결과를 저장합니다. 이후 받아온 결과를 UI에 표시하거나 다른 처리를 수행할 수 있습니다.

## 결론
이번 블로그 포스트에서는 Firebase_core 패키지를 사용하여 플러터 앱에서 Firebase Machine Learning 모델을 적용하는 방법을 알아보았습니다. Firebase_core를 초기화하고 Firebase Machine Learning 모델을 호출하는 방법에 대해 알아보았으며, 이를 통해 앱에 기계 학습 기능을 추가할 수 있습니다.

더 자세한 내용은 아래 참고 자료를 참고해주세요.

## 참고 자료
- [Flutter Documentation](https://flutter.dev/docs)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Firebase Machine Learning Documentation](https://firebase.google.com/docs/ml)