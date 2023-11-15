---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

## 서론

웹 애플리케이션을 개발할 때, API 요청을 보내고 받은 데이터를 앱 내부의 객체로 매핑하는 작업은 매우 중요합니다. 이를 위해 Swift에서는 Moya와 ObjectMapper를 사용할 수 있습니다. Moya는 네트워크 요청을 추상화하고 간결하게 작성할 수 있는 라이브러리이며, ObjectMapper는 JSON 데이터를 Swift 객체로 변환하기 위한 라이브러리입니다. 이번 글에서는 Moya와 ObjectMapper를 함께 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드를 설명하겠습니다.

## Moya 및 ObjectMapper 설치

먼저, Moya와 ObjectMapper를 프로젝트에 추가해야 합니다. Cocoapods를 사용한다면 `Podfile`에 다음과 같이 추가해주세요:

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다:

```bash
$ pod install
```

이제 Moya 및 ObjectMapper를 사용할 준비가 되었습니다.

## Moya 기본 설정

Moya를 사용하기 위해서는 `MoyaProvider`를 초기화해야 합니다. 보통 `enum`을 만들고, 그 안에 API 엔드포인트에 대한 정보를 기술합니다. 예를 들어, 다음과 같이 `enum`을 만들 수 있습니다:

```swift
import Moya

enum MyAPI {
    case getUser(id: Int)
}

extension MyAPI: TargetType {
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

let provider = MoyaProvider<MyAPI>()
```

위에서는 `MyAPI` enum을 통해 `/users/1`와 같은 엔드포인트로 GET 요청을 보낼 수 있습니다. `MoyaProvider`를 초기화하고 `MyAPI`를 사용하여 요청을 보낼 준비가 되었습니다.

## ObjectMapper를 사용하여 데이터 매핑

데이터를 매핑하기 위해 ObjectMapper를 사용할 준비가 되었습니다. Moya의 응답 결과는 `MoyaResponse` 객체이며, 이를 ObjectMapper를 사용하여 Swift 객체로 매핑할 수 있습니다.

예를 들어, API에서 반환하는 JSON 데이터가 다음과 같다고 가정해보겠습니다:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

해당 데이터를 매핑하기 위해, 다음과 같이 Swift 객체를 만들 수 있습니다:

```swift
import ObjectMapper

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

let responseJSON = try? JSONSerialization.jsonObject(with: response.data, options: .allowFragments)
let user = Mapper<User>().map(JSON: responseJSON as! [String: Any])
```

위 코드에서는 `User` 클래스를 정의하고, `Mappable` 프로토콜을 준수합니다. `mapping(map:)` 메소드를 사용하여 JSON 데이터와 객체 간의 매핑을 설정합니다. `response.data`는 Moya의 응답 객체입니다. `JSONSerialization`을 사용하여 JSON 데이터를 Swift Dictionary로 변환하고, 이를 `Mapper`를 사용하여 `User` 객체로 매핑합니다.

## 예제 코드 설명

이제 예제 코드에 대해 간단히 설명하겠습니다.

1. `MoyaProvider<MyAPI>()`를 사용하여 MoyaProvider를 초기화합니다.
2. MoyaProvider의 `request(_:completion:)` 메소드를 사용하여 API 요청을 보냅니다. 이 메소드는 비동기로 동작하며, 결과는 클로저로 전달됩니다.
3. 응답을 받은 후, 응답 데이터를 JSON으로 변환합니다. 이는 `JSONSerialization`을 사용하여 수행할 수 있습니다.
4. JSON 데이터를 ObjectMapper를 사용하여 `User` 클래스에 매핑합니다.

이제 Moya와 ObjectMapper를 사용하여 API 요청 후 데이터 매핑하는 방법을 알게 되었습니다.

## 결론

이번 글에서는 Swift Moya와 ObjectMapper를 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드를 설명했습니다. Moya는 네트워킹 작업을 추상화하여 간결하고 간편하게 작성할 수 있도록 도와주며, ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 매핑할 수 있습니다. 이러한 두 가지 라이브러리를 함께 사용하면 웹 애플리케이션 개발이 더욱 편리해질 것입니다.

## 참고 자료

- [Moya GitHub repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub repository](https://github.com/tristanhimmelman/ObjectMapper)