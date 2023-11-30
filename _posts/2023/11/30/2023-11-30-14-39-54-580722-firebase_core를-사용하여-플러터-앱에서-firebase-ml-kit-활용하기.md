---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase ML Kit 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 Google이 제공하는 클라우드 기반 개발 플랫폼으로, 다양한 기능을 제공하고 있습니다. Firebase ML Kit는 Firebase의 일부로 제공되는 머신 러닝 기능을 활용할 수 있는 도구입니다. 이 기능은 이미지, 텍스트, 얼굴 등을 인식하고 분석하는 데 사용될 수 있습니다.

이번 블로그 포스트에서는 Flutter 앱에서 Firebase의 ML Kit 기능을 활용하기 위해 Firebase_core 패키지를 사용하는 방법에 대해 알아보겠습니다.

## Firebase_core 패키지 추가하기

Firebase ML Kit를 사용하기 위해서는 먼저 Firebase_core 패키지를 프로젝트에 추가해야 합니다. `pubspec.yaml` 파일에서 dependencies 섹션에 아래와 같이 추가해주세요.

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.10.0
  firebase_ml_vision: ^1.1.0
```

이후 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 다운로드합니다.

## Firebase 설정하기

Firebase ML Kit를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성하고 설정해야 합니다. Firebase 콘솔에서 새로운 프로젝트를 생성하고, 앱을 추가합니다. Flutter 앱의 패키지 이름을 입력하고, 다운로드된 `google-services.json` 파일을 프로젝트의 `android/app` 폴더에 추가해주세요.

이후 `main.dart` 파일에서 Firebase_core를 초기화하는 코드를 추가해야 합니다. 아래 코드를 `main()` 함수의 첫 번째 줄에 추가하세요.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

## ML Kit 기능 사용하기

Firebase ML Kit에는 다양한 기능이 있지만, 이번 포스트에서는 이미지 라벨링 기능을 사용해보겠습니다. ML Kit의 이미지 라벨링은 이미지에 포함된 여러 가지 개체 또는 물체에 대한 라벨을 제공합니다.

아래 코드는 이미지 라벨링 기능을 사용하여 이미지에 포함된 물체의 라벨을 출력하는 예제입니다.

```dart
import 'package:firebase_ml_vision/firebase_ml_vision.dart';

Future<List<String>> detectLabels(String imagePath) async {
  final File imageFile = File(imagePath);
  final FirebaseVisionImage visionImage = FirebaseVisionImage.fromFile(imageFile);
  final ImageLabeler labeler = FirebaseVision.instance.imageLabeler();
  
  final List<ImageLabel> labels = await labeler.processImage(visionImage);
  
  List<String> labelList = [];
  for (ImageLabel label in labels) {
    labelList.add(label.text);
  }
  
  return labelList;
}
```

위 코드를 사용하여, 이미지 파일의 경로를 전달하면 해당 이미지에 있는 라벨이 리스트로 반환됩니다. 이제 앱에서 이 함수를 호출하여 이미지 라벨링을 수행할 수 있습니다.

## 결론

이번 포스트에서는 Firebase_core 패키지를 사용하여 Flutter 앱에서 Firebase ML Kit을 활용하는 방법에 대해 알아보았습니다. Firebase의 다양한 기능을 활용하면 플러터 앱에 강력한 머신 러닝 기능을 추가할 수 있습니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/ml-kit)를 참고하시기 바랍니다.