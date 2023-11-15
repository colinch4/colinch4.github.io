---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 API 요청 후 데이터 매핑하는 방법과 코드 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

Moya와 ObjectMapper는 Swift에서 API 요청을 보내고 받은 데이터를 쉽게 매핑하기 위해 많이 사용되는 라이브러리입니다. 이 블로그 포스트에서는 Moya와 ObjectMapper를 사용하여 API 요청 후 데이터를 매핑하는 방법과 코드 예제를 다루겠습니다.

## Moya와 ObjectMapper란?

- Moya: Alamofire를 기반으로 한 네트워킹 추상화 라이브러리로, 강력한 기능을 간편하게 사용할 수 있도록 도와줍니다.
- ObjectMapper: JSON과 Swift 모델 객체 사이의 매핑을 쉽게 해주는 라이브러리로, JSON을 Swift 모델로 변환하거나 그 반대로 변환할 수 있습니다.

## Moya와 ObjectMapper 설치

먼저, 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가하고 설치해주세요.

```swift
pod 'Moya'
pod 'ObjectMapper'
```

설치가 완료되면, 프로젝트에서 Moya와 ObjectMapper를 import 해줍니다.

```swift
import Moya
import ObjectMapper
```

## API 요청 및 데이터 매핑

Moya와 ObjectMapper를 이용하여 API 요청 후 데이터를 매핑하는 과정은 다음과 같습니다.

1. API 요청을 정의하는 Target을 생성합니다.
2. MoyaProvider를 이용하여 API 요청을 보냅니다.
3. 응답 받은 데이터를 ObjectMapper를 이용하여 매핑합니다.

다음은 코드 예제입니다.

```swift
import Moya
import ObjectMapper

struct User: Mappable {
    var name: String?
    var email: String?
    
    init?(map: Map) { }
    
    mutating func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
}

enum API {
    case getUser(id: Int)
}

extension API: TargetType {
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
        return nil
    }
}

let provider = MoyaProvider<API>()

provider.request(.getUser(id: 1)) { result in
    switch result {
        case .success(let response):
            do {
                let user = try response.mapJSON()
                if let mappedUser = Mapper<User>().map(JSONObject: user) {
                    // 매핑된 데이터 사용
                    print(mappedUser.name)
                    print(mappedUser.email)
                }
            } catch {
                print("매핑 에러: \(error.localizedDescription)")
            }
        case .failure(let error):
            print("요청 에러: \(error.localizedDescription)")
    }
}
```

위 예제에서는 API 요청을 정의하는 Target을 `enum API`와 `extension API: TargetType`으로 작성했습니다. 

`User` 구조체는 ObjectMapper를 사용하여 JSON 데이터를 매핑하기 위한 모델입니다.

마지막으로, MoyaProvider의 `request` 메서드를 사용하여 API 요청을 보내고 응답 받은 데이터를 ObjectMapper를 이용하여 매핑하고 있습니다.

위 예제는 GET 방식의 API 요청을 다루고 있지만, Moya와 ObjectMapper는 다양한 HTTP 메서드와 JSON 데이터를 다룰 수 있으므로, 본인의 프로젝트의 요구사항에 맞게 코드를 수정하여 사용하면 됩니다.

## 결론

이 블로그 포스트에서는 Moya와 ObjectMapper를 사용하여 API 요청 후 데이터를 매핑하는 방법과 코드 예제에 대해 알아보았습니다. Moya와 ObjectMapper는 Swift 개발에 있어서 네트워킹과 데이터 매핑을 효율적으로 처리할 수 있는 강력한 라이브러리입니다. 프로젝트에 적용하여 보다 간편하고 효율적인 API 요청과 데이터 매핑 구현을 해보시기 바랍니다.

> **참고 자료:**
> - [Moya GitHub Repository](https://github.com/Moya/Moya)
> - [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)
> - [Moya Documentation](https://github.com/Moya/Moya/blob/master/Docs/Endpoints.md)
> - [ObjectMapper Documentation](https://github.com/tristanhimmelman/ObjectMapper)