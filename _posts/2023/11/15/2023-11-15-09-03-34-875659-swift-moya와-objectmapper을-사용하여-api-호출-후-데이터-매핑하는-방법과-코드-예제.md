---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 API 호출 후 데이터 매핑하는 방법과 코드 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

API 호출 후 데이터를 매핑하는 작업은 iOS 애플리케이션 개발에서 상당히 흔한 작업입니다. 이를 위해 Swift의 Moya와 ObjectMapper 라이브러리를 함께 사용하면 간편하게 데이터를 매핑할 수 있습니다. 이번 글에서는 Moya와 ObjectMapper을 사용하여 API 호출 후 데이터를 매핑하는 방법과 코드 예제에 대해 알아보겠습니다.

## Moya 소개

Moya는 Swift 네트워킹 라이브러리로, Alamofire을 기반으로 만들어진 강력한 도구입니다. Moya를 사용하면 간단한 인터페이스를 통해 네트워크 요청을 처리할 수 있습니다.

Moya를 사용하기 위해 다음과 같이 Podfile에 Moya와 Alamofire를 추가합니다.

```ruby
platform :ios, '12.0'

target 'YourApp' do
  use_frameworks!

  pod 'Moya'
  pod 'Alamofire'
end
```

## ObjectMapper 소개

ObjectMapper는 Swift에서 JSON 데이터를 객체로 매핑하기 위한 라이브러리입니다. ObjectMapper를 사용하면 JSON 데이터를 쉽게 처리할 수 있습니다.

ObjectMapper를 사용하기 위해 다음과 같이 Podfile에 ObjectMapper를 추가합니다.

```ruby
platform :ios, '12.0'

target 'YourApp' do
  use_frameworks!

  pod 'ObjectMapper'
end
```

## Moya와 ObjectMapper를 함께 사용하여 데이터 매핑하기

먼저, Moya Provider를 생성하고 API를 호출하는 코드를 작성해야 합니다. 다음은 Moya Provider를 생성하는 예제입니다.

```swift
import Moya

enum API {
    case getUser(userID: Int)
}

extension API: TargetType {
    var baseURL: URL { return URL(string: "https://api.example.com")! }
    var path: String {
        switch self {
        case .getUser(let userID):
            return "/users/\(userID)"
        }
    }
    var method: Moya.Method {
        switch self {
        case .getUser:
            return .get
        }
    }
    var sampleData: Data {
        return Data()
    }
    var task: Task {
        return .requestPlain
    }
    var headers: [String : String]? {
        return nil
    }
}

let provider = MoyaProvider<API>()
```

다음으로, ObjectMapper를 사용하여 API 호출 결과를 데이터 모델로 매핑하는 코드를 작성합니다. 먼저, 매핑할 데이터 모델을 정의해야 합니다. 예를 들어, 다음과 같이 User 모델을 정의할 수 있습니다.

```swift
import ObjectMapper

struct User: Mappable {
    var id: Int?
    var name: String?
    
    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
    }
}
```

다음은 실제로 API를 호출하고 ObjectMapper를 사용하여 데이터를 매핑하는 예제입니다.

```swift
provider.request(.getUser(userID: 1)) { result in
    switch result {
    case let .success(response):
        do {
            let user = try response.map(to: User.self)
            print(user)
        } catch {
            print("Failed to map response to User model")
        }
    case let .failure(error):
        print("API request failed with error: \(error.localizedDescription)")
    }
}
```

위 예제에서는 `response.map(to: User.self)`를 사용하여 API 응답 데이터를 User 모델로 매핑합니다.

이렇게 Moya와 ObjectMapper를 함께 사용하여 API 호출 후 데이터를 매핑할 수 있습니다. Moya와 ObjectMapper는 각각 강력한 기능을 제공하므로, iOS 애플리케이션 개발에서 유용하게 사용할 수 있습니다.

## 참고 자료

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)