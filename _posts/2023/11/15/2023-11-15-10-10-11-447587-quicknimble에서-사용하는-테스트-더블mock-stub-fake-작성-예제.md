---
layout: post
title: "[swift] Quick/Nimble에서 사용하는 테스트 더블(Mock, Stub, Fake) 작성 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 포스트에서는 Swift 프로젝트에서 테스트 더블을 작성하는 방법을 설명하겠습니다. 테스트 더블은 테스트 환경에서 실제 객체를 대체하여 모의(Mock), 가짜(Fake), 무언가를 반환하는 행위(Stub)를 수행하는 객체입니다. 이를 통해 의존성을 분리하고 테스트의 격리성을 유지할 수 있습니다.

## Quick/Nimble 소개

Quick은 BDD(Behavior-Driven Development) 프레임워크로, Nimble은 Quick에 통합된 매처(matcher) 라이브러리입니다. Quick는 테스트 코드를 작성할 때 선언적인 언어를 제공하여 가독성을 높이고, Nimble은 쉽게 테스트를 검증할 수 있는 강력한 도구입니다. 이 두 라이브러리를 사용하여 테스트 더블을 작성해보겠습니다.

## Mock 작성 예제

Mock은 다른 객체와의 상호작용을 검증하기 위해 사용됩니다. 아래는 Mock 객체의 작성 방법을 보여주는 예제입니다.

```swift
protocol NetworkManagerProtocol {
    func fetchData(completion: @escaping (Result<Data, Error>) -> Void)
}

class MockNetworkManager: NetworkManagerProtocol {
    var fetchDataCalled = false

    func fetchData(completion: @escaping (Result<Data, Error>) -> Void) {
        fetchDataCalled = true
        // 데이터 반환 또는 에러 처리 등을 수행
    }
}
```

위 예제에서 `NetworkManagerProtocol`은 네트워크 작업을 수행하는 `fetchData` 메서드를 가진 프로토콜입니다. `MockNetworkManager` 클래스는 이 프로토콜을 구현하여 `fetchDataCalled` 프로퍼티를 사용하여 메서드 호출 여부를 검증할 수 있습니다.

## Stub 작성 예제

Stub은 특정 동작을 가진 객체를 대체하여 테스트에서 사용됩니다. 아래는 Stub 객체의 작성 방법을 보여주는 예제입니다.

```swift
protocol DatabaseManagerProtocol {
    func save(data: Data)
    func fetchData() -> Data?
}

class StubDatabaseManager: DatabaseManagerProtocol {
    private var savedData: Data?

    func save(data: Data) {
        savedData = data
    }

    func fetchData() -> Data? {
        return savedData
    }
}
```

위 예제에서 `DatabaseManagerProtocol` 프로토콜은 데이터베이스 작업을 수행하는 `save`와 `fetchData` 메서드를 가지고 있습니다. `StubDatabaseManager` 클래스는 이 프로토콜을 구현하여 `savedData` 프로퍼티를 사용하여 데이터 저장 및 반환을 수행합니다.

## Fake 작성 예제

Fake는 실제 객체와 비슷한 동작을 가지면서 테스트에 특화된 구현을 제공하는 객체입니다. 아래는 Fake 객체의 작성 방법을 보여주는 예제입니다.

```swift
protocol CacheManagerProtocol {
    func save(data: Data, forKey key: String)
    func fetchData(forKey key: String) -> Data?
}

class FakeCacheManager: CacheManagerProtocol {
    private var cache: [String: Data] = [:]

    func save(data: Data, forKey key: String) {
        cache[key] = data
    }

    func fetchData(forKey key: String) -> Data? {
        return cache[key]
    }
}
```

위 예제에서 `CacheManagerProtocol` 프로토콜은 데이터를 캐시에 저장하고 가져오는 `save`와 `fetchData` 메서드를 가지고 있습니다. `FakeCacheManager` 클래스는 이 프로토콜을 구현하여 `cache` 프로퍼티를 사용하여 데이터를 캐시에 저장하고 반환합니다.

## 결론

이 포스트에서는 Swift 프로젝트에서 Quick/Nimble을 사용하여 테스트 더블을 작성하는 예제를 살펴보았습니다. Mock, Stub, Fake을 사용하여 객체의 상호작용 검증 및 동작 대체를 수행할 수 있습니다. 이를 통해 테스트의 격리성을 유지하고 코드의 신뢰성을 높일 수 있습니다.

> 참고:
> - [Quick](https://github.com/Quick/Quick)
> - [Nimble](https://github.com/Quick/Nimble)