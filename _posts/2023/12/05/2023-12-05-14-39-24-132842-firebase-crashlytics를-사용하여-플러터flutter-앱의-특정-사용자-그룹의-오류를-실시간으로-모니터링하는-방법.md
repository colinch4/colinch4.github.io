---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 특정 사용자 그룹의 오류를 실시간으로 모니터링하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 앱의 안정성을 추적하고 앱이 충돌하는 경우 보고서를 생성하여 개발자가 문제를 해결할 수 있도록 도와주는 훌륭한 도구입니다. 이번 글에서는 Flutter 앱에서 특정 사용자 그룹의 오류를 실시간으로 모니터링하기 위해 Firebase Crashlytics를 사용하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

Firebase Console (https://console.firebase.google.com)으로 이동하여 프로젝트를 생성하거나 기존 프로젝트를 선택합니다. Firebase 프로젝트에 앱을 추가한 후, Firebase Crashlytics를 활성화해야 합니다.

1. 앱이 선택된 상태에서 왼쪽 메뉴의 **"Crashlytics"**를 클릭합니다.
2. **"시작하기"** 버튼을 클릭하여 Crashlytics를 활성화합니다.
3. Flutter 프로젝트의 **pubspec.yaml** 파일에 다음 의존성을 추가하세요:

```flutter
dependencies:
  firebase_crashlytics: ^2.3.0
```

4. Flutter 프로젝트의 **main.dart** 파일에서 Firebase Crashlytics 패키지를 임포트합니다:

```dart
import 'package:firebase_crashlytics/firebase_crashlytics.dart';
```

## 2. 사용자 그룹 설정

특정 사용자 그룹의 오류를 모니터링하기 위해 Firebase Crashlytics에서 사용자 식별 정보를 설정해야 합니다. 사용자 식별자는 사용자를 유일하게 식별하는 값이어야 합니다. 휴대폰 번호, 이메일 주소, 사용자 ID 등을 사용할 수 있습니다.

```dart
FirebaseCrashlytics.instance.setUserIdentifier("user_id_here");
```

위 코드에서 "user_id_here" 부분은 실제 사용자 식별자로 대체해야 합니다.

## 3. 오류 보고서 확인

Firebase Crashlytics가 오류를 감지하면 실시간으로 오류 보고서를 생성합니다. Firebase Console에서 다음 단계를 따라 오류 보고서를 확인할 수 있습니다:

1. Firebase Console로 이동합니다.
2. 프로젝트를 선택한 후 왼쪽 메뉴에서 **"Crashlytics"**를 클릭합니다.
3. 오류 목록을 확인하고 특정 오류를 선택합니다.
4. 오류에 대한 자세한 정보와 해당 오류를 발생시킨 사용자 그룹의 정보를 확인할 수 있습니다.

Firebase Crashlytics를 사용하여 Flutter 앱의 특정 사용자 그룹의 오류를 실시간으로 모니터링하는 방법에 대해 알아보았습니다. 이를 통해 앱의 안정성을 향상시키고 문제를 신속하게 해결할 수 있습니다.

더 자세한 내용은 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참고하시기 바랍니다.