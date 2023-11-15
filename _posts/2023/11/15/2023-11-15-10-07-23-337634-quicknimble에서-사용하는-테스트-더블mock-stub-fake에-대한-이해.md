---
layout: post
title: "[swift] Quick/Nimble에서 사용하는 테스트 더블(Mock, Stub, Fake)에 대한 이해"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

## 소개

테스트 더블(Test Double)은 소프트웨어 테스트에서 실제 객체를 대신하는 객체입니다. 이러한 테스트 더블은 테스트 시나리오를 조작하고 의존성을 격리하여 테스트의 신뢰성을 높이는 데 도움이 됩니다. Quick과 Nimble은 Swift에서 유닛 테스트를 작성하기 위한 인기있는 프레임워크인데, 이들 프레임워크는 다양한 테스트 더블을 생성하는 기능을 제공합니다.

## Mock

모킹(Mocking)은 테스트 더블 중 하나로, 메서드 호출 및 속성 변경을 기록하고 확인하는 기능을 가지고 있습니다. 테스트에서 실제 객체의 동작을 시뮬레이션하고 그 결과를 확인함으로써 테스트의 검증을 용이하게 합니다.

```swift
protocol NetworkService {
    func fetchData(completion: @escaping (Result<[String], Error>) -> Void)
}

class MockNetworkService: NetworkService {
    var fetchDataCalled = false
    
    func fetchData(completion: @escaping (Result<[String], Error>) -> Void) {
        fetchDataCalled = true
        // test-specific behavior
        let data = ["item1", "item2", "item3"]
        completion(.success(data))
    }
}

// Usage
func testFetchData() {
    let mockNetworkService = MockNetworkService()
    // 테스트 대상 객체에 mockNetworkService를 주입
    let sut = MyObject(networkService: mockNetworkService)

    sut.doSomething()
    
    // fetchData 메서드가 호출되었는지 확인
    expect(mockNetworkService.fetchDataCalled).to(beTrue())
}
```

## Stub

스털링(Stubbing)은 실제 메서드의 반환 값을 가로채서 특정 값을 반환하도록 하는 것을 말합니다. 스텁 구현을 사용하면 의존성 객체의 특정 동작을 가짜 값으로 대체하여 테스트의 특정 시나리오를 시뮬레이션할 수 있습니다.

```swift
// MyObject에서 사용하는 NetworkService 프로토콜
protocol NetworkService {
    func fetchData(completion: @escaping (Result<[String], Error>) -> Void)
}

class StubNetworkService: NetworkService {
    func fetchData(completion: @escaping (Result<[String], Error>) -> Void) {
        // test-specific behavior
        let data = ["stubbed item1", "stubbed item2", "stubbed item3"]
        completion(.success(data))
    }
}

// Usage
func testFetchData() {
    let stubNetworkService = StubNetworkService()
    // 테스트 대상 객체에 stubNetworkService를 주입
    let sut = MyObject(networkService: stubNetworkService)

    sut.doSomething()
    
    // 기대하는 데이터가 반환되는지 확인
    let expectedData = ["stubbed item1", "stubbed item2", "stubbed item3"]
    expect(sut.data).to(equal(expectedData))
}
```

## Fake

페이크(Fake)는 실제 시스템과 유사한 동작을 가지는 구현체입니다. 실제로 데이터를 저장하거나 외부 리소스에 액세스하는 등의 동작을 수행합니다. 페이크 객체를 사용하면 실제 환경을 모방하여 통합 테스트를 수행할 수 있습니다.

```swift
class FakeNetworkService: NetworkService {
    var data: [String] = []
    
    func fetchData(completion: @escaping (Result<[String], Error>) -> Void) {
        // 실제 데이터를 가져와서 저장
        data = fetchRealData()
        completion(.success(data))
    }
}

// Usage
func testFetchData() {
    let fakeNetworkService = FakeNetworkService()
    // 테스트 대상 객체에 fakeNetworkService를 주입
    let sut = MyObject(networkService: fakeNetworkService)

    sut.doSomething()
    
    // 실제 데이터가 저장되는지 확인
    expect(fakeNetworkService.data).toNot(beEmpty())
}
```

## 결론

테스트 더블을 사용하면 테스트의 격리성을 유지하고 특정 시나리오를 테스트할 수 있습니다. Quick과 Nimble은 Mock, Stub, Fake를 쉽게 생성하고 사용할 수 있도록 기능을 제공하므로 테스트 코드 작성 시 이러한 기능을 적극 활용하면 유닛 테스트의 품질을 높일 수 있습니다.

---

## 참고 자료

- [Quick](https://github.com/Quick/Quick)
- [Nimble](https://github.com/Quick/Nimble)
- [Martin Fowler's article - Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
- [Fake Objects - Martin Fowler](https://martinfowler.com/bliki/FakeObject.html)
- [Unit Testing with Quick & Nimble in Swift](https://roadfiresoftware.com/2018/02/unit-testing-with-quick-nimble-in-swift/)