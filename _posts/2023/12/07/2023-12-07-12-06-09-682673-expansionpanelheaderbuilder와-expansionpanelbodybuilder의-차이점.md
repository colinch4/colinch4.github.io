---
layout: post
title: "[flutter] ExpansionPanelHeaderBuilder와 ExpansionPanelBodyBuilder의 차이점"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

`ExpansionPanel` 위젯은 사용자가 펼칠 수 있는 패널을 만들어주는 Flutter의 기본 위젯 중 하나입니다. `ExpansionPanel` 위젯은 아코디언 스타일의 UI를 구현하는 데 유용합니다. 

`ExpansionPanel` 위젯은 `headerBuilder`와 `body`를 정의하는 두 가지 중요한 매개 변수를 허용합니다. `headerBuilder`는 사용자에게 패널의 헤더 부분을 만들 수 있는 콜백 함수입니다. 한편 `ExpansionPanelBodyBuilder`는 패널의 본문 부분을 만들 수 있는 콜백 함수입니다. 이 두 가지 콜백 함수의 주요 차이점은 다음과 같습니다.

## ExpansionPanelHeaderBuilder
`ExpansionPanelHeaderBuilder`는 패널의 헤더를 만들기 위한 콜백 함수입니다. 이 콜백 함수는 각 패널의 현재 상태(`isExpanded`)를 인수로 받을 수 있습니다. 이 콜백 함수에서는 `Text` 위젯 등을 사용하여 패널의 제목을 표시할 수 있습니다. 또한 패널 헤더를 누를 때마다 `isExpanded` 값이 전환되는 동작을 추가로 구현할 수도 있습니다.

예제 코드:
```dart
ExpansionPanelHeaderBuilder(
  builder: (BuildContext context, bool isExpanded) {
    return Text(
      isExpanded ? '패널 닫기' : '패널 열기',
      style: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
    );
  },
)
```

## ExpansionPanelBodyBuilder
`ExpansionPanelBodyBuilder`는 패널의 본문을 만들기 위한 콜백 함수입니다. 이 콜백 함수에서는 패널의 본문에 표시할 내용을 구성할 수 있습니다. 주로 `Column`, `ListView`, 또는 다른 위젯을 사용하여 패널 내용을 만들 수 있습니다.

예제 코드:
```dart
ExpansionPanelBodyBuilder(
  body: (BuildContext context) {
    return Column(
      children: [
        Text('패널 내용 1'),
        Text('패널 내용 2'),
        Text('패널 내용 3'),
      ],
    );
  },
)
```

## 결론
`ExpansionPanelHeaderBuilder`와 `ExpansionPanelBodyBuilder`는 각각 패널의 헤더와 본문을 만들기 위한 콜백 함수입니다. 이 두 가지 콜백 함수는 `ExpansionPanel` 위젯의 일부로 사용될 때 기능적으로 연결되며, 사용자 정의 UI를 생성하는 데 유용합니다.

더 자세한 정보는 다음 문서를 참조하십시오:
- [Flutter ExpansionPanel 클래스 문서](https://api.flutter.dev/flutter/material/ExpansionPanel-class.html)