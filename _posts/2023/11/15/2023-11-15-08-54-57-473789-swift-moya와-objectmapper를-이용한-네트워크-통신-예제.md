---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 이용한 네트워크 통신 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

Swift 언어를 사용하여 네트워크 통신을 구현하는 방법 중 Moya와 ObjectMapper를 활용하는 예제를 살펴보겠습니다. Moya는 네트워크 라이브러리로, Alamofire를 기반으로 작동하며 API 요청을 쉽게 구현할 수 있습니다. ObjectMapper는 JSON 데이터와 Swift 객체 간의 매핑을 쉽게 처리할 수 있는 라이브러리입니다.

## Moya와 ObjectMapper 설치하기

Moya와 ObjectMapper를 사용하기 위해 먼저 이들 라이브러리를 설치해야 합니다. CocoaPods를 사용한다면, `Podfile`에 다음과 같은 내용을 추가합니다.

```ruby
target 'YourApp' do
  use_frameworks!

  pod 'Moya'
  pod 'ObjectMapper'
end
```

그리고 터미널을 열어 프로젝트 폴더로 이동한 뒤 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 모델 클래스 생성하기

API 응답 데이터를 매핑할 모델 클래스를 생성합니다. 예를 들어, 서버로부터 받은 JSON 데이터에서 이름(Name), 이메일(Email) 정보를 담는 User 모델을 생성해봅시다.

```swift
import ObjectMapper

struct User: Mappable {
    var name: String?
    var email: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        name <- map["Name"]
        email <- map["Email"]
    }
}
```

Mappable 프로토콜을 채택하여 ObjectMapper 기능을 사용할 수 있도록 합니다. mapping 함수를 구현하여 JSON 키와 모델 프로퍼티를 매핑시킵니다.

## API 요청 구현하기

Moya를 사용하여 API 요청을 구현합니다. 예를 들어, GET 요청으로 사용자 정보를 가져오는 API를 호출하는 함수를 구현해봅시다.

```swift
import Moya

enum UserService {
    case getUserInfo
}

extension UserService: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }

    var path: String {
        switch self {
        case .getUserInfo:
            return "/user"
        }
    }

    var method: Moya.Method {
        switch self {
        case .getUserInfo:
            return .get
        }
    }

    var task: Task {
        switch self {
        case .getUserInfo:
            return .requestPlain
        }
    }

    var headers: [String: String]? {
        return ["Content-Type": "application/json"]
    }
}

let provider = MoyaProvider<UserService>()

provider.request(.getUserInfo) { result in
    switch result {
    case let .success(response):
        do {
            let user = try response.mapJSON(as: User.self)
            print(user.name)
            print(user.email)
        } catch {
            print(error.localizedDescription)
        }
    case let .failure(error):
        print(error.localizedDescription)
    }
}
```

UserService 열거형을 생성하여 API 엔드포인트를 정의합니다. TargetType 프로토콜을 채택하여 baseURL, path, method, task 등을 구현합니다. MoyaProvider 객체를 생성하여 API 요청을 보냅니다. 응답을 받을 때 맵핑할 모델 클래스를 지정하여 JSON 데이터를 User 객체로 매핑합니다.

## 결론

이렇게 Swift Moya와 ObjectMapper를 이용하여 네트워크 통신을 구현하는 방법을 알아보았습니다. Moya를 사용하면 간편하게 API 요청을 처리할 수 있고, ObjectMapper를 사용하면 JSON 데이터와 Swift 객체를 쉽게 매핑할 수 있습니다. 이들 라이브러리를 함께 활용하여 Swift 앱 개발을 더욱 효율적으로 진행할 수 있습니다.

## 참고 자료

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)