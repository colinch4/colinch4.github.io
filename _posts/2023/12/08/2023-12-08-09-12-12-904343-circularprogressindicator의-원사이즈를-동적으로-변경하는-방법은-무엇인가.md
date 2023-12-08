---
layout: post
title: "[flutter] CircularProgressIndicator의 원사이즈를 동적으로 변경하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

우선, CircularProgressIndicator 위젯을 만들고, 이를 크기를 동적으로 변경할 수 있는 StatefulWidget에 포함시킵니다.

```dart
import 'package:flutter/material.dart';

class DynamicCircularProgressIndicator extends StatefulWidget {
  @override
  _DynamicCircularProgressIndicatorState createState() => _DynamicCircularProgressIndicatorState();
}

class _DynamicCircularProgressIndicatorState extends State<DynamicCircularProgressIndicator> {
  double _indicatorSize = 50.0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            CircularProgressIndicator(
              valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
              strokeWidth: 5,
              value: 0.5,
              backgroundColor: Colors.grey,
              semanticsLabel: 'Loading',
              semanticsValue: 'Loading',
              // 동적으로 변경되는 크기값 적용
              // 아래 크기는 예제일 뿐, 프로젝트에 맞게 원하는 크리값을 적용할 것
              // _indicatorSize의 값을 조절하여 크기를 변경
              valueSize: _indicatorSize,
            ),
            SizedBox(
              height: 20,
            ),
            RaisedButton(
              onPressed: () {
                setState(() {
                  // Example: 크기를 클릭할 때마다 20 증가
                  _indicatorSize += 20;
                });
              },
              child: Text('Increase Size'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위의 코드는 CircularProgressIndicator를 동적으로 변경할 수 있는 StatefulWidget을 구현한 것입니다. CircularProgressIndicator 위젯의 valueSize 속성을 사용하여 크기를 동적으로 조절할 수 있습니다. onPressed 콜백에서 setState를 호출하여 _indicatorSize 값을 조절하여 크기를 변경하였습니다.

참고문헌:
- https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html