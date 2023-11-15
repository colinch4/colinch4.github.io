---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

## 소개
Swift에서 Moya와 ObjectMapper는 많은 개발자들에게 인기 있는 라이브러리입니다. Moya는 네트워크 작업을 단순화하고 추상화하는 데 도움을 주며, ObjectMapper는 JSON 데이터를 객체로 매핑하는 데 사용됩니다. 이 두 가지 라이브러리를 함께 사용하면 API 요청 후 받은 데이터를 효과적으로 처리할 수 있습니다.

## 동작 방식
1. Moya를 사용하여 API 요청을 보냅니다.
2. 서버에서 응답이 오면 Moya는 JSON 데이터를 받습니다.
3. ObjectMapper를 사용하여 JSON 데이터를 모델 객체로 매핑합니다.

## 설치
먼저, Moya와 ObjectMapper를 프로젝트에 설치해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같은 의존성을 추가합니다:

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

그리고 설치를 완료하기 위해 터미널에서 다음 명령어를 실행합니다:

```
$ pod install
```

## 예제 코드
이제 Moya와 ObjectMapper를 사용하여 API 요청을 보내고 데이터를 매핑하는 예제 코드를 살펴보겠습니다.

1. 모델 객체 정의하기
```swift
import ObjectMapper

struct User: Mappable {
    var id: Int!
    var name: String!
    var email: String!

    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

2. Moya Provider 생성하기
```swift
import Moya

let provider = MoyaProvider<YourAPI>()
```

3. API 요청 보내기
```swift
provider.request(.getUser(id: 1)) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapObject(User.self)
            // 데이터 매핑 완료된 사용자 객체 사용하기
        } catch let error {
            print("매핑 에러: \(error.localizedDescription)")
        }
    case .failure(let error):
        print("네트워크 에러: \(error.localizedDescription)")
    }
}
```

위의 예제 코드에서 `YourAPI`는 실제 사용하는 API 열거형이어야 합니다. 또한, `getUser(id: 1)`는 사용자 정보를 가져오는 API 요청에 해당하는 케이스로 대체되어야 합니다.

## 결론
Swift Moya와 ObjectMapper를 사용하면 API 요청 후 데이터를 효과적으로 매핑할 수 있습니다. Moya는 네트워크 작업을 추상화하여 편리한 요청 및 응답 처리를 가능하게 해주며, ObjectMapper는 JSON 데이터를 쉽게 모델 객체로 변환할 수 있게 도와줍니다.

더 자세한 내용은 각 라이브러리의 공식 문서를 확인해보세요.

- [Moya GitHub](https://github.com/Moya/Moya)
- [ObjectMapper GitHub](https://github.com/tristanhimmelman/ObjectMapper)