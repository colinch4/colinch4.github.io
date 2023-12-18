---
layout: post
title: "[flutter] 플러터에서 LinearProgressIndicator의 위치 조절 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

LinearProgressIndicator는 진행 상황을 시각적으로 나타내는 위젯으로, 기본적으로 가로 방향으로 화면 상단에 표시됩니다. 그러나 경우에 따라 원하는 위치에 배치해야 하는 경우가 있을 수 있습니다. 이를 조절하는 방법은 간단합니다.

```dart
Center(
  child: LinearProgressIndicator(
    // indicator 속성 설정
  ),
),
```

LinearProgressIndicator를 Center 위젯 내에 넣으면 화면 중앙에 배치됩니다. 당신의 UI 레이아웃에 맞게 다양한 방식으로 LinearProgressIndicator의 위치를 조절할 수 있습니다.

더 자세한 내용은 [공식 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)를 참고하십시오.