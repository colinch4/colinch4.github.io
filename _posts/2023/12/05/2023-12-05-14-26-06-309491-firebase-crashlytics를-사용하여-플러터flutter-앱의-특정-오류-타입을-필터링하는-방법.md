---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 특정 오류 타입을 필터링하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 오류 및 충돌 데이터를 수집하고 플러터 앱의 안정성을 향상시키기 위한 강력한 도구입니다. 이 도구를 사용하면 앱의 오류를 모니터링하고 디버깅할 수 있으며, 오류를 신속하게 해결할 수 있습니다.

Firebase Crashlytics를 사용하여 앱에서 특정 오류 타입을 필터링하는 방법을 알아보겠습니다.

## 1. Firebase Crashlytics 설정하기

먼저, Firebase Crashlytics를 사용하기 위해 Firebase 프로젝트에 앱을 추가하고 Crashlytics를 활성화해야 합니다. Firebase 콘솔에서 프로젝트를 선택하고 Crashlytics 탭으로 이동하여 설정을 진행하세요. 자세한 설정 방법은 [Firebase 문서](https://firebase.google.com/docs/crashlytics)를 참고하세요.

## 2. 특정 오류 타입 필터링하기

Firebase Crashlytics는 오류를 기록할 때 자동으로 오류 타입을 추출합니다. 이를 통해 특정 오류 타입을 필터링하여 원하는 오류에 집중할 수 있습니다.

예를 들어, `NullPointerException` 오류 타입만을 필터링하여 모니터링하고자 한다면, 다음과 같이 코드를 추가할 수 있습니다.

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

void main() async {
  // Firebase 초기화
  await Firebase.initializeApp();
  
  // Crashlytics 초기화
  await FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  
  // 필터링할 오류 타입 설정
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true);
  FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true, ['NullPointerException']);
  
  // 플러터 앱 실행
  runApp(MyApp());
}
```

위 코드에서 `FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true, ['NullPointerException'])`은 `NullPointerException` 오류 타입만을 필터링하여 수집하도록 설정하는 부분입니다. 이렇게 설정하면 오직 `NullPointerException` 오류만을 모니터링할 수 있습니다.

## 3. 오류 데이터 확인하기

Firebase 콘솔에서 Crashlytics 탭으로 이동하여 앱의 오류 데이터를 확인할 수 있습니다. 필터링된 오류 타입만을 볼 수 있으므로, 세부적인 오류 분석 및 디버깅이 가능해집니다.

Firebase Crashlytics를 통해 수집된 오류 데이터는 앱의 안정성 향상과 유저 경험 개선에 큰 도움이 됩니다.

## 결론

이제 Firebase Crashlytics를 사용하여 플러터 앱에서 특정 오류 타입을 필터링하는 방법을 알게 되었습니다. 오류 타입을 정확히 필터링하면 앱의 오류를 더욱 효과적으로 모니터링하고 해결할 수 있습니다. Firebase Crashlytics를 통해 앱의 안정성을 향상시키고, 사용자들에게 좋은 경험을 제공할 수 있도록 노력해보세요.