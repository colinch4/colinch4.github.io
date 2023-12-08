---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator란 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

`CircularProgressIndicator` 위젯은 다양한 속성을 가지고 있어서 디자인적으로 수정할 수 있습니다. 예를 들어, 다양한 크기와 색상을 설정할 수 있으며, 진행 바의 두께를 조절할 수도 있습니다.

아래는 CircularProgressIndicatior를 사용한 예시 코드입니다:

```dart
Center(
  child: CircularProgressIndicator(
    valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
    strokeWidth: 4,
  ),
)
```

이 코드에서는 `valueColor`를 사용하여 프로그레스 바의 색상을 파란색으로 설정하고, `strokeWidth`를 사용하여 프로그레스 바의 두께를 4로 설정하였습니다.

`CircularProgressIndicator`는 사용자에게 앱이 작업을 수행 중임을 시각적으로 알려주는 데에 유용한 위젯입니다. 자세한 내용은 공식 플러터 문서를 참고하시기 바랍니다.