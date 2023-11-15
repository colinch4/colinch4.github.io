---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 블로그 포스트에서는 Swift 5에서 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 요청을 보내고 응답 데이터를 매핑하는 방법을 알아보겠습니다. Moya는 Alamofire를 기반으로한 네트워킹 라이브러리이며, ObjectMapper는 JSON 데이터를 Swift 객체로 매핑하기 위한 라이브러리입니다.

## 요구사항

이 예제 코드를 따라하기 위해서는 먼저 CocoaPods를 설치해야 합니다. CocoaPods가 설치되어 있다면 `Podfile`을 생성하고 다음과 같이 내용을 작성합니다.

```ruby
platform :ios, '12.0'

target 'YourApp' do
  use_frameworks!
  
  pod 'Moya', '~> 14.0'
  pod 'ObjectMapper', '~> 4.2'
end
```

그리고 터미널에서 `pod install` 명령을 실행하여 필요한 라이브러리를 설치합니다.

## 모델 클래스 만들기

API로부터 받을 데이터를 매핑하기 위해 모델 클래스를 정의해야 합니다. 예를 들어, 사용자 정보를 나타내는 `User` 클래스를 만들어보겠습니다.

```swift
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

위의 코드에서 `Mappable` 프로토콜을 준수하는 `User` 클래스를 정의하였습니다. `id`, `name`, `email` 프로퍼티를 매핑하기 위해 `mapping(map:)` 메소드에서 ObjectMapper의 `<-` 연산자를 사용합니다.

## 네트워킹 관리자 만들기

네트워킹 동작을 관리하기 위해 Moya를 사용하는 네트워킹 관리자를 만들어보겠습니다. 다음과 같이 `NetworkManager` 클래스를 정의합니다.

```swift
import Moya

class NetworkManager {
    static let provider = MoyaProvider<API>()
    
    static func getUser(completion: @escaping (User?, Error?) -> ()) {
        provider.request(.getUser) { result in
            switch result {
            case .success(let response):
                do {
                    let user = try response.mapObject(User.self)
                    completion(user, nil)
                } catch {
                    completion(nil, error)
                }
            case .failure(let error):
                completion(nil, error)
            }
        }
    }
}

enum API {
    case getUser
}

extension API: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUser:
            return "/user"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUser:
            return .get
        }
    }
    
    var task: Task {
        switch self {
        case .getUser:
            return .requestPlain
        }
    }
    
    var headers: [String : String]? {
        return nil
    }
}
```

위의 코드에서 `NetworkManager` 클래스는 `getUser` 메소드를 정의하여 API로부터 사용자 정보를 가져올 수 있도록 합니다. `MoyaProvider`를 사용하여 요청을 보내고, 응답을 ObjectMapper의 `mapObject()` 메소드를 사용하여 매핑합니다.

## 데이터 가져오기

이제 `NetworkManager` 클래스의 `getUser` 메소드를 호출하여 데이터를 가져와보겠습니다. 다음과 같이 코드를 작성합니다.

```swift
NetworkManager.getUser { user, error in
    if let user = user {
        print("User ID: \(user.id ?? 0)")
        print("User Name: \(user.name ?? "")")
        print("User Email: \(user.email ?? "")")
    } else if let error = error {
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 코드에서 `getUser` 메소드의 completion closure에서 받은 `User` 객체를 사용하여 사용자 정보를 출력합니다.

## 결론

이제 Swift Moya와 ObjectMapper를 사용하여 네트워크 요청을 보내고 응답 데이터를 매핑하는 방법을 알게되었습니다. 이를 통해 간편하게 네트워킹 코드를 작성하고 JSON 데이터를 Swift 객체로 변환할 수 있습니다.

더 많은 정보를 알고 싶으시다면 다음의 링크들을 참고하세요.

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)