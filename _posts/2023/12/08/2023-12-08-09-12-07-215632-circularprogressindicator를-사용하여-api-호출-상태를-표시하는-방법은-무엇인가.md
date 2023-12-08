---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 API 호출 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

다음은 CircularProgressIndicator를 사용하여 API 호출 상태를 표시하는 간단한 예제입니다.

먼저, API 호출 상태를 관리하는 상태 변수를 만듭니다. 이 변수를 사용하여 API가 호출되는 동안 CircularProgressIndicator를 보여주거나 숨깁니다.

```dart
bool isLoading = false;
```

다음으로, API를 호출하는 함수에서 상태를 관리합니다. API 호출이 시작되면 isLoading을 true로 설정하고, 호출이 완료되면 false로 다시 설정합니다.

```dart
void fetchData() async {
  setState(() {
    isLoading = true;
  });

  try {
    // API 호출 로직
    // ...

    setState(() {
      isLoading = false;
    });
  } catch (error) {
    setState(() {
      isLoading = false;
    });
    // 오류 처리 로직
    // ...
  }
}
```

마지막으로, CircularProgressIndicator를 사용하여 API 호출 상태를 표시합니다. isLoading이 true인 경우에만 CircularProgressIndicator를 표시하도록 조건부 렌더링을 사용합니다.

```dart
isLoading ? CircularProgressIndicator() : Container(),
```

이제 API 호출 상태를 표시하기 위해 CircularProgressIndicator를 사용하는 방법을 알아보았습니다. 이제 이 예제를 참고하여 원하는 기능을 구현할 수 있을 것입니다.