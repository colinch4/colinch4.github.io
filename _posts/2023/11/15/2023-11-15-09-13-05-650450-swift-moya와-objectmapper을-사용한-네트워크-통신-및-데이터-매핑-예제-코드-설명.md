---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 Moya와 ObjectMapper을 사용하여 네트워크 통신을 수행하고 데이터를 매핑하는 예제 코드에 대해 설명하겠습니다. Moya는 Alamofire 기반의 네트워크 추상화 프레임워크로, 간단한 설정과 높은 수준의 추상화로 효율적인 API 호출을 지원합니다. ObjectMapper는 JSON 데이터를 Swift 객체로 변환하기 위한 매핑 라이브러리로, 간단한 설정으로 JSON 데이터를 객체로 변환하거나 객체를 JSON 데이터로 변환할 수 있습니다.

## 예제 코드 설명

먼저, 앱에서 사용할 API 모델과 매핑할 Swift 객체를 생성합니다. 예를 들어, 간단한 사용자 정보를 나타내는 User 모델을 생성해보겠습니다.

```swift
struct User: Mappable {
    var id: Int
    var name: String
    var email: String
    
    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

User 구조체는 Mappable 프로토콜을 준수하도록 선언되어 있으며, ObjectMapper의 매핑 메소드를 이용하여 JSON 데이터를 객체로 변환할 수 있도록 구현되어 있습니다.

다음으로, API 서비스를 정의해보겠습니다. Moya를 사용하여 네트워크 요청을 처리하고, ObjectMapper를 사용하여 응답 데이터를 User 객체로 매핑하는 사전에 정의된 API 요청에 대한 구현을 작성해야 합니다. 아래는 사용자 목록을 가져오는 API를 호출하는 예제입니다.

```swift
import Moya
import ObjectMapper

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
        switch self {
        case .getUsers:
            return .get
        }
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

class APIManager {
    static let provider = MoyaProvider<UserService>()
    
    static func getUsers(completion: @escaping ([User]?) -> Void) {
        provider.request(.getUsers) { result in
            switch result {
            case .success(let response):
                do {
                    let users = try response.mapArray(of: User.self)
                    completion(users)
                } catch {
                    completion(nil)
                }
            case .failure(_):
                completion(nil)
            }
        }
    }
}
```

위의 코드에서는 UserService라는 열거형을 만들어 Moya의 TargetType 프로토콜을 구현합니다. 이를 통해 API의 base URL, 경로, HTTP 메소드 등을 설정할 수 있습니다.

APIManager의 getUsers(completion:) 메소드에서는 Moya Provider를 사용하여 getUsers API를 호출하고, 응답을 받아 User 객체 배열로 매핑하여 completion 핸들러를 호출합니다.

마지막으로, getUsers API를 호출하는 예제 코드를 작성해보겠습니다.

```swift
APIManager.getUsers { users in
    if let users = users {
        for user in users {
            print("User: \(user.name), Email: \(user.email)")
        }
    } else {
        print("Failed to get users")
    }
}
```

위의 코드는 getUsers API를 호출하고, 응답을 받으면 매핑된 User 객체 배열을 순회하며 이름과 이메일을 출력합니다. 응답이 실패하면 "Failed to get users"를 출력합니다.

## 마무리

이번 포스트에서는 Swift에서 Moya와 ObjectMapper을 사용하여 네트워크 통신을 수행하고 데이터를 매핑하는 예제 코드에 대해 알아보았습니다. Moya와 ObjectMapper는 각자의 기능을 효율적으로 제공하므로, 이 두 라이브러리를 함께 사용하면 Swift 앱의 네트워크 통신과 데이터 매핑을 더욱 효율적으로 처리할 수 있습니다.

참고: 
- Moya: [https://github.com/Moya/Moya](https://github.com/Moya/Moya)
- ObjectMapper: [https://github.com/tristanhimmelman/ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)