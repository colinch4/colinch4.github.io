---
layout: post
title: "[flutter] CircularProgressIndicator의 색상을 변경하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

다음은 CircularProgressIndicator의 색상을 변경하는 예제 코드입니다.

```dart
CircularProgressIndicator(
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
)
```

위 예제에서 valueColor를 통해 CircularProgressIndicator의 색상을 변경할 수 있습니다. 여기서 Colors.blue는 사용자가 변경하고 싶은 원하는 색상으로 대체할 수 있습니다.

더 많은 정보를 원하시면 [공식 Flutter 문서](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)를 참고해주세요.