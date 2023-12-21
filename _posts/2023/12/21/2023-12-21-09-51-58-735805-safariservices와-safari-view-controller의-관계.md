---
layout: post
title: "[ios] SafariServices와 Safari View Controller의 관계"
description: " "
date: 2023-12-21
tags: [ios]
comments: true
share: true
---

iOS 앱 내에서 웹 컨텐츠를 표시하거나 웹 브라우징을 허용하는 경우, SafariServices 프레임워크의 Safari View Controller를 사용할 수 있습니다. SafariServices는 iOS 9부터 도입되었으며, 사용자가 iOS 장치에서 웹 브라우징하는 동안 Safari 브라우저의 기능과 형태를 완전히 유지하면서, 응용 프로그램 내에서 웹 페이지를 표시하는 기능을 제공합니다.

## Safari View Controller란?
Safari View Controller는 사용자가 앱을 벗어나지 않고도 웹페이지를 표시하고 웹브라우징을 할 수 있도록 하는 시스템 제공 뷰 컨트롤러입니다. 이를 통해 개발자는 자체 앱 내에서 완전한 Safari 기능을 제공할 수 있습니다.

## SafariServices 프레임워크
SafariServices 프레임워크는 iOS의 기본 사파리 브라우저와 동일한 브라우징 경험을 제공하여 사용자에게 일관된 사용자 경험을 제공할 수 있도록 해줍니다. 또한, SafariServices 프레임워크는 SSO (Single Sign-On) 및 사파리 기반 콘텐츠의 표시 및 상호 작용에 대한 통합 지원도 제공합니다.

## 사용 예시
SafariServices 프레임워크를 사용하여 Safari View Controller를 통해 웹 콘텐츠를 표시하려면 다음과 같이 코드를 작성할 수 있습니다:

```swift
import SafariServices

let url = URL(string: "https://www.example.com")!
let safariViewController = SFSafariViewController(url: url)
present(safariViewController, animated: true, completion: nil)
```

위의 코드는 `SFSafariViewController`로부터 인스턴스를 생성하고, 해당 인스턴스를 사용하여 원하는 URL을 로드한 다음, 현재 view에 present하여 Safari View Controller를 표시합니다.

## 결론
SafariServices 프레임워크와 Safari View Controller는 iOS 앱에서 웹 브라우징을 위한 강력한 기능을 제공합니다. 이를 통해 개발자는 앱 안에서 쉽게 웹 콘텐츠를 표시할 수 있으며, 사용자는 자연스럽게 Safari와 같은 브라우징 경험을 누릴 수 있습니다.

저는 이 문서를 작성할 때 아래의 문서를 참고하였습니다.
- [SafariServices - Apple Developer Documentation](https://developer.apple.com/documentation/safariservices)