---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 사용자의 입력을 대기할 때 로딩 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

사용자가 앱에서 어떤 작업을 수행할 때 로딩이 길어질 수 있다면, 앱이 작업을 수행하는 동안 로딩 상태를 표시하는 것이 중요합니다. 이를 위해 다양한 방법 중 하나는 CircularProgressIndicator를 사용하는 것입니다. CircularProgressIndicator는 작업이 진행 중임을 사용자에게 시각적으로 알려줄 수 있는 간편하고 효과적인 방법입니다.

```dart
import 'package:flutter/material.dart';

class MyLoadingScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: CircularProgressIndicator(),
    );
  }
}
```

위의 코드에서 볼 수 있듯이, CircularProgressIndicator를 사용하여 로딩 상태를 표시하는 것은 매우 간단합니다. 위 코드는 Center 위젯 안에 CircularProgressIndicator를 넣어 화면 중앙에 로딩 상태를 표시하는 예시입니다.

로딩이 길어질 수 있는 모든 작업의 시작과 끝에 CircularProgressIndicator를 추가하여 사용자에게 작업이 진행 중임을 시각적으로 전달할 수 있습니다.

위의 예시 코드를 참고하여, CircularProgressIndicator를 사용하여 앱에서 로딩 상태를 표시하는 방법을 익혀보시기 바랍니다.