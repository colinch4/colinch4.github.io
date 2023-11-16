---
layout: post
title: "[swift] SwiftyJSON을 사용하여 JSON 데이터를 UserDefaults에 저장하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

UserDefaults는 iOS 애플리케이션에서 간단한 데이터 저장을 위해 사용됩니다. 일반적으로 문자열, 숫자, Boolean 값과 같은 간단한 데이터를 저장하는 용도로 자주 사용됩니다. 그러나 JSON 데이터와 같이 복잡한 구조를 가진 데이터를 저장하려면 SwiftyJSON 라이브러리를 사용할 수 있습니다. 

SwiftyJSON은 JSON 데이터를 다루기 쉽도록 하는 강력한 도구입니다. 이 라이브러리를 사용하면 JSON 데이터를 파싱하고 접근하는 것이 훨씬 간편해집니다. 

이번 튜토리얼에서는 SwiftyJSON을 사용하여 JSON 데이터를 UserDefaults에 저장하는 방법에 대해 알아보겠습니다.

## 1. SwiftyJSON 라이브러리 설치하기

먼저, Xcode 프로젝트에 SwiftyJSON 라이브러리를 추가해야 합니다. SwiftyJSON을 설치하려면 CocoaPods를 사용하면 됩니다. Podfile에 다음과 같이 추가해 주세요.

```ruby
pod 'SwiftyJSON'
```

그런 다음 터미널에서 다음 명령을 실행하여 SwiftyJSON을 설치합니다.

```bash
pod install
```

## 2. JSON 데이터 저장하기

이제 SwiftyJSON을 사용하여 JSON 데이터를 UserDefaults에 저장할 수 있습니다. 

먼저, JSON 데이터를 얻어옵니다. 예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해 봅시다.

```json
{
  "name": "John Smith",
  "age": 25,
  "email": "john@gmail.com"
}
```

이제 이 JSON 데이터를 SwiftyJSON으로 파싱합니다. 

```swift
import SwiftyJSON

let jsonString = """
{
  "name": "John Smith",
  "age": 25,
  "email": "john@gmail.com"
}
"""

if let data = jsonString.data(using: .utf8) {
    let json = try JSON(data: data)
    
    // UserDefaults에 JSON 데이터 저장
    UserDefaults.standard.setValue(json.dictionaryObject, forKey: "user")
}
```

위의 코드에서 `jsonString` 변수에 JSON 문자열을 할당한 후, `data(using: .utf8)` 메서드를 사용하여 데이터로 변환합니다. 그리고 `JSON(data: data)`를 사용하여 SwiftyJSON 객체로 파싱합니다. 이제 `UserDefaults.standard.setValue(_:forKey:)` 메서드를 사용하여 JSON 데이터를 `user`라는 키로 UserDefaults에 저장합니다.

## 3. JSON 데이터 불러오기

이제 저장된 JSON 데이터를 불러와 확인할 수 있습니다.

```swift
import SwiftyJSON

if let dict = UserDefaults.standard.dictionary(forKey: "user") {
    let json = JSON(dict)
    
    let name = json["name"].stringValue
    let age = json["age"].intValue
    let email = json["email"].stringValue
    
    print("Name: \(name)")
    print("Age: \(age)")
    print("Email: \(email)")
}
```

위의 코드에서는 `UserDefaults.standard.dictionary(forKey:)` 메서드를 사용하여 저장된 JSON 데이터를 딕셔너리로 가져옵니다. 그리고 `JSON(dict)`를 사용하여 SwiftyJSON 객체로 변환합니다. 이제 `json["key"].stringValue`와 같은 방식으로 JSON 데이터에 접근할 수 있습니다.

이제 JSON 데이터를 UserDefaults에 저장하고 불러올 수 있는 기능을 구현할 수 있습니다. SwiftyJSON을 사용하면 JSON 데이터를 쉽게 다룰 수 있기 때문에, 복잡한 JSON 구조를 가진 데이터를 저장하고 다룰 때 유용합니다.

## 참고 자료

- [SwiftyJSON GitHub 페이지](https://github.com/SwiftyJSON/SwiftyJSON)