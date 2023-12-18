---
layout: post
title: "[flutter] 플러터 LinearProgressIndicator 사용 예제"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터에서 `LinearProgressIndicator`는 진행률을 보여주는 데 사용됩니다. 이 예제에서는 `LinearProgressIndicator`를 어떻게 사용하는지 살펴보겠습니다.

## 선형 진행률 인디케이터 추가

선형 진행률 인디케이터는 앱 화면에서 진행 중인 작업의 진행률을 표시하는 데 유용합니다. 아래는 `LinearProgressIndicator`를 사용하여 화면에 선형 진행률 인디케이터를 추가하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Linear Progress Indicator Example'),
        ),
        body: Center(
          child: LinearProgressIndicator(
            backgroundColor: Colors.grey,
            valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
          ),
        ),
      ),
    );
  }
}
```

위의 코드에서 `LinearProgressIndicator` 위젯을 사용하여 앱의 메인 화면에 선형 진행률 인디케이터를 추가했습니다. `backgroundColor` 속성을 사용하여 인디케이터의 배경색을 설정하고, `valueColor` 속성을 사용하여 인디케이터의 값에 따라 색상을 변경했습니다.

## 결론

이 예제를 통해 `LinearProgressIndicator`를 사용하여 플러터 앱에 선형 진행률 인디케이터를 추가하는 방법을 배웠습니다. 이를 응용하여 앱의 다양한 화면에 진행률 인디케이터를 쉽게 추가할 수 있습니다.

더 많은 정보는 [공식 플러터 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)에서 확인할 수 있습니다.

이상으로 "플러터 LinearProgressIndicator 사용 예제"를 마치겠습니다. 감사합니다!

## Reference
- [플러터 API 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)