---
layout: post
title: "[swift] Swift PromiseKit에서 사용되는 용어 설명 (ex. Promise, Resolver, Then, Catch 등)"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

PromiseKit은 Swift에서 비동기 작업을 처리하기 위한 강력한 라이브러리입니다. PromiseKit을 사용하면 비동기 작업에 대한 결과를 쉽게 처리할 수 있습니다. 이번 포스트에서는 PromiseKit에서 사용되는 주요 용어들을 설명하겠습니다.

## Promise

**Promise**은 비동기 작업의 결과를 나타내는 객체입니다. Promise는 비동기 작업이 완료되면 resolve되고, 실패하면 reject됩니다. Promise는 일반적으로 다음과 같은 형태로 사용됩니다.

```swift
func performAsyncTask() -> Promise<String> {
    return Promise { (resolve, reject) in
        // 비동기 작업 수행
        // 작업이 완료되면 resolve를 호출하여 성공 결과를 전달
        // 작업이 실패하면 reject를 호출하여 실패 결과를 전달
    }
}
```

## Resolver

**Resolver**는 Promise를 사용하여 비동기 작업의 결과를 전달하는 객체입니다. 비동기 작업이 완료되면 Resolver를 사용하여 결과를 전달하게 됩니다. 예를 들어, Promise의 resolve 메소드를 호출하여 성공적인 결과를 전달하거나 reject 메소드를 호출하여 실패 결과를 전달할 수 있습니다.

```swift
func performAsyncTask() -> Promise<String> {
    return Promise { (resolve, reject) in
        // 비동기 작업 수행
        if success {
            resolve("작업 성공")
        } else {
            reject(MyError.error)
        }
    }
}
```

## Then

**Then**은 Promise 객체에서 성공적으로 resolve된 경우 실행되는 메소드입니다. Then 메소드를 사용하여 이전 Promise의 결과를 받아와 추가적인 작업을 수행할 수 있습니다.

```swift
performAsyncTask().then { result in
    // 이전 Promise의 결과를 이용하여 추가 작업 수행
}.catch { error in
    // Promise가 reject된 경우 처리
}
```

## Catch

**Catch**는 Promise에서 발생한 오류를 처리하는 메소드입니다. Promise에서 reject된 경우에만 실행되며, catch 메소드를 사용하여 오류를 처리할 수 있습니다.

```swift
performAsyncTask().catch { error in
    // Promise가 reject된 경우 처리
}
```

위에서 설명한 PromiseKit의 용어들은 비동기 작업을 쉽게 처리하기 위해 사용되는 중요한 개념들입니다. 이해하기 쉬운 코드를 작성하고 유지 보수하기 쉬운 애플리케이션을 개발하기 위해 PromiseKit을 적극적으로 활용해보세요.

## 참고 자료
- [PromiseKit Documentation](https://github.com/mxcl/PromiseKit/blob/master/Documentation/GettingStarted.md)