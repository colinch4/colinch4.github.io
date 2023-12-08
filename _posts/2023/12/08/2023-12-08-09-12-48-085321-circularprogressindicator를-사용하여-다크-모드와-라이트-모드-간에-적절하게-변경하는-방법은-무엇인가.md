---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 다크 모드와 라이트 모드 간에 적절하게 변경하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

우선, StatefulWidget을 사용하여 빌더 메서드 안에서 현재 테마 모드를 확인합니다.

```dart
class MyLoadingWidget extends StatefulWidget {
  @override
  _MyLoadingWidgetState createState() => _MyLoadingWidgetState();
}

class _MyLoadingWidgetState extends State<MyLoadingWidget> {
  @override
  Widget build(BuildContext context) {
    ThemeData theme = Theme.of(context);
    bool isDarkMode = theme.brightness == Brightness.dark;

    return Center(
      child: CircularProgressIndicator(
        // 다크 모드일 때와 라이트 모드일 때의 색상을 조정합니다.
        valueColor: isDarkMode
            ? AlwaysStoppedAnimation<Color>(Colors.white)
            : AlwaysStoppedAnimation<Color>(Colors.blue),
      ),
    );
  }
}
```

이렇게 하면 CircularProgressIndicator가 현재 테마 모드에 맞게 적절하게 변경됩니다.

더 많은 정보를 원하시면 [여기](https://api.flutter.dev/flutter/material/Theme-class.html)를 참고해 주세요.