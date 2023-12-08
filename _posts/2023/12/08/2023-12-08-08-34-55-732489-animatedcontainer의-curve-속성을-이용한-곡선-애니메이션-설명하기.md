---
layout: post
title: "[flutter] AnimatedContainer의 curve 속성을 이용한 곡선 애니메이션 설명하기"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter의 AnimatedContainer 위젯은 UI 요소의 애니메이션을 쉽게 구현할 수 있는 강력한 도구입니다. AnimatedContainer를 사용하면 요소의 속성 변화에 따라 자연스러운 애니메이션을 만들 수 있습니다. 

이번 포스트에서는 AnimatedContainer의 curve 속성을 활용하여 곡선을 가진 애니메이션을 만드는 방법에 대해 설명하겠습니다.

## AnimatedContainer

AnimatedContainer는 Dart 패키지인 Flutter의 일부로 제공되는 위젯으로, 특정 속성의 변경에 따른 부드러운 애니메이션을 적용할 수 있습니다. 이 위젯을 이용하면 편리하게 애니메이션을 구현할 수 있으며, curve 속성을 이용하면 애니메이션의 속도와 변화를 더욱 세밀하게 제어할 수 있습니다.

## curve 속성

curve 속성은 AnimatedContainer의 애니메이션을 조절하는 데 사용됩니다. 기본적으로 선형(Linear) 애니메이션이 적용되지만, curve를 설정하여 애니메이션의 시간에 따른 속도와 변화의 곡선을 설정할 수 있습니다.

예를 들어, easeInOut 곡선은 시작과 끝 부분에서 천천히 시작하거나 끝낼 수 있는 곡선을 지정합니다. 그 외에도 여러 가지 curve가 제공되며, 필요에 따라 선택하여 사용할 수 있습니다.

```dart
AnimatedContainer(
  curve: Curves.easeInOut, // easeInOut curve를 사용한 AnimatedContainer
  duration: Duration(seconds: 1),
  // 다른 속성들...
)
```

위 예제에서는 easeInOut curve를 사용하여 AnimatedContainer의 애니메이션을 조절하고 있습니다.

## 사용 예시

아래 예시는 curve 속성을 이용하여 AnimatedContainer의 애니메이션에 곡선 효과를 적용한 코드입니다.

```dart
bool _isExpanded = false;

void _toggleContainer() {
  setState(() {
    _isExpanded = !_isExpanded;
  });
}

AnimatedContainer(
  curve: Curves.fastOutSlowIn, // 곡선 애니메이션 사용
  duration: Duration(seconds: 1),
  width: _isExpanded ? 200.0 : 100.0,
  height: _isExpanded ? 200.0 : 100.0,
  color: _isExpanded ? Colors.blue : Colors.red,
  child: GestureDetector(
    onTap: () {
      _toggleContainer();
    },
    child: Center(
      child: Text(
        _isExpanded ? 'Click to shrink' : 'Click to expand',
        style: TextStyle(color: Colors.white),
      ),
    ),
  ),
)
```

위 코드에서는 곡선 애니메이션을 사용하여 AnimatedContainer의 크기와 색상을 변화시키는 예시를 보여줍니다. 

## 결론

AnimatedContainer의 curve 속성을 이용하면 애니메이션의 속도와 변화를 미세하게 제어할 수 있습니다. 곡선 애니메이션을 적용하여 더욱 부드럽고 자연스러운 UI 애니메이션을 구현할 수 있습니다.

애니메이션을 더욱 다채롭고 효과적으로 사용하기 위해 curve 속성을 활용해 보세요!

### References

- https://api.flutter.dev/flutter/animation/Curves-class.html
- https://flutter.dev/docs/cookbook/animation/curves

--- 

이미지: unsplash.com/photos/0V_4TGajpKc