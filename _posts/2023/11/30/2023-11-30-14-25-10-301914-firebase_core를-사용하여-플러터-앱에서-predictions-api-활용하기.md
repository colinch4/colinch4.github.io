---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Predictions API 활용하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase는 구글에서 제공하는 모바일 및 웹 앱 개발 플랫폼으로, 다양한 기능과 서비스를 제공합니다. Firebase의 Predictions API는 머신 러닝을 기반으로 한 예측 기능을 제공하여 앱의 성능을 향상시킬 수 있습니다.

이번 포스트에서는 Flutter에서 Firebase_predicitons API를 사용하여 예측 기능을 구현하는 방법을 알아보겠습니다.

## 1. Firebase 설정

먼저, Firebase console에서 프로젝트를 생성하고 Firebase SDK를 설치해야 합니다. Firebase console에 접속하여 프로젝트를 생성한 후 Flutter 앱을 추가합니다. 

Firebase SDK를 설치하기 위해 `firebase_core` 패키지를 `pubspec.yaml` 파일에 추가합니다. 

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^1.0.0
```

SDK를 설치한 후 Firebase 프로젝트의 구성 파일(`google-services.json` 또는 `GoogleService-Info.plist`)을 Flutter 프로젝트의 최상위 수준에 추가합니다.

## 2. Firebase Predictions 설정

Firebase console에서 Predictions 기능을 활성화해야 합니다. Firebase console의 'Predictions' 섹션으로 이동하여 'Predictions API'를 활성화합니다. 이 단계를 거치면 Firebase SDK는 앱에 Predictions API를 사용할 수 있도록 구성됩니다.

## 3. Predictions API 구현

Flutter 앱에서 Predictions API를 사용하기 위해 `firebase_core` 패키지를 초기화해야 합니다. 이를 위해 `main.dart` 파일에 아래와 같이 초기화 코드를 추가합니다.

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

Firebase 초기화 코드를 추가한 후 `PredictionApiClient` 클래스를 생성하여 Predictions API를 호출할 수 있습니다. `PredictionApiClient`는 앱에서 예측 기능을 호출하는 데 사용됩니다. 

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

class PredictionApiClient {
  static const String apiKey = 'YOUR_API_KEY'; // Firebase console에서 API_KEY를 얻어옵니다.

  Future<String> getPrediction(String input) async {
    final url = 'https://firebaseml.googleapis.com/v1beta1/projects/YOUR_PROJECT_ID/modes/YOUR_MODEL_ID:predict?key=$apiKey';

    final response = await http.post(Uri.parse(url),
        headers: {'Content-Type': 'application/json',},
        body: jsonEncode(<String, String>{'text': input}));

    if (response.statusCode == 200) {
      final jsonString = response.body;
      final predictions = jsonDecode(jsonString);
      return predictions['label'];
    } else {
      throw Exception('Failed to predict!');
    }
  }
}
```

위의 코드에서 `apiKey`에는 Firebase console에서 얻은 API 키를 입력해야 합니다. 또한 `url`에서 `YOUR_PROJECT_ID`와 `YOUR_MODEL_ID`를 프로젝트 및 모델 아이디로 교체해야 합니다.

마지막으로, 원하는 화면에서 `PredictionApiClient`를 사용하여 예측을 수행할 수 있습니다.

```dart
final client = PredictionApiClient();

String predictionResult;

void performPrediction(String input) async {
  try {
    predictionResult = await client.getPrediction(input);
  } catch (e) {
    print(e);
  }
}

performPrediction('Hello Firebase Predictions');
print(predictionResult);
```

위의 코드에서 `performPrediction` 메서드를 호출하여 입력값에 대한 예측을 수행합니다. 예측 결과는 `predictionResult` 변수에 저장됩니다.

## 결론

이번 포스트에서는 Flutter에서 Firebase Predictions API를 사용하여 예측 기능을 구현하는 방법을 알아보았습니다. Firebase_predicitons API를 사용하면 앱의 성능을 향상시키고 사용자에게 더 나은 경험을 제공할 수 있습니다. 

더 자세한 정보는 [Firebase Predictions API 문서](https://firebase.google.com/docs/predictions)를 참고하시기 바랍니다.