---
layout: post
title: "[ios] JavaScriptCore를 사용하여 iOS 웹뷰에서 JavaScript 코드 실행하기"
description: " "
date: 2023-12-21
tags: [ios]
comments: true
share: true
---

iOS 앱을 개발할 때, 때때로 웹뷰를 사용하여 웹 페이지를 표시해야 할 때가 있습니다. 때로는 웹페이지가 특정 기능을 수행하기 위해 JavaScript 코드를 실행해야 할 수도 있습니다. 이런 상황에서 iOS의 `JavaScriptCore`를 사용하여 JavaScript 코드를 실행하는 방법에 대해 알아보겠습니다.

## JavaScriptCore란?

`JavaScriptCore`는 WebKit 프레임워크에서 제공하는 JavaScript 엔진으로, iOS 앱 안에서 JavaScript 코드를 실행하고 상호 작용할 수 있도록 해줍니다. 이를 사용하여 iOS 웹뷰에서 JavaScript를 실행할 수 있습니다.

## iOS 웹뷰에서 JavaScript 코드 실행하기

보통 iOS 웹뷰에서 JavaScript 코드를 실행하려면 다음의 단계를 따릅니다.

1. `JavaScriptCore` 프레임워크를 import 합니다.
2. iOS 웹뷰의 `evaluateJavaScript` 메서드를 사용하여 JavaScript 코드를 실행합니다.

다음은 간단한 예제 코드입니다. 

```swift
import JavaScriptCore
import UIKit
import WebKit

class ViewController: UIViewController, WKNavigationDelegate {
    var webView: WKWebView!

    override func loadView() {
        webView = WKWebView()
        webView.navigationDelegate = self
        view = webView
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let context: JSContext = webView.value(forKeyPath: "documentView.webView.mainFrame.javaScriptContext") as! JSContext

        let result = context.evaluateScript("2 + 2")
        print(result) // 출력 결과: Optional(4)
    }
}
```

위의 예제 코드에서는 iOS 웹뷰를 만들고, JavaScriptCore를 사용하여 JavaScript 코드를 실행한 후 결과를 콘솔에 출력합니다.

## 결론

iOS 웹뷰에서 JavaScript 코드를 실행하는 것은 `JavaScriptCore`를 사용하여 간단히 처리할 수 있습니다. 이를 통해 iOS 앱과 웹페이지 간의 상호 작용을 가능하게 할 수 있습니다.

## 참고 자료
1. [JavaScriptCore - Apple Developer Documentation](https://developer.apple.com/documentation/javascriptcore)
2. [WKWebView - Apple Developer Documentation](https://developer.apple.com/documentation/webkit/wkwebview)