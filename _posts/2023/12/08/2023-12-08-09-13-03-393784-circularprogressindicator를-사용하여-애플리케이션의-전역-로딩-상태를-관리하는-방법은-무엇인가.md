---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 애플리케이션의 전역 로딩 상태를 관리하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

로딩 상태를 효과적으로 관리하려면 **CircularProgressIndicator**을 사용하는 것이 유용합니다. **CircularProgressIndicator**는 사용자에게 애플리케이션이 작업을 수행 중임을 시각적으로 알려줍니다. Flutter 애플리케이션에서 **CircularProgressIndicator**를 사용하여 전역 로딩 상태를 관리하는 방법을 살펴보겠습니다.

## 1. CircularProgressIndicator 추가

먼저, 애플리케이션의 전역 로딩 상태를 나타내기 위해 **CircularProgressIndicator** 위젯을 적절한 위치에 추가해야 합니다. 예를 들어, 애플리케이션의 모든 화면 상단에 **CircularProgressIndicator**를 추가하여 전역 로딩 상태를 관리할 수 있습니다.

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('My App'),
        ),
        body: Stack(
          children: [
            // 다른 위젯들과 함께 CircularProgressIndicator 추가
            // 로딩 상태에 따라 가시성 제어 가능
            CircularProgressIndicator(),
            // 나머지 위젯들 추가
          ],
        ),
      ),
    );
  }
}
```

## 2. 로딩 상태 관리

로딩 상태를 관리하려면 **CircularProgressIndicator** 위젯을 가시성을 제어하는 방법이 필요합니다. 보통 **isLoading**과 같은 상태 변수를 사용하여 **CircularProgressIndicator**를 표시할지 여부를 결정합니다. 이 변수를 변경하여 로딩 상태를 쉽게 관리할 수 있습니다.

```dart
class MyLoadingScreen extends StatelessWidget {
  final bool isLoading;

  MyLoadingScreen(this.isLoading);

  @override
  Widget build(BuildContext context) {
    return isLoading ? CircularProgressIndicator() : Container();
  }
}
```

## 3. 비동기 작업과 함께 사용하기

**CircularProgressIndicator**를 주로 비동기 작업 중에 보여주는 것이 일반적입니다. Dart의 **Future**나 **Stream**과 결합하여 비동기 작업을 수행할 때 **CircularProgressIndicator**를 보여줄 수 있습니다.

```dart
class MyAsyncScreen extends StatefulWidget {
  @override
  _MyAsyncScreenState createState() => _MyAsyncScreenState();
}

class _MyAsyncScreenState extends State<MyAsyncScreen> {
  bool _isLoading = false;

  void _loadData() async {
    setState(() {
      _isLoading = true; // 데이터 로딩 시작
    });

    // 비동기 작업 수행
    await fetchData(); // 예: 네트워크 요청

    setState(() {
      _isLoading = false; // 데이터 로딩 완료
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Async Screen'),
      ),
      body: Center(
        child: _isLoading ? CircularProgressIndicator() : ElevatedButton(
          onPressed: _loadData,
          child: Text('Load Data'),
        ),
      ),
    );
  }
}
```

이와 같이 **CircularProgressIndicator**를 사용하여 애플리케이션의 전역 로딩 상태를 관리할 수 있습니다. 위의 방법들을 참고하여 로딩 상태를 시각적으로 표현하고, 효율적으로 관리할 수 있습니다.

## 참고 자료
- [Flutter 공식 문서 - CircularProgressIndicator](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)

---  

위의 내용은 Flutter 애플리케이션에서 **CircularProgressIndicator**를 사용하여 전역 로딩 상태를 관리하는 방법에 대한 가이드입니다. 필요하다면 실제 애플리케이션에 적용하여 로딩 상태를 효과적으로 관리해보시기 바랍니다.