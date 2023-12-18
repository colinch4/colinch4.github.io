---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 사진 업로드 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발하면서 사용자가 사진을 업로드할 때 어떻게 진행률을 표시할 수 있는지 알아보겠습니다.

## 사진 업로드 버튼과 상태 관리

먼저, 사용자가 사진을 업로드하는 버튼을 만들고 그 상태를 관리하는 방법을 알아야 합니다. 이를 위해 **Flutter의 `FlutterFire` 라이브러리나 HTTP 요청을 사용하여 백엔드 서버와 통신**하는 방법을 선택할 수 있습니다.

```dart
import 'package:flutter/material.dart';

class PhotoUploadScreen extends StatefulWidget {
  @override
  _PhotoUploadScreenState createState() => _PhotoUploadScreenState();
}

class _PhotoUploadScreenState extends State<PhotoUploadScreen> {
  bool _isUploading = false;

  void _uploadPhoto() {
    setState(() {
      _isUploading = true;
      // Perform photo upload logic here
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Photo Upload'),
      ),
      body: Center(
        child: _isUploading
            ? CircularProgressIndicator()
            : ElevatedButton(
                onPressed: _uploadPhoto,
                child: Text('Upload Photo'),
              ),
      ),
    );
  }
}
```

위 코드에서는 `_isUploading` 변수를 사용하여 업로드 상태를 관리하고, 버튼을 누르면 `_uploadPhoto` 함수가 호출되어 업로드 상태를 변경합니다.

## 진행률 표시

이제 LinearProgressIndicator를 사용하여 사진이 업로드되는 동안 진행률을 표시해보겠습니다.

```dart
import 'package:flutter/material.dart';

class PhotoUploadScreen extends StatefulWidget {
  @override
  _PhotoUploadScreenState createState() => _PhotoUploadScreenState();
}

class _PhotoUploadScreenState extends State<PhotoUploadScreen> {
  double _uploadProgress = 0.0;  // 추가된 코드

  void _uploadPhoto() {
    // ...중략...

    // 실제 업로드 진행률을 받아오는 로직
    // 다음 코드는 가상의 진행률을 업데이트함
    for (var i = 0; i < 100; i++) {
      setState(() {
        _uploadProgress = (i + 1) / 100;
      });
      await Future.delayed(Duration(milliseconds: 100));
    }

    // ...중략...
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Photo Upload'),
      ),
      body: Center(
        child: _uploadProgress < 1
            ? LinearProgressIndicator(value: _uploadProgress)
            : ElevatedButton(
                onPressed: _uploadPhoto,
                child: Text('Upload Photo'),
              ),
      ),
    );
  }
}
```

이 코드에서는 `_uploadProgress` 변수를 사용하여 업로드 진행률을 저장하고, 이 값을 `LinearProgressIndicator`의 `value` 속성에 전달하여 진행률을 표시하게 됩니다.

## 마치며

이제 LinearProgressIndicator를 사용하여 **사진 업로드의 진행률을 시각적으로 표시**할 수 있게 되었습니다. 앞으로 다양한 UI 요소와 함께 보다 멋진 Flutter 앱을 만들어 보시기 바랍니다.

참고 문헌:

- Flutter 공식 문서: https://flutter.dev/docs
- FlutterFire 라이브러리: https://firebase.flutter.dev

이제 LinearProgressIndicator를 사용하여 사진 업로드의 진행률을 시각적으로 표시할 수 있게 되었습니다. 앞으로 다양한 UI 요소와 함께 보다 멋진 Flutter 앱을 만들어 보시기 바랍니다.

## 참고 자료

- Flutter 공식 문서: [Flutter](https://flutter.dev/docs)
- FlutterFire 라이브러리: [Firebase for Flutter](https://firebase.flutter.dev)