---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용하여 네트워크 요청 후 데이터 매핑하는 방법과 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

## 개요
이번 글에서는 Swift의 Moya와 ObjectMapper 라이브러리를 함께 사용하여 네트워크 요청 후 데이터 매핑하는 방법에 대해 알아보겠습니다. Moya는 네트워크 요청을 보다 쉽게 작성하고 관리할 수 있도록 도와주는 라이브러리이며, ObjectMapper는 JSON 데이터를 모델 객체로 매핑해주는 라이브러리입니다.

## Moya 설치하기
Moya를 사용하기 위해서는 먼저 Moya를 프로젝트에 설치해야 합니다. CocoaPods를 사용하는 경우 Podfile에 다음과 같이 추가합니다.

```ruby
pod 'Moya'
```

설치가 완료되었다면, `import Moya` 문을 추가하여 Moya를 사용할 준비를 합니다.

## ObjectMapper 설치하기
이제 ObjectMapper를 설치해보겠습니다. CocoaPods를 사용하는 경우 Podfile에 다음과 같이 추가하고 설치합니다.

```ruby
pod 'ObjectMapper'
```

설치가 완료되면, `import ObjectMapper` 문을 추가하여 ObjectMapper를 사용할 준비를 합니다.

## 네트워크 요청과 데이터 매핑
이제 Moya와 ObjectMapper를 함께 사용하여 네트워크 요청 후 데이터를 매핑하는 방법에 대해 알아보겠습니다. 예시로 사용할 API는 https://jsonplaceholder.typicode.com/posts 입니다. 이 API는 사용자가 작성한 게시글 목록을 제공합니다.

먼저, Moya를 사용하여 네트워크 요청을 작성합니다. 다음은 GET 방식으로 게시글 목록을 요청하는 코드입니다.

```swift
import Moya

enum PostsAPI {
    case getPosts
}

extension PostsAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://jsonplaceholder.typicode.com")!
    }

    var path: String {
        switch self {
        case .getPosts:
            return "/posts"
        }
    }

    var method: Moya.Method {
        switch self {
        case .getPosts:
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

위의 코드에서 `PostsAPI`는 네트워크 요청에 대한 열거형입니다. `TargetType` 프로토콜을 구현하여 요청에 필요한 정보를 제공합니다.

다음은 ObjectMapper를 사용하여 데이터를 매핑하는 코드입니다. 

```swift
import ObjectMapper

struct Post: Mappable {
    var id: Int?
    var userId: Int?
    var title: String?
    var body: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- map["id"]
        userId <- map["userId"]
        title <- map["title"]
        body <- map["body"]
    }
}

let provider = MoyaProvider<PostsAPI>()

provider.request(.getPosts) { (result) in
    switch result {
    case .success(let response):
        do {
            let posts = try response.map([Post].self)
            // 받아온 데이터(posts)를 사용합니다.
        } catch {
            print("Error mapping data: \(error)")
        }
    case .failure(let error):
        print("Network error: \(error)")
    }
}
```

위의 코드에서 `Post`는 게시글 객체를 의미하는 모델입니다. `Mappable` 프로토콜을 구현하여 JSON 데이터를 객체로 매핑할 수 있도록 합니다.

네트워크 요청을 하고 받아온 응답을 매핑하는 부분은 `provider.request` 클로저 내부에 작성됩니다. `response.map([Post].self)`을 통해 JSON 데이터를 `[Post]` 배열로 매핑하여 사용할 수 있습니다.

## 마무리
이번 글에서는 Swift의 Moya와 ObjectMapper을 함께 사용하여 네트워크 요청 후 데이터 매핑하는 방법과 예제에 대해 알아보았습니다. Moya와 ObjectMapper는 Swift 개발을 보다 효율적으로 할 수 있도록 도와주는 라이브러리이므로, 프로젝트에서 많이 활용해보시기 바랍니다.