---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청에 헤더 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire와 ObjectMapper를 함께 사용하여 네트워크 요청과 JSON 데이터 매핑을 쉽게 할 수 있는 Swift 라이브러리입니다. 이 라이브러리를 사용하여 네트워크 요청을 보낼 때 원하는 헤더를 간단하게 추가할 수 있습니다.

## AlamofireObjectMapper 설치하기

먼저, AlamofireObjectMapper를 설치해야 합니다. CocoaPods를 사용하는 경우 Podfile에 다음을 추가합니다:

```ruby
pod 'AlamofireObjectMapper'
```

그런 다음 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다:

```bash
pod install
```

## 헤더 추가하기

AlamofireObjectMapper를 사용하여 네트워크 요청을 보낼 때 헤더를 추가하는 방법은 간단합니다. 먼저, Alamofire의 `SessionManager`를 사용하여 기본 `HTTPHeaders`를 설정합니다.

```swift
import Alamofire

let headers: HTTPHeaders = [
    "Authorization": "Bearer YOUR_AUTH_TOKEN",
    "Accept": "application/json"
]

let configuration = URLSessionConfiguration.default
configuration.httpAdditionalHeaders = headers

let manager = Alamofire.SessionManager(configuration: configuration)
```

위의 코드에서 `"Authorization"`과 `"Accept"`은 예시입니다. 실제로 사용할 헤더 키와 값으로 바꿔주어야 합니다.

그런 다음, `manager`를 사용하여 네트워크 요청을 보냅니다:

```swift
manager.request("https://api.example.com/users")
    .responseJSON { response in
        // JSON 데이터 매핑 등의 작업을 수행할 수 있습니다.
    }
```

`manager`를 사용하면 이전에 설정한 헤더가 자동으로 추가됩니다.

## 결론

AlamofireObjectMapper를 사용해 네트워크 요청에 헤더를 추가하는 방법을 알아보았습니다. 이를 통해 더욱 유연하고 효율적인 네트워크 통신을 구현할 수 있습니다. 자세한 내용은 [Alamofire](https://github.com/Alamofire/Alamofire)와 [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)의 공식 문서를 참조하시기 바랍니다.