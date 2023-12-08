---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 동시에 여러 작업이 진행되는 상황을 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱에서 여러 작업이 동시에 실행될 때 사용자에게 진행 상황을 시각적으로 표시하는 것은 중요합니다. **CircularProgressIndicator** 위젯을 사용하여 이를 구현할 수 있습니다. 이 위젯은 작업이 진행 중임을 나타내는 회전하는 원형 프로그레스 바를 제공합니다.

아래는 CircularProgressIndicator를 사용하여 동시에 여러 작업이 진행되는 상황을 표시하는 방법에 대한 예제입니다.

1. **CircularProgressIndicator 추가**

먼저, 해당 작업이 진행 중일 때 CircularProgressIndicator를 화면에 표시할 위치에 해당 위젯을 추가합니다. 예를 들어, 다음과 같이 작성할 수 있습니다.

```dart
    Center(
      child: CircularProgressIndicator(),
    )
```

2. **Future나 비동기 작업과 함께 사용**

또 다른 방법은 **Future**나 비동기 작업과 함께 CircularProgressIndicator를 사용하는 것입니다. 다음은 비동기 작업을 수행하는 동안 CircularProgressIndicator를 보여주는 예제 코드입니다.

```dart
    FutureBuilder<void>(
      future: _yourAsyncTask(),
      builder: (BuildContext context, AsyncSnapshot<void> snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return CircularProgressIndicator();
        } else {
          return YourWidget(); // 완료된 후에 보여줄 내용
        }
      },
    )
```

위에서 **_yourAsyncTask()**는 실제 비동기 작업을 수행하는 메서드를 나타냅니다.

3. **작업 완료 후 CircularProgressIndicator 숨기기**

마지막으로, 작업이 완료된 후에는 CircularProgressIndicator를 숨기고 작업 결과를 사용자에게 표시해야 합니다.

동시에 여러 작업이 진행되는 상황을 표시할 때에는 사용자 경험을 중요시하는 것이 좋습니다. CircularProgressIndicator를 통해 작업이 진행 중임을 시각적으로 나타내고, 작업이 완료된 후에는 해당 결과를 화면에 제공하여 사용자가 현재 상황을 파악할 수 있도록 합니다.

이상입니다. 위의 예시를 통해 CircularProgressIndicator를 사용하여 동시에 여러 작업이 진행되는 상황을 표시하는 방법에 대해 알아보았습니다.

관련 참고 자료:
- Flutter CircularProgressIndicator: https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html