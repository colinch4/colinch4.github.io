---
layout: post
title: "[flutter] 플러터 Swipeable과 React Native에서의 Swipeable 비교"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

플러터와 React Native는 모바일 앱 개발을 위한 인기 있는 프레임워크입니다. 이번에는 두 프레임워크에서 제공하는 Swipeable(좌우로 드래그하여 동작하는) 기능을 비교해보겠습니다. 

## Swipeable이란?
Swipeable은 모바일 앱에서 많이 사용되는 기능으로, 리스트 아이템이나 카드를 좌우로 드래그하여 삭제, 수정 또는 추가 기능을 수행할 수 있도록 합니다.

## 플러터의 Swipeable
플러터에서는 `Dismissible` 위젯을 사용하여 Swipeable 기능을 구현할 수 있습니다. 이 위젯은 드래그하여 아이템을 제거하는 기능을 쉽게 추가할 수 있도록 도와줍니다. 예를 들어, 다음과 같이 간단하게 사용할 수 있습니다.

```dart
Dismissible(
  key: Key(item.id),
  onDismissed: (direction) {
    setState(() {
      items.removeAt(index);
    });
  },
  background: Container(
    color: Colors.red,
    child: Icon(Icons.delete),
  ),
  child: ListTile(title: Text(item.title)),
);
```

## React Native의 Swipeable
React Native에서 Swipeable을 구현하려면 `react-native-gesture-handler` 라이브러리를 사용하여 Swipeable View를 만들 수 있습니다. 다음은 React Native에서 Swipeable을 구현하는 예제입니다.

```javascript
{% raw %}
import { Swipeable } from 'react-native-gesture-handler';

function ListItem() {
  const renderRightActions = () => (
    <View style={{ width: 80, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Delete</Text>
    </View>
  );

  return (
    <Swipeable renderRightActions={renderRightActions}>
      <View style={{ backgroundColor: 'white', padding: 20 }}>
        <Text>Item to swipe</Text>
      </View>
    </Swipeable>
  );
}
{% endraw %}
```

## 결론
플러터와 React Native 모두 Swipeable 기능을 구현하는 데 유용한 도구를 제공합니다. 두 프레임워크의 Swipeable 구현 방법은 조금씩 다를 수 있지만, 모바일 앱에서 사용하기 편리한 Swipeable 기능을 쉽게 추가할 수 있습니다.

이상으로, 플러터와 React Native에서의 Swipeable 비교를 마치겠습니다.

## 참고 자료
- [플러터 공식 문서](https://flutter.dev/docs)
- [React Native 공식 문서](https://reactnative.dev/docs/getting-started)