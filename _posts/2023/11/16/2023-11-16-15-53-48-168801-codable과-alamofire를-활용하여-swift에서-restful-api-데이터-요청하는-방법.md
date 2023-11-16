---
layout: post
title: "[swift] Codable과 Alamofire를 활용하여 Swift에서 RESTful API 데이터 요청하는 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 RESTful API를 사용하여 데이터를 요청하고 처리하는 방법을 알아보겠습니다. Codable 프로토콜과 Alamofire 라이브러리를 활용하여 간편하게 JSON 데이터를 가져오고, Swift 객체로 변환하여 사용할 수 있습니다.

## 1. Alamofire 라이브러리 추가하기

Swift에서 Alamofire를 사용하기 위해서는 먼저 Alamofire 라이브러리를 프로젝트에 추가해야 합니다. CocoaPods를 사용하는 경우, `Podfile`에 다음과 같이 Alamofire를 추가합니다.

```swift
pod 'Alamofire', '~> 5.0'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 2. Codable 프로토콜을 이용하여 모델 정의하기

Swift에서 Codable 프로토콜을 사용하면 JSON 데이터를 Swift 객체로 변환할 수 있습니다. 예를 들어, 서버에서 받아올 사용자 정보를 다음과 같이 정의할 수 있습니다.

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}
```

위의 예제에서 `User` 구조체는 Codable 프로토콜을 채택하고, JSON 데이터의 키와 매핑되는 프로퍼티들을 포함하고 있습니다.

## 3. Alamofire를 사용하여 데이터 요청하기

Alamofire를 사용하여 RESTful API로부터 데이터를 요청하고 Codable 프로토콜을 채택한 객체로 디코딩하는 방법을 알아보겠습니다. 다음은 GET 요청을 보내고, 받아온 JSON 데이터를 `User` 객체로 변환하는 예제입니다.

```swift
import Alamofire

func fetchUsers(completion: @escaping ([User]) -> Void) {
    AF.request("https://api.example.com/users").responseJSON { response in
        switch response.result {
        case .success(let json):
            do {
                let jsonData = try JSONSerialization.data(withJSONObject: json)
                let decoder = JSONDecoder()
                let users = try decoder.decode([User].self, from: jsonData)
                completion(users)
            } catch {
                print("JSON decoding error: \(error)")
            }
        case .failure(let error):
            print("Network request failed: \(error)")
        }
    }
}
```

위의 예제에서 `fetchUsers` 함수는 Alamofire를 사용하여 서버로부터 JSON 데이터를 받아오고, 받아온 데이터를 `User` 배열로 디코딩하여 완료 핸들러에 전달합니다.

## 4. 데이터 요청 및 처리

이제 데이터를 요청하고 받아온 결과를 처리하는 방법을 알아보겠습니다. 다음은 `fetchUsers` 함수를 사용하여 사용자 목록을 요청하고, 받아온 사용자 정보를 출력하는 예제입니다.

```swift
fetchUsers { users in
    for user in users {
        print("ID: \(user.id), Name: \(user.name), Email: \(user.email)")
    }
}
```

위의 예제에서는 `fetchUsers` 함수를 호출하고, 받아온 사용자 정보를 반복문을 통해 출력하고 있습니다.

이렇게 Swift에서 Codable과 Alamofire를 함께 사용하여 RESTful API 데이터를 요청하고 처리할 수 있습니다. Codable을 사용하면 JSON 데이터를 Swift 객체로 쉽게 변환할 수 있으며, Alamofire를 사용하면 네트워크 요청을 간편하게 처리할 수 있습니다.

---

## 참고 자료

- [Swift Codable Documentation](https://developer.apple.com/documentation/swift/codable)
- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)