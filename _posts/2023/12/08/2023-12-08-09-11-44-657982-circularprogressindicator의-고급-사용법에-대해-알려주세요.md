---
layout: post
title: "[flutter] CircularProgressIndicator의 고급 사용법에 대해 알려주세요."
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

CircularProgressIndicator는 주로 작업 진행 상태를 표시하는 데 사용됩니다. 하지만 이 위젯을 활용하여 더 다양한 시각적 효과를 구현할 수 있습니다. 이번 포스트에서는 CircularProgressIndicator의 고급 사용법에 대해 알아보겠습니다.

## 1. 커스텀 CircularProgressIndicator 디자인

일반적으로 CircularProgressIndicator는 회전하는 효과를 주기 위해 사용됩니다. 그러나 이를 통해 커스텀 디자인을 구현할 수 있습니다. 예를 들어, 선 두께나 색상을 변경하여 CircularProgressIndicator를 원하는 디자인으로 만들 수 있습니다.

```dart
Container(
  width: 50,
  height: 50,
  child: CircularProgressIndicator(
    strokeWidth: 5,  // 두께 조절
    valueColor: AlwaysStoppedAnimation<Color>(Colors.red),  // 색상 조절
  ),
),
```

## 2. CircularProgressIndicator에 애니메이션 추가

CircularProgressIndicator에 다양한 애니메이션 효과를 추가하여 보다 동적인 디자인을 구현할 수 있습니다. 예를 들어, ScaleTransition을 사용하여 크기가 변하는 애니메이션 효과를 줄 수 있습니다.

```dart
Container(
  width: 50,
  height: 50,
  child: CircularProgressIndicator(
    value: null,  // null로 설정하여 전체 동그라미를 그립니다.
    strokeWidth: 5,
    valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
  ),
),
```

## 3. CircularProgressIndicator의 외형 커스터마이징

CircularProgressIndicator의 외형을 커스터마이징하여 다양한 디자인을 구현할 수 있습니다. 예를 들어, BoxShape.circle을 사용하여 원형이 아닌 다른 모양의 Indicator를 만들 수 있습니다.

```dart
Container(
  width: 50,
  height: 50,
  decoration: BoxDecoration(
    shape: BoxShape.circle,
    color: Colors.transparent,
    border: Border.all(
      color: Colors.green,
      width: 4,
    ),
  ),
  child: CircularProgressIndicator(
    strokeWidth: 0,  // 기본 Indicator 숨김
  ),
),
```

## 4. CircularProgressIndicator의 사용자 정의

선언적으로 사용하고 있는 CircularProgressIndicator를 코드로 직접 정의하여, 보다 다양한 기능을 구현할 수 있습니다. 이를 통해 다양한 애니메이션을 표현하거나 사용자 상호작용에 반응하는 Indicator를 만들 수 있습니다.

```dart
class CustomCircularProgressIndicator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      width: 50,
      height: 50,
      child: RotationTransition(
        turns: AlwaysStoppedAnimation(0.25),  // 회전 애니메이션 추가
        child: CircularProgressIndicator(
          strokeWidth: 5,
          valueColor: AlwaysStoppedAnimation<Color>(Colors.purple),
        ),
      ),
    );
  }
}
```

이렇게해서 현재까지 CircularProgressIndicator의 고급 사용법에 대해 알아보았습니다. 추가로 궁금한 점이 있으면 언제든지 물어봐주세요!