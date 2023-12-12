---
layout: post
title: "[flutter] RefreshIndicator와 함께 사용하는 FutureBuilder 이해하기"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

Flutter 앱을 개발할 때 데이터를 비동기적으로 불러오는 경우가 많습니다. 이때 RefreshIndicator와 FutureBuilder를 함께 사용하여 스크롤하여 새로고침하는 동작을 구현하고, 데이터를 비동기적으로 로드하고 나타내는 기능을 추가할 수 있습니다. 이번 글에서는 RefreshIndicator와 FutureBuilder를 함께 사용하는 방법을 살펴보겠습니다.

## RefreshIndicator란?

RefreshIndicator는 스크롤하여 새로고침하는 기능을 제공합니다. 일반적으로 ListView나 GridView 등과 함께 사용되어 사용자가 화면을 아래로 당겨 새로고침하도록 유도합니다.

## FutureBuilder란?

FutureBuilder는 비동기적으로 데이터를 불러와서 나타내는데 사용됩니다. FutureBuilder는 Future 객체를 받아 그 결과에 따라 다양한 UI를 빌드할 수 있도록 해줍니다.

### RefreshIndicator와 FutureBuilder 함께 사용하기

```dart
RefreshIndicator(
  onRefresh: () {
    // 데이터 새로고침 동작 구현
    return Future.delayed(Duration(seconds: 1));
  },
  child: FutureBuilder(
    // 비동기적으로 데이터를 불러오는 Future 객체
    future: fetchData(),
    builder: (context, snapshot) {
      if (snapshot.connectionState == ConnectionState.waiting) {
        return CircularProgressIndicator();
      } else if (snapshot.hasError) {
        return Text('Error: ${snapshot.error}');
      } else {
        return ListView.builder(
          itemCount: snapshot.data.length,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text(snapshot.data[index].title),
              subtitle: Text(snapshot.data[index].subtitle),
            );
          },
        );
      }
    },
  ),
)
```

위 예제에서는 RefreshIndicator를 사용하여 새로고침 동작을 구현하고, FutureBuilder를 사용하여 비동기적으로 데이터를 불러와서 UI를 나타내는 부분을 구현했습니다.

이제 RefreshIndicator와 FutureBuilder를 함께 사용하여 데이터를 새로고침하고 나타내는 Flutter 앱을 만들 수 있는 방법에 대해 이해하셨을 것입니다. 이를 통해 사용자가 쉽게 새로고침하여 최신 데이터를 확인할 수 있는 기능을 구현할 수 있습니다.

## 참고 자료
- [Flutter Documentation](https://flutter.dev/docs)
- [RefreshIndicator class - Flutter API Reference](https://api.flutter.dev/flutter/material/RefreshIndicator-class.html)
- [FutureBuilder class - Flutter API Reference](https://api.flutter.dev/flutter/widgets/FutureBuilder-class.html)