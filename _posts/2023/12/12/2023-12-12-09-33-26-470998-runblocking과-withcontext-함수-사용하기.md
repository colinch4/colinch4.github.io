---
layout: post
title: "[kotlin] runBlocking과 withContext 함수 사용하기"
description: " "
date: 2023-12-12
tags: [kotlin]
comments: true
share: true
---

Kotlin은 동시성 프로그래밍을 쉽게 처리할 수 있는 많은 기능을 제공합니다. 두 가지 중요한 함수인 `runBlocking`과 `withContext`를 사용하여 동시성을 다루는 방법을 살펴보겠습니다.

## 1. `runBlocking` 함수

`runBlocking` 함수는 코루틴을 실행하는 데 사용됩니다. 이 함수를 사용하면 메인 스레드를 블록하지 않고도 코루틴을 실행할 수 있습니다. 주로 테스트 코드나 코루틴을 호출하는 최상위 레벨 함수에서 사용됩니다.

아래는 `runBlocking` 함수를 사용하여 간단한 코루틴을 실행하는 예제입니다.

```kotlin
import kotlinx.coroutines.*

fun main() {
    runBlocking {
        launch {
            delay(1000L)
            println("World!")
        }
        println("Hello,")
    }
}
```

## 2. `withContext` 함수

`withContext` 함수는 다른 디스패처에서 코루틴을 실행할 때 사용됩니다. 디스패처는 스레드 풀이나 스레드들의 묶음으로, 코루틴이 실행되는 컨텍스트를 정의합니다.

아래는 `withContext` 함수를 사용하여 백그라운드 스레드에서 작업을 수행하는 예제입니다.

```kotlin
import kotlinx.coroutines.*

suspend fun main() = withContext(Dispatchers.Default) {
    // 백그라운드 스레드에서 작업을 수행
    println("This is executed in the background")
}
```

`withContext` 함수를 호출하면 지정된 디스패처에서 코루틴이 실행되며, 해당 블록 내에서 실행되는 모든 코루틴도 지정된 디스패처에서 실행됩니다.

위 방법들을 사용하여 Kotlin에서 동시성을 다루는 방법을 살펴보았습니다. 이러한 함수들을 사용하면 간단하고 효율적으로 코루틴을 다룰 수 있습니다.

참고:
- [Kotlin Coroutines Guide](https://kotlinlang.org/docs/coroutines-guide.html)
- [Kotlin withContext Documentation](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/with-context.html)
- [Kotlin runBlocking Documentation](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html)