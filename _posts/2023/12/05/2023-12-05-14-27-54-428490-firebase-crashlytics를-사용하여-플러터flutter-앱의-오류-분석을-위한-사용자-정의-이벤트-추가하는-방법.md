---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류 분석을 위한 사용자 정의 이벤트 추가하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 플러터(Flutter) 앱의 오류를 신속하게 분석하고 추적하는 데 도움을 주는 도구입니다. 이 도구를 사용하면 앱에 발생한 오류와 관련된 디버그 정보를 수집하고 분석하여 앱의 안정성과 신뢰성을 향상시킬 수 있습니다. 이제 Firebase Crashlytics를 사용하여 플러터 앱에 사용자 정의 이벤트를 추가해보겠습니다.

## 1. Firebase Crashlytics 설정

먼저, Firebase Crashlytics를 사용하기 위해 Firebase 프로젝트에 앱을 추가하고 Firebase SDK를 설정해야 합니다. Firebase Console에서 프로젝트를 생성하고, 플러터 앱의 `pubspec.yaml` 파일에 Firebase Crashlytics의 의존성을 추가합니다.

```yaml
dependencies:
  firebase_core: ^1.0.0
  firebase_crashlytics: ^2.2.0
```

그리고 Firebase Crashlytics를 초기화하는 코드를 앱의 `main.dart` 파일에 추가합니다. 

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  FlutterError.onError = FirebaseCrashlytics.instance.recordFlutterError;
  
  // ...
  
  runApp(MyApp());
}
```

## 2. 사용자 정의 이벤트 추가

Firebase Crashlytics에 사용자 정의 이벤트를 추가하기 위해서는 `FirebaseCrashlytics` 클래스의 `log` 메서드를 사용해야 합니다. 예를 들어, 앱에서 사용자가 특정 버튼을 클릭한 경우를 추적하고 싶다면 다음과 같이 코드를 작성할 수 있습니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void trackButtonClickEvent() {
  FirebaseCrashlytics.instance.log('Button Clicked');
  
  // Additional custom event code...
}
```

위의 예제 코드에서 `log` 메서드를 사용하여 'Button Clicked'라는 사용자 정의 이벤트를 Firebase Crashlytics에 로깅하고 있습니다. 이러한 사용자 정의 이벤트는 Firebase Crashlytics 대시보드에서 확인할 수 있습니다.

또한, `log` 메서드 외에도 `setCustomKey` 메서드를 사용하여 사용자 정의 키와 값을 설정할 수도 있습니다. 이를 통해 추가적인 디버그 정보를 수집하고 분석할 수 있습니다.

```dart
FirebaseCrashlytics.instance.setCustomKey('User ID', '123456');
FirebaseCrashlytics.instance.setCustomKey('Locale', 'en_US');
```

이제 위의 예제를 참고하여 플러터 앱에 필요한 사용자 정의 이벤트를 추가해보세요. Firebase Crashlytics를 통해 발생한 오류와 함께 사용자 행동에 대한 정보를 수집하여 앱의 안정성을 향상시킬 수 있습니다.

## 결론

Firebase Crashlytics를 사용하여 플러터 앱에 사용자 정의 이벤트를 추가하는 방법을 살펴보았습니다. 이를 통해 앱의 오류 분석과 디버깅을 보다 간편하게 할 수 있습니다. Firebase Crashlytics를 적극적으로 활용하여 앱의 품질과 안정성을 개선해보세요.

## 참고자료
- [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)
- [Firebase 플러그인 공식 문서](https://pub.dev/packages/firebase_crashlytics)