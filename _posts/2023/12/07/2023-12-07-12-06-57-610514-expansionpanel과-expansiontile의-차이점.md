---
layout: post
title: "[flutter] ExpansionPanel과 ExpansionTile의 차이점"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

Flutter에서는 UI 요소를 효율적으로 사용하기 위해 다양한 위젯을 제공합니다. ExpansionPanel과 ExpansionTile은 UI를 확장 가능한 패널로 만드는 데 사용되는 두 가지 위젯입니다. 

## ExpansionPanel

ExpansionPanel은 패널의 상태를 바탕으로 컨텐츠를 확장하거나 축소하는 기능을 제공합니다. ExpansionPanel 위젯은 PanelHeaderBuilder, PanelBodyBuilder, isExpanded 세 가지 필수 매개변수를 필요로 합니다. PanelHeaderBuilder는 패널의 헤더를 정의하고, PanelBodyBuilder는 패널의 바디를 정의합니다. isExpanded는 패널이 확장되었는지의 여부를 설정하는 bool 값을 취합니다.

예시 코드:

```dart
List<ExpansionPanel> _panels = [
  ExpansionPanel(
    headerBuilder: (BuildContext context, bool isExpanded) {
      return ListTile(
        title: Text('패널 1'),
      );
    },
    body: Container(
      child: Text('패널 1 내용'),
    ),
    isExpanded: false,
  ),
  // 다른 패널들...
];

ExpansionPanelList(
  expandedHeaderPadding: EdgeInsets.zero,
  elevation: 1,
  elevationPadding: EdgeInsets.all(0),
  children: _panels.map<ExpansionPanel>((ExpansionPanel panel) {
    return panel;
  }).toList(),
)
```

## ExpansionTile

ExpansionTile도 패널을 확장 가능하게 만들어주는 위젯입니다. 그러나 ExpansionTile은 ExpansionPanel과 비교하여 더 간편하고 사용하기가 쉽습니다. ExpansionTile은 ListTile 위젯을 사용하여 패널의 제목과 확장된 내용을 정의합니다. 확장 상태를 저장하고 관리하는 기능들은 ExpansionTile 위젯 내부에서 자동으로 처리됩니다.

예시 코드:

```dart
ExpansionTile(
  title: Text('패널 제목'),
  children: <Widget>[
    ListTile(
      title: Text('패널 내용'),
    ),
  ],
)
```

## 결론

ExpansionPanel과 ExpansionTile은 모두 UI를 확장 가능한 패널로 만들어주는 위젯입니다. 그러나 ExpansionTile은 더 간편하고 사용하기가 쉽기 때문에, 대부분의 경우에서 추천되는 선택지입니다. ExpansionPanel은 특별한 상황에서 사용되며 패널 상태를 자체적으로 관리해야 할 때 유용합니다.