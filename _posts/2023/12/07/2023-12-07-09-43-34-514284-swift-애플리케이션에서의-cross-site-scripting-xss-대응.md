---
layout: post
title: "[swift] Swift 애플리케이션에서의 Cross-site Scripting (XSS) 대응"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

## 목차
- [XSS란 무엇인가?](#xss란-무엇인가)
- [Swift 애플리케이션에서의 XSS 공격 대응](#swift-애플리케이션에서의-xss-공격-대응)
  - [1. 사용자 입력 검증](#1-사용자-입력-검증)
  - [2. 문자열 이스케이프](#2-문자열-이스케이프)
  - [3. Content Security Policy (CSP) 설정](#3-content-security-policy-csp-설정)
- [참고 자료](#참고-자료)

## XSS란 무엇인가?
Cross-site Scripting (XSS)은 웹 애플리케이션에서 발생할 수 있는 보안 취약점 중 하나입니다. 공격자는 악의적인 스크립트를 제공하여 사용자의 브라우저에서 실행되도록 하여, 사용자의 정보를 탈취하거나 애플리케이션을 조작할 수 있습니다.

XSS 공격은 주로 사용자의 입력값을 그대로 출력화면에 표시할 때 발생하는데, 이는 Swift 애플리케이션에서도 동일한 위험을 가질 수 있습니다.

## Swift 애플리케이션에서의 XSS 공격 대응

### 1. 사용자 입력 검증
XSS 공격을 대응하기 위해서는 사용자의 입력 값을 신뢰할 수 있는 형태로 변환해야 합니다. Swift 애플리케이션에서는 사용자의 입력값을 검증하고, 필요한 경우에는 특수문자나 HTML 태그를 제거 또는 이스케이프 처리해야 합니다.

```swift
let userInput = "<script>alert('XSS')</script>"
let safeInput = userInput.replacingOccurrences(of: "<", with: "&lt;").replacingOccurrences(of: ">", with: "&gt;")

print(safeInput) // &lt;script&gt;alert('XSS')&lt;/script&gt;
```

### 2. 문자열 이스케이프
Swift 애플리케이션에서는 `NSAttributedString`을 사용하여 텍스트를 표시하는 경우도 많습니다. 이 경우에는 문자열에 HTML이 포함될 수 있으므로, 이스케이프 처리를 해주어야 합니다.

```swift
let htmlString = "<p>This is some <b>bold</b> text.</p>"
let encodedString = htmlString.data(using: .utf8)?.base64EncodedString()

let attributedString = try? NSAttributedString(data: Data(base64Encoded: encodedString ?? "") ?? Data(), options: [.documentType: NSAttributedString.DocumentType.html], documentAttributes: nil)

print(attributedString?.string ?? "") // This is some bold text.
```

### 3. Content Security Policy (CSP) 설정
CSP는 웹 애플리케이션에서 XSS 공격을 방지하기 위한 기술입니다. CSP를 사용하면 애플리케이션에서 로드되는 외부 리소스의 도메인과 허용되는 스크립트 실행 방식을 제한할 수 있습니다.

Swift 애플리케이션에서 웹뷰를 사용하는 경우에는 `WKWebView`의 `configuration` 속성을 사용하여 CSP를 설정할 수 있습니다.

```swift
import WebKit

let webView = WKWebView()
let userScript = WKUserScript(source: "default-src 'self'; script-src 'self' example.com", injectionTime: .atDocumentEnd, forMainFrameOnly: true)

let contentController = webView.configuration.userContentController
contentController.addUserScript(userScript)
```

## 참고 자료
- [Cross-site Scripting (XSS) - OWASP](https://owasp.org/www-community/attacks/xss/)
- [NSAttributedString - Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsattributedstring)
- [WKWebView - Apple Developer Documentation](https://developer.apple.com/documentation/webkit/wkwebview)
- [WebKit Content Security Policy Level 2 Specification](https://developer.apple.com/documentation/webkitjs/content_security_policy_level_2_specification)