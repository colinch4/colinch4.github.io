---
layout: post
title: "[swift] Swift에서 Codable과 Alamofire를 활용한 JSON 데이터 전송 및 수신 예시"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift 프로그래밍 언어에서 Codable과 Alamofire 라이브러리를 사용하면 JSON 데이터를 쉽게 전송하고 수신할 수 있습니다. Codable은 Swift 4에서 추가된 프로토콜로, JSON 데이터와 Swift의 객체 사이의 변환을 자동으로 처리해줍니다. Alamofire은 네트워킹 작업을 간편하게 처리할 수 있는 라이브러리입니다.

이 문서에서는 Codable과 Alamofire를 사용하여 JSON 데이터를 서버에 전송하는 예시와 서버로부터 JSON 데이터를 수신하는 예시를 소개하겠습니다.

## JSON 데이터 전송 예시

먼저, Alamofire를 설치하고 Swift 프로젝트에 import 해줍니다. 그런 다음, POST 요청을 보내는 코드를 작성해 보겠습니다.

```swift
import Alamofire

struct User: Codable {
    let username: String
    let email: String
}

let user = User(username: "john_doe", email: "john_doe@example.com")

AF.request("https://api.example.com/users", method: .post, parameters: user, encoder: JSONParameterEncoder.default).response { response in
    switch response.result {
    case .success:
        print("JSON 데이터 전송 성공")
    case .failure(let error):
        print("전송 실패: \(error)")
    }
}
```

위의 코드에서는 User라는 Codable 구조체를 정의하고, 그 안에 username과 email 프로퍼티를 선언했습니다. 그리고 이 구조체를 사용하여 user 객체를 생성합니다. Alamofire의 `request` 메서드를 사용하여 API 엔드포인트에 POST 요청을 보내고, 인코딩 방식을 JSON으로 지정합니다. 응답을 처리하기 위해 `response` 클로저를 사용합니다.

## JSON 데이터 수신 예시

이제 서버로부터 JSON 데이터를 수신하는 예시를 살펴보겠습니다. 이 예시에서는 GET 요청을 사용하여 JSON 데이터를 서버로부터 가져옵니다.

```swift
import Alamofire

struct Post: Codable {
    let id: Int
    let title: String
    let body: String
}

AF.request("https://api.example.com/posts", method: .get).responseDecodable(of: [Post].self) { response in
    switch response.result {
    case .success(let posts):
        for post in posts {
            print("제목: \(post.title), 내용: \(post.body)")
        }
    case .failure(let error):
        print("수신 실패: \(error)")
    }
}
```

위의 예시에서는 Post라는 Codable 구조체를 정의하고, 이 구조체를 배열로 사용합니다. Alamofire의 `request` 메서드를 사용하여 API 엔드포인트에 GET 요청을 보내고, 수신받은 JSON 데이터를 `[Post].self` 형태로 디코딩합니다. 응답을 처리하기 위해 `responseDecodable` 클로저를 사용합니다.

## 결론

이 문서에서는 Swift에서 Codable과 Alamofire를 사용하여 JSON 데이터를 전송하고 수신하는 예시를 소개하였습니다. Codable을 사용하면 Swift 객체와 JSON 데이터 간의 변환을 간편하게 처리할 수 있으며, Alamofire를 사용하면 HTTP 요청과 응답 처리를 더욱 편리하게 할 수 있습니다.

더 자세한 내용은 아래의 링크를 참고하세요.

- Codable 문서: [https://docs.swift.org/swift-book/LanguageGuide/Codable.html](https://docs.swift.org/swift-book/LanguageGuide/Codable.html)
- Alamofire GitHub 저장소: [https://github.com/Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)