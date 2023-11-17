---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 응답을 객체로 변환하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire와 ObjectMapper 라이브러리를 결합한 것으로, JSON 응답을 쉽게 객체로 변환할 수 있도록 도와줍니다. 

## 1. Cocoapods을 이용해 라이브러리 추가하기

먼저, 프로젝트에 AlamofireObjectMapper를 추가해야 합니다. Podfile에 다음과 같이 추가합니다:

```ruby
pod 'Alamofire'
pod 'ObjectMapper'
pod 'AlamofireObjectMapper'
```

그리고 터미널에서 `pod install`을 실행하여 라이브러리를 설치합니다.

## 2. 모델 클래스 생성하기

JSON 응답을 객체로 변환하기 위해 모델 클래스를 만들어야 합니다. 예를 들어, 사용자 정보를 받아오는 API의 응답이 다음과 같다고 가정해봅시다:

```json
{
  "name": "John",
  "age": 30,
  "email": "john@example.com"
}
```

위 JSON 응답을 다음과 같이 매칭하는 User 모델 클래스를 생성합니다:

```swift
import Foundation
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    var email: String?
    
    required init?(map: Map) {}
    
    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        email <- map["email"]
    }
}
```

## 3. 네트워크 요청 및 응답 처리하기

AlamofireObjectMapper를 사용하여 네트워크 요청을 보내고 응답을 처리하는 예제를 보겠습니다.

```swift
import Alamofire
import AlamofireObjectMapper

let url = "https://api.example.com/user"

Alamofire.request(url).responseObject { (response: DataResponse<User>) in
    switch response.result {
    case .success(let user):
        // 응답을 User 객체로 받아와서 처리합니다
        print(user.name)
        print(user.age)
        print(user.email)
    case .failure(let error):
        // 네트워크 에러 처리
        print(error.localizedDescription)
    }
}
```

위 코드에서 `responseObject` 함수는 Alamofire의 `request` 함수와 함께 사용하여 JSON 응답을 User 객체로 변환합니다. 이후, success 블록에서 User 객체를 사용하여 응답을 처리할 수 있습니다.

이렇게 AlamofireObjectMapper를 사용하면 네트워크 응답을 간단히 객체로 변환할 수 있습니다.

더 자세한 내용은 [AlamofireObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/AlamofireObjectMapper)를 참고하시기 바랍니다.