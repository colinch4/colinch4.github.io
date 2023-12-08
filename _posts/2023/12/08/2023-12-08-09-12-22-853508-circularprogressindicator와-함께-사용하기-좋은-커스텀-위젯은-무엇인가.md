---
layout: post
title: "[flutter] CircularProgressIndicator와 함께 사용하기 좋은 커스텀 위젯은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하다보면 사용자에게 진행 중인 작업을 시각적으로 표시해주어야 하는 경우가 많습니다. 이때 CircularProgressIndicator는 유용한 위젯 중 하나이지만 때로는 해당 위젯을 커스텀하여 더 많은 기능을 추가할 필요가 있습니다. 이번 포스트에서는 CircularProgressIndicator와 함께 사용하기 좋은 커스텀 위젯 몇 가지를 살펴보겠습니다.

## 1. **CircularProgressButton**

이 위젯은 CircularProgressIndicator와 함께 사용하기 좋으며, 사용자가 버튼을 누르면 작업 진행 상황을 보여줄 수 있습니다. 또한 사용자의 입력을 받을 수 있는 반면, 작업이 완료되면 버튼의 모양을 변경하여 사용자에게 완료되었음을 알릴 수 있습니다.

```dart
CircularProgressButton(
  onPressed: () {
    // 작업 시작
  },
  // 버튼의 속성 설정
  ...
)
```

## 2. **CircularProgressIndicatorWithText**

이 위젯은 CircularProgressIndicator의 중앙에 진행 상황을 텍스트로 표시하는 기능을 추가하는데 유용합니다. 사용자에게 좀 더 직관적으로 현재의 작업 진행 상황을 알려줄 수 있습니다.

```dart
CircularProgressIndicatorWithText(
  progress: _progress, // 현재 진행률
  text: 'Uploading...', // 진행 중에 표시할 텍스트
)
```

## 3. **CustomCircularProgress**

이 위젯은 CircularProgressIndicator를 사용하여 일반적인 진행 상황을 표시하는데 쓰이지만, 외부에서 커스텀할 수 있는 기능들을 추가하여 다양한 디자인 요소를 적용할 수 있습니다.

```dart
CustomCircularProgress(
  progress: _progress, // 현재 진행률
  color: Colors.blue, // 색상 설정
  strokeWidth: 5.0, // 선의 두께 설정
)
```

각각의 위젯은 다양한 상황에 맞게 사용할 수 있으며, CircularProgressIndicator와 결합하여 작업의 진행 상황을 시각적으로 효과적으로 표시할 수 있습니다. 

더 많은 정보는 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하세요.

이상으로 'CircularProgressIndicator와 함께 사용하기 좋은 커스텀 위젯'에 대한 포스트를 마치도록 하겠습니다. 언제나 기술적인 이야기에 찾아와 주셔서 감사합니다.