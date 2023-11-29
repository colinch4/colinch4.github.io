---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth GATT 특성 쓰기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth GATT (Generic Attribute Profile)는 Bluetooth로 연결된 장치 간의 통신을 위한 프로토콜입니다. Swift에서 RxBluetoothKit 라이브러리를 사용하면 Bluetooth GATT 특성을 읽고 쓰는 작업을 간단하게 수행할 수 있습니다.

## RxBluetoothKit 설치하기

먼저 RxBluetoothKit을 프로젝트에 설치해야 합니다. `Podfile`에 다음과 같이 추가하고, 터미널에서 `pod install` 명령어를 실행하세요.

```swift
pod 'RxBluetoothKit'
```

## Bluetooth GATT 특성 쓰기

RxBluetoothKit은 Bluetooth GATT 서비스 및 특성에 대한 추상화 계층을 제공하여 개발자가 쉽게 사용할 수 있도록 합니다. 다음은 RxBluetoothKit을 사용하여 Bluetooth GATT 특성을 쓰는 예제 코드입니다.

```swift
import RxSwift
import CoreBluetooth
import RxBluetoothKit

// 사용할 서비스 UUID와 특성 UUID
let serviceUUID = CBUUID(string: "1234")
let characteristicUUID = CBUUID(string: "5678")

// 중앙 매니저 생성
let centralManager = CentralManager(queue: .main)

// 연결된 페리피럴에서 특성 쓰기
let disposable = centralManager
    .connect(peripheral)
    .flatMap { _ in
        peripheral.writeValue(data, for: characteristic, type: .withResponse)
    }
    .subscribe(onNext: { characteristic in
        // 특성 쓰기 성공
        print("Characteristic write success")
    }, onError: { error in
        // 특성 쓰기 실패
        print("Characteristic write error: \(error.localizedDescription)")
    })

// DisposeBag에 disposable 추가
disposeBag.insert(disposable)
```

위 코드에서 `serviceUUID`는 GATT 서비스의 UUID, `characteristicUUID`는 GATT 특성의 UUID입니다.

`CentralManager`를 사용하여 중앙 매니저를 생성하고, `peripheral`에 연결합니다. 그 후 `writeValue(data: Data, for: CBMutableCharacteristic, type: CBCharacteristicWriteType)` 메서드를 통해 특성에 값(Data)를 쓸 수 있습니다. 값 쓰기가 성공하면 `onNext` 클로저가 호출되고, 실패할 경우 `onError` 클로저가 호출됩니다.

위 코드는 RxSwift를 사용하므로 적절한 DisposeBag를 사용하여 disposable을 관리하는 것이 좋습니다.

## 마무리

이번 포스트에서는 Swift에서 RxBluetoothKit을 사용하여 Bluetooth GATT 특성을 쓰는 방법을 알아보았습니다. RxBluetoothKit을 이용하면 Bluetooth GATT 특성을 간편하게 쓰고 관리할 수 있으므로, Bluetooth 기능을 활용한 앱을 개발할 때 유용하게 사용할 수 있습니다.

## 참고 자료

- [RxBluetoothKit GitHub Repository](https://github.com/Polidea/RxBluetoothKit)
- [Core Bluetooth - Apple Developer Documentation](https://developer.apple.com/documentation/corebluetooth)
- [Bluetooth GATT - Bluetooth Developer Portal](https://developer.bluetooth.org/technology-specific-pages/gatt)

[swift]: /swift