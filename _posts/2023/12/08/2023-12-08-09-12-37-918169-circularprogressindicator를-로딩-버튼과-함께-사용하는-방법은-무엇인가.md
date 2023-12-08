---
layout: post
title: "[flutter] CircularProgressIndicator를 로딩 버튼과 함께 사용하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발할 때, 사용자에게 로딩 작업이 진행 중임을 시각적으로 전달하기 위해 CircularProgressIndicator와 함께 로딩 버튼을 표시하는 것이 유용할 수 있습니다. 

이 포스트에서는 StatelessWidget와 StatefulWidget을 사용하여 CircularProgressIndicator와 로딩 버튼을 함께 사용하는 방법에 대해 알아보겠습니다.

## StatelessWidget을 활용한 CircularProgressIndicator와 로딩 버튼 함께 사용하기

다음은 StatelessWidget를 사용하여 CircularProgressIndicator와 로딩 버튼을 함께 사용하는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class LoadingButtonExample extends StatelessWidget {
  final bool isLoading;
  final VoidCallback onPressed;

  const LoadingButtonExample({
    required this.isLoading,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: isLoading ? null : onPressed,
      child: isLoading
          ? CircularProgressIndicator(
              valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
            )
          : Text('로딩 버튼'),
    );
  }
}
```

위의 예제 코드에서 `LoadingButtonExample`은 `isLoading` 속성을 사용하여 버튼이 로딩 중인지 여부를 결정하고, `onPressed` 콜백을 사용하여 버튼 클릭 이벤트를 처리합니다.

## StatefulWidget을 활용한 CircularProgressIndicator와 로딩 버튼 함께 사용하기

다음은 StatefulWidget을 사용하여 CircularProgressIndicator와 로딩 버튼을 함께 사용하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class LoadingButtonExample extends StatefulWidget {
  final VoidCallback onPressed;

  const LoadingButtonExample({required this.onPressed});

  @override
  _LoadingButtonExampleState createState() => _LoadingButtonExampleState();
}

class _LoadingButtonExampleState extends State<LoadingButtonExample> {
  bool isLoading = false;

  void setLoading(bool value) {
    setState(() {
      isLoading = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: isLoading
          ? null
          : () async {
              setLoading(true);
              await widget.onPressed();
              setLoading(false);
            },
      child: isLoading
          ? CircularProgressIndicator(
              valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
            )
          : Text('로딩 버튼'),
    );
  }
}
```

위의 예제 코드에서 `LoadingButtonExample`은 StatefulWidget을 사용하여 버튼의 로딩 상태를 관리합니다. 버튼이 클릭되면 `onPressed` 콜백이 실행되고, 중간에 `isLoading` 상태가 변경됩니다.

## 마치며
이제 당신은 CircularProgressIndicator와 로딩 버튼을 함께 사용하는 방법에 대해 알게 되었습니다. 위의 예제 코드를 참고하여 앱 개발 시 효율적으로 로딩 상태를 관리하고 사용자에게 시각적인 피드백을 제공할 수 있습니다.

참고 문헌:
- [Flutter 공식 문서](https://flutter.dev/docs)