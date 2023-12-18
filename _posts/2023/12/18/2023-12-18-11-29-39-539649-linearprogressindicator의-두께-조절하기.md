---
layout: post
title: "[flutter] LinearProgressIndicator의 두께 조절하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

`LinearProgressIndicator`는 Flutter에서 진행률을 표시하는 데 사용되는 위젯입니다. 기본적으로 `LinearProgressIndicator`의 두께는 일정하지만, 필요에 따라 조절할 수 있습니다. 

이 기술 블로그에서는 `LinearProgressIndicator`의 두께를 조절하는 방법에 대해 살펴보겠습니다.

## 1. 두께 속성 이해

`LinearProgressIndicator` 위젯은 `valueColor`, `backgroundColor`, `minHeight`, `value`, `color`, `backgroundColor` 등 다양한 속성을 제공합니다. 그 중에서 우리는 `minHeight` 속성을 사용하여 두께를 조절할 수 있습니다.

## 2. 두께 조절 방법

### 2.1 `minHeight` 속성 사용

`minHeight` 속성은 `LinearProgressIndicator`의 최소 높이를 나타냅니다. 이를 이용해서 `LinearProgressIndicator`의 두께를 조절할 수 있습니다. 다음은 `minHeight` 속성을 사용하여 `LinearProgressIndicator`의 두께를 조절하는 예시 코드입니다.

```dart
LinearProgressIndicator(
  minHeight: 10, // 10의 값은 다른 값을 적용하여 두께를 조절할 수 있습니다
)
```

`minHeight` 속성은 원하는 두께에 맞게 값을 조절하여 사용할 수 있습니다.

## 3. 결론

우리는 `LinearProgressIndicator`의 두께를 `minHeight` 속성을 활용하여 조절하는 방법에 대해 알아보았습니다. 이를 통해 앱의 디자인에 적합한 진행률 인디케이터를 만들 수 있습니다.

**참고:** 
- Flutter `LinearProgressIndicator` 위젯 문서: [https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)
  
이상으로 `LinearProgressIndicator`의 두께를 조절하는 방법에 대한 설명을 마치겠습니다. 감사합니다.

**태그:** Flutter, LinearProgressIndicator, 두께, minHeight, 진행률 표시