---
layout: post
title: "[kotlin] SupervisorJob과 CoroutineExceptionHandler 사용하기"
description: " "
date: 2023-12-12
tags: [kotlin]
comments: true
share: true
---

> 본 문서에서는 Kotlin의 코루틴에서 `SupervisorJob`과 `CoroutineExceptionHandler`를 사용하여 부모 코루틴에 속한 자식 코루틴의 실패를 관리하는 방법에 대해 다룹니다.

## 1. SupervisorJob이란?

`SupervisorJob`은 부모 코루틴이 실패한 경우 자식 코루틴에게 영향을 미치지 않도록 하는 데 사용됩니다.  
일반적인 `Job`은 부모 코루틴이 실패하면 관련된 모든 자식 코루틴도 취소됩니다. 하지만 `SupervisorJob`은 부모 코루틴의 실패에도 자식 코루틴을 계속 실행할 수 있습니다.

```kotlin
val supervisorJob = SupervisorJob()
val coroutineScope = CoroutineScope(Dispatchers.Default + supervisorJob)
```

## 2. CoroutineExceptionHandler 적용하기

`CoroutineExceptionHandler`는 코루틴 내에서 발생하는 예외를 처리하기 위한 인터페이스입니다. 자식 코루틴에서 발생한 예외를 처리하고자 할 때 사용됩니다.

```kotlin
val exceptionHandler = CoroutineExceptionHandler { _, exception ->
    println("Caught $exception")
}

val job = coroutineScope.launch(exceptionHandler) {
    // 예외가 발생할 수 있는 작업 수행
}
```

## 3. SupervisorJob과 CoroutineExceptionHandler 함께 사용하기

`SupervisorJob`과 `CoroutineExceptionHandler`를 함께 사용하여 부모 코루틴과 관련된 자식 코루틴에서 발생하는 예외를 처리할 수 있습니다.

```kotlin
val supervisorJob = SupervisorJob()
val coroutineScope = CoroutineScope(Dispatchers.Default + supervisorJob)
val exceptionHandler = CoroutineExceptionHandler { _, exception ->
    println("Caught $exception")
}

val job = coroutineScope.launch(exceptionHandler) {
    // 예외가 발생할 수 있는 작업 수행
}
```

위와 같이 `SupervisorJob`과 `CoroutineExceptionHandler`를 함께 사용하면 부모 코루틴이 실패하더라도 자식 코루틴이 멈추지 않고 계속 실행될 수 있습니다.

## 4. 결론

코루틴에서 `SupervisorJob`과 `CoroutineExceptionHandler`를 사용하면 부모 코루틴의 실패에도 자식 코루틴을 안전하게 관리할 수 있습니다.  
`SupervisorJob`은 부모 코루틴을 실패해도 자식 코루틴이 영향을 받지 않도록 하고, `CoroutineExceptionHandler`은 자식 코루틴에서 발생한 예외를 적절히 처리할 수 있도록 도와줍니다.

이렇게 함께 사용하여 안정적인 코루틴 기반 애플리케이션을 구축할 수 있습니다.

---
참고 자료:
- [Kotlin Coroutine Exception Handling](https://kotlinlang.org/docs/exception-handling.html#handling-exceptions-in-coroutines)