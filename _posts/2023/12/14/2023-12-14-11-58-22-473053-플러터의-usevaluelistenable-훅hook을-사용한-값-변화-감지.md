---
layout: post
title: "[flutter] 플러터의 useValueListenable 훅(hook)을 사용한 값 변화 감지"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 모바일 앱을 개발하기 위한 Google의 UI 프레임워크입니다. 최근에 플러터에 추가된 **useValueListenable** 훅은 값의 변화를 감지하여 UI를 업데이트하는 데에 유용합니다. 

## useValueListenable 훅이란 무엇인가요?

**useValueListenable** 훅은 플러터의 **hooks** 패키지에 포함되어 있으며, UI를 업데이트하는 데 필요한 데이터 변화를 감지할 수 있습니다. 리액트의 **useState** 훅과 유사하지만, 특정한 값의 변화를 감지하는 데에 특화되어 있습니다.

## 사용법

다음은 **useValueListenable** 훅을 사용하여 값의 변화를 감지하는 간단한 예제 코드입니다.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final count = useState(0);
    final countNotifier = useValueListenable(count);
    
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Value Listenable Hook'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Count: ${count.value}',
              ),
              RaisedButton(
                child: Text('Increment'),
                onPressed: () {
                  count.value++;
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

위의 코드에서, **useValueListenable**를 사용하여 **count** 변수의 변화를 감지하고 이를 화면에 반영하고 있습니다.

## 결론

플러터의 **useValueListenable** 훅을 사용하면 값을 감지하여 UI를 업데이트하는 작업을 더 효율적으로 수행할 수 있습니다. 이 훅을 적절히 활용하면 앱의 성능과 사용자 경험을 향상시킬 수 있습니다.

더 많은 정보를 원하시면 [플러터 공식 문서](https://flutter.dev/docs)를 참조하시기 바랍니다.