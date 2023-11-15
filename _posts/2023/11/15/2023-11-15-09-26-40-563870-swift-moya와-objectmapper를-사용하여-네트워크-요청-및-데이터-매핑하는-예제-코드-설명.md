---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift Moya와 ObjectMapper를 함께 사용하여 네트워크 요청을 보내고, 응답 데이터를 매핑하는 방법에 대해 알아보겠습니다.

Moya는 Swift에서 네트워크 요청을 쉽게 구현할 수 있는 라이브러리이며, ObjectMapper는 JSON 데이터를 Swift 객체로 변환하기 위한 라이브러리입니다. 두 라이브러리를 함께 사용하면 네트워크 요청을 보내고 응답 데이터를 매핑하는 과정을 간단하게 구현할 수 있습니다.

## Moya와 ObjectMapper 설치

먼저, 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. Moya를 설치하기 위해 `CocoaPods`를 이용하는 경우, `Podfile`에 다음과 같이 작성합니다.

```ruby
target 'YourProject' do
  use_frameworks!
  pod 'Moya'
  pod 'ObjectMapper'
end
```

설치가 완료되면, 아래와 같이 `import`문을 통해 두 라이브러리를 가져옵니다.

```swift
import Moya
import ObjectMapper
```

## 네트워크 요청 및 데이터 매핑

다음으로, 실제로 네트워크 요청을 보내고 데이터를 매핑하는 예제 코드를 작성해보겠습니다. 예제로는 사용자 정보를 가져오는 API를 호출하고, 응답 데이터를 User 객체로 매핑하는 과정을 보여줍니다.

먼저, MoyaProvider를 초기화합니다.

```swift
let provider = MoyaProvider<YourAPI>()
```

다음으로, 네트워크 요청을 보냅니다. Moya의 `request` 메서드를 사용하고, 클로저를 통해 응답을 처리합니다.

```swift
provider.request(.getUserInfo) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.map(to: User.self)
            // User 객체를 사용하여 필요한 작업을 수행합니다.
        } catch let error {
            // 매핑 오류 처리
            print("Mapping error: \(error)")
        }
    case .failure(let error):
        // 네트워크 요청 오류 처리
        print("Network request error: \(error)")
    }
}
```

위의 예제에서 `YourAPI`는 Moya의 `TargetType` 프로토콜을 준수하는 프로토콜입니다. `getUserInfo`는 `YourAPI`에 정의된 열거형 케이스로, 실제 API의 엔드포인트와 필요한 파라미터를 설정합니다.

매핑 과정에서 ObjectMapper를 사용하여 JSON 데이터를 `User` 객체로 변환합니다. `try response.map(to: User.self)` 코드에서 `User.self`는 매핑 대상 객체의 타입을 나타냅니다. 만약 매핑이 실패하면, `catch` 블록에서 오류 처리를 할 수 있습니다.

이제, 위의 예제 코드를 참고하여 실제 프로젝트에 Moya와 ObjectMapper를 적용하여 네트워크 요청 및 데이터 매핑을 구현해보세요.

## 참고 자료

- [Moya GitHub 저장소](https://github.com/Moya/Moya)
- [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)