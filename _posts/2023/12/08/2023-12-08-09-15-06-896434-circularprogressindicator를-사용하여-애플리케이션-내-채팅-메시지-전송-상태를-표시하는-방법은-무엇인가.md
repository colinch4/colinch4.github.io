---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션 내 채팅 메시지 전송 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

채팅 애플리케이션을 개발할 때, 사용자에게 메시지 전송 상태를 시각적으로 표시하는 것은 매우 중요합니다. Flutter에서는 CircularProgressIndicator 위젯을 사용하여 이러한 기능을 손쉽게 구현할 수 있습니다. 이 문서에서는 CircularProgressIndicator를 사용하여 애플리케이션 내 채팅 메시지 전송 상태를 표시하는 방법에 대해 알아보겠습니다.

## 1. CircularProgressIndicator란?

CircularProgressIndicator는 애플리케이션 내에서 작업이 진행 중임을 나타내는 데 사용되는 Material Design의 진행 표시기입니다. 이는 사용자에게 진행 상황을 시각적으로 보여줄 수 있어 매우 유용합니다.

## 2. 채팅 메시지 전송 상태 표시하기

```dart
import 'package:flutter/material.dart';

class ChatScreen extends StatelessWidget {
  bool _isSendingMessage = false; // 메시지 전송 상태를 나타내는 변수

  void _sendMessage() {
    // 메시지 전송 함수
    // 전송 시작 시 _isSendingMessage를 true로 설정
    // 전송 완료 시 _isSendingMessage를 false로 설정
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('채팅'),
      ),
      body: Center(
        child: _isSendingMessage
            ? CircularProgressIndicator()  // 메시지 전송 중에는 CircularProgressIndicator 표시
            : ElevatedButton(
                onPressed: _sendMessage,
                child: Text('메시지 전송'),
              ),
      ),
    );
  }
}
```

위의 예시 코드에서, `_isSendingMessage` 변수는 메시지 전송 상태를 나타내고, 이 값을 통해 메시지 전송 중에는 CircularProgressIndicator를 표시하고, 전송이 완료되면 다른 콘텐츠를 표시할 수 있습니다. `_sendMessage` 함수는 실제로 메시지를 전송하고 전송 상태를 업데이트합니다.

## 3. 마치며

이제 Flutter에서 CircularProgressIndicator를 사용하여 채팅 메시지 전송 상태를 표시하는 방법에 대해 간단히 알아보았습니다. 이를 응용하여 실제 채팅 애플리케이션에서 사용자 경험을 높일 수 있는 기능을 구현해 보세요.

더 자세한 내용은 [공식 Flutter 문서](https://flutter.dev/docs)를 참고하시기 바랍니다.