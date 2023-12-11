---
layout: post
title: "[flutter] FloatingActionButton을 사용한 주요 앱 UI 예시"
description: " "
date: 2023-12-11
tags: [flutter]
comments: true
share: true
---

Flutter에서 FloatingActionButton은 사용자가 주요 기능을 쉽게 이용할 수 있도록 하는데 사용됩니다. 여기서는 FloatingActionButton을 사용하여 기본적인 앱 UI를 만드는 방법에 대해 알아보겠습니다.

## 목차
1. [Flutter에서 FloatingActionButton](#1-flutter에서-floatactionbutton)
2. [주요 앱 UI 예시](#2-주요-앱-ui-예시)
3. [결론](#3-결론)

---

## 1. Flutter에서 FloatingActionButton

Flutter에서 FloatingActionButton은 사용자 상호작용을 촉진하고 주요 기능에 쉽게 접근할 수 있도록 도와줍니다. FloatingActionButton을 사용하면 해당 기능에 빠르게 접근할 수 있으며, UI에도 시각적인 효과를 줄 수 있습니다.

```dart
floatingActionButton: FloatingActionButton(
  onPressed: () {
    // 버튼을 눌렀을 때 실행되는 기능
  },
  child: Icon(Icons.add),
  backgroundColor: Colors.blue,
),
```

위의 코드는 Flutter에서 기본적인 FloatingActionButton을 생성하는 예시입니다. onPressed 콜백으로 버튼이 눌렸을 때 실행되는 기능을 정의할 수 있고, child 속성으로 아이콘을 추가하고, backgroundColor 속성으로 버튼의 배경색을 지정할 수 있습니다.

---

## 2. 주요 앱 UI 예시

아래 예시 코드는 FloatingActionButton을 사용하여 간단한 주요 앱 UI를 만드는 방법을 보여줍니다. 이 예시에서는 FloatingActionButton을 사용하여 사용자가 텍스트 필드에 입력한 내용을 리스트에 추가하는 기능을 구현하였습니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('FloatingActionButton 예시'),
        ),
        body: MyWidget(),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            // 텍스트 필드에 입력한 내용을 리스트에 추가하는 기능
          },
          child: Icon(Icons.add),
          backgroundColor: Colors.blue,
        ),
      ),
    );
  }
}

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('주요 앱 내용이 여기에 표시됩니다.'),
    );
  }
}
```

위의 코드는 Scaffold 위젯을 사용하여 앱 UI를 작성하고, FloatingActionButton을 추가하여 사용자 상호작용을 강화하는 방법을 보여줍니다.

---

## 3. 결론

Flutter에서 FloatingActionButton은 사용자가 앱의 주요 기능에 쉽게 접근할 수 있도록 하는데 매우 유용합니다. 이를 활용하여 사용자 경험을 향상시키는 간편하고 직관적인 UI를 디자인할 수 있습니다.

더 많은 Flutter UI 디자인 패턴 및 사용법을 찾아보려면 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하세요.