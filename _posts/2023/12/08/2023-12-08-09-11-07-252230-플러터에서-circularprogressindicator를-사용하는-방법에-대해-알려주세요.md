---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator를 사용하는 방법에 대해 알려주세요."
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

다음은 CircularProgressIndicator를 사용하는 방법입니다.

### 1. 기본 CircularProgressIndicator 사용

```dart
import 'package:flutter/material.dart';

class MyLoadingWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(),
    );
  }
}
```

### 2. 특정 색상 및 두께로 설정

```dart
import 'package:flutter/material.dart';

class MyCustomLoadingWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(
        valueColor: AlwaysStoppedAnimation<Color>(Colors.blue), // 색상 설정
        strokeWidth: 5, // 두께 설정
      ),
    );
  }
}
```

### 확인해야 할 점
- CircularProgressIndicator는 작업이 진행 중임을 나타내므로, 작업이 완료되면 화면에서 제거되어야 합니다.

CircularProgressIndicator를 사용하여 앱에서 작업이 진행 중임을 사용자에게 알릴 수 있습니다. 위 코드를 사용하여 간단히 CircularProgressIndicator를 구현할 수 있습니다.

더 자세한 내용은 [공식 문서](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)를 확인하시기 바랍니다.