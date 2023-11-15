---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 예제에서는 Swift Moya와 ObjectMapper 라이브러리를 사용하여 RESTful API에 대한 네트워크 통신을 수행하고, 응답 데이터를 객체로 매핑하는 방법을 설명합니다.

## 전제 조건
- Swift 5
- Xcode 11 이상

## Moya 및 ObjectMapper 설치

먼저, Moya와 ObjectMapper를 프로젝트에 설치해야 합니다. Cocoapods를 사용하여 설치하는 경우, Podfile에 다음의 의존성을 추가합니다:

```ruby
target 'YourProjectName' do
  use_frameworks!
  pod 'Moya', '~> 14.0'
  pod 'ObjectMapper', '~> 4.2'
end
```

그리고 터미널에서 다음 명령을 실행하여 의존성을 설치합니다:

```
$ pod install
```

## 모델 클래스 생성

먼저, API 응답과 매핑할 모델 클래스를 생성합니다. 예를 들어, 특정 사용자의 정보를 담을 `User` 모델을 정의합니다.

```swift
import ObjectMapper

class User: Mappable {
    var id: Int = 0
    var name: String = ""
    var email: String = ""

    required init?(map: Map) {}

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

`Mappable` 프로토콜을 채택하여 ObjectMapper에서 필요한 매핑 메소드를 구현합니다. `required init?(map: Map)` 메소드는 ObjectMapper에 의해 자동으로 호출되며, `mapping(map: Map)` 메소드에서 실제 데이터와 모델 속성을 매핑합니다. 이 예제에서는 `id`, `name`, `email` 속성을 매핑하도록 구현했습니다.

## 네트워크 관리 객체 생성

이제 Moya를 사용하여 네트워크 통신을 관리하는 객체를 생성합니다. 아래의 코드는 사용자 정보를 가져오기 위한 API 요청을 정의한 예입니다.

```swift
import Moya

enum UserService {
    case getUser(id: Int)
}

extension UserService: TargetType {
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
        switch self {
        case .getUser:
            return .get
        }
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

let provider = MoyaProvider<UserService>()
```

`UserService`는 네트워크 요청을 정의하는 enum 타입이며, `TargetType` 프로토콜을 채택하여 필요한 속성과 메소드를 구현합니다. `baseURL`은 API의 기본 URL을 설정하고, `path`는 각 API 요청에 대한 경로를 정의합니다. `method`는 HTTP 요청 메소드를 설정하며, `task`는 요청에 필요한 데이터를 설정합니다. `headers`는 요청에 필요한 헤더 정보를 설정하며, `sampleData`는 테스트용 샘플 데이터를 반환합니다.

## 네트워크 요청 및 데이터 매핑

이제 생성한 네트워크 관리 객체(`provider`)를 사용하여 API 요청을 보내고, 응답 데이터를 매핑하는 과정을 설명합니다. 예를 들어, 특정 사용자의 정보를 가져오는 API를 호출하는 코드는 다음과 같습니다.

```swift
provider.request(.getUser(id: 1)) { (result) in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapObject(User.self)
            print(user.name)
        } catch {
            print("Mapping error: \(error)")
        }
    case .failure(let error):
        print("Network error: \(error)")
    }
}
```

`provider.request(.getUser(id: 1))`를 호출하여 API 요청을 보냅니다. 성공적인 응답인 경우, `response.mapObject(User.self)`를 호출하여 응답 데이터를 `User` 모델로 매핑합니다. 매핑이 성공하면, 매핑된 모델 객체를 사용하여 데이터를 처리할 수 있습니다. 네트워크에 실패한 경우, `failure` 블록에서 에러를 처리합니다.

## 결론

이 예제에서는 Swift Moya와 ObjectMapper를 사용하여 네트워크 통신을 수행하고, 응답 데이터를 객체로 매핑하는 방법을 보여주었습니다. Moya의 단순한 API 요청 정의와 ObjectMapper의 편리한 데이터 매핑을 통해 빠르고 간편하게 네트워크 통신을 구현할 수 있습니다.

> 참고: [Moya 공식 문서](https://github.com/Moya/Moya)
> 참고: [ObjectMapper 공식 문서](https://github.com/tristanhimmelman/ObjectMapper)