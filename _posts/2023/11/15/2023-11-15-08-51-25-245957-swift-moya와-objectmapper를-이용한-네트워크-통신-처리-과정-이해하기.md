---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 이용한 네트워크 통신 처리 과정 이해하기"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

## 목차
- [소개](#소개)
- [Moya란?](#moya란)
- [ObjectMapper란?](#objectmapper란)
- [네트워크 통신 처리 과정](#네트워크-통신-처리-과정)
  - [Moya 설정](#moya-설정)
  - [API 모델 정의](#api-모델-정의)
  - [네트워크 요청](#네트워크-요청)
  - [응답 처리](#응답-처리)
  - [오류 처리](#오류-처리)
- [마무리](#마무리)

## 소개
이번 블로그 포스트에서는 Swift 프로젝트에서 네트워크 통신을 처리할 때 많이 사용되는 `Moya`와 `ObjectMapper` 라이브러리에 대해 알아보겠습니다. 이 두 라이브러리를 함께 사용하면 네트워크 요청과 응답 처리를 간편하게 구현할 수 있습니다.

## Moya란?
`Moya`는 Swift에서 네트워크 통신을 추상화하는 라이브러리입니다. `Alamofire`를 기반으로 작동하며, 간편한 API 요청과 응답 처리를 위한 기능을 제공합니다. `Moya`는 RESTful API를 구성하는 각 엔드포인트를 enum으로 정의하고, 각 엔드포인트에 대한 기본 URL, path, HTTP 메소드 등을 설정하여 사용할 수 있습니다.

## ObjectMapper란?
`ObjectMapper`는 JSON 데이터를 Swift 객체로 매핑해주는 라이브러리입니다. `ObjectMapper`는 다양한 JSON 구조를 간편하게 매핑할 수 있는 많은 기능을 제공합니다. 이를 통해 네트워크 응답을 쉽게 파싱하여 사용할 수 있습니다.

## 네트워크 통신 처리 과정
아래는 `Moya`와 `ObjectMapper`를 이용한 네트워크 통신 처리 과정입니다.

### Moya 설정
먼저, `Moya`를 프로젝트에 추가하고 필요한 의존성을 설정해야 합니다. 아래는 `Podfile`에 `Moya`와 `ObjectMapper`를 추가하는 예시입니다.

```ruby
# Podfile
target 'MyApp' do
  use_frameworks! 

  pod 'Moya'
  pod 'ObjectMapper'
  
  # ...
end
```

프로젝트를 업데이트 한 후, `import Moya`와 `import ObjectMapper`를 추가해줍니다.

### API 모델 정의
`Moya`를 사용하여 API 모델을 구성해야 합니다. 아래는 예시입니다.

```swift
// MyAPI.swift
import Moya

enum MyAPI {
  case getUser(userID: Int)
  case createUser(name: String, email: String)
}

extension MyAPI: TargetType {
  var baseURL: URL {
    return URL(string: "https://api.example.com")!
  }
  
  var path: String {
    switch self {
      case .getUser(let userID):
        return "/users/\(userID)"
      case .createUser:
        return "/users"
    }
  }
  
  var method: Moya.Method {
    switch self {
      case .getUser:
        return .get
      case .createUser:
        return .post
    }
  }
  
  var task: Task {
    switch self {
      case .getUser, .createUser:
        return .requestPlain
    }
  }
  
  var headers: [String: String]? {
    return ["Content-Type": "application/json"]
  }
}
```

### 네트워크 요청
`Moya`를 이용하여 API 요청을 보내는 방법은 매우 간단합니다. 아래는 예시입니다.

```swift
// MyAPIService.swift
import Moya

class MyAPIService {
  let provider = MoyaProvider<MyAPI>()
  
  func getUser(userID: Int, completion: @escaping (Result<User, Error>) -> Void) {
    provider.request(.getUser(userID: userID)) { result in
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
  
  // ...
}
```

### 응답 처리
`ObjectMapper`를 이용하여 네트워크 응답을 매핑하는 방법은 아래와 같습니다.

```swift
// User.swift
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

### 오류 처리
네트워크 오류에 대한 처리를 위해 `Moya`의 `Result` 타입을 활용할 수 있습니다. 아래는 예시입니다.

```swift
// MyAPIService.swift
import Moya

class MyAPIService {
  // ...
  
  func createUser(name: String, email: String, completion: @escaping (Result<Void, Error>) -> Void) {
    provider.request(.createUser(name: name, email: email)) { result in
      switch result {
        case .success(let response):
          if response.statusCode == 201 {
            completion(.success(()))
          } else {
            let error = NSError(domain: "APIError", code: response.statusCode, userInfo: nil)
            completion(.failure(error))
          }
        case .failure(let error):
          completion(.failure(error))
      }
    }
  }
  
  // ...
}
```

## 마무리
위의 예시를 통해 Swift 프로젝트에서 `Moya`와 `ObjectMapper`를 이용한 네트워크 통신 처리 과정을 이해할 수 있었습니다. 이 두 라이브러리는 강력한 기능을 제공하며, 프로젝트에서 네트워크 통신을 처리할 때 효율적으로 사용할 수 있습니다. 추가로 더 많은 기능과 사용 방법을 알아보기 위해 공식 문서와 예제 코드를 참고해보세요.