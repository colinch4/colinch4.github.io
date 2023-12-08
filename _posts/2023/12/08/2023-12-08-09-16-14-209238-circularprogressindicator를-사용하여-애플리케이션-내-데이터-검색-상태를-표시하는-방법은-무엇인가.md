---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션 내 데이터 검색 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter를 사용하여 데이터를 검색하거나 가져올 때, 애플리케이션의 UI 상태를 정보로 업데이트하는 것이 중요합니다. 이를 위해 CircularProgressIndicator를 활용하여 사용자에게 데이터 검색 상태를 전달하는 것이 효과적입니다.

## 1. CircularProgressIndicator Widget 추가

가장 먼저, CircularProgressIndicator Widget을 사용하여 데이터가 검색되는 동안 진행 표시를 표시하기 위해 해당 위젯을 UI에 추가해야 합니다. 

```dart
Center(
  child: CircularProgressIndicator(),
)
```

## 2. 데이터 검색 상태와 연동

데이터 검색 작업을 수행하는 동안, CircularProgressIndicator를 활성화하고, 작업이 완료되면 해당 위젯을 비활성화 해야 합니다. 보통 `Future`나 `async/await`를 사용하여 비동기 작업을 수행하고, 그에 따라 UI를 변경합니다.

```dart
bool _isLoading = false;

void _fetchData() async {
  setState(() {
    _isLoading = true;
  });

  // 비동기 작업 수행
  await fetchData();

  setState(() {
    _isLoading = false;
  });
}
```

## 3. CircularProgressIndicator와 연동된 UI 업데이트

마지막으로, `_isLoading` 변수를 사용하여 CircularProgressIndicator를 표시하고 숨김으로써 UI에 이를 반영합니다.

```dart
Center(
  child: _isLoading ? CircularProgressIndicator() : YourDataWidget(),
)
```

이와 같은 방식으로, CircularProgressIndicator를 사용하여 데이터 검색 또는 가져오기 상태를 사용자에게 시각적으로 전달할 수 있습니다.

이렇게 하면 사용자들은 애플리케이션이 작업을 수행 중임을 알 수 있고, 데이터가 로드될 때까지 기다리고 있음을 인지할 수 있습니다.