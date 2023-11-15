---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 네트워크 요청 후 데이터를 모델에 매핑하는 코드 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift 프로그래밍 언어에서 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 요청을 보내고 받은 데이터를 모델에 매핑하는 방법을 알아보겠습니다.

## Moya 소개

[Moya](https://github.com/Moya/Moya)는 Swift에서 네트워크 작업을 쉽게 처리하기 위한 추상화된 네트워킹 라이브러리입니다. Moya를 사용하면 네트워크 작업에 대한 추상적인 계층을 제공하여 작업을 더 간결하고 유지보수하기 쉽게 만들어줍니다.

## ObjectMapper 소개

[ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)는 Swift에서 JSON 데이터를 객체로 매핑하기 위한 라이브러리입니다. ObjectMapper를 사용하면 JSON 데이터와 Swift 객체 간의 변환 작업을 쉽게 처리할 수 있습니다.

## 설치

먼저 Moya와 ObjectMapper 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가하고 `pod install` 명령을 실행합니다.

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

## 모델 정의

네트워크로부터 받은 데이터를 매핑하기 위해 먼저 모델을 정의해야 합니다. 예를 들어, 다음과 같이 `User` 모델을 정의하겠습니다.

```swift
import Foundation
import ObjectMapper

struct User: Mappable {
    var id: Int?
    var name: String?
    var email: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

`Mappable` 프로토콜을 구현하는 것으로 ObjectMapper와 연동할 수 있습니다. `mapping(map:)` 함수에서 JSON 키와 속성을 매핑합니다.

## 네트워크 요청

이제 Moya를 사용하여 네트워크 요청을 보내보겠습니다. 다음은 Moya를 사용한 기본적인 네트워크 요청 코드입니다.

```swift
import Moya

let provider = MoyaProvider<API>()

provider.request(.getUser(id: 1)) { result in
    switch result {
    case .success(let response):
        do {
            let json = try JSONSerialization.jsonObject(with: response.data, options: [])
            if let user = Mapper<User>().map(JSON: json as! [String: Any]) {
                // 성공적으로 모델에 매핑된 경우 사용자 정보를 활용할 수 있습니다.
                print(user.name ?? "No name")
            }
        } catch {
            print("JSON serialization error: \(error.localizedDescription)")
        }
    case .failure(let error):
        print("Network request error: \(error.localizedDescription)")
    }
}
```

위의 코드에서는 `MoyaProvider`를 초기화한 후 `.getUser(id: 1)`와 같은 열거형 값을 사용하여 요청을 보냅니다. 네트워크 요청 결과는 `result` 매개변수로 받게 되며, 성공적인 경우 JSON 데이터를 ObjectMapper를 사용하여 `User` 모델에 매핑합니다.

## 결론

이 예제에서는 Swift에서 Moya와 ObjectMapper를 사용하여 네트워크 요청 후 데이터를 모델에 매핑하는 방법을 알아보았습니다. Moya를 사용하면 네트워크 작업을 추상화하여 코드를 간결하게 유지할 수 있고, ObjectMapper를 사용하면 JSON 데이터를 객체로 쉽게 매핑할 수 있습니다. 이러한 라이브러리들은 Swift 개발을 편리하게 만들어주며, 네트워크 작업과 데이터 매핑에 큰 도움이 됩니다.