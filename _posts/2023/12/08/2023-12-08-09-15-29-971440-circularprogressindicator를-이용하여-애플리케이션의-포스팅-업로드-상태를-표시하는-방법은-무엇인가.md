---
layout: post
title: "[flutter] CircularProgressIndicator를 이용하여 애플리케이션의 포스팅 업로드 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

다음은 Flutter에서 CircularProgressIndicator를 사용하여 애플리케이션의 포스팅 업로드 상태를 표시하는 간단한 예제코드입니다.

```dart
import 'package:flutter/material.dart';

class PostingScreen extends StatefulWidget {
  @override
  _PostingScreenState createState() => _PostingScreenState();
}

class _PostingScreenState extends State<PostingScreen> {
  bool _isUploading = false;

  void _uploadPost() {
    // 포스팅 업로드 로직
    // 업로드 중일 때 _isUploading 상태를 true로 업데이트
    setState(() {
      _isUploading = true;
    });

    // 포스팅 업로드 완료 후 _isUploading 상태를 false로 업데이트
    // 업로드 완료 후 다음 화면으로 이동
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('포스팅'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _isUploading
                ? CircularProgressIndicator()
                : RaisedButton(
                    onPressed: _uploadPost,
                    child: Text('포스팅 업로드'),
                  ),
          ],
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: PostingScreen(),
  ));
}
```

위의 예제 코드에서는 애플리케이션의 포스팅 업로드 상태를 표시하기 위해 CircularProgressIndicator를 사용하고 있습니다. RaisedButton을 통해 포스팅 업로드를 시작하면서, _isUploading 상태를 변경하여 CircularProgressIndicator를 화면에 표시합니다.

이러한 방법으로 CircularProgressIndicator를 활용하여 애플리케이션의 포스팅 업로드 상태를 표시할 수 있습니다.