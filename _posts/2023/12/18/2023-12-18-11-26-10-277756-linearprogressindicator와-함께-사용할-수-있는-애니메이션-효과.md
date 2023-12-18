---
layout: post
title: "[flutter] LinearProgressIndicator와 함께 사용할 수 있는 애니메이션 효과"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter에서 `LinearProgressIndicator`는 진행률을 시각적으로 나타내는 데 사용됩니다. 이번 포스트에서는 `LinearProgressIndicator`와 함께 사용할 수 있는 **애니메이션 효과**에 대해 알아보겠습니다.

## 1. 애니메이션 효과 소개

애니메이션 효과를 사용하면 사용자 경험을 향상시킬 수 있습니다. `LinearProgressIndicator`와 함께 사용할 수 있는 몇 가지 애니메이션 효과를 다음에서 살펴보겠습니다.

### 1.1. 애니메이션 효과 1

첫 번째 애니메이션 효과는 해당 프로세스 진행률에 맞게 색상이 변화하는 것입니다.

```dart
AnimatedContainer(
  duration: Duration(milliseconds: 500),
  curve: Curves.linear,
  color: _progressValue == 1.0 ? Colors.green : Colors.blue,
  child: LinearProgressIndicator(
    value: _progressValue,
  ),
),
```

위 코드에서 `AnimatedContainer`를 사용하여 프로세스 진행률에 따라 색상이 변경됩니다.

### 1.2. 애니메이션 효과 2

두 번째 애니메이션 효과는 프로그레스 바가 부드럽게 증가하는 것입니다.

```dart
AnimatedSize(
  duration: Duration(milliseconds: 500),
  curve: Curves.linear,
  vsync: this,
  child: LinearProgressIndicator(
    value: _progressValue,
  ),
),
```

위의 코드에서 `AnimatedSize` 위젯을 사용하여 프로그레스 바가 부드럽게 증가하는 애니메이션 효과를 생성합니다.

## 2. 결론

Flutter에서 `LinearProgressIndicator`를 사용할 때 애니메이션 효과를 함께 사용하여 사용자에게 더 나은 미각적인 경험을 제공할 수 있습니다. 위에서 소개한 애니메이션 효과를 활용하여 진행률을 표시할 때 더 매력적인 UI를 만들어보세요.

기사: [Flutter 공식 문서 - Animation](https://api.flutter.dev/flutter/animation/animation-library.html)

**참고 문헌:**  
- Flutter 공식 문서: https://api.flutter.dev/