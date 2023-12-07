---
layout: post
title: "[flutter] ExpansionPanelList 위젯을 이용한 다중 ExpansionPanel 관리"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

ExpansionPanelList는 Flutter에서 다중으로 확장 가능한 패널을 관리하는 위젯입니다. 각 패널은 헤더와 내용으로 구성되어 있으며, 헤더를 클릭하면 해당 패널의 내용이 확장되거나 축소됩니다. 이 글에서는 ExpansionPanelList 위젯을 사용하여 다중 확장 패널을 관리하는 방법을 알아보겠습니다.

## ExpansionPanelList 위젯 사용하기

ExpansionPanelList를 사용하기 위해서는 먼저 ExpansionPanelList 위젯을 생성해야 합니다. ExpansionPanelList는 ExpansionPanel을 리스트로 받아서 표시하므로, ExpansionPanel을 생성하여 ExpansionPanelList에 추가해야 합니다. 각 ExpansionPanel은 헤더와 내용 위젯을 가지고 있습니다. 헤더 위젯은 확장/축소 기능을 담당하고, 내용 위젯은 헤더를 클릭했을 때 보여질 내용을 담당합니다.

```dart
ExpansionPanelList(
  elevation: 1,
  expandedHeaderPadding: EdgeInsets.all(0),
  expansionCallback: (int index, bool isExpanded) {
    setState(() {
      _isOpenList[index] = !isExpanded;
    });
  },
  children: _buildExpansionPanels(),
)
```

위 코드에서 `_buildExpansionPanels()`는 ExpansionPanel의 리스트를 생성하는 메서드입니다. 이 메서드에서는 ExpansionPanel을 생성하여 리스트에 추가하는 작업을 수행합니다. 각 ExpansionPanel의 헤더와 내용은 위젯으로 구현되어야 합니다.

```dart
List<ExpansionPanel> _buildExpansionPanels() {
  return _dataList.map<ExpansionPanel>((data) {
    return ExpansionPanel(
      headerBuilder: (BuildContext context, bool isExpanded) {
        return ListTile(
          title: Text(data.header),
        );
      },
      body: ListTile(
        title: Text(data.content),
      ),
      isExpanded: _isOpenList[_dataList.indexOf(data)],
    );
  }).toList();
}
```

위 코드에서 `_dataList`는 ExpansionPanel이 표시할 데이터를 담고 있는 리스트입니다. ExpansionPanel은 headerBuilder와 body로 구성되어 있으며, 헤더와 내용은 위에서 정의한 데이터를 사용하여 표시됩니다.

## ExpansionPanelList 사용 예시

다음은 ExpansionPanelList를 사용하여 다중 확장 패널을 관리하는 예시입니다.

```dart
class ExpansionPanelListExample extends StatefulWidget {
  @override
  _ExpansionPanelListExampleState createState() => _ExpansionPanelListExampleState();
}

class _ExpansionPanelListExampleState extends State<ExpansionPanelListExample> {
  List<Data> _dataList = [
    Data(header: 'Header 1', content: 'Content 1'),
    Data(header: 'Header 2', content: 'Content 2'),
    Data(header: 'Header 3', content: 'Content 3'),
  ];
  List<bool> _isOpenList = [false, false, false];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('ExpansionPanelList Example'),
      ),
      body: SingleChildScrollView(
        child: ExpansionPanelList(
          elevation: 1,
          expandedHeaderPadding: EdgeInsets.all(0),
          expansionCallback: (int index, bool isExpanded) {
            setState(() {
              _isOpenList[index] = !isExpanded;
            });
          },
          children: _buildExpansionPanels(),
        ),
      ),
    );
  }

  List<ExpansionPanel> _buildExpansionPanels() {
    return _dataList.map<ExpansionPanel>((data) {
      return ExpansionPanel(
        headerBuilder: (BuildContext context, bool isExpanded) {
          return ListTile(
            title: Text(data.header),
          );
        },
        body: ListTile(
          title: Text(data.content),
        ),
        isExpanded: _isOpenList[_dataList.indexOf(data)],
      );
    }).toList();
  }
}

class Data {
  final String header;
  final String content;

  Data({required this.header, required this.content});
}
```

위 예시 코드를 실행하면 ExpansionPanelList가 표시되며, 헤더를 클릭하면 해당 패널의 내용이 확장되거나 축소됩니다.

## 마무리

이번 글에서는 ExpansionPanelList 위젯을 사용하여 다중 확장 패널을 관리하는 방법에 대해 알아보았습니다. ExpansionPanelList의 기능을 활용하여 개발하면 다중 확장 패널을 간편하게 관리할 수 있습니다. 참고로, ExpansionPanelList 위젯은 Material Design의 패널 컨트롤을 제공하므로, 모바일 앱에서 다양한 확장 패널을 구성할 때 유용하게 사용할 수 있습니다.

참고 자료:
- [Flutter ExpansionPanelList documentation](https://api.flutter.dev/flutter/material/ExpansionPanelList-class.html)
- [Flutter ExpansionPanel documentation](https://api.flutter.dev/flutter/material/ExpansionPanel-class.html)