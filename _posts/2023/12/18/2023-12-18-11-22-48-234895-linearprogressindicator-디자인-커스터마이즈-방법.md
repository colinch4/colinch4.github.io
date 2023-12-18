---
layout: post
title: "[flutter] LinearProgressIndicator 디자인 커스터마이즈 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter에서 제공하는 `LinearProgressIndicator` 위젯은 기본적으로 Material Design에 따라 디자인되어 있습니다. 그러나 몇 가지 속성을 사용하여 이를 커스터마이즈할 수 있습니다.

## 기본 LinearProgressIndicator 생성

먼저, 기본 `LinearProgressIndicator`를 생성하는 방법을 살펴봅시다.

```dart
LinearProgressIndicator(
  value: _progressValue,
  backgroundColor: Colors.grey,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
)
```

위 코드에서 `value`는 진행 상태를 나타내며, `backgroundColor`는 지시기의 배경색을 설정하고, `valueColor`는 진행 표시기의 색상을 설정합니다. 이러한 속성들을 사용하여 기본 `LinearProgressIndicator`의 디자인을 바꿀 수 있습니다.

## BoxDecoration으로 디자인 수정

더 나아가, `BoxDecoration`을 사용하여 `LinearProgressIndicator`의 디자인을 더욱 세밀하게 수정할 수 있습니다. 예를 들어, `BoxDecoration`의 `borderRadius` 속성을 사용하여 `LinearProgressIndicator`의 모서리를 둥글게 만들거나, `gradient`를 사용하여 그라데이션 효과를 줄 수 있습니다.

```dart
LinearProgressIndicator(
  value: _progressValue,
  backgroundColor: Colors.grey,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
  // BoxDecoration 사용
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(10.0),
    gradient: LinearGradient(
      colors: [Colors.blue, Colors.green],
    ),
  ),
)
```

위와 같이 `decoration` 속성을 추가하여 `LinearProgressIndicator`의 디자인을 세부적으로 수정할 수 있습니다.

## 요약

Flutter에서의 `LinearProgressIndicator`는 여러 가지 방법으로 디자인을 커스터마이즈할 수 있습니다. 기본적인 속성들과 `BoxDecoration`을 사용하여 다양한 디자인을 구현할 수 있습니다.

내용이 유용하실 것 같습니다.

## 참고 자료
- Flutter 공식 문서: https://flutter.dev/docs
- Flutter Widget 카탈로그: https://flutter.dev/docs/development/ui/widgets