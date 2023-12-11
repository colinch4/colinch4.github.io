---
layout: post
title: "[swift] DispatchQueue qos(Quality of Service) 설정 방법"
description: " "
date: 2023-12-11
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발하다 보면 여러 가지 작업을 사용자 인터페이스와 관련 없이 백그라운드에서 실행해야 할 때가 있습니다. 이때 GCD(Grand Central Dispatch)의 DispatchQueue를 사용하여 작업을 스케줄링할 수 있습니다. 

다만, 앱 내에서 다양한 작업들이 동시에 실행되는 경우에는 어떤 작업이 우선적으로 처리되어야 하는지를 명시해야 합니다. 이때 QoS(Quality of Service)를 지정하여 각 작업에 대한 우선순위를 부여할 수 있습니다.

## QoS란 무엇인가?

QoS는 시스템 리소스의 활용을 최적화하여 서비스의 품질을 보장하는 것을 의미합니다. Apple의 GCD에서는 6가지의 QoS 클래스를 제공하며, 각 클래스는 특정한 종류의 작업에 적합하도록 정의되어 있습니다.

## QoS 클래스 종류

1. **userInteractive**: 사용자와 상호작용하고 있는 작업
2. **userInitiated**: 사용자가 시작한 작업
3. **default**: 기본적인 작업
4. **utility**: 오랫동안 실행되는 작업
5. **background**: 백그라운드에서 실행되는 작업
6. **unspecified**: QoS를 지정하지 않은 경우 기본값으로 처리됨

## DispatchQueue를 사용하여 QoS 설정하기

다음은 GCD를 사용하여 DispatchQueue에 QoS를 설정하는 방법입니다.

```swift
let queue = DispatchQueue(label: "com.example.myqueue", qos: .background)
queue.async {
    // 백그라운드에서 실행될 작업
}
```

위의 예제에서는 `background` QoS를 가진 DispatchQueue를 생성하여 백그라운드에서 실행되어야 하는 작업을 스케줄링하고 있습니다.

QoS를 지정하지 않은 경우 기본값이 적용되므로, 특정 QoS를 사용하려면 생성 시에 명시적으로 지정해주어야 합니다.

## 결론

DispatchQueue의 QoS 설정을 통해 앱 내에서 다양한 작업들에 대한 우선순위를 부여할 수 있으며, 시스템 리소스를 효율적으로 활용하여 사용자 경험을 향상시킬 수 있습니다.

더 자세한 내용은 [DispatchQueue 공식 문서](https://developer.apple.com/documentation/dispatch)를 참고하시기 바랍니다.