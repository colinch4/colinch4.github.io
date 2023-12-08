---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 데이터 로딩 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---
# flutter에서 데이터 로딩 상태를 표시하는 방법

이번 글에서는 flutter 앱에서 데이터 로딩 상태를 표시하는 방법에 대해 알아보겠습니다.

## CircularProgressIndicator란?

CircularProgressIndicator는 flutter에서 데이터가 로딩 중임을 나타내는데 사용되는 위젯입니다. 로딩 중일 때 앱이 정지되었거나 작동 중임을 사용자에게 알려주기 위해 사용됩니다.

## CircularProgressIndicator 사용 방법

다음은 CircularProgressIndicator를 사용하여 데이터 로딩 상태를 표시하는 간단한 예제입니다.

```dart
import 'package:flutter/material.dart';

class MyLoadingScreen extends StatelessWidget {
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
위 예제에서는 CircularProgressIndicator 위젯을 사용하여, 화면의 중앙에 로딩 중임을 알리는 동그란 인디케이터가 표시됩니다.

## Customizing CircularProgressIndicator

CircularProgressIndicator는 색상, 두께, 크기 등 여러 속성을 커스터마이징 할 수 있습니다. 필요에 따라 CircularProgressIndicator를 사용자 정의하여 앱의 디자인과 일치시킬 수 있습니다.

이상으로 flutter에서 데이터 로딩 상태를 표시하는 방법에 대해 알아보았습니다. 추가적인 설명이 필요하다면 자세한 flutter 공식 문서를 참고하시기를 권장합니다.
```