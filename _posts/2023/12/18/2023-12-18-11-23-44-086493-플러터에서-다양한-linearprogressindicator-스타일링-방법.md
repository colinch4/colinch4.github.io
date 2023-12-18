---
layout: post
title: "[flutter] 플러터에서 다양한 LinearProgressIndicator 스타일링 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터에서 `LinearProgressIndicator`는 작업이 진행 중임을 시각적으로 나타내는 데 사용됩니다. 기본적인 `LinearProgressIndicator` 스타일링 방법부터 고급 스타일링 방법까지 살펴보겠습니다.

## 기본 스타일링

기본 `LinearProgressIndicator`를 사용하여 가장 간단한 형태로 스타일링할 수 있습니다. 예를 들면:

```dart
LinearProgressIndicator(
  backgroundColor: Colors.grey,
  valueColor: AlwaysStoppedAnimation(Colors.blue),
)
```

위 예제에서 `backgroundColor`는 진행 표시줄의 배경색을 나타내며, `valueColor`는 진행률을 나타내는 색을 나타냅니다.

## 고급 스타일링

`LinearProgressIndicator`를 상속하여 사용자 정의 `Widget`을 만들어 원하는 형태로 스타일링할 수 있습니다. 예를 들어:

```dart
class CustomProgressBar extends LinearProgressIndicator {
  CustomProgressBar()
      : super(
          backgroundColor: Colors.grey,
          valueColor: AlwaysStoppedAnimation(Colors.blue),
        );

  @override
  _CustomProgressBarState createState() => _CustomProgressBarState();
}

class _CustomProgressBarState extends State<CustomProgressBar> {
  @override
  Widget build(BuildContext context) {
    return LinearProgressIndicator(
      backgroundColor: Colors.grey,
      valueColor: AlwaysStoppedAnimation(Colors.blue),
      value: 0.5,
    );
  }
}
```

위 예제에서 `CustomProgressBar`는 `LinearProgressIndicator`를 상속하고 해당 스타일을 적용하는 사용자 정의 `Widget`을 만듭니다.

## 결론

`LinearProgressIndicator`를 스타일링하는 방법은 매우 유연하며, 기본적으로 제공되는 스타일링 옵션 외에도 사용자 정의할 수 있습니다. 이러한 다양한 스타일링 옵션을 활용하여 앱에 가장 적합한 형태로 `LinearProgressIndicator`를 사용할 수 있습니다.

참고문헌:
- [Flutter 공식 문서](https://flutter.dev/docs/development/ui/widgets/material#LinearProgressIndicator)