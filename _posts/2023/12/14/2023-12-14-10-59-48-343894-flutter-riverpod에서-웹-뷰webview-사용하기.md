---
layout: post
title: "[flutter] Flutter Riverpod에서 웹 뷰(WebView) 사용하기"
description: " "
date: 2023-12-14
tags: [flutter]
comments: true
share: true
---

웹 뷰(WebView)는 Flutter 앱에서 웹 콘텐츠를 표시하는 화면 요소입니다. riverpod는 상태 관리를 위한 강력한 라이브러리로, Flutter 앱에서 WebView를 사용하는 데 도움을 줍니다. 이 글에서는 Flutter 프로젝트에 riverpod와 WebView를 통합하는 방법을 알아보겠습니다.

## 1. flutter_webview_plugin 설치하기

먼저, `flutter_webview_plugin`을 pubspec.yaml 파일의 dependencies에 추가하여 웹 뷰(WebView)를 사용할 수 있도록 설치합니다.

```json
dependencies:
  flutter_webview_plugin: ^0.3.11
```

설치가 완료되면 터미널에서 `flutter pub get` 명령어를 실행하여 패키지를 가져옵니다.

## 2. Riverpod Provider 생성하기

아래와 같이 Riverpod의 Provider를 사용하여 웹 뷰(WebView)를 관리합니다. 

```dart
final webViewProvider = StateNotifierProvider<WebViewModel, WebViewModelState>((ref) {
  return WebViewModel();
});
```

## 3. WebView 위젯 생성하기

WebView 위젯은 Provider로부터 URL을 받아 웹 페이지를 표시합니다.

```dart
class WebViewWidget extends ConsumerWidget {
  @override
  Widget build(BuildContext context, ScopedReader watch) {
    final url = watch(webViewProvider.state).url;
    return WebView(
      initialUrl: url,
      javascriptMode: JavascriptMode.unrestricted,
    );
  }
}
```

위 코드에서 `watch(webViewProvider.state).url`은 Riverpod Provider로부터 URL을 가져오는 부분입니다.

## 4. Riverpod Provider 상태 업데이트하기

아래와 같이 Riverpod Provider의 상태를 업데이트하여 WebView의 URL을 변경할 수 있습니다.

```dart
class WebViewModel extends StateNotifier<WebViewModelState> {
  WebViewModel() : super(WebViewModelState());

  void updateUrl(String newUrl) {
    state = state.copyWith(url: newUrl);
  }
}

class WebViewModelState {
  final String url;

  WebViewModelState({this.url = ''});

  WebViewModelState copyWith({String url}) {
    return WebViewModelState(
      url: url ?? this.url,
    );
  }
}
```

## 마치며

위 방법을 통해 Riverpod를 사용하여 Flutter 앱에 WebView를 통합할 수 있습니다. 이를 통해 상태 관리와 뷰 표시를 Riverpod를 통해 효과적으로 관리할 수 있습니다.

## 참고 자료

- [flutter_webview_plugin 패키지](https://pub.dev/packages/flutter_webview_plugin)
- [Riverpod 공식 문서](https://riverpod.dev/)