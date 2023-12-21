---
layout: post
title: "[flutter] flutter_launcher_icons.yaml 파일 구성 요소 설명"
description: " "
date: 2023-12-22
tags: [flutter]
comments: true
share: true
---

1. [flutter_launcher_icons.yaml 파일의 역할](#1-flutter_launcher_iconsyaml-파일의-역할)
2. [flutter_launcher_icons.yaml 파일의 구성 요소](#2-flutter_launcher_iconsyaml-파일의-구성-요소)
3. [예시 코드](#3-예시-코드)
4. [참고 자료](#4-참고-자료)

---

## 1. flutter_launcher_icons.yaml 파일의 역할

`flutter_launcher_icons.yaml` 파일은 Flutter 앱의 아이콘을 설정하는 데 사용됩니다. 이 파일은 앱의 아이콘을 생성하고 관리하는 데 필요한 구성을 지정하는데 사용됩니다.

---

## 2. flutter_launcher_icons.yaml 파일의 구성 요소

`flutter_launcher_icons.yaml` 파일은 다음과 같은 구성 요소를 포함할 수 있습니다:

- `image_path`: 아이콘 이미지의 상대 또는 절대 경로를 지정합니다.
- `image_path_android`: 안드로이드용 아이콘 이미지의 상대 또는 절대 경로를 지정합니다.
- `image_path_ios`: iOS용 아이콘 이미지의 상대 또는 절대 경로를 지정합니다.
- `adaptive_icon_background`: 안드로이드용 적응형 아이콘 배경 이미지의 상대 또는 절대 경로를 지정합니다.
- `adaptive_icon_foreground`: 안드로이드용 적응형 아이콘 전경 이미지의 상대 또는 절대 경로를 지정합니다.
- `adaptive_icon_background_android`: 안드로이드용 적응형 아이콘 배경 이미지의 상대 또는 절대 경로를 지정합니다.
- `adaptive_icon_foreground_android`: 안드로이드용 적응형 아이콘 전경 이미지의 상대 또는 절대 경로를 지정합니다.
- `generate_legacy_icon`: 레거시 아이콘을 생성할지 여부를 설정합니다.

---

## 3. 예시 코드

다음은 `flutter_launcher_icons.yaml` 파일의 예시 코드입니다.

```yaml
flutter_icons:
  image_path: "assets/icon/icon.png"
  image_path_android: "assets/icon/icon_android.png"
  image_path_ios: "assets/icon/icon_ios.png"
  adaptive_icon_background: "assets/icon/adaptive_background.png"
  adaptive_icon_foreground: "assets/icon/adaptive_foreground.png"
  adaptive_icon_background_android: "assets/icon/adaptive_background_android.png"
  adaptive_icon_foreground_android: "assets/icon/adaptive_foreground_android.png"
  generate_legacy_icon: true
```

---

## 4. 참고 자료

- [Flutter Launcher Icons 공식 문서](https://pub.dev/packages/flutter_launcher_icons)