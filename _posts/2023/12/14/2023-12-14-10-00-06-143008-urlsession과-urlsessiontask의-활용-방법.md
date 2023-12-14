---
layout: post
title: "[swift] URLSession과 URLSessionTask의 활용 방법"
description: " "
date: 2023-12-14
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발할 때 네트워크 통신은 중요한 부분입니다. **URLSession**과 **URLSessionTask**는 네트워킹을 단순화하고 관리하는 데 도움을 주는 클래스입니다. 이러한 클래스를 사용하여 원격 서버와 데이터를 주고받는 방법을 살펴보겠습니다.

## URLSession

**URLSession**은 네트워크 데이터 전송의 중앙 집중 지점으로, 데이터 전송을 위한 작업을 생성하고 관리하는 인터페이스를 제공합니다. URLSession은 데이터를 요청하고 응답을 처리하여 데이터 전송을 관리합니다.

아래는 **URLSession**을 사용하여 데이터를 가져오는 간단한 예제입니다.

```swift
let url = URL(string: "https://api.example.com/data")!
let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
    if let error = error {
        print("Error: \(error)")
    } else if let data = data {
        // 데이터를 처리하는 로직
    }
}
task.resume()
```

위의 코드에서 `URLSession.shared.dataTask(with:completionHandler:)` 메서드를 사용하여 데이터를 가져옵니다. 요청에 대한 응답은 completionHandler에서 처리됩니다.

## URLSessionTask

**URLSessionTask**는 개별 네트워크 데이터 전송 작업을 나타내며, URLSession 객체가 생성한 작업입니다. URLSessionTask는 작업을 강제로 취소하거나, 일시 중지하거나, 다시 시작하는 등의 작업을 할 수 있습니다.

아래는 **URLSessionTask**의 간단한 사용 예시입니다.

```swift
let url = URL(string: "https://api.example.com/upload")!
var request = URLRequest(url: url)
request.httpMethod = "POST"
let dataTask = URLSession.shared.uploadTask(with: request, from: data) { (data, response, error) in
    // 업로드 완료 후의 처리 로직
}
dataTask.resume()
```

위의 코드에서는 `URLSession.shared.uploadTask(with:from:completionHandler:)` 메서드를 사용하여 데이터를 업로드합니다.

**URLSession**과 **URLSessionTask**는 iOS 앱에서 네트워크 통신을 간편하게 처리할 수 있도록 도와주는 중요한 클래스 및 타입들입니다. 올바르게 활용하면 네트워크 통신 코드를 효율적으로 관리할 수 있습니다.

더 자세한 정보는 [Apple 개발자 문서](https://developer.apple.com/documentation/foundation/urlsession)를 참고하시기 바랍니다.