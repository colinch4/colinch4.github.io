---
layout: post
title: "[swift] Swift Moya에서 Request/Response 모델링하기"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

Swift Moya는 네트워크 통신을 위한 강력한 라이브러리입니다. 이 라이브러리를 사용하면 간단하게 네트워크 요청을 보내고 응답을 받을 수 있습니다. 이번에는 Moya를 사용하여 Request와 Response를 모델링하는 방법에 대해 알아보겠습니다.

## 1. Request 모델링

Request 모델은 서버로 보낼 요청의 정보를 가지고 있습니다. 이 모델은 Moya의 `TargetType` 프로토콜을 준수하도록 구현됩니다.

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
            return "/user/\(id)"
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

위의 코드에서 `MyAPI`는 사용자 정보를 가져오는 요청을 정의한 것입니다. `TargetType` 프로토콜을 준수하기 위해 필요한 속성과 메서드를 구현해야 합니다. `baseURL`은 API의 기본 URL이며, `path`는 해당 요청의 경로를 정의합니다. `method`는 HTTP 메서드를 나타내며, `sampleData`는 테스트용 샘플 데이터입니다. `task`는 요청의 파라미터를 설정하고, `headers`는 요청에 필요한 헤더를 정의합니다.

## 2. Response 모델링

Response 모델은 서버로부터 받은 응답의 정보를 가지고 있습니다. Moya는 기본적으로 JSON 응답을 처리하기 때문에, 응답 데이터를 디코딩하기 위해 Codable 프로토콜을 준수하는 모델을 만들어야 합니다.

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}
```

위의 코드에서 `User`는 서버로부터 받은 사용자 정보를 나타내는 모델입니다. `Codable` 프로토콜을 준수하도록 구현되어 있으며, `id`, `name`, `email` 속성을 가지고 있습니다.

## 3. Request 보내고 Response 처리하기

이제 실제로 Moya를 사용하여 요청을 보내고 응답을 처리하는 방법을 알아보겠습니다.

```swift
let provider = MoyaProvider<MyAPI>()

provider.request(.getUser(id: 123)) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.map(User.self)
            print(user)
        } catch {
            print("Error decoding response: \(error)")
        }
    case .failure(let error):
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 코드에서 `MoyaProvider` 인스턴스를 생성하고, `request` 메서드를 호출하여 요청을 보냅니다. 요청의 성공 또는 실패에 따라 적절한 처리를 할 수 있습니다. 응답이 성공한 경우, `map` 메서드를 사용하여 응답 데이터를 `User` 모델로 디코딩합니다. 디코딩에 실패한 경우에는 에러를 처리합니다.

위의 예제에서는 GET 요청을 보내고 응답을 처리하는 방법을 보여주었지만, Moya는 POST, PUT, DELETE 등 다양한 요청을 처리할 수 있습니다. Request 모델과 Response 모델을 적절하게 구성하여 다양한 API 요청을 손쉽게 처리할 수 있습니다.

## 마무리

Swift Moya를 사용하여 Request와 Response를 모델링하는 방법을 알아보았습니다. 이를 통해 네트워크 요청을 간단하게 구성하고, 서버로부터 받은 응답을 쉽게 처리할 수 있습니다. Moya의 강력한 기능을 활용하여 다양한 API 통신을 더욱 효율적으로 처리해보세요.