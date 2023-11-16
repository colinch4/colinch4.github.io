---
layout: post
title: "[swift] Swift에서 Codable과 Alamofire를 사용한 네트워크 데이터 전송 처리 예제"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift에서 Codable과 Alamofire를 함께 사용하여 네트워크 데이터 전송을 처리하는 방법을 알아보겠습니다. Codable은 Swift 4부터 도입된 프로토콜로, JSON과 같은 외부 데이터 형식을 간편하게 Swift 객체로 변환하거나 그 반대로 변환할 수 있도록 도와줍니다. Alamofire는 네트워킹 라이브러리로, HTTP 요청을 보내고 응답을 받는 일을 간단하게 처리해줍니다.

## 준비 사항

먼저 프로젝트에 Alamofire를 설치해야 합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 Alamofire를 추가합니다.

```ruby
pod 'Alamofire'
```

그리고 터미널을 열어 프로젝트 폴더로 이동한 후 다음 명령어를 실행하여 Alamofire를 설치합니다.

```bash
pod install
```

이제 준비가 모두 끝났습니다. 예제 코드로 넘어가보겠습니다.

## 예제 코드

먼저 Codable 프로토콜을 준수하는 구조체를 정의합니다. 이 구조체는 API 응답으로 받은 JSON 데이터를 매핑하기 위해 사용될 것입니다.

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}
```

다음으로 Alamofire를 사용하여 네트워크 요청을 보내고 응답을 처리하는 코드를 작성합니다.

```swift
import Alamofire

let url = "https://api.example.com/users"

Alamofire.request(url).responseJSON { response in
    switch response.result {
    case .success(let value):
        // 응답이 성공적으로 도착한 경우 코드 작성
        if let data = response.data {
            do {
                let user = try JSONDecoder().decode(User.self, from: data)
                print(user)
            } catch {
                print("JSON decoding error: \(error)")
            }
        }
    case .failure(let error):
        // 응답이 실패한 경우 에러 처리
        print("Network request failed: \(error)")
    }
}
```

위 코드에서는 Alamofire.request 메서드를 사용하여 API 요청을 보냅니다. 응답이 성공적으로 도착한 경우 JSON 데이터를 User 구조체로 변환하고, 실패한 경우에는 에러를 출력합니다.

## 실행

위 예제 코드를 실행해보기 위해선 API 엔드포인트 URL을 실제 사용 가능한 URL로 변경해야 합니다. 실제 API가 없는 경우 [JSONPlaceholder](https://jsonplaceholder.typicode.com/)와 같은 더미 API를 사용할 수 있습니다.

위 코드를 실행하면 더미 데이터를 받아와서 User 구조체로 변환한 후 출력하게 됩니다.

이제 Swift에서 Codable과 Alamofire를 사용하여 네트워크 데이터를 처리하는 방법에 대해 알아보았습니다. 이를 활용하여 실제 프로젝트에서 데이터를 전송하고 처리하는 데 유용하게 활용할 수 있습니다.