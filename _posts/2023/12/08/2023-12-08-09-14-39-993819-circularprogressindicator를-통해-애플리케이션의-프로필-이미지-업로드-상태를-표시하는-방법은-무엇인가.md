---
layout: post
title: "[flutter] CircularProgressIndicator를 통해 애플리케이션의 프로필 이미지 업로드 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

프로필 이미지를 업로드할 때, 사용자에게 업로드 상태를 시각적으로 표시하는 것은 좋은 사용자 경험을 제공합니다. 이를 위해 Flutter에서는 CircularProgressIndicator를 사용하여 간단하게 업로드 상태를 표시할 수 있습니다.

## 1. CircularProgressIndicator 위젯 추가

우선, 프로필 이미지가 업로드되는 동안에만 표시될 CircularProgressIndicator 위젯을 추가해야 합니다. 다음은 간단한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

class ProfilePage extends StatefulWidget {
  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  bool _isUploading = false;  // 업로드 상태 여부를 저장하는 변수

  void _uploadProfileImage() async {
    setState(() {
      _isUploading = true;  // 이미지 업로드 시작 시 상태를 true로 변경
    });

    // 이미지 업로드 코드 작성

    setState(() {
      _isUploading = false;  // 이미지 업로드 완료 시 상태를 false로 변경
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('프로필 편집'),
      ),
      body: Center(
        child: _isUploading
            ? CircularProgressIndicator()  // 이미지 업로드 상태일 때 CircularProgressIndicator 표시
            : Text('프로필 이미지'),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _uploadProfileImage,
        tooltip: '프로필 이미지 업로드',
        child: Icon(Icons.add_a_photo),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: ProfilePage(),
  ));
}
```

위 코드에서 ```_isUploading``` 변수는 이미지 업로드 중인지를 나타내며, ```_uploadProfileImage()``` 함수는 이미지 업로드를 처리합니다. 이미지가 업로드되는 동안에는 CircularProgressIndicator가 표시되고, 업로드가 완료된 후에는 프로필 이미지가 표시됩니다.

## 2. 사용자 경험 개선

더 나은 사용자 경험을 위해, CircularProgressIndicator의 색상과 크기를 조정하는 등의 추가적인 UI/UX 개선을 적용할 수 있습니다.

프로필 이미지 업로드 상태를 표시하는 방법에 대한 자세한 내용은 [공식 Flutter 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.