---
layout: post
title: "[swift] Swift에서 Codable과 Alamofire를 사용하여 API 데이터 전송하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 Codable 프로토콜과 Alamofire 라이브러리를 사용하여 API 데이터를 전송하는 방법을 알아보겠습니다.

## 1. Codable 프로토콜 소개

Codable 프로토콜은 Swift 4부터 도입된 프로토콜로, 데이터를 직렬화하거나 역직렬화하는 기능을 제공합니다. Codable을 사용하면 JSON, XML 등과 같은 다양한 형식의 데이터를 Swift 객체로 쉽게 변환할 수 있습니다.

Codable 프로토콜을 사용하기 위해서는 데이터 모델 객체에 Codable을 준수하도록 선언해야 합니다. Codable을 준수하기 위해서는 해당 객체의 프로퍼티가 모두 Codable을 준수해야 합니다.

## 2. Alamofire 라이브러리 소개

Alamofire는 Swift에서 네트워크 통신을 쉽게 처리하기 위한 라이브러리입니다. 간편한 API를 제공하며, 비동기적인 방식으로 데이터를 전송할 수 있습니다. 우리는 Alamofire를 사용하여 API에 HTTP 요청을 보내고, 데이터를 전송할 것입니다.

## 3. Codable과 Alamofire를 함께 사용하여 API 데이터 전송하기

먼저 Alamofire를 프로젝트에 추가해야 합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 Alamofire를 추가합니다.

```swift
pod 'Alamofire'
```

프로젝트를 빌드하고 나면 Alamofire를 import하여 사용할 수 있습니다.

```swift
import Alamofire
```

API 데이터를 전송하기 위해서는 API의 엔드포인트 URL과 전송할 데이터 모델 객체가 필요합니다. 여기서는 사용자 정보를 업데이트하는 API를 예로 들겠습니다.

```swift
struct User: Codable {
    var name: String
    var age: Int
}

let updateEndpoint = "https://api.example.com/updateUser"

let userData = User(name: "John Doe", age: 30)
```

Codable을 준수하는 User 구조체를 정의했고, 업데이트할 사용자 데이터를 userData로 생성했습니다.

이제 Alamofire의 `request` 메서드를 사용하여 API에 HTTP 요청을 보냅니다. `request` 메서드의 파라미터로 HTTP 메서드와 엔드포인트 URL을 전달하고, `parameters` 파라미터에는 전송할 데이터 객체를 JSON으로 변환한 후 전달합니다.

```swift
Alamofire.request(updateEndpoint, method: .post, parameters: userData, encoding: JSONEncoding.default)
    .responseJSON { response in
        switch response.result {
        case .success(let value):
            // 성공적으로 데이터를 전송한 경우
            let json = JSON(value)
            // JSON 응답을 처리하는 코드를 작성할 수 있습니다.
        case .failure(let error):
            // 데이터 전송이 실패한 경우
            print(error)
        }
}