---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 소셜 미디어 업로드 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

이번 포스트에서는 Flutter 앱에서 소셜 미디어에 사진 또는 비디오를 업로드할 때 업로드 진행률을 사용자에게 시각적으로 표시하는 방법에 대해 알아보겠습니다.

## 1. LinearProgressIndicator란?

**LinearProgressIndicator**는 사용자에게 작업이 진행 중임을 시각적으로 알려주는 UI 요소입니다. 주로 작업이 얼마나 완료되었는지를 표시할 때 사용됩니다. 

## 2. 소셜 미디어 업로드 진행률 표시하기

아래는 Flutter에서 **LinearProgressIndicator**를 사용하여 소셜 미디어 업로드 진행률을 표시하는 간단한 예제코드입니다.

```dart
import 'package:flutter/material.dart';

class SocialMediaUploadScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Upload to Social Media'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            RaisedButton(
              onPressed: () {
                // TODO: Handle social media upload
              },
              child: Text('Upload'),
            ),
            SizedBox(height: 20),
            LinearProgressIndicator(), // 업로드 진행률 표시
          ],
        ),
      ),
    );
  }
}
```

위 예제에서는 **LinearProgressIndicator**를 사용하여 업로드 버튼을 누르면 소셜 미디어 업로드 작업이 시작되며, 이 과정에서 진행률이 표시됩니다.

## 3. 결론

이렇게 Flutter에서 **LinearProgressIndicator**를 활용하여 사용자에게 소셜 미디어 업로드 진행률을 표시하는 방법에 대해 알아보았습니다. 이를 통해 사용자가 업로드 작업이 얼마나 완료되었는지를 쉽게 확인할 수 있습니다.

소셜 미디어 업로드 작업 외에도 다양한 작업의 진행률을 표시하기 위해 **LinearProgressIndicator**를 활용할 수 있습니다.

향후 포스트에서는 **CircularProgressIndicator** 및 **퍼센테이지 표시 기능**에 대해서도 알아보겠습니다.

참고: [Flutter LinearProgressIndicator](https://api.flutter.dev/flutter/material/LinearProgressIndicator-class.html)