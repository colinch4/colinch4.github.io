---
layout: post
title: "[flutter] CircularProgressIndicator를 활용한 플러터 앱의 게시글 작성 상태 표시 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

# Flutter 앱의 게시글 작성 상태 표시 방법

이번 게시글에서는 Flutter 앱에서 게시글이 작성되는 상태를 표시하기 위해 `CircularProgressIndicator`를 활용하는 방법에 대해 알아보겠습니다.

## 1. CircularProgressIndicator 소개

`CircularProgressIndicator`는 플러터에서 작업이 진행 중임을 시각적으로 나타내는 데 사용됩니다. 이 컴포넌트는 화면에 원형의 진행률 표시기를 표시하여 사용자가 앱이 작업을 수행 중임을 알 수 있도록 도와줍니다.

## 2. 게시글 작성 상태 표시 방법

게시글이 작성되는 동안 `CircularProgressIndicator`를 화면에 표시하여 사용자에게 작업이 수행 중임을 시각적으로 전달할 수 있습니다. 아래는 간단한 예시 코드입니다.

```dart
import 'package:flutter/material.dart';

class PostScreen extends StatefulWidget {
  @override
  _PostScreenState createState() => _PostScreenState();
}

class _PostScreenState extends State<PostScreen> {
  bool isPosting = false;

  void _publishPost() {
    setState(() {
      isPosting = true;
    });

    // 게시글 작성 로직 수행

    setState(() {
      isPosting = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('게시글 작성'),
      ),
      body: Center(
        child: isPosting ? CircularProgressIndicator() : ElevatedButton(
          onPressed: _publishPost,
          child: Text('게시글 작성'),
        ),
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: PostScreen(),
  ));
}
```

위 코드에서 `isPosting` 변수를 사용하여 게시글 작성 중인지를 표시하고, 화면에 `CircularProgressIndicator`를 표시합니다. 게시글 작성이 완료되면 `isPosting` 변수를 다시 `false`로 설정하여 표시를 제거합니다.

이를 통해 사용자는 앱이 게시글을 작성하는 동안 작업이 수행 중임을 알 수 있게 됩니다.

## 결론

게시글이나 다른 비동기 작업이 발생할 때, 사용자에게 작업이 진행 중임을 명확히 전달하는 것은 중요합니다. `CircularProgressIndicator`를 활용하여 이러한 작업 상태를 시각적으로 표시함으로써 사용자 경험을 향상시킬 수 있습니다.

---

이상으로 Flutter 앱에서 게시글 작성 상태를 표시하는 방법에 대해 살펴보았습니다. 만약 궁금한 점이 있으시다면 언제든지 문의해 주세요.