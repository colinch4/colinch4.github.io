---
layout: post
title: "[android] 안드로이드에서 CORS(Cross-Origin Resource Sharing) 다루기"
description: " "
date: 2023-12-20
tags: [android]
comments: true
share: true
---

인터넷에서 자원을 가져오거나 전송할 때, CORS(Cross-Origin Resource Sharing)는 다른 출처의 리소스에 대한 접근을 제어하는 메커니즘입니다. 안드로이드 앱에서 CORS 문제를 다루는 방법에 대해 알아봅시다.

## CORS란 무엇인가?

CORS는 웹 애플리케이션에서 한 도메인 또는 포트에서 로드된 자바스크립트가 다른 출처의 API에 접근할 수 있도록 하는 메커니즘입니다. 이것은 보안 상의 이유로 브라우저가 AJAX 요청을 차단하는 것을 우회하는 데 사용됩니다.

## 안드로이드 앱에서 CORS 다루기

안드로이드에서 CORS 문제를 해결하려면 `WebView`를 사용하여 외부 리소스에 액세스해야 하는 경우가 많습니다. 이때, `WebView`에서 `setWebChromeClient()` 메서드를 사용하여 `WebChromeClient`를 구현하여 CORS 정책을 우회할 수 있습니다.

```java
webView.setWebChromeClient(new WebChromeClient() {
    @Override
    public void onReceivedResponseHeaders(WebView view, WebResourceRequest request, WebResourceResponse response) {
        super.onReceivedResponseHeaders(view, request, response);
        // CORS policy handling code
    }
});
```

위의 코드 예제에서 `onReceivedResponseHeaders()` 메서드를 오버라이드하여 CORS 정책을 적용할 수 있습니다.

## 결론

안드로이드 앱에서 CORS 문제를 다루는 것은 외부 리소스에 대한 접근을 보안적으로 제어하는 중요한 요소입니다. 위의 방법을 사용하여 안전하게 외부 리소스에 액세스할 수 있도록 안드로이드 앱을 구현할 수 있습니다.

참고문헌: [Mozilla Developer](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

이제 안드로이드 앱에서 CORS 문제를 다루는 방법에 대해 더 잘 이해하셨을 것입니다. 안드로이드 앱을 개발하거나 웹 리소스에 액세스할 때 CORS 문제를 안전하게 다루실 수 있을 것입니다.