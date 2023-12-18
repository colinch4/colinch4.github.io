---
layout: post
title: "[flutter] LinearProgressIndicator의 높이 조절하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter에서 `LinearProgressIndicator`를 사용할 때 기본 높이가 마음에 들지 않는다면 어떻게 조절할 수 있을까요? 이 글에서는 `LinearProgressIndicator`의 높이를 조절하는 방법을 알아보겠습니다.

## 1. 높이 조절 방법

`LinearProgressIndicator`의 높이를 조절하려면 `SizedBox`나 `Container`와 같은 위젯을 사용하여 `LinearProgressIndicator`를 감싸주면 됩니다. 아래는 예시 코드입니다.

```dart
Container(
  height: 10,  // 높이 조절
  child: LinearProgressIndicator(),
)
```

위의 예제에서 `Container` 위젯의 `height` 속성을 조절하여 `LinearProgressIndicator`의 높이를 변경할 수 있습니다.

## 2. 추가적인 스타일링

`LinearProgressIndicator`의 높이 조절 이외에도 배경색, 전경색 등의 추가적인 스타일을 적용할 수 있습니다. 예를 들면, `LinearProgressIndicator`의 두께, 각도 등을 조절할 수 있습니다.

```dart
Container(
  height: 10,  // 높이 조절
  child: LinearProgressIndicator(
    backgroundColor: Colors.grey,  // 배경색
    valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),  // 전경색
  ),
)
```

## 3. 결론

`LinearProgressIndicator`의 높이를 조절하는 방법과 추가적인 스타일링에 대해 알아보았습니다. 필요에 따라 위젯을 감싸거나 기타 스타일 속성을 이용하여 `LinearProgressIndicator`를 원하는 모양으로 꾸밀 수 있습니다.

더 많은 정보는 [Flutter 공식 문서](https://flutter.dev/docs/development/ui/widgets/material/LinearProgressIndicator)를 참고하세요.