---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift의 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 요청과 데이터 매핑을 수행하는 방법을 알아보겠습니다. Moya는 네트워크 추상화 라이브러리로, 네트워크 요청을 쉽게 작성하고 관리할 수 있도록 도와줍니다. ObjectMapper는 JSON 데이터를 Swift 객체로 매핑해주는 라이브러리입니다.

## 설치 및 설정

먼저, CocoaPods를 사용하여 프로젝트에 Moya와 ObjectMapper를 설치합니다. Podfile에 다음과 같이 추가하고, 터미널에서 `pod install` 명령어를 실행합니다.

```ruby
pod 'Moya', '~> 14.0'
pod 'ObjectMapper', '~> 4.2'
```

설치가 완료되면, 프로젝트에서 다음과 같이 Moya 및 ObjectMapper를 import합니다.

```swift
import Moya
import ObjectMapper
```

## API 모델 정의

먼저, API 모델을 정의합니다. 예를 들어, 간단한 사용자 정보를 가져오는 API를 사용하는 경우 다음과 같이 모델을 구성할 수 있습니다.

```swift
struct User: Mappable {
    var name: String?
    var age: Int?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}
```

`Mappable` 프로토콜을 구현하여 ObjectMapper에서 JSON 데이터를 객체로 매핑할 수 있도록 합니다.

## 네트워크 요청

이제 Moya를 사용하여 네트워크 요청을 만들어 보겠습니다. 먼저, API의 Endpoint Enum을 만듭니다.

```swift
enum API {
    case getUserInfo(userId: String)
}
```

각각의 Endpoint는 사용자 정보를 가져오는 API를 나타냅니다.

다음으로, MoyaProvder를 생성해서 Endpoint와 ObjectMapper와 연결합니다.

```swift
private let provider = MoyaProvider<API>(plugins: [NetworkLoggerPlugin()])

extension API: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com/")!
    }

    var path: String {
        switch self {
        case .getUserInfo(let userId):
            return "users/\(userId)"
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
        return .requestPlain
    }

    var headers: [String: String]? {
        return nil
    }
}
```

위의 코드에서 baseURL은 API의 기본 URL을 나타냅니다. path는 각 Endpoint에 대한 경로를 정의하고, method는 HTTP 메소드를 나타냅니다. sampleData는 테스트를 위한 샘플 데이터이며, task는 요청에 필요한 데이터를 나타냅니다. headers는 추가로 전달할 헤더가 있는 경우 정의합니다.

## 데이터 매핑

네트워크 요청이 성공하고, 데이터를 받아왔다면 ObjectMapper를 사용하여 JSON 데이터를 객체로 매핑해야 합니다. 예를 들어, 다음과 같이 사용자의 정보를 가져오는 함수가 있다고 가정합니다.

```swift
func getUserInfo(userId: String, completion: @escaping (Result<User, Error>) -> Void) {
    provider.request(.getUserInfo(userId: userId)) { result in
        switch result {
        case .success(let response):
            do {
                let user = try response.mapObject(User.self)
                completion(.success(user))
            } catch {
                completion(.failure(error))
            }
        case .failure(let error):
            completion(.failure(error))
        }
    }
}
```

위의 코드에서는 MoyaProvider의 request 메소드를 사용하여 네트워크 요청을 보냅니다. 응답 결과를 확인한 후, ObjectMapper의 mapObject 메소드를 사용하여 JSON 데이터를 User 객체로 매핑합니다.

## 활용

이제 getUserInfo 함수를 사용하여 사용자 정보를 가져와 보겠습니다.

```swift
getUserInfo(userId: "123") { result in
    switch result {
    case .success(let user):
        print("이름: \(user.name ?? ""), 나이: \(user.age ?? 0)")
    case .failure(let error):
        print("에러 발생: \(error)")
    }
}
```

위의 코드는 userId가 "123"인 사용자의 정보를 가져오고, 성공적으로 매핑된 결과를 출력합니다.

## 결론

Swift의 Moya와 ObjectMapper를 사용하여 네트워크 요청과 데이터 매핑을 수행하는 방법을 알아보았습니다. 이러한 라이브러리를 사용하면 네트워크 요청을 간단하게 작성하고, JSON 데이터를 Swift 객체로 쉽게 매핑할 수 있습니다.