---
layout: post
title: "[ios] SFSafariViewController"
description: " "
date: 2023-12-26
tags: [ios]
comments: true
share: true
---

SFSafariViewController는 iOS 앱 내에서 웹 브라우징을 위한 시스템 제공 뷰 컨트롤러이다.

## 특징

- **기본 브라우저 사용**: SFSafariViewController는 사용자의 기본 웹 브라우저 설정을 따르므로 사용자가 이미 로그인한 상태나 쿠키가 저장된 상태를 바로 가져올 수 있다.

- **간편한 사용**: 단 몇 줄의 코드만으로도 SFSafariViewController를 띄울 수 있어서 사용하기 매우 쉽다.

- **사용자 경험**: SFSafariViewController는 웹 브라우징을 즐겁고 편리하게 만들어주는 기능들을 지원한다. 카드 스타일의 모달 뷰를 이용해 사용자의 흐름을 깨지 않고 브라우징을 할 수 있다.

## 예제

```swift
import SafariServices

let url = URL(string: "https://www.example.com")!
let safariViewController = SFSafariViewController(url: url)
present(safariViewController, animated: true, completion: nil)
```

## 결론

SFSafariViewController를 사용하면 웹 브라우징 기능을 쉽게 앱에 추가할 수 있고, 기존의 사용자 브라우저 설정을 그대로 활용할 수 있어서 사용자 경험을 개선시킬 수 있다.

더 많은 정보는 [애플 공식 문서](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller)에서 확인할 수 있다.