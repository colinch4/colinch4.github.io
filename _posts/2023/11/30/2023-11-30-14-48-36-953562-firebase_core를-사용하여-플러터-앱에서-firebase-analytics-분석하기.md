---
layout: post
title: "[flutter] Firebase_core를 사용하여 플러터 앱에서 Firebase Analytics 분석하기"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

Firebase Analytics는 Firebase 앱 개발 플랫폼의 일부로서, 사용자 행동 및 앱의 성능에 대한 통계 및 분석 정보를 제공합니다. Flutter에서 Firebase Analytics를 사용하면 사용자의 행동을 추적하고 앱의 성능을 측정 및 개선할 수 있습니다.

## Firebase 프로젝트 설정

Firebase Analytics를 사용하려면 먼저 Firebase 프로젝트에서 앱을 설정해야 합니다. Firebase 콘솔로 이동하여 새 프로젝트를 만든 후, 앱을 추가하고 Firebase 구성 파일을 다운로드하세요. 다운로드한 파일을 프로젝트의 `android/app` 및 `ios/Runner` 폴더에 추가합니다.

## Firebase Analytics 패키지 설치

Firebase Analytics를 Flutter 앱에 통합하려면 `firebase_analytics` 패키지를 사용해야 합니다. `pubspec.yaml` 파일에 다음 의존성을 추가하세요:

```dart
dependencies:
  firebase_analytics: ^8.0.0-dev.14
```

그런 다음 터미널에서 `flutter pub get` 명령을 실행하여 패키지를 다운로드하세요.

## Firebase 앱 초기화

Firebase를 사용하여 앱을 초기화해야 합니다. 앱이 처음 실행될 때 `main()` 함수에서 Firebase 초기화를 수행해야 합니다. 다음은 초기화하는 방법의 예입니다:

```dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  // Flutter 앱 초기화 코드
  await Firebase.initializeApp();
  
  // 앱 시작
  runApp(MyApp());
}
```

## 사용자 이벤트 추적

Firebase Analytics를 사용하여 사용자의 이벤트를 추적할 수 있습니다. 예를 들어, 사용자가 특정 화면을 방문할 때마다 해당 이벤트를 기록하고 싶다고 가정해 보겠습니다. 다음은 이벤트를 기록하는 과정입니다:

```dart
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:firebase_analytics/observer.dart';

class MyScreen extends StatelessWidget {
  final FirebaseAnalytics analytics = FirebaseAnalytics();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('My Screen')),
      body: Center(
        child: Text('Welcome to My Screen!'),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _trackScreenView('My Screen'); // 사용자 이벤트 추적
        },
        child: Icon(Icons.analytics),
      ),
    );
  }

  Future<void> _trackScreenView(String screenName) async {
    await analytics.setCurrentScreen(
      screenName: screenName,
      screenClassOverride: 'MyScreen',
    );
  }
}
```

위 예에서는 `MyScreen` 위젯에 `FirebaseAnalytics` 인스턴스를 생성하고, 부동 작업 버튼이 탭될 때마다 `_trackScreenView` 메소드를 호출하여 이벤트를 기록합니다. `setCurrentScreen` 메소드를 사용하여 현재 화면을 설정하고, 선택적으로 `screenClassOverride` 파라미터를 사용하여 화면 클래스 이름을 지정할 수 있습니다.

## 앱 실행 이벤트 추적

앱의 실행 이벤트를 추적하려면 `main()` 함수에서 앱 시작 이벤트를 기록해야 합니다. 다음은 시작 이벤트를 기록하는 예입니다:

```dart
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:firebase_analytics/observer.dart';

void main() async {
  // Flutter 앱 초기화 코드
  await Firebase.initializeApp();

  // Firebase Analytics 초기화
  FirebaseAnalytics analytics = FirebaseAnalytics();

  // 앱 시작 이벤트 추적
  await analytics.logAppOpen();

  // 앱 시작
  runApp(MyApp());
}
```

위 예제에서는 `main()` 함수에서 `logAppOpen()` 메소드를 호출하여 앱 시작 이벤트를 기록합니다.

## Firebase Analytics 이벤트 및 사용자 속성

Firebase Analytics를 사용하면 사용자 지정 이벤트와 사용자 속성을 추가로 기록할 수 있습니다. 이를 통해 앱의 사용자 인사이트를 더욱 풍부하게 수집할 수 있습니다. Firebase 콘솔에서 사용자 정의 이벤트 및 사용자 속성을 확인할 수 있습니다.

- 사용자 정의 이벤트 기록 예시:

  ```dart
  await analytics.logEvent(
    name: 'video_play',
    parameters: {
      'video_id': '12345',
      'video_name': 'Flutter Tutorial',
    },
  );
  ```

- 사용자 속성 설정 예시:

  ```dart
  await analytics.setUserProperty(
    name: 'user_type',
    value: 'premium',
  );
  ```

Firebase Analytics를 활용하여 사용자 행동을 추적하고 앱의 성능을 측정할 수 있습니다. Firebase 콘솔을 통해 수집한 데이터를 확인하여 앱을 개선하는 데 도움을 받을 수 있습니다. 자세한 내용은 [Firebase Analytics 문서](https://firebase.flutter.dev/docs/analytics/overview/)를 참조하세요.

## 참고 자료

- [Firebase Analytics 문서](https://firebase.flutter.dev/docs/analytics/overview/)
- [Firebase 다운로드 페이지](https://console.firebase.google.com/)
- [firebase_analytics Flutter 패키지](https://pub.dev/packages/firebase_analytics)