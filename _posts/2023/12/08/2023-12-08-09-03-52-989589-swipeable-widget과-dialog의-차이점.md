---
layout: post
title: "[flutter] Swipeable Widget과 Dialog의 차이점"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

모바일 애플리케이션을 개발할 때 필요한 기본적인 UI 컴포넌트 중 하나는 Swipeable Widget과 Dialog이다. 이 두 가지 컴포넌트는 사용자 경험을 향상시키고 기능적인 부분을 처리하는 데 도움이 된다. 하지만 두 컴포넌트는 서로 다른 목적과 사용 사례를 가지고 있다.

## Swipeable Widget

Swipeable Widget은 사용자가 화면에서 좌우로 스와이프하여 특정 작업을 실행할 수 있는 인터랙티브한 컴포넌트이다. 예를 들어, 사용자가 이메일 앱을 사용하는 경우, 각 이메일 항목 옆에 스와이프할 수 있는 아이콘이 있어서 사용자가 해당 이메일을 삭제하거나 아카이브할 수 있다. 이러한 Swipeable Widget은 목록이나 그리드와 같은 컬렉션을 다룰 때 유용하다.

```dart
SwipeToDismiss(
  key: Key(item),
  child: ListTile(
    title: Text(item),
  ),
  onDismissed: (direction) {
    // 해당 아이템을 삭제하거나 다른 작업 실행
  },
  background: Container(
    color: Colors.red,
    child: Icon(Icons.delete),
    alignment: Alignment.centerRight,
  ),
);
```

## Dialog

반면에 Dialog은 애플리케이션에서 정보를 표시하고 사용자의 입력이나 확인을 요청하는 데 사용된다. 주로 사용자와 상호작용이나 결정이 필요한 경우에 팝업 형태로 화면에 나타난다. 예를 들어, 사용자에게 어떤 작업을 수행하기 전에 확인 메시지를 표시하거나 입력 폼을 보여줄 때 사용된다.

```dart
showDialog(
  context: context,
  builder: (BuildContext context) {
    return AlertDialog(
      title: Text('알림'),
      content: Text('이 작업을 실행하시겠습니까?'),
      actions: <Widget>[
        FlatButton(
          onPressed: () {
            // 작업 실행
          },
          child: Text('확인'),
        ),
        FlatButton(
          onPressed: () {
            // 취소
            Navigator.of(context).pop();
          },
          child: Text('취소'),
        ),
      ],
    );
  },
);
```

## 결론

Swipeable Widget과 Dialog은 각각 다른 사용 사례와 목적을 가지고 있으며, 이를 적절히 활용하여 애플리케이션의 사용자 경험을 향상시키고 기능적인 요소를 유연하게 다룰 수 있다.

더 많은 정보를 원하신다면 Flutter 공식 문서를 참고해 주세요.

[Flutter 공식 문서](https://flutter.dev/docs)