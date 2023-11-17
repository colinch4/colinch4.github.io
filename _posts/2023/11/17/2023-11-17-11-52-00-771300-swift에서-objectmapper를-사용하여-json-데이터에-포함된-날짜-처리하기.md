---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터에 포함된 날짜 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 JSON 데이터와 Swift 객체 간의 매핑을 쉽게 처리할 수 있는 유용한 라이브러리입니다. 이러한 ObjectMapper를 사용하여 JSON 데이터에 포함된 날짜를 처리하는 방법을 알아보겠습니다.

## ObjectMapper 설치

먼저, ObjectMapper 라이브러리를 설치해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같은 항목을 추가합니다:

```swift
pod 'ObjectMapper'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

Carthage를 사용하는 경우, Cartfile에 다음과 같은 항목을 추가한 후 터미널에서 `carthage update` 명령을 실행하여 라이브러리를 설치합니다:

```swift
github "Hearst-DD/ObjectMapper"
```

## 날짜 형식 지정

JSON 데이터에 포함된 날짜를 Swift 객체에 매핑하기 전에, ObjectMapper에게 날짜 형식을 지정해야 합니다. 날짜 형식은 `DateFormatter` 클래스를 사용하여 지정할 수 있습니다.

```swift
import ObjectMapper

let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy-MM-dd"
```

위 예제에서는 "yyyy-MM-dd" 형식의 날짜를 사용하도록 지정한 것입니다. 만약 다른 형식을 사용하고 싶다면, 해당 형식에 맞게 날짜 형식 문자열을 수정하면 됩니다.

## JSON 데이터에서 날짜 추출

이제 ObjectMapper를 사용하여 JSON 데이터에서 날짜를 추출하는 방법을 알아보겠습니다. ObjectMapper는 `map` 함수를 사용하여 JSON 데이터의 특정 필드를 매핑하며, 날짜 필드를 추출할 때 `DateTransform`을 사용합니다.

```swift
import ObjectMapper

class MyObject: Mappable {
    var name: String?
    var age: Int?
    var birthDate: Date?

    required init?(map: Map) {}

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        birthDate <- (map["birth_date"], DateTransform())
    }
}
```

위의 예제에서는 `MyObject`라는 Swift 클래스를 선언하고, `Mappable` 프로토콜을 채택하여 ObjectMapper에게 매핑 정보를 전달합니다. `birthDate` 필드는 JSON 데이터의 `birth_date`에 해당되며, `DateTransform`을 사용하여 날짜로 매핑됩니다.

## 날짜를 JSON 데이터로 변환

Swift 객체에 포함된 날짜를 JSON 데이터로 변환하기 위해서는 `TransformOf`를 사용합니다. 이를 활용하여 날짜를 JSON 문자열로 변환할 수 있습니다.

```swift
import ObjectMapper

let myObject = MyObject()
myObject.name = "John"
myObject.age = 30
myObject.birthDate = Date()

let jsonString = myObject.toJSONString()

print(jsonString)
```

위의 예제에서는 `MyObject` 객체를 생성하고 필드에 값을 할당한 뒤, `toJSONString` 함수를 호출하여 JSON 문자열로 변환합니다. 변환된 JSON 문자열은 `jsonString` 상수에 저장되며, 콘솔에 출력됩니다.

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 데이터에 포함된 날짜를 처리하는 방법을 알아보았습니다. ObjectMapper의 `DateTransform`과 `TransformOf`를 적절하게 활용하면 JSON 데이터와 Swift 객체 간의 날짜 매핑을 손쉽게 처리할 수 있습니다. ObjectMapper의 공식 문서와 예제를 참고하여 더 자세한 정보를 확인할 수 있습니다.

## References

- [ObjectMapper 공식 GitHub 저장소](https://github.com/Hearst-DD/ObjectMapper)