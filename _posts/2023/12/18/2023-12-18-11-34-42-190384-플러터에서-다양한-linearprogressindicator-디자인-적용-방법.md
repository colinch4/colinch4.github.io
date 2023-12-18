---
layout: post
title: "[flutter] 플러터에서 다양한 LinearProgressIndicator 디자인 적용 방법"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

플러터에서 `LinearProgressIndicator` 위젯은 작업이나 페이지 로딩 상태를 시각적으로 표시하는 데 사용됩니다. 기본 스타일도 있지만, 경우에 따라 다양한 디자인을 적용하고 싶을 수 있습니다. 이번 포스트에서는 플러터에서 `LinearProgressIndicator`에 다양한 디자인을 적용하는 방법을 살펴보겠습니다.

## 기본적인 LinearProgressIndicator

가장 먼저, `LinearProgressIndicator`를 기본적으로 생성하는 방법을 살펴보겠습니다. 

```dart
LinearProgressIndicator()
```

## 색상 변경하기

`LinearProgressIndicator`의 색상을 변경하려면 `valueColor` 속성을 사용하여 색상을 지정해야 합니다.

```dart
LinearProgressIndicator(
  valueColor: AlwaysStoppedAnimation<Color>(Colors.red),
)
```

## 진행률 바꾸기

진행률을 변경하려면 `value` 속성을 사용하여 값을 지정합니다.

```dart
LinearProgressIndicator(
  value: 0.5,
)
```

## 배경색 변경하기

`LinearProgressIndicator`의 배경색을 변경하려면 `backgroundColor` 속성을 사용하여 배경색을 지정할 수 있습니다.

```dart
LinearProgressIndicator(
  backgroundColor: Colors.grey,
)
```

## 요약

플러터에서 `LinearProgressIndicator`를 다양한 디자인으로 꾸밀 수 있는 여러 가지 방법에 대해 살펴봤습니다. 이러한 옵션들을 활용하여 앱의 디자인을 더욱 다채롭게 만들어보세요.