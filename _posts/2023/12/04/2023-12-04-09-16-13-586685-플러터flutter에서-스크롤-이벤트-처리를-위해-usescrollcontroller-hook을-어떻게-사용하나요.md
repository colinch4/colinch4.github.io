---
layout: post
title: "[flutter] 플러터(Flutter)에서 스크롤 이벤트 처리를 위해 useScrollController Hook을 어떻게 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)에서 스크롤 이벤트를 처리하기 위해서는 ScrollController를 사용해야 합니다. 이 때, 플러터 2.15.0 버전부터는 useScrollController Hook을 사용하여 ScrollController를 간편하게 관리할 수 있습니다.

먼저, flutter_hooks 패키지가 설치되어 있는지 확인해야 합니다. 만약 설치되어 있지 않다면, pubspec.yaml 파일의 dependencies 섹션에 다음과 같이 추가합니다.

```
dependencies:
  flutter_hooks: ^1.1.0
```

이제 useScrollController Hook을 사용하여 스크롤 이벤트를 처리할 수 있습니다. 다음은 예제 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final scrollController = useScrollController();

    useEffect(() {
      scrollController.addListener(() {
        if (scrollController.position.atEdge) {
          if (scrollController.position.pixels == 0) {
            // 스크롤이 최상단에 도달할 때 처리할 로직
            print('Reached the top');
          } else {
            // 스크롤이 최하단에 도달할 때 처리할 로직
            print('Reached the bottom');
          }
        }
      });

      return () {
        scrollController.dispose();
      };
    }, []);

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Scroll Event Example'),
        ),
        body: ListView.builder(
          controller: scrollController,
          itemCount: 100,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text('Item $index'),
            );
          },
        ),
      ),
    );
  }
}
```

위 코드에서는 useEffect Hook을 사용하여 스크롤 이벤트 리스너를 등록하고, 스크롤 이벤트에 따라 로직을 처리하고 있습니다. 스크롤이 최상단에 도달하거나 최하단에 도달한다면 각각 'Reached the top'과 'Reached the bottom'을 출력하도록 설정되어 있습니다.

이제 앱을 실행하고 스크롤 이벤트를 테스트해보세요. 스크롤이 최상단이나 최하단에 도달하면 해당 메시지가 출력될 것입니다.

이 예제 코드를 참고하여 플러터에서 스크롤 이벤트를 처리하는 방법을 익힐 수 있습니다.