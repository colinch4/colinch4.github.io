---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift의 Moya와 ObjectMapper를 사용하여 네트워크 요청을 수행하고 응답 데이터를 매핑하는 방법을 알아보겠습니다. Moya는 Alamofire를 기반으로한 네트워킹 라이브러리이며, ObjectMapper는 JSON 데이터를 객체로 매핑해주는 라이브러리입니다. 이 두 라이브러리를 함께 사용하면 편리하게 네트워크 요청과 데이터 매핑을 처리할 수 있습니다.

## Moya와 ObjectMapper 설치하기

먼저, Moya와 ObjectMapper를 프로젝트에 설치해야 합니다. 이를 위해서는 Cocoapods를 사용하거나 Swift Package Manager를 사용할 수 있습니다. 프로젝트 폴더에서 `Podfile`을 생성하고 다음과 같이 작성하세요.

```ruby
platform :ios, '9.0'

target 'YourApp' do
  use_frameworks!

  pod 'Moya'
  pod 'ObjectMapper'
end
```

그리고 터미널에서 `pod install` 명령어를 실행하여 의존성을 설치합니다.

## 네트워크 요청 및 데이터 매핑 예제 코드

이제 네트워크 요청을 보내는 코드를 작성해보겠습니다. 먼저, Moya에서 사용할 API 열거형을 정의합니다. 예를 들어, GitHub API를 사용한다고 가정해봅시다.

```swift
import Moya

enum GitHubAPI {
  case getUser(username: String)
}

extension GitHubAPI: TargetType {
  var baseURL: URL {
    return URL(string: "https://api.github.com")!
  }

  var path: String {
    switch self {
    case .getUser(let username):
      return "/users/\(username)"
    }
  }

  var method: Moya.Method {
    return .get
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

let provider = MoyaProvider<GitHubAPI>()
```

이제 데이터를 매핑하는 코드를 작성해보겠습니다. ObjectMapper는 매핑할 객체를 정의하고, 매핑할 JSON 데이터를 입력하여 매핑을 수행합니다. 예를 들어, GitHub 사용자 정보를 매핑하는 객체를 생성하고, Moya로부터 받은 응답 데이터를 ObjectMapper를 사용하여 이 객체로 매핑해보겠습니다.

```swift
import ObjectMapper

struct GitHubUser: Mappable {
  var name: String?
  var bio: String?
  var followers: Int?
  var following: Int?

  init?(map: Map) {

  }

  mutating func mapping(map: Map) {
    name <- map["name"]
    bio <- map["bio"]
    followers <- map["followers"]
    following <- map["following"]
  }
}

provider.request(.getUser(username: "apple")) { result in
  switch result {
  case let .success(response):
    do {
      let json = try response.mapJSON()
      if let user = Mapper<GitHubUser>().map(JSONObject: json) {
        // 매핑된 데이터를 사용하여 작업 수행
        print("User Name: \(user.name ?? "")")
        print("Bio: \(user.bio ?? "")")
        print("Followers: \(user.followers ?? 0)")
        print("Following: \(user.following ?? 0)")
      }
    } catch {
      print("Error mapping JSON")
    }
  case let .failure(error):
    print("Network error: \(error.localizedDescription)")
  }
}
```

위 코드에서는 `MoyaProvider`를 사용하여 GitHub API로 네트워크 요청을 보냅니다. 그리고 응답을 받아오면 ObjectMapper를 사용하여 JSON 데이터를 `GitHubUser` 객체로 매핑합니다. 매핑된 데이터를 이용하여 원하는 작업을 수행할 수 있습니다.

이제 코드를 실행해보면, GitHub 사용자 "apple"의 정보가 출력되는 것을 확인할 수 있습니다.

## 마무리

이번에는 Swift Moya와 ObjectMapper를 사용하여 네트워크 요청을 보내고 응답 데이터를 매핑하는 예제 코드를 알아보았습니다. Moya와 ObjectMapper는 Swift 개발자들에게 강력한 네트워킹 및 데이터 매핑 기능을 제공해주는 라이브러리입니다. 이를 통해 편리하게 네트워크 요청을 수행하고 데이터를 매핑할 수 있습니다.

## 참고 자료

- [Moya GitHub 레포지토리](https://github.com/Moya/Moya)
- [ObjectMapper GitHub 레포지토리](https://github.com/tristanhimmelman/ObjectMapper)