---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션 내 쇼핑 카트 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

애플리케이션 개발 중에는 사용자에게 작업이 실행 중임을 알리고자 할 때가 있습니다. 대표적인 예로 쇼핑 카트에 물건을 추가하는 과정에서의 상태 표시가 있습니다.

이 포스트에서는 Flutter 애플리케이션에서 **CircularProgressIndicator**를 사용하여 쇼핑 카트의 상태를 표시하는 방법을 알아보겠습니다.

## 1. CircularProgressIndicator 추가하기

먼저, **CircularProgressIndicator**를 쇼핑 카트 화면에 추가해야 합니다. 이를 위해서는 다음의 코드를 사용할 수 있습니다.

```dart
import 'package:flutter/material.dart';

class ShoppingCartScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Shopping Cart'),
      ),
      body: Center(
        child: CircularProgressIndicator(),
      ),
    );
  }
}
```

위의 코드에서 **Center** 위젯 안에 **CircularProgressIndicator**를 추가함으로써, 해당 위젯이 화면 가운데에 표시됩니다.

## 2. 쇼핑 카트 로직과 결합하기

다음으로는 쇼핑 카트 로직과 **CircularProgressIndicator**를 결합하여 작업이 완료될 때까지 화면에 로딩 상태를 표시하는 방법을 알아보겠습니다.

```dart
// 쇼핑 카트 로딩 중 상태 플래그
bool isLoading = true;

@override
Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(
      title: Text('Shopping Cart'),
    ),
    body: Center(
      child: isLoading
          ? CircularProgressIndicator()
          : ShoppingCartContents(), // 로딩이 완료되면 쇼핑 카트 내용 표시
    ),
  );
}
```

위의 코드에서 **isLoading** 플래그를 사용하여 현재 로딩 중 상태를 표시하고, 그에 따라 **CircularProgressIndicator** 또는 실제 쇼핑 카트 내용을 화면에 표시합니다.

## 결론

이제 Flutter 애플리케이션에서 **CircularProgressIndicator**를 사용하여 쇼핑 카트의 상태를 표시하는 방법에 대해 알아보았습니다. 이를 통해 사용자에게 로딩 중임을 시각적으로 알리고, 좀 더 사용자 친화적인 애플리케이션을 개발할 수 있습니다.

더 많은 정보 및 사용 예제는 [Flutter 공식 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.