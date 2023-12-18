---
layout: post
title: "[flutter] 플러터에서 다양한 LinearProgressIndicator 애니메이션 효과 적용 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터에서 제공하는 `LinearProgressIndicator` 위젯은 작업 진행 상태를 시각적으로 표시하는 데 사용됩니다. 이 위젯에 애니메이션 효과를 적용하여 사용자 경험을 향상시킬 수 있습니다. 다음은 해당 애니메이션 효과를 적용하는 방법에 대한 설명입니다.

## 1. 기본 애니메이션 효과

기본적으로 `LinearProgressIndicator`는 애니메이션 효과를 가지고 있습니다. 아래와 같은 코드를 사용하여 기본 애니메이션을 구현할 수 있습니다.
```dart
LinearProgressIndicator()
```

## 2. 색상 및 두께 변경

애니메이션 효과를 향상시키기 위해 `LinearProgressIndicator`의 색상 및 두께를 변경할 수 있습니다. 아래와 같은 코드를 사용하여 이를 구현할 수 있습니다.
```dart
LinearProgressIndicator(
  backgroundColor: Colors.grey,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
  value: 0.5,
)
```

## 3. 커스텀 애니메이션 효과

더욱 독창적인 애니메이션 효과를 원한다면, `LinearProgressIndicator`를 커스터마이징하여 사용자 정의 애니메이션 효과를 적용할 수 있습니다. 여러 가지 애니메이션 라이브러리와 결합하여 이를 구현할 수 있는데, 가장 인기 있는 예는 `flutter_animation_progress_bar` 패키지를 사용하는 것입니다.

```yaml
dependencies:
  flutter_animation_progress_bar: ^2.2.0
```

```dart
AnimatedProgressBar(
  theme: ProgressBarTheme(
    height: 20,
    borderRadius: BorderRadius.zero,
  ),
  value: 60,
  backgroundColor: Colors.grey,
  barColor: Colors.blue,
)
```
이 패키지를 사용하면 화려하고 다양한 애니메이션 효과를 `LinearProgressIndicator`에 적용할 수 있습니다.

`LinearProgressIndicator`에 애니메이션 효과를 적용하여 사용자에게 미적 경험을 제공할 수 있으며, 위에서 제시한 방법을 통해 이를 쉽게 구현할 수 있습니다.

더 자세한 내용은 flutter 공식 문서를 참고해 주세요.

[플러터 공식 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)