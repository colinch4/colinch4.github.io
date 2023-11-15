---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 예제에서는 Swift의 Moya와 ObjectMapper 라이브러리를 사용하여 REST API 호출 및 응답 데이터 처리하는 방법에 대해 설명하겠습니다.

## Moya란?

Moya는 Alamofire를 기반으로하는 간단하고 타입 세이프한 네트워크 라이브러리입니다. Moya는 REST API를 호출하기 위한 간단한 인터페이스를 제공하며, 네트워크 요청을 정의하고 모델 데이터를 매핑하는 데 도움을 줍니다.

## ObjectMapper란?

ObjectMapper는 객체와 JSON 데이터 간의 매핑을 위한 Swift 라이브러리입니다. ObjectMapper를 사용하면 JSON 데이터를 Swift 객체로 변환하거나 Swift 객체를 JSON 데이터로 변환할 수 있습니다.

## 예제 코드 설명

### 1. 모델 클래스 생성

먼저, API 응답 데이터를 매핑하기 위한 모델 클래스를 만듭니다. 예를 들어, 사용자 정보를 나타내는 `User` 모델 클래스를 생성합니다.

```swift
class User: Mappable {
    var id: Int?
    var name: String?
    var email: String?

    required init?(map: Map) {}

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

### 2. API 요청 정의

다음으로, Moya를 사용하여 REST API 호출을 정의합니다. 예를 들어, 사용자 목록을 가져오는 `UserService`라는 API 서비스를 생성합니다.

```swift
enum UserService {
    case getUsers
}

extension UserService: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUsers:
            return "/users"
        }
    }
    
    var method: Moya.Method {
        return .get
    }
    
    var sampleData: Data {
        return Data()
    }
    
    var task: Task {
        return .requestPlain
    }
    
    var headers: [String: String]? {
        return ["Content-Type": "application/json"]
    }
}
```

### 3. API 호출 및 데이터 처리

Moya를 사용하여 API를 호출하고 ObjectMapper를 사용하여 응답 데이터를 매핑합니다. 아래 코드는 `UserService`를 사용하여 사용자 목록을 가져오는 예제입니다.

```swift
let provider = MoyaProvider<UserService>()

provider.request(.getUsers) { result in
    switch result {
    case let .success(response):
        do {
            let users = try response.mapArray(User.self)
            for user in users {
                print(user.name)
            }
        } catch {
            print("Mapping error: \(error)")
        }
    case let .failure(error):
        print("Network error: \(error)")
    }
}
```

위의 코드에서, `response.mapArray(User.self)`를 통해 API 응답 데이터를 `User` 객체의 배열로 매핑합니다. 이후, 매핑된 데이터를 사용하여 원하는 작업을 수행할 수 있습니다.

## 결론

이 예제에서는 Moya와 ObjectMapper를 사용하여 REST API 호출과 응답 데이터 매핑을 처리하는 방법에 대해 알아보았습니다. Moya와 ObjectMapper는 Swift 프로젝트에서 네트워크 통신 및 데이터 매핑을 효율적으로 처리하는 데 도움이 될 수 있습니다. 추가적인 정보와 자세한 사용법은 [Moya GitHub 저장소](https://github.com/Moya/Moya)와 [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)를 참조하시기 바랍니다.