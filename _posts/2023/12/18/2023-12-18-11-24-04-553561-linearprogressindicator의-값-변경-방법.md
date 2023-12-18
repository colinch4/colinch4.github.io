---
layout: post
title: "[flutter] LinearProgressIndicator의 값 변경 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

이번에는 Flutter 앱에서 LinearProgressIndicator의 값을 변경하는 방법에 대해 알아보겠습니다.

1. **LinearProgressIndicator 생성**

먼저, LinearProgressIndicator를 생성하고 값을 변경하는 방법을 알아보겠습니다. 아래는 기본적인 LinearProgressIndicator 코드의 예시입니다.

```dart
LinearProgressIndicator()
```

2. **값 변경**

이제 LinearProgressIndicator의 값을 변경해 보겠습니다. LinearProgressIndicator는 'value' 속성을 통해 진행 상태를 표시합니다. 아래의 예시 코드는 LinearProgressIndicator의 값을 0.5로 변경하는 예시입니다.

```dart
LinearProgressIndicator(value: 0.5)
```

위와 같은 방법으로 'value' 속성을 사용하여 LinearProgressIndicator의 값을 동적으로 변경할 수 있습니다.

이상으로, Flutter 앱에서 LinearProgressIndicator의 값을 변경하는 방법에 대해 알아보았습니다. 관련하여 추가적인 정보는 [공식 문서](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)를 참고하시기 바랍니다.