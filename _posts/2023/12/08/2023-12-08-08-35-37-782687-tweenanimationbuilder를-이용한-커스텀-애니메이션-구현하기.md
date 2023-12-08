---
layout: post
title: "[flutter] TweenAnimationBuilder를 이용한 커스텀 애니메이션 구현하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter에서 애니메이션을 만들기 위해 TweenAnimationBuilder를 사용할 수 있습니다. 이 위젯은 시작값과 끝값 사이의 애니메이션을 만들어주는 편리한 기능을 제공합니다. 이번 포스트에서는 TweenAnimationBuilder를 사용하여 커스텀 애니메이션을 구현하는 방법에 대해 알아보겠습니다.

## 1. TweenAnimationBuilder란?

TweenAnimationBuilder는 Flutter에서 제공하는 위젯으로, 시작값과 끝값 사이의 애니메이션을 편리하게 만들어주는 기능을 제공합니다. 이를 통해 자신만의 커스텀 애니메이션을 만들 수 있습니다. 

## 2. TweenAnimationBuilder의 구성 요소

TweenAnimationBuilder는 아래의 4가지 요소로 구성됩니다.

- **duration**: 애니메이션의 지속 시간을 설정합니다.
- **tween**: 시작값과 끝값을 지정합니다.
- **builder**: 현재 값에 대한 위젯을 만들어주는 함수입니다.
- **onEnd**: 애니메이션이 끝날 때 호출되는 콜백 함수입니다.

## 3. TweenAnimationBuilder 사용 예시

다음은 TweenAnimationBuilder를 사용하여 커스텀 애니메이션을 구현하는 간단한 예시입니다.

```dart
TweenAnimationBuilder<double>(
  duration: Duration(seconds: 1),
  tween: Tween<double>(begin: 0, end: 300),
  builder: (BuildContext context, double value, Widget? child) {
    return Container(
      height: value,
      width: value,
      color: Colors.blue,
    );
  },
)
```

위의 예시에서는 높이와 너비가 0부터 300까지 변화하는 애니메이션을 만들고 있습니다.

## 4. 마무리

이번 포스트에서는 Flutter의 TweenAnimationBuilder를 사용하여 커스텀 애니메이션을 구현하는 방법에 대해 알아보았습니다. TweenAnimationBuilder를 잘 사용하면 다양한 애니메이션을 쉽게 만들 수 있으니, 많은 활용을 기대해 봅니다.

더 많은 정보는 [Flutter 공식 문서](https://flutter.dev/docs)에서 확인할 수 있습니다.