---
layout: post
title: "[swift] DispatchGroup과 DispatchSemaphore 활용하기"
description: " "
date: 2023-12-18
tags: [swift]
comments: true
share: true
---

DispatchGroup과 DispatchSemaphore는 iOS 및 macOS 앱을 개발할 때 비동기적으로 작업을 관리하고 제어하는 데 유용한 기능들입니다. DispatchGroup은 여러 개의 비동기 작업이 완료될 때까지 기다리는 데 사용하고, DispatchSemaphore는 병렬 작업의 개수 제어에 활용됩니다.

## DispatchGroup 사용하기

DispatchGroup은 여러 개의 비동기 작업이 완료될 때까지 기다릴 수 있는 그룹을 만들 수 있습니다. 이를 통해 앱이 모든 비동기 작업이 완료될 때까지 기다리고 특정 동작을 수행할 수 있습니다.

다음은 DispatchGroup을 사용하여 비동기 작업을 수행하는 간단한 예제입니다.

```swift
let group = DispatchGroup()

group.enter()
// 비동기 작업 1 수행
task1 {
    group.leave()
}

group.enter()
// 비동기 작업 2 수행
task2 {
    group.leave()
}

group.notify(queue: .main) {
    // 모든 비동기 작업이 완료되면 수행할 작업
    print("모든 작업 완료")
}
```

위 코드에서 `enter()`로 그룹에 진입을 표시하고, 비동기 작업이 완료되면 `leave()`로 그룹을 떠나게 합니다. `notify(queue:execute)`를 사용하여 모든 작업이 완료되면 특정 동작을 수행할 수 있습니다.

## DispatchSemaphore 사용하기

DispatchSemaphore는 특정 작업의 최대 병렬 실행 횟수를 제어하는 데에 사용됩니다. 특정 개수 이상의 작업이 동시에 실행되지 않도록 제어할 수 있어서, 자원을 효율적으로 활용할 수 있습니다.

다음은 DispatchSemaphore를 사용하여 최대 병렬 실행 횟수를 3회로 제한하는 예제입니다.

```swift
let semaphore = DispatchSemaphore(value: 3)
let queue = DispatchQueue.global()

for _ in 0..<10 {
    queue.async {
        semaphore.wait()
        // 실행할 작업
        doWork {
            semaphore.signal()
        }
    }
}
```

위 코드에서 `DispatchSemaphore`를 이용하여 세마포어를 초기화하고, `wait()`로 세마포어 값이 0일 때 대기하고, 작업이 끝나면 `signal()`로 세마포어 값을 증가시킵니다.

DispatchGroup과 DispatchSemaphore는 병렬 처리를 제어하고 관리하기 위한 유용한 도구로, 스레드의 안전성을 유지하고 병렬 작업을 효과적으로 관리하는 데에 활용됩니다.

참고문헌:

- [DispatchGroup - Apple Developer Documentation](https://developer.apple.com/documentation/dispatch/dispatchgroup)
- [DispatchSemaphore - Apple Developer Documentation](https://developer.apple.com/documentation/dispatch/dispatchsemaphore)