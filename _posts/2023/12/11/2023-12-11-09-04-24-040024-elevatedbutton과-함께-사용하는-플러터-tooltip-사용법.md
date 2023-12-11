---
layout: post
title: "[flutter] ElevatedButton과 함께 사용하는 플러터 Tooltip 사용법"
description: " "
date: 2023-12-11
tags: [flutter]
comments: true
share: true
---

플러터에서 버튼에 마우스를 올렸을 때 툴팁을 표시하는 일반적인 방법은 `Tooltip` 위젯을 사용하는 것입니다. `Tooltip` 위젯을 `ElevatedButton`과 함께 사용하는 방법을 알아보겠습니다.

## 1. ElevatedButton에 Tooltip 추가하기

`ElevatedButton`에 `Tooltip`을 추가하려면 다음과 같이 하십시오.

```dart
ElevatedButton(
  onPressed: () {
    // 버튼을 눌렀을 때 수행할 작업
  },
  child: Tooltip(
    message: '이 버튼을 누르면 작업을 수행합니다.',
    child: Text('버튼'),
  ),
)
```

위의 코드에서 `ElevatedButton`의 `child` 속성에 `Tooltip`을 추가하여 버튼 자체를 툴팁으로 래핑하였습니다.

## 2. 툴팁 위치 지정하기

툴팁이 표시될 위치를 지정할 수도 있습니다. 예를 들어, 툴팁을 버튼 상단에 표시하려면 다음과 같이 하면 됩니다.

```dart
ElevatedButton(
  onPressed: () {
    // 버튼을 눌렀을 때 수행할 작업
  },
  child: Tooltip(
    message: '이 버튼을 누르면 작업을 수행합니다.',
    child: Text('버튼'),
    preferBelow: false, // 툴팁을 위쪽에 표시
  ),
)
```

## 3. 마무리

이제 `ElevatedButton`과 함께 `Tooltip` 위젯을 사용하는 방법에 대해 알아보았습니다. 이를 활용하여 사용자가 버튼에 마우스를 올렸을 때 추가 설명을 제공하는 효과적인 방법으로 활용할 수 있습니다.

참고문헌:
- [플러터 공식 문서](https://api.flutter.dev/flutter/material/Tooltip-class.html)