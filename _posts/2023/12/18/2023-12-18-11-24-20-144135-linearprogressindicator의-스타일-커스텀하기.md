---
layout: post
title: "[flutter] LinearProgressIndicator의 스타일 커스텀하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 애플리케이션을 개발하다 보면 가끔 기본적인 위젯을 커스텀해야 하는 상황이 있습니다. 이번 글에서는 `LinearProgressIndicator` 위젯의 스타일을 커스텀하는 방법을 알아보겠습니다.

## 1. LinearProgressIndicator의 기본 스타일

먼저, `LinearProgressIndicator`의 기본 스타일을 확인해보겠습니다.

```dart
LinearProgressIndicator(
  value: 0.5,
);
```

## 2. LinearProgressIndicator의 스타일 커스텀하기

### 2.1. 배경색과 완료된 영역의 색상 변경

`LinearProgressIndicator`의 배경색과 완료된 영역의 색상을 변경하려면 `LinearProgressIndicator`를 `Container`로 감싸고, 각각의 색상을 지정해야 합니다.

```dart
Container(
  child: LinearProgressIndicator(
    value: 0.5,
    backgroundColor: Colors.grey,
    valueColor: AlwaysStoppedAnimation<Color>(Colors.green),
  ),
);
```

### 2.2. 두께 변경

`LinearProgressIndicator`의 두께를 커스텀하려면 `LinearProgressIndicator`의 `LinearProgressIndicator`를 사용하면 됩니다.

```dart
LinearProgressIndicator(
  value: 0.5,
  minHeight: 10,
);
```

### 2.3. 반경 변경

또한, `LinearProgressIndicator`의 완료된 영역의 반경을 변경하려면 `LinearProgressIndicator`를 `Theme`로 감싸고, `ThemeData`를 사용하여 `borderRadius`를 지정하면 됩니다.

```dart
Theme(
  data: ThemeData(
    accentColor: Colors.green,
    primaryColor: Colors.grey,
  ),
  child: LinearProgressIndicator(
    value: 0.5,
  ),
);
```

이렇게 하면 `LinearProgressIndicator`의 스타일을 간단하게 커스텀할 수 있습니다.

## 3. 마치며

이번 글에서는 `LinearProgressIndicator`의 스타일을 커스텀하는 방법을 알아보았습니다. 위젯을 커스텀하는 방법은 다양하기 때문에 상황에 맞게 적절한 방법을 선택하여 사용하면 됩니다.

더 많은 정보를 원하시면 다음 문서를 참고해보세요: [공식 Flutter 문서 - LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)