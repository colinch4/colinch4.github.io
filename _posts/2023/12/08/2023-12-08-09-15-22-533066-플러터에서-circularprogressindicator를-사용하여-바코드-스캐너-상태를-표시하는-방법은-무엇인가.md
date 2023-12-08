---
layout: post
title: "[flutter] 플러터에서 CircularProgressIndicator를 사용하여 바코드 스캐너 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

아래는 CircularProgressIndicator를 사용하여 바코드 스캐너 상태를 표시하는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';

class BarcodeScannerScreen extends StatefulWidget {
  @override
  _BarcodeScannerScreenState createState() => _BarcodeScannerScreenState();
}

class _BarcodeScannerScreenState extends State<BarcodeScannerScreen> {
  bool _isScanning = false;

  void _startScan() {
    // 바코드 스캔을 시작하는 로직
    setState(() {
      _isScanning = true;
    });
  }

  void _stopScan() {
    // 바코드 스캔을 멈추는 로직
    setState(() {
      _isScanning = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('바코드 스캐너'),
      ),
      body: Center(
        child: _isScanning
            ? Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  CircularProgressIndicator(),
                  SizedBox(height: 16),
                  Text('바코드 스캔 중...'),
                ],
              )
            : ElevatedButton(
                onPressed: _startScan,
                child: Text('스캔 시작'),
              ),
      ),
    );
  }
}
```

위의 코드에서, CircularProgressIndicator는 `_isScanning` 변수에 따라 표시되거나 숨겨집니다. 바코드 스캔이 진행 중일 때는 CircularProgressIndicator가 나타나고, 스캔이 완료되면 CircularProgressIndicator가 사라집니다.

이와 같이 CircularProgressIndicator를 사용하면 플러터 애플리케이션에서 바코드 스캐너의 상태를 효과적으로 표시할 수 있습니다.