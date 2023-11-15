---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 RESTful API 통신 코드 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift 언어를 기반으로 RESTful API 통신을 위해 Moya와 ObjectMapper 라이브러리를 사용하는 방법을 살펴보겠습니다.

## Moya?

[Moya](https://github.com/Moya/Moya)는 네트워크 작업을 추상화하고 쉽게 다룰 수 있도록 도와주는 라이브러리입니다. Alamofire와 함께 사용되어 직관적이고 간결한 코드로 네트워크 통신을 구현할 수 있습니다.

## ObjectMapper?

[ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)는 JSON 데이터를 객체로 매핑해주는 라이브러리입니다. JSON 데이터를 받아와서 Swift 객체로 변환하거나, Swift 객체를 JSON 데이터로 변환할 때 용이하게 사용할 수 있습니다.

### 설치

먼저, 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

설치를 완료한 후, 프로젝트를 열고 `import Moya`와 `import ObjectMapper`를 해당 파일에서 선언해주세요.

### 모델 클래스 생성

데이터 매핑을 위해 필요한 모델 클래스를 생성해야 합니다. 예를 들어, 사용자 정보를 나타낼 User 클래스를 생성해보겠습니다.

```swift
import Foundation
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
```

위의 코드에서 `Mappable` 프로토콜을 채택한 User 클래스를 정의했습니다. `id`, `name`, `email` 프로퍼티는 ObjectMapper를 통해 매핑될 JSON 키입니다.

### API Provider 생성

Moya를 사용하여 API Provider를 생성합니다. API Provider는 API 요청을 보내고 응답을 받는 역할을 합니다. 예를 들어, 사용자 정보를 가져오는 API를 호출하는 `UserProvider`를 생성해보겠습니다.

```swift
import Moya

enum UserProvider {
    case getUser(id: Int)
}

extension UserProvider: TargetType {
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

    var task: Task {
        return .requestPlain
    }

    var headers: [String: String]? {
        return nil
    }

    var sampleData: Data {
        return Data()
    }
}
```

위의 코드에서 `UserProvider`는 getUser API를 호출하는 열거형 타입입니다. TargetType 프로토콜을 채택하여 baseURL, path, method, task 등의 정보를 정의했습니다.

### API 호출

이제 API를 호출하고 데이터를 매핑하는 코드를 작성해보겠습니다. getUser API를 호출하는 코드는 다음과 같습니다.

```swift
import Moya
import ObjectMapper

let provider = MoyaProvider<UserProvider>()

provider.request(.getUser(id: 1)) { result in
    switch result {
    case let .success(response):
        do {
            let json = try response.mapJSON()
            if let user = Mapper<User>().map(JSONObject: json) {
                // 성공적으로 매핑된 사용자 정보
                print(user)
            }
        } catch {
            // 매핑 실패
            print("Error mapping JSON: \(error)")
        }
    case let .failure(error):
        // API 요청 실패
        print("API request failed: \(error)")
    }
}
```

위의 코드에서 `MoyaProvider<UserProvider>()`를 사용하여 UserProvider에 정의된 getUser API를 호출하고, 응답 결과를 처리합니다. 응답 데이터는 ObjectMapper를 사용하여 User 객체로 매핑되고, 성공적으로 매핑되었을 경우 해당 사용자 정보를 출력합니다.

이러한 방식으로 Moya와 ObjectMapper를 사용하여 RESTful API 통신을 구현할 수 있습니다.

---

위의 예제 코드 및 설명에 대한 자세한 내용은 [Moya GitHub 페이지](https://github.com/Moya/Moya)와 [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)에서 확인하실 수 있습니다.