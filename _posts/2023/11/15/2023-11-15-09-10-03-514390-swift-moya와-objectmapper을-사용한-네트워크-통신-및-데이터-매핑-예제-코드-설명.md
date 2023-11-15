---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift Moya와 ObjectMapper을 사용하여 서버와의 네트워크 통신을 수행하고 받은 데이터를 매핑하는 방법을 설명하겠습니다. Moya는 Alamofire를 기반으로 한 네트워크 라이브러리이며, ObjectMapper는 JSON 데이터를 Swift 객체로 변환하기 위한 라이브러리입니다. 이 두 가지 라이브러리를 함께 사용하여 효율적인 네트워크 통신과 데이터 매핑을 할 수 있습니다.

## Moya 및 ObjectMapper 설치

먼저 Moya와 ObjectMapper를 설치해야 합니다. CocoaPods를 사용한다면 Podfile에 다음과 같이 추가합니다:

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

설치가 완료되면 프로젝트를 다시 빌드하고 import 문을 통해 Moya 및 ObjectMapper를 가져올 준비를 합니다.

## 네트워크 통신 설정

Moya는 네트워크 통신을 위한 몇 가지 설정을 제공합니다. 먼저, API에 대한 열거형을 만들어 각각의 열거형 케이스에는 해당 API의 endpoints와 요청 방법을 지정합니다. 예를 들어, 다음과 같이 사용자 정보를 얻기 위한 API를 정의할 수 있습니다:

```swift
import Moya

enum UserAPI {
    case getUserInfo(userId: Int)
}

extension UserAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUserInfo(let userId):
            return "/users/\(userId)"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUserInfo:
            return .get
        }
    }
    
    var sampleData: Data {
        return Data()
    }
    
    var task: Task {
        switch self {
        case .getUserInfo:
            return .requestPlain
        }
    }
    
    var headers: [String: String]? {
        return nil
    }
}
```

위 예제에서는 `UserAPI`라는 열거형을 정의하고, `TargetType` 프로토콜을 구현하여 각 API의 엔드포인트, 요청 방법, 샘플 데이터 등을 지정합니다.

## 네트워크 요청

이제 Moya를 사용하여 네트워크 요청을 보내는 방법을 살펴보겠습니다. 예를 들어, 사용자 정보를 얻는 API를 호출하는 코드는 다음과 같습니다:

```swift
import Moya

let provider = MoyaProvider<UserAPI>()

provider.request(.getUserInfo(userId: 1)) { (result) in
    switch result {
    case .success(let response):
        do {
            let user = try response.map(User.self) // ObjectMapper를 사용하여 JSON 데이터 매핑
            print(user)
        } catch {
            print("Error mapping user info: \(error)")
        }
        
    case .failure(let error):
        print("Network error: \(error)")
    }
}
```

위 예제에서 `MoyaProvider`를 생성하고 `request` 메서드를 사용하여 네트워크 요청을 보냅니다. 성공적인 응답을 받은 경우, ObjectMapper를 사용하여 JSON 데이터를 `User` 객체로 매핑하고 출력합니다. 에러인 경우, 해당 에러를 적절히 처리합니다.

## 데이터 매핑 클래스

마지막으로 ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 매핑하는 방법을 알아보겠습니다. 예를 들어, 아래와 같이 `User` 클래스를 생성하여 사용자 정보를 매핑할 수 있습니다:

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

위 예제에서 `User` 구조체는 `Mappable` 프로토콜을 구현하고, `id`, `name`, `email`과 같은 속성들을 매핑합니다. ObjectMapper는 JSON 키를 사용하여 각 속성들의 값을 매핑합니다.

## 결론

이와 같이 Swift Moya와 ObjectMapper를 함께 사용하여 네트워크 통신을 수행하고 데이터를 매핑하는 방법을 살펴보았습니다. Moya를 사용하면 네트워크 요청을 쉽게 관리할 수 있고, ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 편리하게 매핑할 수 있습니다.