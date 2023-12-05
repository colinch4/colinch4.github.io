---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류와 충돌을 실시간으로 모니터링하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 모바일 앱을 개발하기 위한 인기있는 프레임워크입니다. 개발자들은 플러터를 사용하여 크로스 플랫폼 앱을 만들 수 있고, 빠른 개발과 효율적인 성능을 경험할 수 있습니다. 그러나 앱을 출시한 후에도 오류와 충돌은 불가피한 일입니다. 이러한 문제를 실시간으로 모니터링하고 해결하기 위해 Firebase Crashlytics를 사용할 수 있습니다.

Firebase Crashlytics는 구글이 개발한 강력한 오류 보고 및 모니터링 도구로, 앱에서 발생한 오류 및 충돌 정보를 실시간으로 수집하여 개발자에게 전달하는 기능을 제공합니다. 이를 통해 개발자는 앱 사용자들이 겪는 문제를 빠르게 파악하고, 개선하기 위한 조치를 취할 수 있습니다.

## Firebase 프로젝트 생성하기

Firebase Crashlytics를 통합하기 위해 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔에 접속하여 프로젝트를 생성한 후, 프로젝트 설정에서 앱을 추가해야 합니다. 여기서는 Android 앱을 추가하는 예를 들겠습니다.

1. Firebase 콘솔에 접속하여 프로젝트를 생성합니다.
2. 프로젝트 설정으로 이동한 다음, "앱 추가" 버튼을 클릭합니다.
3. 패키지 이름과 앱 닉네임을 입력하고, "앱 등록" 버튼을 클릭합니다.
4. 다운로드한 구성 파일(`google-services.json`)을 프로젝트의 `android/app` 디렉터리에 복사합니다.

## Flutter 앱에 Firebase Crashlytics 통합하기

Firebase 프로젝트를 만들고 구성 파일을 플러터 프로젝트에 추가한 후, 이제 Firebase Crashlytics를 통합해보겠습니다.

1. `pubspec.yaml` 파일을 열고 `firebase_crashlytics` 패키지를 추가합니다:

```yaml
dependencies:
  flutter:
    sdk: flutter
  firebase_crashlytics: ^2.0.0
```

2. 패키지를 가져올 때, 별칭을 지정하여 사용하도록 `main.dart` 파일의 상단에 다음과 같이 수정합니다:

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart' as crashlytics;
```

3. Firebase Crashlytics를 초기화하고 활성화하는 코드를 `main()` 함수에 추가합니다:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp();
  crashlytics.FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);

  FlutterError.onError = crashlytics.FirebaseCrashlytics.instance.recordFlutterError;

  runZonedGuarded<Future<void>>(() async {
    runApp(MyApp());
  }, (error, stackTrace) {
    crashlytics.FirebaseCrashlytics.instance.recordError(error, stackTrace);
  });
}
```

4. 앱에서 오류를 시뮬레이션할 수 있도록 다음 예제 코드를 추가합니다:

```dart
RaisedButton(
  onPressed: () {
    // Divide by zero to simulate an error
    int result = 10 ~/ 0;
  },
  child: Text('Trigger Crash'),
),
```

5. 앱을 실행하고 'Trigger Crash' 버튼을 누르면 오류가 발생하고 Firebase Crashlytics에 보고됩니다.

## Firebase 콘솔에서 오류 확인하기

Firebase 콘솔에서 실시간으로 앱의 오류 및 충돌 정보를 모니터링할 수 있습니다. Firebase 콘솔에서 Crashlytics 섹션으로 이동하면, 오류 발생 로그와 해당 디바이스 정보를 확인할 수 있습니다. 이 정보를 활용하여 앱의 문제를 신속하게 해결할 수 있습니다.

## 결론

Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류와 충돌을 실시간으로 모니터링하는 방법을 알아보았습니다. Firebase Crashlytics는 앱의 안정성을 개선하고 사용자 경험을 향상시키는데 도움을 줄 수 있는 강력한 도구입니다. 개발자는 오류를 신속하게 파악하고 해결함으로써, 사용자들에게 더 나은 앱을 제공할 수 있습니다.

더 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참조하십시오.