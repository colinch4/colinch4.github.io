---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 함께 사용하는 방법"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

서버와 통신하고 데이터를 받아오는 작업은 iOS 애플리케이션 개발에서 빈번하게 이루어집니다. 이를 위해 Moya와 ObjectMapper은 많은 개발자들에게 효율적인 도구로 알려져 있습니다. 이번 글에서는 Swift에서 Moya와 ObjectMapper을 함께 사용하는 방법에 대해 알아보겠습니다.

## Moya란?
Moya는 Swift에서 네트워킹을 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. Alamofire를 기반으로 만들어져 있으며, 네트워킹 작업을 추상화하여 간단하게 사용할 수 있도록 제공합니다.

## ObjectMapper란?
ObjectMapper는 Swift에서 JSON 데이터를 모델 객체로 매핑하는 작업을 쉽게 처리해주는 라이브러리입니다. JSON 데이터를 객체로 변환하거나, 객체를 JSON 데이터로 변환하는 작업을 간편하게 처리할 수 있습니다.

## Moya와 ObjectMapper 함께 사용하기
Moya와 ObjectMapper을 함께 사용하면, 서버에서 받아온 JSON 데이터를 Moya의 response로 받고, ObjectMapper를 사용하여 해당 데이터를 모델 객체로 변환할 수 있습니다.

먼저, Moya를 설치하고 필요한 import 구문을 추가하세요.
```swift
import Moya
```

다음으로, ObjectMapper를 설치하고 필요한 import 구문을 추가하세요.
```swift
import ObjectMapper
```

이제 Moya로 네트워킹을 구현하고 ObjectMapper로 JSON 데이터를 모델 객체로 매핑하는 코드를 작성해보겠습니다.

```swift
enum MyAPI {
    case getUsers
}

extension MyAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://your-api-url.com")!
    }
    
    var path: String {
        switch self {
        case .getUsers:
             return "/users"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUsers:
             return .get
        }
    }
    
    var sampleData: Data {
        return Data()
    }
    
    var task: Task {
        switch self {
        case .getUsers:
            return .requestPlain
        }
    }
    
    var headers: [String: String]? {
        return [
            "Content-Type": "application/json"
        ]
    }
}

class MyService {
    let provider = MoyaProvider<MyAPI>()
    
    func getUsers(completion: @escaping ([UserModel]?, Error?) -> Void) {
        provider.request(.getUsers) { result in
            switch result {
            case let .success(response):
                do {
                    let json = try response.mapJSON()
                    if let userArray = json as? [[String: Any]] {
                        let userList = Mapper<UserModel>().mapArray(JSONArray: userArray)
                        completion(userList, nil)
                    }
                } catch {
                    completion(nil, error)
                }
            case let .failure(error):
                completion(nil, error)
            }
        }
    }
}
```

위의 코드에서 `MyAPI` enum은 API 엔드포인트를 정의합니다. `Task`에서는 어떤 작업을 수행할지, `headers`에서는 어떤 헤더를 사용할지를 정의합니다.

`MyService` 클래스에서는 `MoyaProvider`를 사용하여 네트워킹 작업을 수행합니다. `getUsers` 메서드에서 `provider.request`를 호출하여 데이터를 받아옵니다. 그리고 받아온 데이터를 ObjectMapper를 사용하여 모델 객체로 변환한 후, completion 핸들러를 호출하여 데이터를 전달합니다.

이제 Moya와 ObjectMapper을 함께 사용하는 방법을 알게 되었습니다. 이를 활용하여 Swift 애플리케이션에서 효율적인 네트워킹 작업을 수행할 수 있습니다.

> **참고 자료**
> - [Moya GitHub 저장소](https://github.com/Moya/Moya)
> - [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)