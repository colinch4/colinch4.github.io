---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 API 요청 후 JSON 데이터를 매핑하는 방법"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift Moya와 ObjectMapper를 사용하여 API 요청 후 받아온 JSON 데이터를 매핑하는 방법을 알아보겠습니다. Swift Moya는 네트워크 요청을 쉽게 처리할 수 있는 라이브러리이며, ObjectMapper는 데이터를 모델 객체로 매핑하는 라이브러리입니다. 두 라이브러리를 함께 사용하면 간편하게 API 요청과 데이터 매핑을 처리할 수 있습니다.

## 선행 작업

먼저 프로젝트에 Swift Moya와 ObjectMapper를 설치해야 합니다. CocoaPods를 사용한다면 Podfile에 다음과 같이 라이브러리를 추가합니다.

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다. 만약 Carthage를 사용한다면 Cartfile에 라이브러리를 추가하고 `carthage update` 명령어를 실행하여 라이브러리를 설치할 수 있습니다.

## Moya와 ObjectMapper를 이용한 API 요청 및 데이터 매핑

다음은 Moya와 ObjectMapper를 사용하여 API 요청 후 데이터를 매핑하는 예제 코드입니다. 간단한 GET 요청을 보내고 받아온 데이터를 User 객체로 매핑하는 방법을 보여줍니다.

```swift
import Moya
import ObjectMapper

enum API {
    case getUser(userID: Int)
}

extension API: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUser(let userID):
            return "/users/\(userID)"
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

class UserService {
    let provider = MoyaProvider<API>()
    
    func getUser(userID: Int, completion: @escaping (User?, Error?) -> Void) {
        provider.request(.getUser(userID: userID)) { result in
            switch result {
            case let .success(response):
                do {
                    let json = try response.mapJSON()
                    if let user = Mapper<User>().map(JSONObject: json) {
                        completion(user, nil)
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

위의 코드는 `API` 열거형을 만들어 각 API 엔드포인트를 정의하고, `TargetType` 프로토콜을 구현하여 요청에 필요한 정보를 제공합니다. 그리고 `UserService` 클래스에서 실제로 API를 호출하는 `getUser` 메소드를 구현합니다.

`getUser` 메소드에서는 MoyaProvider를 사용하여 API 요청을 보내고, 응답을 받아온 후 ObjectMapper를 사용하여 JSON 데이터를 User 객체로 매핑합니다. 매핑이 성공하면 매핑된 User 객체를 completion closure를 통해 반환하고, 매핑이 실패하면 에러를 반환합니다.

## 결론

Swift Moya와 ObjectMapper를 함께 사용하면 API 요청 후 JSON 데이터를 간편하게 매핑할 수 있습니다. 위의 예제 코드를 참고하여 프로젝트에 적용해보세요. 두 라이브러리는 각각 다양한 기능과 옵션을 제공하기 때문에 문서를 참고하여 필요한 기능을 활용할 수도 있습니다.

## 참고 자료

- [Moya](https://github.com/Moya/Moya)
- [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)