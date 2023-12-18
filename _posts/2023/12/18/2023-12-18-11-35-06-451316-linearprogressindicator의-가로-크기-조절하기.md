---
layout: post
title: "[flutter] LinearProgressIndicator의 가로 크기 조절하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter에서 `LinearProgressIndicator` 위젯을 사용하여 앱 로딩 상태를 표시할 수 있습니다. 그러나 기본적으로 `LinearProgressIndicator`는 정해진 크기로 표시되며, 이를 개발자가 직접 조절할 수 있는 방법이 필요합니다.

이 블로그 포스트에서는 `LinearProgressIndicator` 위젯의 가로 크기를 조절하는 방법에 대해 알아보겠습니다.

## `LinearProgressIndicator` 위젯의 가로 크기 조절

`LinearProgressIndicator` 위젯의 가로 크기를 조절하려면 `SizedBox`나 `Container` 등을 사용하여 크기를 지정해주어야 합니다. 아래의 예제 코드는 `LinearProgressIndicator`의 가로 크기를 200으로 지정하는 방법을 보여줍니다.

```dart
Container(
  width: 200.0,
  child: LinearProgressIndicator(),
)
```

위 예제에서 `Container` 위젯을 사용하여 `LinearProgressIndicator`를 감싸고, `width` 속성을 통해 가로 크기를 200으로 설정하였습니다.

## 결론

Flutter에서 `LinearProgressIndicator` 위젯의 가로 크기를 조절하는 방법을 살펴보았습니다. 위 예제를 참고하여 원하는 크기로 `LinearProgressIndicator`를 조절해보세요.

더 많은 정보는 [Flutter 공식 문서](https://flutter.dev/docs/development/ui/widgets/material#LinearProgressIndicator)를 참고하시기 바랍니다.