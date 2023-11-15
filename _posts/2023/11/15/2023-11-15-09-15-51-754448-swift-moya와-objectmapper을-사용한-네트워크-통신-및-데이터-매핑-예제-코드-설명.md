---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift에서 Moya와 ObjectMapper을 함께 사용하여 네트워크 통신을 수행하고 데이터를 매핑하는 방법을 알아보겠습니다. Moya는 네트워크 추상화 라이브러리로, Alamofire를 기반으로 구현되어 있습니다. ObjectMapper는 JSON 데이터를 Swift 객체로 매핑하는데 사용되는 라이브러리입니다.

## Moya 및 ObjectMapper 설치

먼저 프로젝트에 Moya와 ObjectMapper을 설치해야 합니다. CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 의존성을 설치합니다.

## 모델 클래스 생성

데이터를 매핑하기 위해 모델 클래스를 생성해야 합니다. 예를 들어, 서버로부터 받아온 JSON 데이터의 구조와 동일한 구조를 가지는 `User` 모델 클래스를 생성해보겠습니다.

```swift
import Foundation
import ObjectMapper

class User: Mappable {
    var name: String?
    var email: String?
    var age: Int?

    required init?(map: Map) {}

    func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
        age <- map["age"]
    }
}
```

위의 코드에서 `User` 클래스는 `Mappable` 프로토콜을 준수하며, `name`, `email`, `age` 속성을 가지고 있습니다. `mapping(map:)` 메서드를 통해 JSON 키와 속성 간의 매핑을 정의합니다.

## 네트워크 통신 및 데이터 매핑

이제 Moya와 ObjectMapper를 사용하여 네트워크 통신 및 데이터 매핑을 수행하는 예제 코드를 작성해보겠습니다. 아래 코드는 서버로부터 `User` 객체를 가져오는 API를 호출하는 예제입니다.

```swift
import Moya
import ObjectMapper

let provider = MoyaProvider<API>()

provider.request(.getUser(userID: 123)) { result in
    switch result {
    case .success(let response):
        do {
            let json = try response.mapJSON()
            if let user = Mapper<User>().map(JSONObject: json) {
                // 데이터 매핑 성공
                print(user.name)
                print(user.email)
                print(user.age)
            }
        } catch {
            // 데이터 매핑 실패
            print("Mapping error: \(error)")
        }
    case .failure(let error):
        // 네트워크 요청 실패
        print("Network error: \(error)")
    }
}
```

위의 코드에서 `MoyaProvider`를 사용하여 API 요청을 보냅니다. `.getUser(userID:)`와 같은 API 열거형을 사용하여 요청의 타입과 파라미터를 정의합니다. 응답은 `result` 매개변수로 받으며, 성공 시 응답 데이터를 JSON으로 매핑하고 `User` 객체로 변환합니다. 매핑에 실패한 경우 또는 네트워크 요청 실패 시 에러를 처리할 수 있도록 오류 처리 로직을 구현합니다.

이제 위의 예제 코드를 활용하여 Swift에서 Moya와 ObjectMapper를 사용한 네트워크 통신 및 데이터 매핑을 수행할 수 있습니다.

## 참고 자료

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)