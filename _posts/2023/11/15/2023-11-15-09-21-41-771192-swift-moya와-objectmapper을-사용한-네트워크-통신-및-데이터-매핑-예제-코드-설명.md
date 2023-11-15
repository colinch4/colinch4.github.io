---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift 프레임워크인 Moya와 ObjectMapper을 사용하여 네트워크 통신과 데이터 매핑을 어떻게 수행하는지 알아보겠습니다.

Moya는 Alamofire의 추상화 레이어이며, 더 간편하고 편리한 네트워크 통신을 제공합니다. ObjectMapper는 JSON 데이터를 객체로 매핑하는 라이브러리로, 서버에서 받은 JSON 데이터를 모델 클래스로 매핑하는 데 사용됩니다.

## Moya 설치 및 설정

Moya를 사용하기 위해 먼저 Cocoapods를 이용하여 Moya를 설치해야 합니다.

```ruby
# Podfile

platform :ios, '10.0'

target 'YourProjectName' do
    use_frameworks!

    pod 'Moya', '~> 14.0'
end
```

설치가 완료되면, 터미널에서 `pod install` 명령어를 실행하여 종속성을 설치합니다.

## 네트워크 요청 작성

Moya는 프로바이더를 기반으로 네트워크 요청을 작성합니다. 프로바이더는 API 요청의 기본 URL, 헤더, Endpoint 등을 정의하는 파일입니다. 

```swift
import Moya

enum MyAPI {
    case getUsers
    case getUserDetails(id: Int)
}

extension MyAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUsers:
            return "/users"
        case .getUserDetails(let id):
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

위 코드에서는 MyAPI 열거형으로 API 요청을 정의했습니다. getUsers와 getUserDetails로 사용자 목록 및 특정 사용자 정보를 가져오는 요청을 정의했으며, TargetType 프로토콜을 구현하여 baseURL, path, method 등을 지정했습니다.

## 네트워크 요청 실행

네트워크 요청을 실행하기 위해서는 MoyaProvider를 사용해야 합니다.

```swift
import Moya

let provider = MoyaProvider<MyAPI>()

provider.request(.getUsers) { result in
    switch result {
    case let .success(response):
        do {
            let users = try response.map([User].self)
            print(users)
        } catch {
            print(error)
        }
    case let .failure(error):
        print(error)
    }
}
```

위 코드에서는 MoyaProvider를 사용하여 getUsers 요청을 실행하고, 반환된 결과를 처리하는 방법을 보여줍니다. 성공적인 경우, response.map 메서드를 사용하여 JSON 데이터를 User 객체로 매핑합니다. 실패한 경우, 에러 메시지를 출력합니다.

## ObjectMapper를 사용하여 데이터 매핑

ObjectMapper를 사용하여 JSON 데이터를 모델 클래스로 매핑할 수 있습니다. 아래는 데이터 매핑을 위한 예제 코드입니다.

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

위 코드에서는 User 구조체를 생성하고, Mappable 프로토콜을 구현하여 JSON 데이터를 객체로 매핑합니다. mapping(map:) 메서드를 사용하여 JSON과 객체의 속성을 연결합니다.

Moya와 ObjectMapper을 함께 사용하면 Swift에서 더욱 편리하고 간단하게 네트워크 통신과 데이터 매핑을 수행할 수 있습니다. Moya의 추상화된 네트워크 계층과 ObjectMapper의 객체 매핑 기능을 통해 빠르고 효율적인 개발을 할 수 있습니다.

## 참고 자료

- [Moya 공식 문서](https://github.com/Moya/Moya)
- [ObjectMapper 공식 문서](https://github.com/tristanhimmelman/ObjectMapper)