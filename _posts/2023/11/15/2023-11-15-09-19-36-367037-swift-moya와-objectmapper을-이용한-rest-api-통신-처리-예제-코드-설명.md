---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift 언어를 사용하여 Moya와 ObjectMapper를 이용하여 REST API 통신을 처리하는 방법에 대해 알아보겠습니다.

## 1. Moya란?

Moya는 Swift에서 네트워크 작업을 간단하게 처리할 수 있는 라이브러리입니다. Alamofire를 기반으로하여 네트워크 호출을 추상화하고, 간결하고 타입 안전한 형태로 API 클라이언트를 만들 수 있도록 도와줍니다.

Moya를 사용하면 네트워크 요청을 정의하고, 응답을 처리할 수 있는 모델을 구성할 수 있습니다. 하나의 서비스에 대한 API 호출을 쉽게 구현할 수 있으며, MoyaProvider를 통해 네트워크 요청을 보내고 응답을 받아올 수 있습니다.

## 2. ObjectMapper란?

ObjectMapper는 Swift에서 JSON 데이터와 모델 객체 간의 매핑을 도와주는 라이브러리입니다. JSON 데이터를 모델 객체로 변환하거나, 모델 객체를 JSON 데이터로 변환하는 작업을 쉽고 간편하게 처리할 수 있습니다.

ObjectMapper를 사용하면 JSON 데이터를 명시적으로 매핑할 필요 없이, 모델 객체의 프로퍼티와 JSON 키를 자동으로 매핑할 수 있습니다.

## 3. 예제 코드 설명

아래는 Moya와 ObjectMapper를 사용하여 REST API 통신을 처리하는 예제 코드입니다.

```swift
import Moya
import ObjectMapper

// API 요청을 위한 열거형 정의
enum API {
    case getUser(id: Int)
}

// Moya를 사용하여 API를 서비스로 정의
let provider = MoyaProvider<API>()

// 사용자 모델 객체
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

// API 요청 처리 및 모델 객체로 변환
provider.request(.getUser(id: 1)) { result in
    switch result {
    case let .success(response):
        do {
            let user = try response.mapObject(User.self)
            // 모델 객체를 사용하여 데이터 처리
            print("User: \(user.name), Email: \(user.email)")
        } catch {
            // 매핑 실패 시 에러 처리
            print("Mapping Error: \(error.localizedDescription)")
        }
    case let .failure(error):
        // 네트워크 에러 처리
        print("Network Error: \(error.localizedDescription)")
    }
}
```

위 코드는 getUser라는 API 요청을 보내고, 응답으로 받아온 데이터를 User 모델 객체로 매핑하는 예제입니다.

먼저 API를 정의하기 위해 `API` 열거형을 정의합니다. `getUser` 케이스에는 사용자 ID를 파라미터로 전달하여 특정 사용자의 정보를 요청할 수 있습니다.

다음으로, MoyaProvider를 생성하고 API 요청을 보냅니다. MoyaProvider의 `request` 메서드를 호출하여 API 요청을 보내고 응답을 받아옵니다.

성공한 경우에는 ObjectMapper의 `mapObject` 메서드를 사용하여 JSON 데이터를 User 모델 객체로 매핑합니다. 모델 객체를 사용하여 데이터를 처리할 수 있습니다.

실패한 경우에는 네트워크 에러나 매핑 에러를 처리합니다.

이렇게 Moya와 ObjectMapper를 함께 사용하여 REST API 통신을 처리할 수 있습니다.

## 4. 참고 자료

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)