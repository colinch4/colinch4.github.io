---
layout: post
title: "[flutter] AnimatedContainer의 ease-in-out 애니메이션 효과 설명하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter에서 UI 구성 요소를 애니메이션으로 부드럽게 변화시키기 위해 `AnimatedContainer`를 사용할 수 있습니다. 

`AnimatedContainer`는 크기, 색상 또는 위치와 같은 속성들을 변경할 때 부드러운 애니메이션 효과를 적용할 수 있도록 도와줍니다.

## ease-in-out 애니메이션 효과란?

`ease-in-out` 애니메이션은 시작과 끝 지점에서의 변화가 점차적으로 가속도를 둔화하거나 줄여가는 애니메이션 효과를 의미합니다. 이는 변화의 시작과 끝을 자연스럽게 만들어주어 사용자 경험을 향상시킵니다.

예를 들어, 화면의 위젯 크기가 변할 때 `ease-in-out` 애니메이션 효과가 적용되면, 처음에는 변화가 느리게 시작하여 사용자가 주의를 기울이게 하고 나중에는 느려지면서 자연스럽게 애니메이션이 끝나는 효과를 줄 수 있습니다.

예제 코드:

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  curve: Curves.easeInOut,
  width: _isExpanded ? 200 : 100,
  height: _isExpanded ? 200 : 100,
  color: _isExpanded ? Colors.blue : Colors.green,
  child: Center(
    child: Text('AnimatedContainer'),
  ),
)
```

위의 예제 코드에서 `AnimatedContainer`의 `curve` 속성을 `Curves.easeInOut`으로 설정하여 ease-in-out 애니메이션 효과를 부여하고 있습니다.

`Curves.easeInOut`는 시작과 끝에서의 변화가 점차적으로 가속도를 둔화시키는 효과를 가지고 있어요.

이렇게 `AnimatedContainer`를 사용하여 ease-in-out 애니메이션 효과를 부여하면 앱의 UI가 부드럽고 자연스럽게 변화함으로써 더 나은 사용자 경험을 제공할 수 있습니다.

## 마치며

지금까지 `AnimatedContainer`의 ease-in-out 애니메이션 효과에 대해 알아보았습니다. 이를 통해 Flutter 앱에서 부드럽고 자연스러운 UI 애니메이션을 구현할 수 있게 되었습니다.

더 많은 정보를 원하시면 [Flutter 공식 문서](https://flutter.dev/docs)를 확인해보세요.