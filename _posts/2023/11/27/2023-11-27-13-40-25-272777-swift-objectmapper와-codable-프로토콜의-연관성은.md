---
layout: post
title: "[swift] Swift ObjectMapper와 Codable 프로토콜의 연관성은?"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Swift에서 객체와 JSON 데이터 간의 매핑을 도와주는 ObjectMapper와 Codable 프로토콜은 모두 데이터 모델을 처리하는 데 사용됩니다. 그러나 두 가지 접근 방식에는 몇 가지 차이점이 있습니다.

## ObjectMapper

ObjectMapper는 SwiftyJSON에 영감을 받아 개발된 라이브러리로, JSON 데이터를 Swift 객체로 변환하거나 그 반대로 변환하는 데 사용됩니다. ObjectMapper는 다음과 같은 장점을 제공합니다.

1. 유연한 매핑: ObjectMapper를 사용하면 JSON 데이터의 특정 필드를 각각의 객체 속성에 매핑시킬 수 있습니다. JSON 데이터와 객체의 속성 이름이 다르더라도 매핑이 가능합니다.
2. 커스텀 변환: ObjectMapper를 사용하면 JSON 데이터를 원하는 형식으로 변환할 수 있습니다. 예를 들어, 날짜 형식을 변환하거나, 숫자를 문자열로 변환할 수 있습니다.
3. 대규모 프로젝트 지원: ObjectMapper는 대규모 프로젝트에서도 효율적으로 사용할 수 있습니다. 객체 간의 관계를 매핑하거나 복잡한 데이터 구조를 처리하는 데 유용합니다.

## Codable 프로토콜

Codable 프로토콜은 Swift 4에서 도입된 프로토콜로, JSON 데이터와 Swift 객체 간의 변환을 간단하게 처리할 수 있습니다. Codable은 ObjectMapper보다 간단하고 직관적인 사용법을 제공합니다.

1. 자동 매핑: Codable을 사용하면 Swift 객체의 속성 이름과 JSON 데이터의 필드 이름이 서로 일치할 때 자동으로 매핑됩니다. 따로 매핑 로직을 작성할 필요가 없습니다.
2. 인코딩 및 디코딩 지원: Codable은 객체를 JSON 데이터로 인코딩하거나 JSON 데이터를 객체로 디코딩하는 데 사용될 수 있습니다. 이는 네트워크 통신에서 데이터를 주고받을 때 유용합니다.
3. Swift 표준 라이브러리 일부: Codable은 Swift 표준 라이브러리의 일부로 포함되어 있으므로, 별도의 외부 라이브러리를 설치할 필요가 없습니다.

## 결론

Swift ObjectMapper와 Codable 프로토콜은 데이터 모델과 JSON 데이터 간의 매핑을 도와주는 도구입니다. ObjectMapper는 유연하고 커스텀 변환을 쉽게 할 수 있는 장점이 있으며, 대규모 프로젝트에서의 활용에 강점을 보입니다. Codable은 간단하고 직관적인 사용법을 제공하며, Swift 표준 라이브러리에 내장되어 있어 외부 라이브러리를 추가로 설치할 필요가 없습니다. 어떤 방법을 선택하느냐는 프로젝트의 특성과 요구사항에 따라 다를 수 있습니다.

**참고 자료:**
- [Swift ObjectMapper - GitHub](https://github.com/tristanhimmelman/ObjectMapper)
- [Codable - Apple Developer Documentation](https://developer.apple.com/documentation/swift/codable)