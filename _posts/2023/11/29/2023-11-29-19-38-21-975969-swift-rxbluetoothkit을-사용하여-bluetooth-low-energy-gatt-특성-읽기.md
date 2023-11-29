---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 특성 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력 장치 간에 데이터를 전송하기 위한 무선 통신 표준입니다. Swift RxBluetoothKit은 iOS와 macOS에서 BLE 장치와 상호 작용하기 위한 간편한 인터페이스를 제공하는 라이브러리입니다. 이 블로그 포스트에서는 Swift RxBluetoothKit을 사용하여 BLE GATT (Generic Attribute Profile) 특성을 읽어오는 방법에 대해 알아보겠습니다.

## GATT 특성 읽기

BLE 장치는 하나 이상의 서비스를 제공하며, 각 서비스는 여러 GATT 특성으로 구성됩니다. GATT 특성은 장치의 속성이나 상태를 말하며, 읽기 및 쓰기 작업을 통해 사용자와 장치 간에 데이터를 교환할 수 있습니다.

RxBluetoothKit을 사용하여 GATT 특성을 읽으려면 다음 단계를 따라야 합니다.

1. `Peripheral` 객체를 생성하여 특정 BLE 장치와 연결합니다.
2. 연결된 `Peripheral` 객체에서 읽을 특성의 UUID를 사용하여 `Characteristic` 객체를 찾습니다.
3. `Characteristic` 객체의 `readValue()` 함수를 호출하여 특성의 값을 읽어옵니다.

아래는 위의 단계를 코드로 표현한 예시입니다.

```swift
import RxBluetoothKit
import CoreBluetooth

let peripheralIdentifier = UUID(uuidString: "장치의 UUID")!
let characteristicIdentifier = CBUUID(string: "특성의 UUID")

let disposeBag = DisposeBag()

_ = CentralManager.shared.scanForPeripherals(withServices: nil)
    .filter { $0.peripheral.identifier == peripheralIdentifier }
    .take(1)
    .flatMap { $0.peripheral.establishConnection() }
    .flatMap { $0.discoverServices(nil) }
    .flatMap { Observable.from($0) }
    .flatMap { $0.discoverCharacteristics(nil) }
    .flatMap { Observable.from($0) }
    .filter { $0.uuid == characteristicIdentifier }
    .flatMap { $0.readValue() }
    .subscribe(onNext: { characteristic in
        // 특성의 값을 사용하여 작업을 수행합니다.
        print("특성 값: \(characteristic.value ?? Data())")
    })
    .disposed(by: disposeBag)
```

위의 코드는 BLE 장치를 스캔하고, 연결을 설정하며, 서비스와 특성을 탐색한 후, 특정 특성의 값을 읽어옵니다. 이 때, `peripheralIdentifier`와 `characteristicIdentifier` 변수에는 읽을 장치와 특성의 UUID를 지정해야 합니다.

## 결론

Swift RxBluetoothKit을 사용하면 BLE 장치와 간편하게 상호 작용할 수 있습니다. 이 라이브러리를 사용하여 GATT 서비스와 특성을 읽고 쓰는 등의 작업을 수행할 수 있습니다. 앞으로 BLE에 대한 연결과 데이터 교환을 필요로하는 프로젝트를 진행할 때, Swift RxBluetoothKit을 고려해보세요.

## 참고 자료
- [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)
- [Apple Developer Documentation - Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)