---
layout: post
title: "[flutter] 플러터에서 LinearProgressIndicator를 사용한 화면 전환 효과 적용 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터 앱을 개발하다 보면 사용자가 이벤트를 기다리는 동안에 화면 전환 효과를 제공하기 위해 진행 바를 표시하는 경우가 있습니다. 이런 경우, **LinearProgressIndicator** 위젯을 사용하여 이를 구현할 수 있습니다.

이번 포스트에서는 **LinearProgressIndicator**를 사용하여 화면 전환 효과를 적용하는 방법을 살펴보겠습니다.

## 1. LinearProgressIndicator 추가

먼저, **LinearProgressIndicator**를 화면에 추가해야 합니다. 이를 위해 다음과 같이 코드를 작성합니다.

```dart
import 'package:flutter/material.dart';

class MyScreen extends StatefulWidget {
  @override
  _MyScreenState createState() => _MyScreenState();
}

class _MyScreenState extends State<MyScreen> {
  bool _isLoading = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('My Screen'),
      ),
      body: Stack(
        children: <Widget>[
          // 여기에 나타낼 내용을 추가합니다.

          _isLoading
              ? LinearProgressIndicator(
                  backgroundColor: Colors.grey,
                  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
                )
              : Container(),
        ],
      ),
    );
  }
}
```

위 예제 코드에서 `_isLoading` 변수를 사용하여 로딩 상태를 관리하고, 그에 따라 **LinearProgressIndicator**를 표시하거나 숨김 처리하고 있습니다.

## 2. 화면 전환 시 LinearProgressIndicator 제어

화면 전환 시에는 `_isLoading` 변수를 true로 설정하여 **LinearProgressIndicator**를 표시하고, 데이터를 불러오는 작업이 끝나면 다시 false로 변경하여 **LinearProgressIndicator**를 숨깁니다. 이를 통해 사용자에게 진행 상황을 시각적으로 보여줄 수 있습니다.

```dart
// 예를 들어, 특정 버튼을 눌렀을 때 데이터를 불러오는 작업을 한다고 가정합니다.
void _loadData() {
  setState(() {
    _isLoading = true;
  });

  // 데이터를 불러오는 비동기 작업을 수행합니다.
  fetchData().then((data) {
    // 데이터 불러오기 완료 후
    setState(() {
      _isLoading = false;
    });
  });
}
```

위의 `_loadData` 메서드는 데이터를 불러오는 중간에 **LinearProgressIndicator**를 표시하고, 데이터를 성공적으로 불러오면 **LinearProgressIndicator**를 숨기는 예시입니다.

이제 **LinearProgressIndicator**를 사용하여 플러터 앱의 화면 전환 효과를 구현할 수 있습니다. 위의 예제를 참고하여 앱 개발에 활용해 보세요!