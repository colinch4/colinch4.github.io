---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth GATT 특성 알림 받기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift 프로그래밍 언어와 RxBluetoothKit 라이브러리를 사용하여 Bluetooth GATT 특성 알림을 받는 방법에 대해서 알아보겠습니다.

## RxBluetoothKit 소개

RxBluetoothKit은 iOS 및 macOS에서 Bluetooth Low Energy(BLE) 장치와 상호작용하기 위한 우수한 라이브러리입니다. 이 라이브러리는 RxSwift를 기반으로 하며, BLE 장치의 검색, 연결, 서비스 및 특성 읽기/쓰기, 알림(subscription) 등의 작업을 간편하게 수행할 수 있게 도와줍니다.

## 알림 구독하기

GATT(General Attribute) 프로토콜을 사용하는 BLE 장치에서 알림을 받기 위해서는 해당 특성을 "구독"해야 합니다. 이를 위해 RxBluetoothKit의 `Peripheral` 클래스의 `observeValueUpdateAndSetNotification(for:onRawValueUpdate:notificationState:withFilter:isInitial:` 메서드를 사용할 수 있습니다.

```swift
import RxSwift
import CoreBluetooth
import RxBluetoothKit

let manager = CentralManager()
let peripheral: Peripheral = ... // 연결된 BLE 장치

// 특성 구독
peripheral.observeValueUpdateAndSetNotification(for: characteristic, onRawValueUpdate: { (characteristic, error) in
    if let error = error {
        // 에러 처리
        return
    }

    // 특성의 값을 읽어옴
    let value = characteristic.value
    // 값 처리
}).subscribe(onNext: { (notificationState) in
    if notificationState.notification { 
        // 알림 구독 성공
    } else { 
        // 알림 구독 취소됨
    }
}).disposed(by: disposeBag)
```

위의 코드에서 `observeValueUpdateAndSetNotification(for:onRawValueUpdate:notificationState:withFilter:isInitial:` 메서드는 다음과 같은 인자를 받습니다:

- `characteristic`: 구독할 특성 객체
- `onRawValueUpdate`: 특성 값이 업데이트될 때 호출되는 클로저
- `notificationState`: 알림 상태에 대한 정보를 전달하는 옵저버블
- `withFilter`: 필터링을 위한 조건을 설정하는 클로저 (optional)
- `isInitial`: 초기 구독인지 여부를 설정하는 Bool 값 (optional)

알림 구독 성공 시 `notificationState.notification` 값은 true로 설정되며, 알림 구독 취소 시 false로 설정됩니다.

## 요약

이렇게 Swift RxBluetoothKit을 사용하여 Bluetooth GATT 특성 알림을 받는 방법에 대해 알아보았습니다. RxBluetoothKit은 강력한 기능과 편리한 인터페이스를 제공하여 BLE 장치와의 상호작용을 쉽게 구현할 수 있게 도와줍니다. 더 자세한 내용은 [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)를 참고하시기 바랍니다.