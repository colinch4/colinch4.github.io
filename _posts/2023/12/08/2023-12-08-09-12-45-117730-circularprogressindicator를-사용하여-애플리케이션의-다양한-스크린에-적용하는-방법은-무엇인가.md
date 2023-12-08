---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션의 다양한 스크린에 적용하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

애플리케이션에서 사용자에게 프로세스가 진행 중임을 시각적으로 표시하는 데 사용되는 CircularProgressIndicator는 Flutter에서 손쉽게 적용할 수 있습니다. 해당 위젯을 사용하여 애플리케이션이 다양한 상황에서 로딩 중임을 알리는 방법에 대해 다루겠습니다.

## 1. CircularProgressIndicator란?

CircularProgressIndicator는 주로 애플리케이션이 데이터를 로딩하거나 프로세스가 진행 중임을 나타내기 위해 화면에 표시되는 반원 형태의 프로그레스 바입니다. 이를 통해 사용자는 현재 시스템 또는 애플리케이션이 작업 처리 중임을 파악할 수 있습니다.

## 2. CircularProgressIndicator 적용 방법

**2.1. 단일 화면에 CircularProgressIndicator 표시**
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

**2.2. 다른 위젯과 함께 사용하기**
```dart
import 'package:flutter/material.dart';

class MyDataScreen extends StatelessWidget {
  bool isLoading = true; // 로딩 상태를 나타내는 변수

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('데이터 화면'),
      ),
      body: isLoading
          ? Center(
              child: CircularProgressIndicator(),
            )
          : ListView(
              children: [
                // 데이터 표시를 위한 다른 위젯들
              ],
            ),
    );
  }
}
```

## 3. CircularProgressIndicator를 사용하기 위한 주의사항

- CircularProgressIndicator는 반드시 작업이 진행 중임을 명확히 알리는데 사용되어야 합니다.
- 너무 많은 곳에 사용되거나 오랫동안 표시되는 것은 사용자 경험을 저해할 수 있습니다.

애플리케이션의 로딩 상태를 명확히 시각적으로 표현하기 위해 CircularProgressIndicator를 적절하게 활용할 수 있습니다. 정확한 상황과 타이밍에 사용하여 사용자가 현재 애플리케이션이 작업 중임을 인지할 수 있도록 할 필요가 있습니다.