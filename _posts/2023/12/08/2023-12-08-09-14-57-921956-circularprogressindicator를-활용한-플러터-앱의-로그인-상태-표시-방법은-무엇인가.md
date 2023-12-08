---
layout: post
title: "[flutter] CircularProgressIndicator를 활용한 플러터 앱의 로그인 상태 표시 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱에서 로그인 상태를 표시하려면 CircularProgressIndicator를 사용하여 사용자에게 로그인 프로세스가 진행 중임을 시각적으로 알릴 수 있습니다. 이를 통해 사용자는 앱이 작업을 수행 중임을 인지할 수 있습니다.

## 1. CircularProgressIndicator 위젯

CircularProgressIndicator 위젯은 플러터에서 로딩 상태를 표시하는 데 사용됩니다. 이 위젯은 기본적으로 회전하는 원 형태의 로딩 인디케이터를 표시합니다.

```dart
CircularProgressIndicator()
```

## 2. Flutter 앱에서의 로그인 상태 표시

로그인 버튼을 누른 후에는 CircularProgressIndicator를 표시하고, 로그인이 완료되면 CircularProgressIndicator를 제거하는 방식을 사용할 수 있습니다.

```dart
bool _isLoading = false;

void _handleLogin() {
  setState(() {
    _isLoading = true;
  });

  // Perform login process here

  setState(() {
    _isLoading = false;
  });
}

Widget build(BuildContext context) {
  return Scaffold(
    body: Center(
      child: _isLoading
          ? CircularProgressIndicator()
          : ElevatedButton(
              onPressed: _handleLogin,
              child: Text('Login'),
            ),
    ),
  );
}
```

위 코드에서는 `_isLoading` 변수를 사용하여 현재 로그인 상태를 추적하고, `_handleLogin` 함수 내에서 로그인 프로세스가 시작되면 `_isLoading`을 true로 설정하여 CircularProgressIndicator를 표시하고, 로그인이 완료되면 다시 false로 설정하여 CircularProgressIndicator를 숨깁니다.

이와 같이 CircularProgressIndicator를 활용하여 플러터 앱에서 로그인 상태를 표시할 수 있습니다.

참고: [Flutter CircularProgressIndicator](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)