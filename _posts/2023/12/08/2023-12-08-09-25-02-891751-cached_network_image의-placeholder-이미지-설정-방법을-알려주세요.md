---
layout: post
title: "[flutter] cached_network_image의 placeholder 이미지 설정 방법을 알려주세요."
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

cached_network_image는 Flutter 앱에서 원격 이미지를 캐싱하여 로딩 시간을 단축해주는 유용한 라이브러리입니다. 이 라이브러리를 사용하여 placeholder 이미지를 설정하는 방법은 매우 간단합니다.

## 1. cached_network_image 라이브러리 추가

먼저, pubspec.yaml 파일에 cached_network_image 라이브러리를 추가합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  cached_network_image: ^2.5.0
```

위와 같이 dependencies 섹션에 cached_network_image 라이브러리를 추가한 후 `flutter packages get`을 통해 의존성을 설치합니다.

## 2. Placeholder 이미지 설정

cached_network_image를 사용하여 placeholder 이미지를 설정하려면 CachedNetworkImage 위젯의 placeholder 파라미터를 사용하면 됩니다. 아래는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:cached_network_image/cached_network_image.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Cached Network Image Placeholder Example'),
        ),
        body: Center(
          child: CachedNetworkImage(
            imageUrl: 'https://example.com/image.jpg',
            placeholder: (context, url) => CircularProgressIndicator(), // Placeholder 위젯 설정
            errorWidget: (context, url, error) => Icon(Icons.error), // 에러 시 표시할 위젯 설정
          ),
        ),
      ),
    );
  }
}
```

위 코드에서 `placeholder` 파라미터를 사용하여 로딩 중에 표시할 위젯을 설정했습니다. 이후 해당 이미지가 로딩되면 placeholder 이미지가 대체됩니다.

이와 같이 간단하게 cached_network_image에서 placeholder 이미지를 설정할 수 있습니다.

## 참고 자료
- [cached_network_image 라이브러리 공식 문서](https://pub.dev/packages/cached_network_image)