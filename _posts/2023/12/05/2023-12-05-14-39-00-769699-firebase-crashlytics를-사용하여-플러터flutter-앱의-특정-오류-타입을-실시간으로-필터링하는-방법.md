---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 특정 오류 타입을 실시간으로 필터링하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

Firebase Crashlytics는 플러터(Flutter) 애플리케이션에서 발생하는 오류를 실시간으로 모니터링하고 분석할 수 있는 강력한 도구입니다. 이를 통해 앱의 사용자에게 좋은 사용자 경험을 제공하기 위해 빠르게 문제를 해결할 수 있습니다. 이번 블로그에서는 Firebase Crashlytics를 사용하여 앱에서 발생하는 특정 오류 타입을 실시간으로 필터링하는 방법에 대해 알아보겠습니다.

## Firebase Crashlytics 설정하기
Firebase Crashlytics를 사용하기 위해서는 Firebase 프로젝트에 앱을 등록하고 SDK를 설정해야 합니다. Firebase 프로젝트 생성 및 앱 설정에 대한 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/flutter/setup?platform=android)를 참고하시기 바랍니다.

## 특정 오류 타입 필터링하기
Firebase Crashlytics에서 특정 오류 타입을 필터링하기 위해서는 Firebase Console에서 필터링 설정을 변경해야 합니다. 아래는 필터링 설정을 변경하는 방법입니다.

1. Firebase Console(https://console.firebase.google.com/)에 접속합니다.
2. 해당 앱을 선택합니다.
3. 'Crashlytics' 탭을 클릭합니다.
4. '오류 이벤트 필터링' 섹션에서 '오류 형식' 드롭다운을 클릭합니다.
5. 필터링할 특정 오류 타입을 선택합니다. 예를 들어, '예외'를 선택할 경우 앱에서 발생하는 예외 관련 오류만 필터링되게 됩니다.
6. 선택이 완료되면 '저장' 버튼을 클릭하여 설정을 저장합니다.

이제 Firebase Crashlytics는 설정한 특정 오류 타입만 필터링하여 앱에서 발생하는 해당 오류에 대한 정보를 제공합니다. 이를 통해 개발자는 실시간으로 앱의 이슈를 추적하고 빠르게 문제를 해결할 수 있습니다.

## 결론
Firebase Crashlytics를 사용하여 앱의 특정 오류 타입을 실시간으로 필터링하는 방법에 대해 알아보았습니다. Firebase Crashlytics는 앱의 안정성 및 사용자 경험을 향상시키는 강력한 도구입니다. 앱 개발 시에는 Firebase Crashlytics를 활용하여 오류를 신속하게 해결할 수 있도록 하는 것이 좋습니다.

더 많은 정보를 원하시면 [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)를 참고하시기 바랍니다.