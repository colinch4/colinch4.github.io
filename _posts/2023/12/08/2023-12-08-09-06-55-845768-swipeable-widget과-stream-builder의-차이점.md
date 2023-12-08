---
layout: post
title: "[flutter] Swipeable Widget과 Stream Builder의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

이번 글에서는 Flutter 앱 개발 시 자주 사용되는 **Swipeable Widget**과 **Stream Builder**의 차이점을 알아보겠습니다.

## Swipeable Widget

**Swipeable Widget**은 사용자가 각 항목을 swipe(스와이프)하여 원하는 동작을 수행할 수 있도록 하는 기능을 제공합니다. 예를 들어, 메일함 앱에서 이메일 항목을 swipe하여 삭제 또는 보관할 수 있는 UI를 구현하고 싶다면 **Swipeable Widget**을 사용할 수 있습니다. 이런 기능을 제공하기 위해 **Swipeable Widget**은 **onSwipe** 이벤트에 대한 처리를 간편하게 구현할 수 있도록 해줍니다.

```dart
SwipeActionCell(
  key: GlobalKey(),
  actions: <SwipeAction>[
    SwipeAction(
      title: 'Delete',
      onTap: (handler) {
        _deleteItem(item);
        handler(false);
      },
      color: Colors.red,
    ),
    SwipeAction(
      title: 'Archive',
      onTap: (handler) {
        _archiveItem(item);
        handler(false);
      },
      color: Colors.blue,
    ),
  ],
  child: ListTile(
    title: Text(item.title),
    subtitle: Text(item.subtitle),
  ),
),
```

위의 예시 코드는 **Swipeable Widget**을 사용하여 리스트의 각 항목을 swipe하여 삭제 또는 보관할 수 있는 UI를 구현한 것입니다.

## Stream Builder

**Stream Builder**는 **Stream**에서 방출되는 데이터에 따라 UI를 업데이트할 수 있도록 도와줍니다. 예를 들어, 실시간으로 변화하는 데이터를 화면에 반영하고 싶을 때 **Stream Builder**를 사용할 수 있습니다. 예를 들어, 채팅방 화면에서 상대방의 메시지를 실시간으로 반영하고 싶을 때 **Stream Builder**를 사용하여 쉽게 구현할 수 있습니다.

```dart
StreamBuilder<List<Message>>(
  stream: chatRoomMessagesStream,
  builder: (context, snapshot) {
    if (snapshot.hasData) {
      return ListView.builder(
        itemCount: snapshot.data.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(snapshot.data[index].text),
            subtitle: Text(snapshot.data[index].timestamp),
          );
        },
      );
    } else {
      return CircularProgressIndicator();
    }
  },
)
```

위의 예시 코드는 **Stream Builder**를 사용하여 실시간 채팅방의 메시지를 화면에 반영한 것입니다. **chatRoomMessagesStream**은 실시간으로 메시지를 방출하는 **Stream**을 가정한 것입니다.

## 결론

**Swipeable Widget**과 **Stream Builder**는 각기 다른 목적과 사용 사례를 가지고 있습니다. **Swipeable Widget**은 사용자 상호작용을 통해 특정 동작을 수행하는 UI를, **Stream Builder**는 **Stream**에서 방출되는 데이터에 따라 동적으로 UI를 업데이트하는 데 사용됩니다.

이러한 기능들을 효과적으로 사용하여 Flutter 앱의 사용자 경험을 향상시키는데 도움이 될 것입니다.

## References
- [Flutter Documentation - SwipeActionCell](https://pub.dev/packages/swipedetector)
- [Flutter Documentation - StreamBuilder](https://api.flutter.dev/flutter/widgets/StreamBuilder-class.html)