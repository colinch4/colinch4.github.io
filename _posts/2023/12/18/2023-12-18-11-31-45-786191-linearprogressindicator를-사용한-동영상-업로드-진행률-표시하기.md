---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 동영상 업로드 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

동영상을 업로드하는 기능을 구현할 때, 사용자에게 업로드 진행 상황을 시각적으로 표시해주는 것은 중요합니다. Flutter에서는 LinearProgressIndicator 위젯을 사용하여 이를 쉽게 구현할 수 있습니다. 이 블로그 포스트에서는 Flutter 애플리케이션에서 동영상 업로드 진행률을 표시하기 위해 LinearProgressIndicator를 어떻게 사용하는지에 대해 설명하겠습니다.

## 1. LinearProgressIndicator란?

`LinearProgressIndicator`는 작업의 진행 상황을 표시하는 데 사용되는 Material Design 스타일의 선형 진행 막대 위젯입니다. 애니메이션 효과를 포함하여 작업이 얼마나 완료되었는지 시각적으로 보여줍니다.

## 2. 코드 예제

아래는 동영상 업로드 진행률을 표시하기 위해 LinearProgressIndicator를 사용하는 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class VideoUploadScreen extends StatefulWidget {
  @override
  _VideoUploadScreenState createState() => _VideoUploadScreenState();
}

class _VideoUploadScreenState extends State<VideoUploadScreen> {
  double _uploadProgress = 0.0;

  // 동영상 업로드 메서드
  void _uploadVideo() {
    // 동영상 업로드를 시작하고, 진행률을 업데이트하는 로직
    // 업로드 진행률을 setState()를 통해 업데이트
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('동영상 업로드'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            LinearProgressIndicator(
              value: _uploadProgress,
              backgroundColor: Colors.grey,
              valueColor: AlwaysStoppedAnimation<Color>(Colors.blue),
            ),
            SizedBox(height: 20.0),
            ElevatedButton(
              onPressed: () {
                _uploadVideo();
              },
              child: Text('동영상 업로드 시작'),
            ),
          ],
        ),
      ),
    );
  }
}
```

위 코드에서, `VideoUploadScreen` 위젯은 동영상 업로드 화면을 나타내며, `_uploadProgress` 변수를 사용하여 업로드 진행률을 나타냅니다. `_uploadVideo` 메서드는 업로드를 시작하고 진행률을 업데이트하는 로직을 포함하고 있습니다.

## 3. 진행률 표시

`LinearProgressIndicator` 위젯은 `value` 속성을 통해 진행률을 표시합니다. 이 값은 0.0에서 1.0 사이의 값을 가져야 하며, 0.0은 아무런 진행이 없음을, 1.0은 작업이 완료되었음을 의미합니다.

## 4. 결론

Flutter의 `LinearProgressIndicator`를 사용하면 동영상 업로드나 다른 작업의 진행 상황을 시각적으로 표시할 수 있습니다. 이를 통해 사용자는 작업이 얼마나 완료되었는지를 쉽게 파악할 수 있게 됩니다.

참고: [Flutter LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)