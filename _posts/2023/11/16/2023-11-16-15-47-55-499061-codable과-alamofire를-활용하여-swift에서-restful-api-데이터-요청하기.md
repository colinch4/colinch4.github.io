---
layout: post
title: "[swift] Codable과 Alamofire를 활용하여 Swift에서 RESTful API 데이터 요청하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 RESTful API를 통해 데이터를 요청하는 방법을 알아보겠습니다. Swift에서는 Codable과 Alamofire를 함께 사용하여 간편하게 API 요청을 처리할 수 있습니다.

## 1. Alamofire 설치하기

Alamofire는 Swift용 HTTP 네트워킹 라이브러리로, 편리한 네트워킹 기능을 제공합니다. 프로젝트에 Alamofire를 설치하기 위해서는 CocoaPods 또는 Swift Package Manager를 사용할 수 있습니다.

CocoaPods를 사용하는 경우, `Podfile`에 다음과 같이 추가합니다:

```
pod 'Alamofire'
```

그리고 터미널에서 다음 명령을 실행하여 팟을 설치합니다:

```
$ pod install
```

Swift Package Manager를 사용하는 경우, Xcode 프로젝트에서 `File → Swift Packages → Add Package Dependency`를 선택하고, `https://github.com/Alamofire/Alamofire.git`을 입력하여 패키지를 추가합니다.

## 2. Codable 프로토콜 채택하기

Codable 프로토콜은 Swift 4에서 소개된 프로토콜로, Swift 객체와 JSON 데이터 간의 변환을 쉽게 처리할 수 있도록 도와줍니다. API 요청에 대한 응답 데이터를 Swift 객체로 변환하기 위해 Codable 프로토콜을 사용합니다.

예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해봅시다:

```json
{
    "id": 1,
    "name": "John",
    "age": 25
}
```

해당 JSON 데이터를 Swift 객체로 변환하기 위해 다음과 같이 Codable 프로토콜을 채택한 구조체를 정의합니다:

```swift
struct Person: Codable {
    let id: Int
    let name: String
    let age: Int
}
```

## 3. API 요청하기

이제 Alamofire와 Codable을 함께 사용하여 API 요청을 처리해보도록 하겠습니다. 예를 들어, 서버에 있는 사용자 정보를 요청하는 API를 호출하고, 응답 데이터를 Swift 객체로 변환하는 방법을 알아보겠습니다.

```swift
import Alamofire

let apiUrl = "https://api.example.com/users"

AF.request(apiUrl).responseJSON { response in
    switch response.result {
    case .success(let json):
        if let jsonData = try? JSONSerialization.data(withJSONObject: json, options: []),
           let person = try? JSONDecoder().decode(Person.self, from: jsonData) {
            // 응답 데이터를 Swift 객체로 변환한 후 처리 로직 작성
            print(person.name)
            print(person.age)
        }
    case .failure(let error):
        // 에러 처리 로직 작성
        print(error.localizedDescription)
    }
}
```

위 코드에서는 Alamofire를 사용하여 `apiUrl`에 지정된 URL로 GET 요청을 보내고, 응답을 받은 후에는 JSON 데이터를 Swift 객체로 변환합니다. 이때, `Person` 구조체는 Codable 프로토콜을 채택하여 JSON 데이터를 매핑할 수 있도록 합니다.

## 4. 정리

이번 포스트에서는 Swift에서 Codable과 Alamofire를 사용하여 RESTful API 데이터를 요청하는 방법을 알아보았습니다. Alamofire를 사용해 HTTP 요청을 보내고, Codable을 사용해 응답 데이터를 Swift 객체로 변환할 수 있습니다. 이러한 방법을 통해 Swift로 간편하게 API 요청을 처리할 수 있습니다.

자세한 내용은 다음 참고 자료를 확인해주세요.

- Alamofire 공식문서: [https://github.com/Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)
- Codable 공식문서: [https://developer.apple.com/documentation/swift/codable](https://developer.apple.com/documentation/swift/codable)
- SwiftUI로 RESTful API와 함께 데이터 표시하기: [https://developer.apple.com/tutorials/swiftui/working-with-apis](https://developer.apple.com/tutorials/swiftui/working-with-apis)