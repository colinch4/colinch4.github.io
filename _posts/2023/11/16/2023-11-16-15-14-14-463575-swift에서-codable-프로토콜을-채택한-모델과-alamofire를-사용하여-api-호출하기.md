---
layout: post
title: "[swift] Swift에서 Codable 프로토콜을 채택한 모델과 Alamofire를 사용하여 API 호출하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 Codable 프로토콜은 JSON 데이터와 Swift 객체 간의 변환을 간편하게 처리할 수 있는 강력한 도구입니다. 

Alamofire는 Swift에서 널리 사용되는 네트워킹 라이브러리로, 간편한 API 호출을 가능하게 해줍니다. 

이 블로그 포스트에서는 Swift에서 Codable 프로토콜을 채택한 모델과 Alamofire를 사용하여 API를 호출하는 방법에 대해 알아보겠습니다.

## Codable 프로토콜 채택한 모델 정의하기

우선, API에서 반환되는 JSON 데이터를 Swift 객체로 매핑하기 위해 Codable 프로토콜을 채택한 모델을 정의해야 합니다. Codable을 사용하면 각 프로퍼티를 JSON 키와 매핑하여 데이터를 자동으로 디코딩하거나 인코딩할 수 있습니다.

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}
```

위의 예제에서는 사용자 정보를 담을 User라는 모델을 정의하였습니다. User 모델은 id, name, email 세 개의 프로퍼티를 가지고 있으며, Codable 프로토콜을 채택하였습니다.

## Alamofire를 사용하여 API 호출하기

Alamofire를 사용하여 API를 호출하려면 먼저 Alamofire 라이브러리를 프로젝트에 추가해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같은 의존성을 추가하고 `pod install` 명령을 실행합니다.

```ruby
pod 'Alamofire'
```

API를 호출하기 위해 다음과 같은 코드를 작성합니다.

```swift
import Alamofire

func fetchUser() {
    let url = "https://api.example.com/users"
    AF.request(url).responseJSON { response in
        switch response.result {
        case .success(let value):
            do {
                let data = try JSONSerialization.data(withJSONObject: value, options: .prettyPrinted)
                let decoder = JSONDecoder()
                let user = try decoder.decode(User.self, from: data)
                print(user)
            } catch {
                print(error)
            }
        case .failure(let error):
            print(error)
        }
    }
}
```

위의 코드에서는 Alamofire의 `request` 메서드를 사용하여 API를 호출하고, 응답을 처리하기 위해 `responseJSON` 메서드를 사용합니다. 성공적인 응답이 도착하면, JSON 데이터를 Swift 객체로 변환하기 위해 `JSONDecoder`를 사용합니다.

## API 호출하기

이제 `fetchUser` 함수를 호출하여 API를 호출하고 사용자 정보를 가져올 수 있습니다.

```swift
fetchUser()
```

위의 코드를 실행하면, API에서 반환되는 JSON 데이터를 User 객체로 변환하여 출력합니다.

이처럼 Swift에서 Codable 프로토콜과 Alamofire를 함께 사용하여 API 호출을 간편하게 처리할 수 있습니다. Codable을 사용하면 JSON 데이터와 Swift 객체 간의 변환을 쉽게 처리할 수 있으며, Alamofire는 네트워킹 요청을 쉽게 관리할 수 있는 강력한 도구입니다.

---

참고 자료:

- [Codable - Apple Developer Documentation](https://developer.apple.com/documentation/swift/codable)
- [Alamofire - GitHub](https://github.com/Alamofire/Alamofire)