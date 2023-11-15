---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 Moya와 ObjectMapper을 함께 사용하여 REST API 통신을 처리하는 예제 코드를 작성해보겠습니다. Moya는 네트워크 라이브러리이며, ObjectMapper는 JSON 데이터를 모델 객체로 매핑해주는 라이브러리입니다.

## 1. Moya 및 ObjectMapper 설치

먼저, Moya와 ObjectMapper를 프로젝트에 추가해야 합니다. 이를 위해서는 Cocoapods를 사용할 수 있습니다. `Podfile`에 다음과 같이 추가해주세요.

```
pod 'Moya'
pod 'ObjectMapper'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치해줍니다.

## 2. 모델 클래스 생성

먼저, 통신 결과를 매핑할 모델 클래스를 생성해야 합니다. 예를 들어, `User`라는 이름의 모델 클래스를 만들어보겠습니다. 

```swift
import Foundation
import ObjectMapper

struct User: Mappable {
    var name: String?
    var email: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
}
```

위의 코드는 `User` 모델 클래스를 정의하고, `Mappable` 프로토콜을 채택하여 ObjectMapper를 사용할 수 있도록 합니다. `name`과 `email`은 JSON 데이터와 매핑될 프로퍼티입니다.

## 3. API 서비스 생성

이제 Moya를 사용하여 API 서비스를 생성합니다. 예를 들어, 유저 정보를 가져오는 GET API를 호출하는 `UserService`를 생성해보겠습니다.

```swift
import Moya

enum UserService {
    case getUser(userId: Int)
}

extension UserService: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }

    var path: String {
        switch self {
        case .getUser(let userId):
            return "/user/\(userId)"
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
        return ["Content-type": "application/json"]
    }
}
```

위의 코드는 `UserService` 열거형으로 GET API 호출을 위한 서비스를 정의하고, `TargetType` 프로토콜을 채택하여 Moya와 연동할 수 있도록 합니다. `baseURL`, `path`, `method`, `task`, `headers` 등을 설정하여 API 호출에 필요한 정보를 지정합니다.

## 4. API 통신 및 결과 처리

이제 API 서비스를 사용하여 실제 통신을 수행하고 결과를 처리해보겠습니다.

```swift
import Moya
import ObjectMapper

let provider = MoyaProvider<UserService>()

provider.request(.getUser(userId: 1)) { (result) in
    switch result {
    case .success(let response):
        do {
            let json = try response.mapJSON()
            if let user = Mapper<User>().map(JSONObject: json) {
                // API 통신 및 결과 처리
                print("User name: \(user.name ?? "")")
                print("User email: \(user.email ?? "")")
            }
        } catch {
            print("Error mapping JSON: \(error)")
        }
    case .failure(let error):
        print("API request failed: \(error.errorDescription ?? "")")
    }
}
```

위의 코드는 MoyaProvider를 사용하여 API 호출을 수행하고, ObjectMapper를 사용하여 JSON 데이터를 `User` 모델 객체로 매핑합니다. 성공적으로 매핑된 경우에는 `User` 객체의 정보를 출력하게 됩니다. 통신에 실패하거나 JSON 매핑에 실패한 경우에는 에러 메시지를 출력합니다.

## 마무리

이렇게 Swift에서 Moya와 ObjectMapper을 함께 사용하여 REST API 통신을 처리하는 예제 코드를 살펴보았습니다. Moya와 ObjectMapper은 각각 네트워크 통신과 데이터 매핑에 용이한 기능을 제공해주므로, 해당 기능을 활용하여 효율적으로 REST API 통신을 구현할 수 있습니다.

참고 자료:
- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)