---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션 로딩 화면을 만드는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

먼저, 다음과 같이 CircularProgressIndicator를 포함한 StatefulWidget을 만듭니다.

```dart
import 'package:flutter/material.dart';

class LoadingScreen extends StatefulWidget {
  @override
  _LoadingScreenState createState() => _LoadingScreenState();
}

class _LoadingScreenState extends State<LoadingScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: CircularProgressIndicator(),
      ),
    );
  }
}
```

위의 코드에서 LoadingScreen은 CircularProgressIndicator를 포함한 StatelessWidget을 반환합니다. 이 코드를 메인 애플리케이션의 시작점으로 설정하면, CircularProgressIndicator가 표시된 로딩 화면이 표시됩니다.

더 많은 사용자 정의가 필요한 경우, CircularProgressIndicator의 모양, 색상 등을 조정할 수도 있습니다. 하지만 기본적으로 위의 예제는 간단한 로딩 화면을 만드는 방법을 보여줍니다.

더 자세한 내용은 Flutter 공식 문서를 참조하시기 바랍니다.