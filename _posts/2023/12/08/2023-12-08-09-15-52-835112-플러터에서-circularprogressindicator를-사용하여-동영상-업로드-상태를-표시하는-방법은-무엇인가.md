---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator를 사용하여 동영상 업로드 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

1. 먼저, CircularProgressIndicator를 사용할 StatefulWidget을 생성합니다.

```dart
import 'package:flutter/material.dart';

class VideoUploadScreen extends StatefulWidget {
  VideoUploadScreen({Key key}) : super(key: key);

  @override
  _VideoUploadScreenState createState() => _VideoUploadScreenState();
}

class _VideoUploadScreenState extends State<VideoUploadScreen> {
  bool _isUploading = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('동영상 업로드'),
      ),
      body: Center(
        child: _isUploading ? CircularProgressIndicator() : RaisedButton(
          onPressed: () {
            // 업로드 시작
            setState(() {
              _isUploading = true;
            });
            // 동영상 업로드 로직 실행
            uploadVideo().then((value) {
              // 업로드 완료 후 상태 변경
              setState(() {
                _isUploading = false;
              });
            });
          },
          child: Text('동영상 업로드 시작'),
        ),
      ),
    );
  }

  Future<void> uploadVideo() async {
    // 업로드 로직 구현
    // 예를 들어, HTTP 요청을 통한 업로드 등
  }
}
```

2. 코드에서 `_isUploading` 불리언 변수는 업로드 중 상태를 나타냅니다. 동영상을 업로드할 때 버튼을 누르면 `_isUploading`이 true로 변경되어 CircularProgressIndicator가 나타납니다.

3. `uploadVideo` 함수는 실제 동영상 업로드 로직을 담당합니다. 이 예시 코드에서는 비동기 메소드인 `uploadVideo`가 완료되면 `_isUploading`이 false로 변경됩니다.

이러한 방식으로 CircularProgressIndicator를 사용하여 플러터 앱에서 동영상 업로드 상태를 표시할 수 있습니다.