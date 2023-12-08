---
layout: post
title: "[flutter] CircularProgressIndicator의 기능과 역할은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter의 CircularProgressIndicator는 진행 상태를 시각적으로 나타내는 위젯입니다. 이 위젯은 주로 데이터를 불러오거나 계산하는 등의 작업이 수행 중일 때 사용됩니다.

## CircularProgressIndicator의 기능

### 1. 진행 상태 표시
ProgressIndicator는 데이터의 처리 상태를 시각적으로 나타내어 사용자에게 진행 중임을 알립니다.

### 2. 사용자 경험 향상
앱이 데이터를 불러오거나 처리하는 동안에는 사용자에게 작업이 진행 중임을 알려주는 것이 좋은 사용자 경험을 제공합니다. CircularProgressIndicator는 이러한 상황에서 유용하게 활용될 수 있습니다.

## CircularProgressIndicator 사용 예시

```dart
Center(
  child: CircularProgressIndicator(),
)
```

## 결론

ProgressIndicator는 작업이 진행 중임을 시각적으로 나타내어 사용자에게 편의를 제공합니다. 이를 통해 앱의 사용자 경험을 개선할 수 있습니다.

자세한 내용은 [Flutter 공식 문서](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)를 참고하시기 바랍니다.