---
layout: post
title: "[flutter] Scaffold에서 persistentFooterButtons를 클릭했을 때의 동작을 정의하는 방법은 어떻게 되나요?"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

우선, `Scaffold` 위젯을 생성한 후 `persistentFooterButtons` 속성에 버튼 위젯을 추가합니다. 각 버튼은 `FlatButton`이나 `ElevatedButton`과 같은 위젯으로 생성할 수 있습니다.

```dart
Scaffold(
  appBar: AppBar(
    title: Text('Persistent Footer Buttons Example'),
  ),
  persistentFooterButtons: <Widget>[
    FlatButton(
      onPressed: () {
        // 첫 번째 버튼을 클릭했을 때의 동작을 여기에 정의합니다.
      },
      child: Text('Button 1'),
    ),
    ElevatedButton(
      onPressed: () {
        // 두 번째 버튼을 클릭했을 때의 동작을 여기에 정의합니다.
      },
      child: Text('Button 2'),
    ),
  ],
  body: Center(
    child: Text(
      'Click the persistent footer buttons!',
    ),
  ),
);
```

각 버튼의 `onPressed` 콜백에 클릭했을 때 실행되길 원하는 동작을 정의하면 됩니다.

이러한 방식으로 `persistentFooterButtons`를 사용하여 클릭했을 때의 동작을 정의할 수 있습니다.