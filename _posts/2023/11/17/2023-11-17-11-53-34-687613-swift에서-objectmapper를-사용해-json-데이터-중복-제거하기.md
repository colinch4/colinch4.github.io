---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용해 JSON 데이터 중복 제거하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

JSON 데이터는 자주 사용되는 데이터 형식이며, 종종 중복된 데이터를 포함할 수 있습니다. 중복된 데이터를 제거하여 데이터 크기를 줄이고 처리 속도를 향상시킬 수 있습니다. 이번 블로그에서는 Swift에서 ObjectMapper를 사용하여 JSON 데이터에서 중복된 값을 제거하는 방법에 대해 알아보겠습니다.

## ObjectMapper 소개

ObjectMapper는 Swift에서 가장 인기있는 JSON 매핑 라이브러리 중 하나입니다. ObjectMapper를 사용하면 JSON 데이터를 Swift 객체로 매핑하거나, Swift 객체를 JSON 데이터로 변환할 수 있습니다. ObjectMapper는 이러한 기능 외에도 다양한 유틸리티 메서드를 제공하여 JSON 데이터를 간편하게 다룰 수 있도록 도와줍니다.

## JSON 데이터에서 중복 제거하기

JSON 데이터에서 중복된 값을 제거하기 위해 ObjectMapper의 `distinctUnionOfObjects` 메서드를 사용할 수 있습니다. 이 메서드는 배열의 요소를 고유한 값으로만 구성된 배열로 변환해주는 역할을 합니다.

다음은 ObjectMapper를 사용하여 JSON 데이터에서 중복된 값을 제거하는 예제 코드입니다.

```swift
import ObjectMapper

// 중복된 값을 제거할 JSON 데이터
let json = """
{
    "fruits": ["apple", "banana", "apple", "orange", "banana"]
}
"""

// ObjectMapper를 사용하여 JSON 데이터를 매핑
if let jsonObject = Mapper<Dictionary<String, Any>>().map(JSONString: json) {
    if let fruits = jsonObject["fruits"] as? [String] {
        let uniqueFruits = Array(Set(fruits))
        print(uniqueFruits)
    }
}
```

위의 코드에서는 `json` 변수에 중복된 값을 포함한 JSON 데이터를 할당하고, ObjectMapper를 사용하여 JSON 데이터를 매핑합니다. 그리고 `fruits` 키에 해당하는 값인 배열에서 `Set`을 사용하여 중복된 값을 제거하고, 다시 배열로 변환하여 출력합니다.

실행 결과는 다음과 같이 나타납니다.

```
["banana", "orange", "apple"]
```

위에서 사용된 `Set`은 Swift의 Set 자료구조를 나타냅니다. Set은 순서와 상관없이 유일한 값을 저장하는 컬렉션 타입으로, 중복된 값을 제거하는데 매우 유용합니다.

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 데이터에서 중복된 값을 제거하는 방법을 알아보았습니다. ObjectMapper의 `distinctUnionOfObjects` 메서드를 활용하면 중복된 값을 간단하게 제거할 수 있습니다. 이를 통해 데이터 크기를 줄이고 처리 속도를 향상시킬 수 있습니다.