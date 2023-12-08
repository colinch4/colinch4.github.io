---
layout: post
title: "[flutter] flutter_svg에서 이미지에 알파블렌딩(alpha blending)을 적용하는 방법은?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

## flutter_svg에서 알파 블렌딩 적용하기

flutter_svg는 벡터 이미지 및 SVG 파일을 표시하는 데 사용되는 플러터(widget) 패키지입니다. 이미지에 알파 블렌딩을 적용하려면 다음 단계를 따르면 됩니다.

### 1. 이미지 파일 확인

먼저, 알파 블렌딩을 적용하려는 이미지가 SVG 형식으로 제공되는지 확인하세요. 

### 2. SVG 이미지 가져오기

SVG 이미지를 가져오기 위해 flutter_svg 패키지의 `SvgPicture` 위젯을 사용합니다. 

예시:
```dart
import 'package:flutter_svg/flutter_svg.dart';
  
SvgPicture.asset(
  'assets/image.svg',
  // 알파 블렌딩 적용
  blendMode: BlendMode.srcOver, 
  // 적용할 블렌딩 모드 선택
);
```

### 3. 알파 블렌딩 적용

`SvgPicture` 위젯의 `blendMode` 속성을 사용하여 원하는 알파 블렌딩 모드를 선택할 수 있습니다. 여기서 `BlendMode.srcOver`와 같은 값을 사용하여 적용할 수 있습니다.

위의 예시 코드에서 `blendMode: BlendMode.srcOver` 부분은 알파 블렌딩을 적용하는 부분입니다. 

이제, flutter_svg를 사용하여 이미지에 알파 블렌딩을 적용하는 방법에 대해 알아보았습니다. 어떤 도움이 되셨는지요?

### 참고 자료
- [flutter_svg 공식 문서](https://pub.dev/packages/flutter_svg)