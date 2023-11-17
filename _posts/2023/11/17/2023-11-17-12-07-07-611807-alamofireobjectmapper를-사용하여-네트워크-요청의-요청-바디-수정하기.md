---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 요청 바디 수정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

애플리케이션에서 네트워크 요청을 보낼 때, 종종 요청 바디를 수정해야 할 때가 있습니다. 이때 AlamofireObjectMapper 라이브러리를 사용하면 네트워크 요청의 요청 바디를 쉽게 수정할 수 있습니다. 

이번 포스트에서는 AlamofireObjectMapper를 사용하여 네트워크 요청의 요청 바디를 수정하는 방법에 대해 알아보겠습니다.

## 1. Alamofire 및 AlamofireObjectMapper 라이브러리 설치하기

먼저, 프로젝트에 Alamofire와 AlamofireObjectMapper 라이브러리를 설치해야 합니다. CocoaPods를 사용하여 설치하는 경우, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'Alamofire'
pod 'AlamofireObjectMapper'
```

설치 후, 프로젝트를 업데이트하기 위해 터미널에서 다음 명령어를 실행합니다.

```
$ pod install
```

## 2. 네트워크 요청 및 요청 바디 수정하기

요청 바디를 수정하기 위해서는 ObjectMapper를 사용하여 JSON 데이터를 객체로 매핑해야 합니다. 이때, 객체는 매핑되기 위해 Mappable 프로토콜을 준수해야 합니다.

예를 들어, 다음과 같이 사용자 정보를 담은 User 클래스가 있다고 가정해 봅시다.

```swift
import ObjectMapper

class User: Mappable {
    var name: String?
    var email: String?
    
    required init?(map: Map) { }
    
    func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
}
```

이제 Alamofire를 사용하여 네트워크 요청을 보낼 수 있습니다. 요청 바디를 수정할 때에는 `ObjectMapper`의 `toJSONString()` 메서드를 사용하여 객체를 JSON 문자열로 변환한 후, `CustomStringConvertible` 프로토콜을 준수하는 `URLRequestConvertible`를 구현해야 합니다.

```swift
import Alamofire
import AlamofireObjectMapper

let user = User()
user.name = "John Doe"
user.email = "john.doe@example.com"

let urlString = "https://api.example.com/user"

if let request = try? URLRequest(url: urlString, method: .post) {
    let modifiedRequestBody = user.toJSONString()
    request.httpBody = modifiedRequestBody?.data(using: .utf8)
    
    Alamofire.request(request)
        .responseObject { (response: DataResponse<UserResponse>) in
            // 응답 데이터 처리
        }
}
```

위의 예제에서는 `Alamofire.request` 메서드를 사용하여 요청을 보내고, `AlamofireObjectMapper`의 `responseObject` 메서드를 사용하여 응답 데이터를 매핑합니다.

요청 바디를 수정하기 전에 원래의 요청을 `URLRequestConvertible` 프로토콜을 구현하여 저장해두었다가, 요청 바디 수정 후에 해당 요청을 보낼 수 있습니다.

## 결론

이제 AlamofireObjectMapper를 사용하여 네트워크 요청의 요청 바디를 쉽게 수정하는 방법을 알아보았습니다. Alamofire와 ObjectMapper를 함께 사용하여 네트워크 요청을 보내고 받는 것이 얼마나 간편하고 효율적인지를 경험해보시기 바랍니다.