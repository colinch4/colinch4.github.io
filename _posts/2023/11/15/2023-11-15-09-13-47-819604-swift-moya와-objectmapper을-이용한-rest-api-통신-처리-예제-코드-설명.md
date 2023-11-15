---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift Moya와 ObjectMapper을 사용하여 REST API 통신을 처리하는 방법에 대해 알아보겠습니다. Swift Moya는 Alamofire 위에 구축된 네트워킹 라이브러리이며, ObjectMapper는 JSON 데이터를 모델 객체로 매핑해주는 라이브러리입니다.

## 필요한 라이브러리 설치

먼저, 프로젝트에 필요한 라이브러리를 설치해야 합니다. 이를 위해 CocoaPods를 사용하겠습니다.

1. 터미널을 열고 프로젝트 루트 디렉토리로 이동합니다.
2. `Podfile`이라는 파일을 생성하고 아래 코드를 추가합니다.

```ruby
platform :ios, '10.0'
use_frameworks!

target 'YourAppTarget' do
  pod 'Moya'
  pod 'ObjectMapper'
end
```

3. 터미널에서 `pod install` 명령어를 실행합니다.

## 모델 클래스 정의

통신으로 받을 데이터의 구조를 모델 클래스로 정의해야 합니다. 예를 들어, 통신으로 받을 유저 데이터를 다음과 같이 정의합니다.

```swift
import ObjectMapper

class User: Mappable {
  var name: String?
  var age: Int?
  
  required init?(map: Map) {}
  
  func mapping(map: Map) {
    name <- map["name"]
    age <- map["age"]
  }
}
```

위의 예제에서는 ObjectMapper의 매핑 기능을 사용하여 JSON 데이터를 모델 클래스의 프로퍼티에 매핑하도록 구현되었습니다.

## API 서비스 정의

Moya를 사용하여 API 서비스를 정의합니다. 예를 들어, 유저 정보를 가져오는 API를 사용해보겠습니다.

```swift
import Moya

enum UserService {
  case getUser(userID: Int)
}

extension UserService: TargetType {
  var baseURL: URL {
    return URL(string: "https://api.example.com")!
  }
  
  var path: String {
    switch self {
    case .getUser(let userID):
      return "/users/\(userID)"
    }
  }
  
  var method: Moya.Method {
    return .get
  }
  
  var sampleData: Data {
    return Data() // 실제 데이터로 대체해야 함
  }
  
  var task: Task {
    return .requestPlain
  }
  
  var headers: [String: String]? {
    return nil
  }
}
```

위의 예제에서는 `getUser(userID: Int)`라는 API를 정의했습니다. 각각의 `TargetType` 프로퍼티를 적절하게 설정해야 합니다.

## API 통신 처리

이제 작성한 API 서비스를 통해 실제로 API를 호출하고 데이터를 받아오는 코드를 작성합니다.

```swift
import Moya
import ObjectMapper

let provider = MoyaProvider<UserService>()

provider.request(.getUser(userID: 123)) { result in
  switch result {
  case let .success(response):
    do {
      let user = try response.mapObject(User.self)
      print(user.name)
      print(user.age)
    } catch {
      print(error)
    }
  case let .failure(error):
    print(error)
  }
}
```

위의 예제에서는 `MoyaProvider`를 사용하여 API를 호출하고, ObjectMapper를 사용하여 JSON 데이터를 `User` 모델 객체로 변환합니다. 성공적으로 변환이 완료되면 해당 객체의 프로퍼티를 사용할 수 있습니다.

## 마무리

이로써 Swift Moya와 ObjectMapper을 사용한 REST API 통신 처리 예제 코드 설명을 마치겠습니다. 이를 통해 간편하게 API 통신과 데이터 매핑을 처리할 수 있게되었습니다. 추가로 필요한 기능이 있다면 각 라이브러리의 공식 문서를 참조하시기 바랍니다.