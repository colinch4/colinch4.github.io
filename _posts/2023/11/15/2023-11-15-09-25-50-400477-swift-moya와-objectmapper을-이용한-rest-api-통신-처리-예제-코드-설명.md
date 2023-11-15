---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제는 Swift 언어를 사용하여 REST API와 통신하는 방법을 알아보겠습니다. 우리는 Moya와 ObjectMapper 라이브러리를 사용하여 API 호출을 처리하고 응답 데이터를 매핑할 것입니다.

## Moya 소개

[Moya](https://github.com/Moya/Moya)는 Swift에서 네트워크 통신을 쉽게 처리하기 위한 현대적인 네트워크 추상화 라이브러리입니다. Moya는 Alamofire를 기반으로 구현되었으며, 네트워크 계층의 추상화, 재시도 기능, 플러그인 기능 등을 제공합니다.

## ObjectMapper 소개

[ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)는 Swift에서 JSON 데이터를 객체로 매핑하기 위한 라이브러리입니다. ObjectMapper는 JSON 데이터를 Swift의 객체로 변환하고, 객체를 JSON 데이터로 변환하는 기능을 제공합니다.

## 예제 코드 설명

아래는 Moya와 ObjectMapper를 이용하여 REST API와 통신하고 응답 데이터를 매핑하는 예제 코드입니다.

```swift
import Moya
import ObjectMapper

// API 요청과 응답을 정의하는 모델 클래스
struct User: Mappable {
    var id: Int?
    var username: String?
    var email: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- map["id"]
        username <- map["username"]
        email <- map["email"]
    }
}

// API 서버와 통신하기 위한 Provider 초기화
let provider = MoyaProvider<API>()

// API 열거형 정의
enum API {
    case getUser(id: Int)
}

extension API: TargetType {
    var baseURL: URL { return URL(string: "https://api.example.com")! }
    
    var path: String {
        switch self {
        case .getUser(let id):
            return "/user/\(id)"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUser:
            return .get
        }
    }
    
    var task: Task {
        switch self {
        case .getUser:
            return .requestPlain
        }
    }
    
    var headers: [String: String]? {
        return ["Content-Type": "application/json"]
    }
    
    var validationType: ValidationType {
        return .successCodes
    }
}

// API 호출 및 응답 데이터 매핑
provider.request(.getUser(id: 1)) { result in
    switch result {
    case let .success(response):
        do {
            let user = try response.mapJSON() as! [String: Any]
            let mappedUser = Mapper<User>().map(JSONObject: user)
            print(mappedUser)
        } catch {
            print("Error mapping user")
        }
    case let .failure(error):
        print("API request failed: \(error)")
    }
}
```

위의 코드에서, `API` 열거형은 요청할 API 엔드포인트를 정의하고, `TargetType` 프로토콜을 채택하여 요청의 세부 정보를 제공합니다. 이후 API 프로바이더를 초기화한 다음, `provider.request` 메서드를 호출하여 API를 호출합니다. 응답은 `mapJSON` 메서드를 통해 JSON으로 변환한 다음, ObjectMapper 라이브러리를 사용하여 응답 데이터를 `User` 객체로 매핑합니다.

이 예제 코드를 참고하여 Swift에서 Moya와 ObjectMapper을 사용하여 REST API를 통신하고 응답 데이터를 처리하는 방법을 익힐 수 있습니다.