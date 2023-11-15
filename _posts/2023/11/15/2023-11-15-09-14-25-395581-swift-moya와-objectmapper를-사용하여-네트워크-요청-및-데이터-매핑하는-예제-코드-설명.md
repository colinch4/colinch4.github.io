---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift의 Moya와 ObjectMapper를 사용하여 네트워크 요청을 수행하고, 서버에서 받은 JSON 데이터를 객체로 매핑하는 방법에 대해 알아보겠습니다.

## 1. Moya 및 ObjectMapper 설치하기

먼저, Moya와 ObjectMapper를 프로젝트에 추가해야 합니다. 이를 위해 CocoaPods를 사용하겠습니다. Podfile에 다음과 같이 작성하여 Moya와 ObjectMapper를 설치합니다.

```ruby
target 'YourProjectName' do
  use_frameworks!
  pod 'Moya'
  pod 'ObjectMapper'
end
```

Podfile을 저장한 후, `pod install` 명령어를 실행하여 의존성을 설치합니다.

## 2. 모델 클래스 작성하기

서버에서 받은 JSON 데이터를 매핑하기 위해 모델 클래스를 작성해야 합니다. 예를 들어, 아래와 같은 User 모델 클래스를 만들어 보겠습니다.

```swift
import Foundation
import ObjectMapper

struct User: Mappable {
    var id: Int
    var name: String
    var email: String

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

위 코드에서는 ObjectMapper의 `Mappable` 프로토콜을 구현한 User 구조체를 정의하였습니다. `mapping` 메서드를 사용하여 JSON 데이터의 키와 매핑할 속성을 지정합니다.

## 3. 네트워크 요청 및 데이터 매핑하기

Moya를 사용하여 네트워크 요청을 보내고, ObjectMapper를 사용하여 받은 JSON 데이터를 User 객체로 매핑하는 방법을 알아보겠습니다.

```swift
import Moya
import ObjectMapper

// Moya Provider 생성
let provider = MoyaProvider<YourAPI>()

provider.request(.getUser(userID: 1)) { result in
    switch result {
    case .success(let response):
        do {
            // JSON 데이터를 User 객체로 매핑
            let user = try response.mapObject(User.self)
            print(user)
        } catch {
            print("Mapping Error: \(error)")
        }
    case .failure(let error):
        print("Network Error: \(error)")
    }
}
```

위 코드에서 `YourAPI`는 실제 네트워크 요청에 대한 열거형입니다. 예를 들어 `.getUser(userID: 1)`는 서버로부터 특정 사용자의 데이터를 요청하는 경우를 나타냅니다.

네트워크 요청에 대한 응답이 성공하면, `response.mapObject(User.self)`를 사용하여 JSON을 User 객체로 매핑합니다. 실패할 경우에는 에러를 처리하도록 합니다.

이제 Moya와 ObjectMapper를 사용하여 네트워크 요청을 보내고, 받은 JSON 데이터를 객체로 매핑하는 과정을 알아보았습니다. 이를 활용하여 원하는 네트워크 요청 및 데이터 매핑을 구현해 보세요!

## 참고 자료
- [Moya GitHub](https://github.com/Moya/Moya)
- [ObjectMapper GitHub](https://github.com/tristanhimmelman/ObjectMapper)