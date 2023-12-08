---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션의 플로팅 액션 버튼 터치 시 로딩 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

안녕하세요! 플러터로 애플리케이션을 개발하는 동안 플로팅 액션 버튼을 터치했을 때 로딩 상태를 표시하는 과정을 알아보겠습니다.

## 1. CircularProgressIndicator 생성

먼저, 플로팅 액션 버튼을 터치했을 때 표시될 로딩 상태를 위해 `CircularProgressIndicator` 위젯을 생성합니다.

```dart
CircularProgressIndicator(
  backgroundColor: Colors.transparent,
  valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
),
```

위 코드에서 `backgroundColor`는 로딩 인디케이터의 배경 색상을 설정하고, `valueColor`는 로딩 인디케이터의 색상을 설정합니다.

## 2. 액션 버튼 터치 시 로딩 상태 표시

이제, 플로팅 액션 버튼을 터치할 때 `setState` 함수를 사용하여 해당 로딩 상태를 표시할 수 있습니다.

```dart
FloatingActionButton(
  onPressed: () {
    setState(() {
      _isLoading = true; // _isLoading은 bool 타입의 상태 변수
    });
    // 여기에 데이터를 가져오거나 작업을 수행하는 코드를 추가할 수 있습니다.
    // 작업이 완료되면 setState를 사용하여 _isLoading을 false로 변경합니다.
  },
  child: Icon(Icons.add),
),
```

위 코드에서 `_isLoading` 변수는 로딩 상태를 나타내는 bool 타입의 변수입니다.

이제, 플로팅 액션 버튼을 터치했을 때 `CircularProgressIndicator`가 표시되도록 설정하고, 작업이 완료되면 로딩 상태를 숨기도록 코드를 구성할 수 있습니다.

이상입니다! 이제 flutter를 사용하여 플로팅 액션 버튼 터치 시 로딩 상태를 표시하는 방법을 알아보았습니다. 추가 질문이 있다면 언제든지 물어보세요!