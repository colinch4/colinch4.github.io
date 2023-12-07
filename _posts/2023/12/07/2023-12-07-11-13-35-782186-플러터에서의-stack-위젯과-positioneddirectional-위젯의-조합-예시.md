---
layout: post
title: "[flutter] 플러터에서의 Stack 위젯과 PositionedDirectional 위젯의 조합 예시"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

Flutter에서 Stack 위젯과 PositionedDirectional 위젯은 화면에 여러 위젯을 겹쳐서 배치하는 데 사용됩니다. 이들 위젯의 조합은 복잡한 UI를 구현할 때 특히 유용합니다. 이번 블로그 포스트에서는 Stack 위젯과 PositionedDirectional 위젯을 함께 사용하는 예시를 소개하겠습니다.

## Stack 위젯

**Stack 위젯**은 여러 위젯을 겹쳐서 표시할 수 있는 위젯입니다. Stack 위젯을 사용하면 위젯을 실제 크기를 변경하거나 이동하지 않고도 겹치게 조합할 수 있습니다.

아래는 Stack 위젯의 기본 구조 예시입니다.

```dart
Stack(
  children: <Widget>[
    // 겹칠 위젯들
  ],
)
```

Stack 위젯은 자식 위젯들을 위에서부터 아래로 순서대로 쌓습니다. 즉, 첫 번째 자식 위젯이 가장 아래에 쌓이고 마지막 자식 위젯이 가장 위에 쌓입니다.

## PositionedDirectional 위젯

**PositionedDirectional 위젯**은 Stack 위젯 내에서 자식 위젯의 위치를 지정하기 위해 사용됩니다. PositionedDirectional 위젯은 부모 위젯인 Stack 위젯에 상대적인 위치를 설정해줍니다.

아래는 PositionedDirectional 위젯의 기본 구조 예시입니다.

```dart
PositionedDirectional(
  top: 10.0,  // 위쪽으로 10.0만큼 이동
  start: 20.0,  // 시작점으로부터 20.0만큼 이동
  child: Container(
    // 자식 위젯
  ),
)
```

PositionedDirectional 위젯은 자식 위젯을 Stack 위젯 내에서 원하는 위치로 이동시킵니다. top, start, end, bottom 등의 속성을 사용하여 이동할 위치를 설정할 수 있습니다.

## Stack과 PositionedDirectional 조합 예시

이제 Stack 위젯과 PositionedDirectional 위젯을 함께 사용하는 예시를 살펴보겠습니다. 이 예시에서는 Stack 위젯 내에 두 개의 컨테이너를 겹쳐서 배치하는 방법을 보여줍니다.

```dart
Stack(
  children: <Widget>[
    PositionedDirectional(
      top: 50.0,
      start: 50.0,
      child: Container(
        width: 100.0,
        height: 100.0,
        color: Colors.red,
        child: Center(
          child: Text(
            'Container 1',
            style: TextStyle(
              color: Colors.white,
              fontSize: 16.0,
            ),
          ),
        ),
      ),
    ),
    PositionedDirectional(
      top: 70.0,
      start: 70.0,
      child: Container(
        width: 60.0,
        height: 60.0,
        color: Colors.blue,
        child: Center(
          child: Text(
            'Container 2',
            style: TextStyle(
              color: Colors.white,
              fontSize: 12.0,
            ),
          ),
        ),
      ),
    ),
  ],
)
```

위의 코드는 Stack 위젯 내에 두 개의 컨테이너를 배치하는 예시입니다. 첫 번째 컨테이너(빨간색)는 상단으로부터 50.0만큼, 좌측으로부터 50.0만큼 이동하며, 가로 100.0px, 세로 100.0px의 사이즈를 갖습니다. 두 번째 컨테이너(파란색)는 첫 번째 컨테이너로부터 상단으로부터 70.0만큼, 좌측으로부터 70.0만큼 이동하며, 가로 60.0px, 세로 60.0px의 사이즈를 갖습니다.

위의 예시 코드를 실행하면 빨간색과 파란색 컨테이너가 겹쳐서 배치된 화면이 표시됩니다.

## 마무리

이번 블로그 포스트에서는 Flutter의 Stack 위젯과 PositionedDirectional 위젯을 함께 사용하는 예시를 소개했습니다. Stack과 PositionedDirectional을 활용하여 다양한 UI를 구성할 수 있으니, 참고해보시고 필요에 따라 유연하게 활용해보세요!