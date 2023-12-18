---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 데이터 응답 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

지난 프로젝트에서 데이터를 가져오는 데 시간이 오래 걸리는 경우가 있었습니다. 그래서 데이터가 응답할 때까지 사용자에게 진행 상황을 시각적으로 보여주는 기능을 추가하기로 했습니다. Flutter에서는 `LinearProgressIndicator` 위젯을 사용하여 이를 구현할 수 있습니다.

## 1. LinearProgressIndicator 이해하기

`LinearProgressIndicator`는 진행률을 수평으로 나타내는 위젯으로, 데이터가 로딩되는 동안에 화면에 표시할 수 있습니다.

## 2. LinearProgressIndicator 사용하기

다음은 `LinearProgressIndicator`를 사용하여 데이터 로딩 중에 화면에 진행률을 표시하는 간단한 예제입니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Data Loading Example'),
        ),
        body: Center(
          child: DataLoadingWidget(),
        ),
      ),
    );
  }
}

class DataLoadingWidget extends StatefulWidget {
  @override
  _DataLoadingWidgetState createState() => _DataLoadingWidgetState();
}

class _DataLoadingWidgetState extends State<DataLoadingWidget> {
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    // Simulate data loading delay
    Future.delayed(Duration(seconds: 5), () {
      setState(() {
        _isLoading = false;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return _isLoading ? LinearProgressIndicator() : Text('Data Loaded');
  }
}
```

위 예제에서는 `DataLoadingWidget` 위젯에서 `LinearProgressIndicator`를 사용하여 데이터가 로딩될 때까지 진행률을 표시하고, 데이터가 로딩되면 진행률 인디케이터 대신 "Data Loaded"라는 텍스트를 표시합니다.

## 3. 마무리

`LinearProgressIndicator`를 사용하여 데이터 응답의 진행 상황을 사용자에게 시각적으로 표시하면 사용자 경험이 향상될 수 있습니다. 데이터 로딩이나 다른 시간이 소요되는 작업이 있을 때 이를 고려하여 사용자 인터페이스를 보다 친화적으로 만들 수 있습니다.

---

참고문헌:
- Flutter 위키: https://flutter.dev/docs/development/ui/widgets/material/LinearProgressIndicator