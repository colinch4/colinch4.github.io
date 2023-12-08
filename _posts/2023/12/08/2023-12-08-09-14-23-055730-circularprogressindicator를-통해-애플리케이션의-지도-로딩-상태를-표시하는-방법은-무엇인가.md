---
layout: post
title: "[flutter] CircularProgressIndicator를 통해 애플리케이션의 지도 로딩 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

애플리케이션에서 지도를 로딩할 때 사용자에게 로딩 상태를 시각적으로 전달하는 것은 중요합니다. Flutter에서는 이를 위해 **CircularProgressIndicator** 위젯을 사용할 수 있습니다. 이 위젯은 동그란 형태의 로딩 인디케이터를 제공하며, 지도가 로딩되는 동안 화면에 표시될 수 있습니다.

## CircularProgressIndicator 추가하기

먼저, **CircularProgressIndicator**를 사용하기 위해 Flutter 프로젝트의 위젯 트리에 이를 추가해야 합니다. 아래는 이를 수행하는 간단한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

class MapScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('지도'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('지도를 로딩 중입니다.'),
            CircularProgressIndicator(), // 이 부분이 추가되었습니다
          ],
        ),
      ),
    );
  }
}
```

위 코드에서 **CircularProgressIndicator** 위젯은 **Center** 위젯 내의 **Column** 위젯에 추가되어 있습니다. 이로써 지도 로딩 중에는 "지도를 로딩 중입니다"라는 메시지와 함께 로딩 인디케이터가 화면에 나타나게 됩니다.

**CircularProgressIndicator** 위젯을 추가하고 나면, 지도가 로딩되는 동안에는 화면에 로딩 인디케이터가 표시됩니다.

## 결론

Flutter의 **CircularProgressIndicator**를 사용하면 간단하게 지도 또는 다른 내용의 로딩 상태를 시각적으로 나타낼 수 있습니다. 이는 사용자에게 현재 진행 중인 작업을 알리고, 대기하고 있는 동안 불편함을 덜어줄 수 있습니다.

참고문헌:
- Flutter 공식 문서: https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html