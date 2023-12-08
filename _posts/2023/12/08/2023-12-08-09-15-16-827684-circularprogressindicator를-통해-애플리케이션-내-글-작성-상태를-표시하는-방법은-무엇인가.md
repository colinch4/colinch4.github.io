---
layout: post
title: "[flutter] CircularProgressIndicator를 통해 애플리케이션 내 글 작성 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

### 1. CircularProgressIndicator 추가
먼저, 글 작성 버튼을 눌렀을 때 CircularProgressIndicator를 애니메이션과 함께 화면에 추가합니다.

```dart
import 'package:flutter/material.dart';

class MyWritingScreen extends StatefulWidget {
  @override
  _MyWritingScreenState createState() => _MyWritingScreenState();
}

class _MyWritingScreenState extends State<MyWritingScreen> {
  bool _isWriting = false;

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        // ... 
      ),
      body: Center(
        child: _isWriting
          ? CircularProgressIndicator()
          : ElevatedButton(
              onPressed: () {
                setState(() {
                  _isWriting = true;
                  // 글 작성 로직 수행
                  // 작업 완료 후 _isWriting 값을 false로 설정하여 CircularProgressIndicator를 제거
                });
              },
              child: Text('글 작성하기'),
            ),
      ),
    );
  }
}
```

### 2. 작업 완료 후 CircularProgressIndicator 제거
글 작성 작업이 완료된 후에는 CircularProgressIndicator를 제거하여 사용자에게 작업이 완료되었음을 알립니다.

위 코드에서 '_isWriting' 값이 false로 설정되면 CircularProgressIndicator가 화면에서 제거됩니다.

이것으로 CircularProgressIndicator를 통해 애플리케이션 내 글 작성 상태를 표시하는 방법을 알아보았습니다. 위 예시 코드를 참고하여 원하는 화면에 CircularProgressIndicator를 적용해 보세요.