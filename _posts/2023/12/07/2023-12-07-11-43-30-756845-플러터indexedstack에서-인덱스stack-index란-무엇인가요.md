---
layout: post
title: "[flutter] 플러터(IndexedStack)에서 인덱스(Stack Index)란 무엇인가요?"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

플러터에서 IndexedStack 위젯은 여러 개의 자식을 가질 수 있으며, 인덱스를 통해 현재 화면에 보여줄 자식을 선택할 수 있는 위젯입니다. IndexedStack은 Stack과 달리 여러 자식 위젯을 겹치게 하지 않고, 현재 인덱스에 해당하는 자식만 화면에 보여줍니다.

인덱스(Stack Index)는 IndexedStack 위젯의 자식 리스트에서 각 자식의 위치를 나타내는 숫자입니다. 기본적으로 첫 번째 자식의 인덱스는 0이며, 두 번째 자식은 1, 세 번째 자식은 2와 같은 식으로 순서대로 증가합니다. 

예를 들어, IndexedStack 위젯에 3개의 자식 위젯이 있다고 가정해 봅시다. 현재 인덱스가 0인 경우 첫 번째 자식이 화면에 보여집니다. 인덱스가 1인 경우 두 번째 자식이, 인덱스가 2인 경우 세 번째 자식이 화면에 나타납니다.

IndexedStack 위젯은 주로 화면 전환이나 탭 바와 같이 여러 페이지가 겹쳐져 있을 때 사용됩니다. 사용자가 원하는 페이지로 전환할 때, 인덱스 값을 변경하여 해당 페이지를 보여주는 방식으로 동작합니다.

아래는 IndexedStack 위젯의 간단한 예시 코드입니다.

```dart
IndexedStack(
  index: _currentIndex,
  children: [
    FirstPage(),
    SecondPage(),
    ThirdPage(),
  ],
),
```

위 코드에서 _currentIndex는 현재 화면에 보여질 자식의 인덱스를 저장하는 변수입니다. 사용자의 조작에 따라 _currentIndex의 값을 변경하여 원하는 페이지를 화면에 표시할 수 있습니다.

자세한 내용과 다른 속성들에 대해서는 [공식 플러터 문서](https://api.flutter.dev/flutter/widgets/IndexedStack-class.html)를 참고하시기 바랍니다.