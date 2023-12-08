---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator를 이용한 데이터 로딩 과정을 표시하는 방법에 대해 알려주세요."
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

## 1. CircularProgressIndicator 추가

가장 먼저, CircularProgressIndicator를 표시할 화면에 해당 위젯을 추가해야 합니다. 다음과 같이 CircularProgressIndicator를 화면에 추가할 수 있습니다.

```dart
import 'package:flutter/material.dart';

class LoadingScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(),
    );
  }
}
```

위 코드에서 `LoadingScreen`은 데이터 로딩 중에 보여질 화면을 구성하는데 사용되는 예시입니다. `CircularProgressIndicator` 위젯을 사용하여 화면의 중앙에 로딩 애니메이션을 배치하고 있습니다.

## 2. 데이터 로딩 상태에 따른 화면 전환

위젯을 추가한 후에는 데이터 로딩 상태에 따라 해당 위젯을 화면에 표시하는 방법을 적용해야 합니다. 예를 들어, `FutureBuilder` 위젯을 사용하여 비동기 데이터 로딩 동안에 로딩 화면을 보여주고, 데이터 로딩이 완료된 후에는 실제 데이터가 보여지도록 할 수 있습니다.

아래 코드는 `FutureBuilder`를 사용하여 데이터 로딩 상태에 따라 화면을 전환하는 예시입니다.

```dart
FutureBuilder(
  future: fetchData(), // 비동기 데이터 로딩 함수 호출
  builder: (context, snapshot) {
    if (snapshot.connectionState == ConnectionState.waiting) {
      return LoadingScreen(); // 데이터 로딩 중에는 로딩 화면을 표시
    } else {
      if (snapshot.hasError) {
        return ErrorScreen(); // 데이터 로딩 중에 오류가 발생한 경우 오류 화면을 표시
      } else {
        return DataScreen(snapshot.data); // 데이터 로딩이 완료된 경우 실제 데이터 화면을 표시
      }
    }
  },
)
```

위에서 `fetchData()`는 실제 데이터를 비동기적으로 로딩하는 함수를 가정하고 있습니다. `FutureBuilder`는 이 함수를 호출하고, 데이터 로딩 상태에 따라 적절한 화면을 보여줍니다.

이제 해당 코드를 적용하여 데이터 로딩 중에 CircularProgressIndicator를 화면에 표시할 수 있을 것입니다.