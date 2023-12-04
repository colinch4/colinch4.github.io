---
layout: post
title: "[flutter] 플러터(Flutter)에서 앱 생명주기 이벤트 처리를 위해 WidgetsBindingObserver를 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

WidgetsBindingObserver는 플러터 앱의 생명주기 이벤트를 관찰하고 처리할 수 있는 인터페이스입니다. 이를 사용하여 앱이 시작, 일시 중지, 재개되는 등의 이벤트를 감지하고 필요한 작업을 수행할 수 있습니다.

다음은 WidgetsBindingObserver를 사용하여 앱 생명주기 이벤트를 처리하는 예제입니다:

1. 먼저, 앱의 상태를 관찰하고자 하는 클래스에 WidgetsBindingObserver 인터페이스를 구현합니다.

```dart
class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }
  
  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }
  
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) {
      // 앱이 재개될 때 수행할 작업
    } else if (state == AppLifecycleState.inactive) {
      // 앱이 비활성화될 때 수행할 작업
    } else if (state == AppLifecycleState.paused) {
      // 앱이 일시 중지될 때 수행할 작업
    } else if (state == AppLifecycleState.detached) {
      // 앱이 백그라운드 상태로 전환될 때 수행할 작업
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
```

2. initState 메서드에서 WidgetsBinding.instance.addObserver(this)를 호출하여 현재 클래스를 WidgetsBindingObserver로 등록합니다.

3. dispose 메서드에서 WidgetsBinding.instance.removeObserver(this)를 호출하여 등록을 해제합니다.

4. didChangeAppLifecycleState 메서드를 재정의하여 원하는 앱 생명주기 이벤트에 대한 작업을 구현합니다. 예를 들어, 앱이 재개될 때 특정 로직을 처리하려면 AppLifecycleState.resumed를 체크한 후 해당 작업을 수행하면 됩니다.

위 예제에서는 앱이 재개, 비활성화, 일시 중지, 백그라운드 전환 등의 생명주기 이벤트를 처리할 수 있도록 구현되어 있습니다. 사용자가 원하는 작업에 맞게 이를 수정하고 활용할 수 있습니다.

참고할만한 문서:
- [Flutter: Handle app lifecycle events with WidgetsBindingObserver](https://flutter.dev/docs/get-started/flutter-for/ios-android#handle-app-lifecycle-events-with-widgetsbindingobserver)