---
layout: post
title: "[swift] Swift Moya를 사용하여 API 요청 후 ObjectMapper를 사용하여 데이터 매핑하기"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

Swift Moya는 네트워크 작업을 간편하게 처리할 수 있는 라이브러리입니다. ObjectMapper는 JSON 데이터를 객체로 매핑할 수 있는 라이브러리입니다. 이 두 가지를 함께 사용하여 API 요청을 처리하고 데이터를 매핑하는 방법에 대해 알아보겠습니다.

## Moya 설치 및 설정

먼저, Moya를 프로젝트에 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 아래와 같이 Moya를 추가합니다.

```
pod 'Moya'
```

설치가 완료되면, Xcode 프로젝트를 열고 `import Moya` 문을 추가합니다.

## Moya를 사용하여 API 요청하기

Moya를 사용하여 API를 호출하려면, 요청할 엔드포인트와 해당 엔드포인트에 대한 서비스를 정의해야 합니다. 예를 들어, 사용자 정보를 가져오기 위해 다음과 같은 엔드포인트를 정의합니다.

```swift
enum UserService {
    case getUser(id: Int)
}

extension UserService: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUser(let id):
            return "/users/\(id)"
        }
    }
    
    var method: Moya.Method {
        return .get
    }
    
    var task: Task {
        return .requestPlain
    }
    
    var headers: [String: String]? {
        return nil
    }
}
```

위의 코드에서 `UserService`는 API의 서비스를 정의하고, `TargetType` 프로토콜을 구현합니다. `baseURL`은 API 서버의 기본 URL을 설정하고, `path`는 요청할 엔드포인트의 경로를 지정합니다. `method`는 HTTP 메서드를 설정하며, `task`는 요청의 파라미터를 설정합니다. `headers`는 요청에 추가할 HTTP 헤더를 설정합니다.

이제 Moya를 사용하여 API를 호출하는 코드를 작성해보겠습니다.

```swift
let provider = MoyaProvider<UserService>()

provider.request(.getUser(id: 123)) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.map(User.self) // ObjectMapper를 사용하여 JSON 데이터를 User 객체로 매핑
            print(user)
        } catch {
            print("Mapping failed")
        }
    case .failure(let error):
        print(error)
    }
}
```

위의 코드에서는 `MoyaProvider`를 사용하여 `UserService`의 `getUser` 엔드포인트에 대한 요청을 보냅니다. 응답 결과는 `Response` 객체로 받게 되며, `map` 메서드를 이용하여 ObjectMapper를 사용하여 JSON 데이터를 원하는 객체로 매핑할 수 있습니다.

## ObjectMapper를 사용하여 데이터 매핑하기

ObjectMapper를 사용하면, JSON 데이터를 객체로 매핑할 수 있습니다. 예를 들어, 사용자 정보를 담은 JSON 데이터를 다음과 같이 매핑할 수 있습니다.

```swift
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

위의 코드에서는 ObjectMapper를 사용하여 JSON 데이터를 User 객체로 매핑하기 위해 `User` 구조체를 정의합니다. `Mappable` 프로토콜을 채택하고, `map` 및 `mapping` 메서드를 구현합니다. 이후, JSON의 key와 객체의 프로퍼티를 매핑시킬 때에는 <- 연산자를 사용합니다.

여기서는 User 객체에 `id`, `name`, `email` 프로퍼티가 있으며, JSON 데이터의 key와 매핑됩니다.

## 결론

이렇게 Swift Moya를 사용하여 API를 호출하고, ObjectMapper를 사용하여 JSON 데이터를 객체로 매핑하는 과정을 알아봤습니다. 이렇게 함께 사용하면 네트워크 작업과 데이터 매핑을 보다 효율적으로 처리할 수 있습니다.

더 자세한 내용은 [Moya 공식 문서](https://github.com/Moya/Moya), [ObjectMapper 공식 문서](https://github.com/tristanhimmelman/ObjectMapper)를 참고하시기 바랍니다.