---
layout: post
title: "[swift] Swift PromiseKit와 Combine 프레임워크의 비교"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Swift 개발자들은 비동기 프로그래밍을 위해 다양한 프레임워크를 사용합니다. 그 중에서도 PromiseKit와 Combine은 많이 사용되고 있습니다. 이 두 프레임워크는 각각의 장단점을 가지고 있으며, 이번 블로그 포스트에서는 Swift PromiseKit와 Combine을 비교해보도록 하겠습니다.

## PromiseKit

PromiseKit은 비동기 코드를 작성하기 위한 프로미스 기반 라이브러리입니다. PromiseKit은 chaining, error handling, cancellation 등의 기능을 제공하여 비동기 작업을 더 쉽게 관리할 수 있도록 도와줍니다. PromiseKit은 Objective-C와 Swift 모두에서 사용할 수 있으며, Cocoa, Cocoa Touch, Swift Package Manager와 같은 여러 플랫폼에서 사용할 수 있습니다.

PromiseKit의 사용법은 간단하고 직관적입니다. 아래는 PromiseKit을 사용하여 비동기 작업을 처리하는 예제 코드입니다.

```swift
func downloadData() -> Promise<Data> {
    return Promise { seal in
        // 비동기 작업
        URLSession.shared.dataTask(with: url) { data, _, error in
            if let error = error {
                seal.reject(error)
            } else if let data = data {
                seal.fulfill(data)
            }
        }.resume()
    }
}

downloadData().done { data in
    // 데이터 다운로드 성공
}.catch { error in
    // 데이터 다운로드 실패
}
```

PromiseKit에서는 `.done`과 `.catch`와 같은 메서드를 사용하여 성공과 실패에 대한 핸들러를 지정할 수 있습니다.

## Combine

Swift 5 부터 도입된 Combine은 비동기 및 동기 이벤트 스트리밍을 위한 프레임워크입니다. Combine은 함수형 및 리액티브 프로그래밍 패러다임에 기반을 두고 있으며, Swift의 기능을 최대한 활용하면서 선언적인 코드를 작성할 수 있도록 지원합니다. Combine은 다른 프레임워크와 함께 사용하거나 단독으로 사용할 수 있으며, Apple의 주요 프레임워크에 내장되어 있습니다.

Combine을 사용하기 위해서는 `Publisher`와 `Subscriber`를 이해해야 합니다. Publisher는 이벤트 스트림을 생성하고, Subscriber는 해당 스트림을 구독하여 이벤트를 처리하는 역할을 합니다. 아래는 Combine을 사용하여 비동기 작업을 처리하는 예제 코드입니다.

```swift
func downloadData() -> AnyPublisher<Data, Error> {
    return URLSession.shared.dataTaskPublisher(for: url)
        .map { $0.data }
        .eraseToAnyPublisher()
}

downloadData()
    .sink(receiveCompletion: { completion in
        // 비동기 작업 완료
    }, receiveValue: { data in
        // 데이터 다운로드 성공
    })
```

Combine에서는 `sink` 메서드를 사용하여 값을 구독하고, `receiveCompletion`과 `receiveValue` 클로저를 통해 작업의 성공과 실패를 처리할 수 있습니다.

## 결론

Swift PromiseKit와 Combine은 모두 비동기 코드를 처리하기 위한 강력한 도구입니다. PromiseKit은 더 오래된 프레임워크이며 단순성과 직관성을 갖고 있습니다. 반면 Combine은 Swift 5에서 새롭게 도입된 프레임워크로서 함수형 및 리액티브 프로그래밍에 기반을 둔 선언적인 코드 작성을 지원합니다.

어떤 프레임워크를 선택할지는 개발자의 선호도와 프로젝트의 요구사항에 따라 다를 수 있습니다. 따라서 일반적으로는 각 프레임워크의 문서를 참고하고, 예제 코드를 작성해보는 것이 도움이 될 것입니다.

- [PromiseKit 공식 홈페이지](https://github.com/mxcl/PromiseKit)
- [Combine 공식 홈페이지](https://developer.apple.com/documentation/combine)

참고: 예제 코드에서 사용된 URL 변수와 관련 메서드는 생략되었습니다. 실제 코드에서는 적절한 값을 사용하여야 합니다.