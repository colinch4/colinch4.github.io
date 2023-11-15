---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 이용한 네트워크 요청 및 데이터 매핑하는 예제 코드"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift 언어의 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 요청을 보내고, 받은 데이터를 매핑하는 방법을 알아보겠습니다.

## Moya 및 ObjectMapper 설치

먼저, Moya와 ObjectMapper 라이브러리를 설치해야 합니다. 프로젝트의 Podfile에 다음과 같이 추가해주세요.

```ruby
target 'YourApp' do
  pod 'Moya'
  pod 'ObjectMapper'
end
```
그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 네트워크 요청 모델 생성

네트워크 요청을 위해 데이터 모델을 생성해야 합니다. 예를 들어, GitHub API로부터 사용자의 정보를 가져오는 요청을 보내기 위한 데이터 모델을 만들어보겠습니다.

```swift
import ObjectMapper

struct User: Mappable {
    var username: String?
    var bio: String?
    
    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        username <- map["login"]
        bio <- map["bio"]
    }
}
```
위 코드에서는 ObjectMapper의 `Mappable` 프로토콜을 구현한 `User` 구조체를 정의하였습니다. `mapping` 메서드에서는 JSON 데이터와 데이터 모델의 프로퍼티를 매핑해줍니다.

## 네트워크 요청 및 데이터 매핑

Moya를 사용하여 네트워크 요청을 보내고, ObjectMapper를 사용하여 응답 데이터를 매핑할 수 있습니다. 아래 예제 코드를 참고해주세요.

```swift
import Moya
import ObjectMapper

let provider = MoyaProvider<GitHub>()

enum GitHub {
    case getUser(username: String)
}

extension GitHub: TargetType {
    var baseURL: URL { return URL(string: "https://api.github.com")! }
    
    var path: String {
        switch self {
        case .getUser(let username):
            return "/users/\(username)"
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

provider.request(.getUser(username: "johnappleseed")) { result in
    switch result {
    case let .success(response):
        do {
            let user = try response.mapJSON(to: User.self)
            // 응답 데이터를 User 모델로 매핑
            print(user.username)
            print(user.bio)
        } catch {
            print("Mapping error:", error)
        }
    case let .failure(error):
        print("Network error:", error)
    }
}
```
위 코드에서는 Moya를 사용하여 `GitHub` 타겟을 정의하고, 네트워크 요청을 생성합니다. `GitHub` 타겟에서는 `getUser` 케이스를 정의하고, 해당 사용자의 정보를 가져오는 URL을 반환합니다.

응답을 받으면 `mapJSON(to:)` 메서드를 사용하여 ObjectMapper를 이용해 JSON 데이터를 `User` 모델로 매핑합니다. 매핑된 데이터를 이용하여 원하는 작업을 수행할 수 있습니다.

이와 같이, Swift의 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 요청과 데이터 매핑을 간편하게 처리할 수 있습니다.

## 참고 문서

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)

**주의:** 위 예제는 Moya와 ObjectMapper를 사용한 간단한 예제이며, 실제 프로젝트에서 사용될 경우 각종 예외 처리와 안정성을 고려해야 합니다.