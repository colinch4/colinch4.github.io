---
layout: post
title: "[swift] Moya와 ObjectMapper를 사용하여 API 호출 및 JSON 파싱하는 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift에서 Moya와 ObjectMapper을 사용하여 API를 호출하고 JSON 데이터를 파싱하는 방법을 살펴보겠습니다.

## Moya란?

Moya는 Alomofire를 기반으로 한 간단한 네트워킹 라이브러리입니다. Moya를 사용하면 네트워킹 코드를 깔끔하고 구조적으로 유지할 수 있습니다.

## ObjectMapper란?

ObjectMapper는 Swift 객체와 JSON 데이터 간의 매핑을 쉽게 해주는 라이브러리입니다. ObjectMapper를 사용하면 JSON 데이터를 객체로 쉽게 변환하거나, 객체를 JSON 데이터로 변환할 수 있습니다.

## 예제 코드

### 1. 프로젝트 설정

먼저, 프로젝트에 Moya와 ObjectMapper를 설치합니다. CocoaPods를 사용하신다면 `Podfile`에 다음 라이브러리를 추가하세요.

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

### 2. API 모델 정의하기

API의 응답에 맞는 데이터 모델을 정의합니다. 예를 들어, 사용자 정보를 가져오는 API가 있다고 가정해봅시다.

```swift
import Foundation
import ObjectMapper

struct User: Mappable {
    var id: Int = 0
    var name: String = ""
    var email: String = ""

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

### 3. API 호출 및 JSON 파싱하기

Moya와 ObjectMapper를 사용하여 API 호출 및 JSON 데이터를 파싱하는 코드를 작성해봅시다.

```swift
import Moya
import ObjectMapper

// Moya Provider 생성
let provider = MoyaProvider<YourAPIService>()

// API 호출
provider.request(.getUser(id: 1)) { result in
    switch result {
    case let .success(response):
        do {
            // JSON 데이터 파싱
            let user = try response.mapObject(User.self)
            print("User ID: \(user.id)")
            print("User Name: \(user.name)")
            print("User Email: \(user.email)")
        } catch {
            print("JSON parsing error: \(error)")
        }
    case let .failure(error):
        print("API request error: \(error)")
    }
}
```

위의 코드에서 `YourAPIService`는 사용자가 정의한 API 서비스 프로바이더입니다. 알맞게 변경하여 사용하세요.

### 4. 실행 결과

API 호출이 성공하면, 서버로부터 받은 JSON 데이터가 User 객체로 변환되어 출력됩니다.

```
User ID: 1
User Name: John Doe
User Email: john.doe@example.com
```

## 결론

Moya와 ObjectMapper를 사용하면 Swift에서 API 호출과 JSON 파싱을 간편하게 처리할 수 있습니다. 이 예제를 참고하여 프로젝트에 적용해보세요. Moya와 ObjectMapper의 문서와 예제 코드들도 깊이 있는 학습을 도와줄 것입니다.