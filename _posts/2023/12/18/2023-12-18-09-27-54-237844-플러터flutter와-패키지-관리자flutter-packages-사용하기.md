---
layout: post
title: "[flutter] 플러터(Flutter)와 패키지 관리자(Flutter Packages) 사용하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 Google에서 개발한 크로스 플랫폼 모바일 앱 개발 프레임워크로, Dart 언어로 앱을 개발할 수 있습니다. 플러터는 다양한 기능을 제공하며, 시각적으로 풍부한 UI를 만들 수 있도록 도와줍니다. 이번 글에서는 플러터의 패키지 관리자를 사용하여 외부 패키지를 설치하고 사용하는 방법에 대해 알아보겠습니다.

## 1. 패키지 관리자(Flutter Packages)란?

플러터는 다양한 기능을 확장하기 위한 외부 패키지를 제공합니다. 이러한 외부 패키지를 편리하게 관리하고 설치하기 위해 패키지 관리자를 사용합니다. 패키지 관리자를 통해 외부 패키지를 손쉽게 추가하고 의존성을 관리할 수 있습니다.

## 2. 패키지 관리자 사용하기

**2.1. `pubspec.yaml` 파일 수정**

먼저, 외부 패키지를 설치하기 위해서는 `pubspec.yaml` 파일을 수정해야 합니다. 해당 파일은 프로젝트 루트 디렉토리에 위치하며, 프로젝트의 의존성 및 설정을 관리합니다. 아래는 `pubspec.yaml` 파일에 패키지를 추가하는 예시입니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
```

위의 예제에서 `cupertino_icons`는 추가하고자 하는 패키지 이름이며, 이러한 방식으로 외부 패키지를 추가할 수 있습니다.

**2.2. 패키지 설치**

`pubspec.yaml` 파일을 수정한 후 터미널을 열고, 프로젝트 루트 디렉토리로 이동하여 아래 명령어를 실행합니다.

```shell
flutter pub get
```

위 명령어를 실행하면 `pubspec.yaml` 파일에 기재된 의존성들을 자동으로 설치합니다.

**2.3. 패키지 사용**

패키지를 성공적으로 설치한 후에는 해당 패키지를 사용할 수 있습니다.

예를 들어, `cupertino_icons` 패키지를 사용하여 아이콘을 표시하려면 아래와 같이 사용합니다.

```dart
import 'package:flutter/cupertino_icons.dart';
```

## 3. 결론

플러터의 패키지 관리자를 통해 외부 패키지를 쉽게 설치하고 사용하는 방법에 대해 알아보았습니다. 외부 패키지를 통해 플러터 앱의 기능을 확장하고 성능을 향상시킬 수 있으니, 프로젝트에 맞는 패키지를 찾아 적극 활용해보시기 바랍니다.

참고: [플러터(Flutter) 공식 문서](https://flutter.dev/docs/development/packages-and-plugins/using-packages)