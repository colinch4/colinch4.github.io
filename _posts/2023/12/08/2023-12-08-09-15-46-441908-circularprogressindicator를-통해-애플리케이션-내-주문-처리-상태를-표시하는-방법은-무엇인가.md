---
layout: post
title: "[flutter] CircularProgressIndicator를 통해 애플리케이션 내 주문 처리 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

**1. CircularProgressIndicator 추가:**
먼저, 주문 처리 상태를 나타내는 화면 또는 위젯에 CircularProgressIndicator를 추가합니다.

```dart
Center(
  child: CircularProgressIndicator(),
),
```

위와 같이 Center 위젯 내에 CircularProgressIndicator를 추가하면 중앙에 표시됩니다.

**2. 주문 처리 상태에 따른 CircularProgressIndicator 제어:**
주문 처리가 시작될 때와 완료될 때 CircularProgressIndicator를 보여주거나 숨기기 위해 상태 변수를 활용합니다.

```dart
bool _isOrderProcessing = false;

...

Center(
  child: _isOrderProcessing ? CircularProgressIndicator() : Container(), // 주문 처리 중일 때만 CircularProgressIndicator 표시
),
```

위 예제에서 `_isOrderProcessing` 변수는 주문 처리 상태를 나타내는 불리언입니다. 주문 처리가 시작되면 `_isOrderProcessing`를 `true`로 설정하여 CircularProgressIndicator가 표시되고, 주문 처리가 완료되면 다시 `false`로 설정하여 숨깁니다.

**3. 주문 처리 상태 업데이트:**
실제 주문 처리 과정에서 상태를 업데이트할 때마다 `_isOrderProcessing` 변수를 변경하여 CircularProgressIndicator를 제어합니다.

```dart
void _processOrder() {
  setState(() {
    _isOrderProcessing = true; // 주문 처리가 시작됨을 나타내기 위해 true로 설정
  });

  // 주문 처리 로직 수행

  setState(() {
    _isOrderProcessing = false; // 주문 처리가 완료됨을 나타내기 위해 false로 설정
  });
}
```

위 예제에서 `_processOrder` 함수는 주문 처리 메서드를 호출하고, 주문 처리가 시작되거나 완료될 때 `_isOrderProcessing` 상태를 업데이트합니다.

이와 같은 방식으로 CircularProgressIndicator를 사용하여 주문 처리 상태를 시각적으로 나타낼 수 있습니다.