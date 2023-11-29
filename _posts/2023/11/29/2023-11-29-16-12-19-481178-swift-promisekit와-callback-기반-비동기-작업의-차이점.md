---
layout: post
title: "[swift] Swift PromiseKit와 Callback 기반 비동기 작업의 차이점"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

비동기 작업은 모던한 애플리케이션 개발에서 중요한 요소입니다. Swift에서 비동기 작업을 처리하기 위해 Callback 기반과 PromiseKit을 사용하는 두 가지 주요 접근 방식이 있습니다. 이 글에서는 이 두 가지 방식의 차이점을 살펴보겠습니다.

## Callback 기반 비동기 작업

Callback 기반 비동기 작업은 오래된 패턴으로, 함수 호출 시 콜백 함수를 전달하여 작업이 완료되면 호출되도록 설계됩니다. 예를 들어, 네트워크 요청을 보내고 응답을 받을 때, 콜백 함수를 등록하여 응답을 처리합니다.

```swift
func fetchData(completion: @escaping (Result<Data, Error>) -> Void) {
    // 비동기 작업 수행 후 completion 호출
    // 성공적인 경우 Result.success(data)을 전달하고, 에러가 발생한 경우 Result.failure(error)를 전달
}
```

Callback 기반 비동기 작업은 몇 가지 문제점을 가지고 있습니다. 첫째, 중첩된 콜백 함수를 사용하면 코드가 복잡해지고 가독성이 저하될 수 있습니다. 둘째, 에러 처리가 번거로워질 수 있습니다. 각 콜백 함수에서 에러를 처리해야하며, 콜백 체인이 길어질수록 에러 처리는 힘들어집니다.

## PromiseKit을 이용한 비동기 작업

PromiseKit은 Swift에서 인기있는 비동기 작업 라이브러리입니다. PromiseKit을 사용하면 비동기 작업을 Promise 객체로 감싸고, then 블록을 사용하여 비동기 작업의 결과를 다룰 수 있습니다.

```swift
func fetchData() -> Promise<Data> {
    return Promise<Data> { (resolver) in
        // 비동기 작업 수행 후 resolver.fulfill(data) 또는 resolver.reject(error)를 호출
    }
}

fetchData().done { data in
    // 비동기 작업이 성공한 경우 실행되는 코드
}.catch { error in
    // 비동기 작업 중 에러가 발생한 경우 실행되는 코드
}
```

PromiseKit은 then 블록과 catch 블록을 사용하여 비동기 작업의 결과를 처리합니다. 코드가 보다 간결하고 가독성이 높아집니다. 또한, PromiseKit은 체이닝을 통해 여러 개의 비동기 작업을 순차적으로 수행할 수 있고, 에러 처리도 간단하게 할 수 있습니다.

## 결론

Swift에서 비동기 작업을 처리하는 두 가지 주요 접근 방식인 Callback 기반과 PromiseKit을 비교해보았습니다. Callback 기반은 오래된 패턴이며 코드가 복잡해지고 가독성이 떨어질 수 있습니다. 반면, PromiseKit은 코드를 간결하고 가독성 좋게 작성할 수 있으며 체이닝과 에러 처리도 쉽게 할 수 있습니다. 따라서, PromiseKit을 사용하면 비동기 작업을 보다 효율적이고 유지보수가 용이한 방식으로 처리할 수 있습니다.

## 참고 자료
- [PromiseKit GitHub Repository](https://github.com/mxcl/PromiseKit)
- [Swift Documentation - Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html)
- [Ray Wenderlich - Getting Started with PromiseKit in Swift](https://www.raywenderlich.com/12160392-getting-started-with-promises-in-swift)