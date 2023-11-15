---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 예제에서는 Swift의 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 통신을 수행하고, 받은 데이터를 매핑하는 방법을 설명하겠습니다.

## Moya와 Alamofire 설치

우선 Moya와 Alamofire를 프로젝트에 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 라이브러리를 추가합니다.

```ruby
pod 'Moya'
pod 'Alamofire'
```

설치한 후에는 `import Moya`와 `import Alamofire`를 해당 파일에 추가해야 합니다.

## Provider 생성

Moya의 Provider를 사용하여 네트워크 통신을 수행합니다. Provider를 생성하기 위해서는 API의 기본 URL과 Moya의 `EndpointClosure`를 지정해야 합니다.

```swift
let provider = MoyaProvider<YourAPIProvider>(endpointClosure: { (target: YourAPIProvider) -> Endpoint in
    let defaultEndpoint = MoyaProvider.defaultEndpointMapping(for: target)
    return defaultEndpoint.adding(newHTTPHeaderFields: ["Content-Type": "application/json"])
})
```

## API 정의

API 요청에 대한 정보를 담고 있는 프로토콜과 열거형을 정의합니다. 열거형은 Moya의 `TargetType` 프로토콜을 준수해야 합니다.

```swift
enum YourAPIProvider {
    case getUser(id: Int)
}

extension YourAPIProvider: TargetType {
    var baseURL: URL {
        return URL(string: "https://your-api.com")!
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
        return nil
    }
}
```

## ObjectMapper를 사용한 데이터 매핑

Moya로부터 받은 데이터를 ObjectMapper를 사용하여 매핑합니다. 이를 위해 응답 데이터에 대한 모델 객체를 정의하고, `mapObject()` 함수를 사용하여 데이터를 매핑합니다.

```swift
import ObjectMapper

struct User: Mappable {
    var id: Int
    var name: String

    init?(map: Map) {
        // 초기화 실패 시 매핑 실패로 처리
        if map.JSON["id"] == nil || map.JSON["name"] == nil {
            return nil
        }
    }

    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
    }
}
```

매핑은 다음과 같이 수행합니다.

```swift
provider.request(.getUser(id: 1)) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapObject(User.self)
            print(user.id) // 유저의 ID 출력
            print(user.name) // 유저의 이름 출력
        } catch {
            print("Failed to map User object")
        }
    case .failure(let error):
        print(error)
    }
}
```

위의 예제 코드에서는 `getUser()` API를 호출하여 유저의 정보를 가져옵니다. 받은 데이터는 `User` 객체에 매핑됩니다.

이와 같이 Moya와 ObjectMapper을 함께 사용하여 네트워크 통신과 데이터 매핑을 손쉽게 수행할 수 있습니다.

## 참고 자료

- [Moya GitHub](https://github.com/Moya/Moya)
- [ObjectMapper GitHub](https://github.com/tristanhimmelman/ObjectMapper)