---
layout: post
title: "[flutter] LinearProgressIndicator를 사용한 다운로드 진행률 표시하기"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

안녕하세요! 이번에는 **flutter** 앱에서 **LinearProgressIndicator**를 사용하여 다운로드 진행률을 표시하는 기능에 대해 알아보겠습니다.

## 1. LinearProgressIndicator란?

**LinearProgressIndicator**는 진행 중인 작업의 진행률을 시각적으로 표시하는 데 사용됩니다. 주로 네트워크에서 파일을 다운로드하거나 업로드하는 경우에 진행률을 나타내는 데 사용됩니다.

## 2. Flutter 앱에 LinearProgressIndicator 추가하기

**LinearProgressIndicator**를 Flutter 앱에 추가하는 것은 매우 간단합니다.

```dart
import 'package:flutter/material.dart';

class DownloadScreen extends StatefulWidget {
  @override
  _DownloadScreenState createState() => _DownloadScreenState();
}

class _DownloadScreenState extends State<DownloadScreen> {
  double _progress = 0.0; // 진행률 변수

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('다운로드 진행률'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // LinearProgressIndicator 추가
            LinearProgressIndicator(value: _progress),
            SizedBox(height: 20),
            Text('${(_progress * 100).toStringAsFixed(2)}% 완료'),
          ],
        ),
      ),
    );
  }
}
```

위 코드에서 **LinearProgressIndicator** 위젯을 추가하고, **_progress** 변수를 사용하여 진행률을 관리하고 표시합니다.

## 3. 진행률 업데이트하기

다운로드 작업이 진행됨에 따라 **_progress** 변수를 업데이트하여 **LinearProgressIndicator**를 업데이트할 수 있습니다.

```dart
void _startDownload() {
  // 다운로드 시작
  // 다운로드 진행률을 업데이트할 때마다 setState를 호출하여 화면을 다시 그리도록 합니다.
  for (int i = 0; i <= 100; i++) {
    Future.delayed(Duration(seconds: 1), () {
      setState(() {
        _progress = i / 100.0; // 진행률 업데이트
      });
    });
  }
}
```

위 코드에서 **_startDownload** 함수를 사용하여 다운로드를 시작하고, **setState**를 통해 **_progress** 변수를 업데이트합니다.

## 마무리

이제 **LinearProgressIndicator**를 사용하여 Flutter 앱에서 다운로드 진행률을 표시하는 방법에 대해 알아보았습니다. **LinearProgressIndicator**를 활용하여 사용자에게 작업 진행 상황을 시각적으로 표시할 수 있습니다.

참고로 **LinearProgressIndicator**는 해당 작업의 진행률을 표시하는 데 사용할 수 있을 뿐만 아니라, 사용자 경험을 증진하고 대기 시간을 줄이는 데에도 도움이 됩니다.

더 많은 자세한 내용은 [공식 Flutter 문서](https://flutter.dev/docs/development/ui/widgets/material/LinearProgressIndicator)를 참고할 수 있습니다.