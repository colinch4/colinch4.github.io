---
layout: post
title: "[flutter] Swipeable Widget과 Touchable Opacity의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

In Flutter, there are several ways to make parts of your app interactive. Two popular methods are **Swipeable Widget** and **Touchable Opacity**. While both are used to create interactive elements, they have differences that make them suitable for different use cases.

## Swipeable Widget

**Swipeable Widget** allows users to swipe left or right to interact with the content. It is commonly used for actions like deleting an item from a list or navigating between different screens. Using the `flutter_swipe_action_cell` package, you can easily implement Swipeable Widgets in your app. 

```dart
import 'package:flutter_swipe_action_cell/flutter_swipe_action_cell.dart';

SwipeActionCell(
  key: Key('key'), // A key to re-render or delete the widget.
  performsFirstActionWithFullSwipe: true,
  trailingActions: <SwipeAction>[
    SwipeAction(
      onTap: (CompletionHandler handler) {
        _performSwipeAction(callback: handler, actionIndex: 0);
      },
      color: Colors.red,
      content: Container(
        padding: EdgeInsets.all(10),
        child: Icon(
          Icons.delete,
          color: Colors.white,
        ),
      ),
    ),
  ],
  child: /* Your content here */,
);
```

## Touchable Opacity

**Touchable Opacity** is used to make any widget tappable. It provides touch feedback when the user presses the widget. This is commonly used for buttons and other elements that the user should be able to interact with.

```dart
import 'package:flutter/material.dart';

class MyButton extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        // Handle the tap event
      },
      child: Container(
        padding: EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.blue,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Text(
          'Tap me',
          style: TextStyle(color: Colors.white, fontSize: 16),
        ),
      ),
    );
  }
}
```

## Which Should You Use?

- Use **Swipeable Widget** when you need to provide swipe-based interactions such as deleting items or revealing hidden actions.
- Use **Touchable Opacity** when you want to make any widget tappable, especially for buttons and other interactive elements.
- **Swipeable Widgets** are more suitable for actions that require swipe gestures, whereas **Touchable Opacity** is ideal for adding tap functionality to any widget.

In conclusion, understanding the differences between Swipeable Widgets and Touchable Opacity will help you choose the right method for creating interactive elements in your Flutter app.

---
*References:*
- Flutter Swipeable Widgets: [flutter_swipe_action_cell](https://pub.dev/packages/flutter_swipe_action_cell)
- Flutter Touchable Opacity: [GestureDetector class](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html)