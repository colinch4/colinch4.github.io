---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 SlideTransition 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

애니메이션 및 전환 효과를 더해 Flutter 앱을 더욱 생동감 있고 사용자 친화적으로 만들 수 있습니다. 이번 글에서는 `AnimatedContainer`와 `SlideTransition`을 함께 사용하여 애니메이션 효과를 구현하는 방법을 살펴보겠습니다.

## 1. AnimatedContainer란?

`AnimatedContainer`는 Flutter 위젯 중 하나로, Widget의 크기, 배경색, 테두리, 위치 등을 애니메이션화할 수 있게 도와줍니다. 이를 통해 일반적인 Container와는 달리 애니메이션을 쉽게 적용할 수 있습니다. 

다음은 `AnimatedContainer`를 이용한 간단한 예제 코드입니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _selected ? 200.0 : 100.0,
  height: _selected ? 100.0 : 200.0,
  color: _selected ? Colors.blue : Colors.red,
  child: Text('AnimatedContainer 예제'),
),
```

위 코드에서 `_selected` 상태에 따라 `AnimatedContainer`의 속성들이 변경됨에 따라 애니메이션이 적용됩니다.

## 2. SlideTransition이란?

`SlideTransition`은 위젯을 수평 또는 수직으로 이동시킬 때 사용되는 애니메이션 위젯입니다. 이를 사용하면 위젯을 부드럽게 움직이게 할 수 있습니다.

다음은 `SlideTransition`를 이용한 예제 코드입니다.

```dart
SlideTransition(
  position: Tween<Offset>(
    begin: Offset(-1, 0),
    end: Offset(0, 0),
  ).animate(animation),
  child: Container(
    width: 100.0,
    height: 100.0,
    color: Colors.blue,
  ),
)
```

위 코드는 `SlideTransition`를 사용하여 `Container`를 화면 왼쪽에서 오른쪽으로 이동시키는 애니메이션을 적용한 예제입니다.

## 3. AnimatedContainer와 SlideTransition 함께 사용하기

이제 두 가지 위젯을 함께 사용하여 좀 더 흥미로운 애니메이션 효과를 낼 수 있습니다. 예제 코드를 통해 어떻게 사용하는지 살펴보겠습니다.

```dart
bool _selected = false;

Container(
  child: GestureDetector(
    onTap: () {
      setState(() {
        _selected = !_selected;
      });
    },
    child: SlideTransition(
      position: Tween<Offset>(
        begin: Offset(-1, 0),
        end: Offset(0, 0),
      ).animate(animationController),
      child: AnimatedContainer(
        duration: Duration(seconds: 1),
        width: _selected ? 200.0 : 100.0,
        height: _selected ? 100.0 : 200.0,
        color: _selected ? Colors.blue : Colors.red,
        child: Center(
          child: Text('애니메이션 효과를 적용한 위젯'),
        ),
      ),
    ),
  ),
),
```

위 코드에서 먼저 `SlideTransition`을 사용하여 `AnimatedContainer`를 왼쪽에서 오른쪽으로 이동시키는 애니메이션을 적용한 후, `GestureDetector`를 이용하여 터치 액션에 따라 `_selected` 상태를 변경하여 `AnimatedContainer`의 크기와 색상을 변경합니다.

이렇게 `AnimatedContainer`와 `SlideTransition`을 함께 사용하여 다양한 애니메이션 효과를 적용할 수 있습니다.

이상으로 Flutter에서 `AnimatedContainer`와 `SlideTransition`을 함께 사용하여 애니메이션 효과를 추가하는 방법을 살펴봤습니다.

참고문헌:
- https://api.flutter.dev/flutter/widgets/AnimatedContainer-class.html
- https://api.flutter.dev/flutter/widgets/SlideTransition-class.html