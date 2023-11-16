---
layout: post
title: "[swift] Swift에서 Alamofire를 사용한 GET 요청 및 Decodable 파싱 예제"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이 예제에서는 Swift에서 Alamofire라이브러리를 사용하여 GET 요청을 수행하고, 응답을 Decodable 객체로 파싱하는 방법을 보여줍니다.

## Alamofire 설치하기
먼저, Alamofire를 설치해야 합니다. Swift 패키지 매니저를 사용하여 다음 명령어를 실행합니다.

```
$ swift package init --type executable
$ swift package update
$ swift package resolve
$ swift package generate-xcodeproj
```

## GET 요청하기
GET 요청을 수행하기 위해 Alamofire를 import합니다.

```swift
import Alamofire
```

그런 다음 `AF.request()` 메소드를 사용하여 GET 요청을 보냅니다. URL은 문자열로 전달하고, 응답은 클로저를 통해 처리합니다.

```swift
AF.request("https://api.example.com/data")
    .responseJSON { response in
        // 응답 처리하기
    }
```

## Decodable로 파싱하기
응답을 Decodable 객체로 파싱하기 위해서는, 응답 데이터의 구조와 일치하는 구조체를 만들어야 합니다.

```swift
struct ApiResponse: Decodable {
    let message: String
    let data: [Person]
}

struct Person: Decodable {
    let name: String
    let age: Int
}
```

이제 `responseDecodable()` 메소드를 사용하여 응답을 파싱합니다. 파싱할 구조체 타입을 전달하고, 클로저를 사용하여 파싱된 객체를 처리할 수 있습니다.

```swift
AF.request("https://api.example.com/data")
    .responseDecodable(of: ApiResponse.self) { response in
        // 파싱된 객체 처리하기
        if let apiResponse = response.value {
            print(apiResponse.message)
            for person in apiResponse.data {
                print(person.name)
                print(person.age)
            }
        }
    }
```

이제 Alamofire를 사용하여 GET 요청을 보내고, 응답을 Decodable 객체로 파싱하는 방법을 알게 되었습니다.

더 자세한 내용은 [Alamofire 공식 문서](https://github.com/Alamofire/Alamofire)를 참고하십시오.