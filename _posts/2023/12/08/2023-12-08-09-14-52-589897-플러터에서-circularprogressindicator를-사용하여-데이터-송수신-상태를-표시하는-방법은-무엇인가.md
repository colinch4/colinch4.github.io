---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator를 사용하여 데이터 송수신 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

다음은 CircularProgressIndicator를 사용하여 데이터 송수신 상태를 표시하는 간단한 예시입니다.

```dart
import 'package:flutter/material.dart';

class MyDataScreen extends StatefulWidget {
  @override
  _MyDataScreenState createState() => _MyDataScreenState();
}

class _MyDataScreenState extends State<MyDataScreen> {
  bool _isLoading = false; // 데이터 로딩 상태

  Future<void> _getData() async {
    setState(() {
      _isLoading = true; // 데이터 로딩 시작
    });

    // 여기에 데이터를 가져오는 비동기 처리 로직 작성

    setState(() {
      _isLoading = false; // 데이터 로딩 완료
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('데이터 화면'),
      ),
      body: Center(
        child: _isLoading
            ? CircularProgressIndicator() // 데이터 로딩 중인 경우, CircularProgressIndicator 표시
            : RaisedButton(
                onPressed: _getData,
                child: Text('데이터 불러오기'),
              ),
      ),
    );
  }
}
```

위 코드는 데이터를 가져오는 동안 CircularProgressIndicator를 표시하는 방법을 보여줍니다. ```_isLoading``` 변수를 사용하여 데이터가 로딩되고 있는지에 대한 상태를 관리하고, 데이터를 가져오는 비동기 처리 로직 안에서 상태를 변경합니다.

플러터에서 CircularProgressIndicator를 커스터마이징하여 애니메이션과 색상을 변경하는 등 다양한 방법으로 활용할 수 있습니다. 자세한 내용은 공식 문서를 참고하시기 바랍니다.

- 공식 문서: [Flutter CircularProgressIndicator](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)