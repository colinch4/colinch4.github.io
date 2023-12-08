---
layout: post
title: "[flutter] AnimatedContainer와 함께 사용하는 AnimatedOpacity 소개"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter의 애니메이션을 적용하는 데에는 여러 가지 방법이 있습니다. 이 중에서 AnimatedContainer와 함께 사용되는 **AnimatedOpacity**를 살펴보겠습니다. 

## AnimatedOpacity란 무엇인가?

**AnimatedOpacity**는 부모 위젯에서 자식 위젯의 투명도를 애니메이션화하는 데 사용됩니다. 이를 통해 부드러운 투명도 전환이 가능해집니다. 이는 예를 들어, 화면 상의 어떤 위젯이 서서히 사라지거나 나타나는 효과를 구현하는 데 사용될 수 있습니다.

## AnimatedOpacity 사용 예시

아래는 AnimatedOpacity를 사용하는 간단한 예시입니다.

```dart
AnimatedOpacity(
  opacity: _visible ? 1.0 : 0.0,
  duration: Duration(milliseconds: 500),
  child: Text('AnimatedOpacity Example'),
)
```

위 코드에서 ```_visible``` 변수의 값을 변경하여 위젯의 투명도를 애니메이션화 할 수 있습니다.

## AnimatedContainer와 함께 사용하기

**AnimatedOpacity**는 **AnimatedContainer**와 같은 다른 애니메이션 위젯들과 함께 사용될 수 있습니다. 예를 들어 **AnimatedContainer**의 크기나 위치를 변경하는 동안에도 자식 위젯의 투명도를 애니메이션화 할 수 있습니다.

```dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  width: _visible ? 200.0 : 100.0,
  height: _visible ? 200.0 : 100.0,
  color: _visible ? Colors.blue : Colors.red,
  child: AnimatedOpacity(
    opacity: _visible ? 1.0 : 0.0,
    duration: Duration(milliseconds: 500),
    child: Text('AnimatedContainer with AnimatedOpacity'),
  ),
)
```

## 요약

**AnimatedOpacity**는 부모 위젯에서 자식 위젯의 투명도를 부드럽게 애니메이션화 하는 데 사용됩니다. 또한 다른 애니메이션 위젯들과 함께 사용하여 다양한 애니메이션 효과를 구현할 수 있습니다.

이렇게 **AnimatedOpacity**와 함께 **AnimatedContainer**를 사용하여 Flutter에서 부드러운 애니메이션을 구현할 수 있습니다.