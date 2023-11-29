---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth GATT 서비스 쓰기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth GATT(Service)는 Bluetooth Low Energy(BLE) 장치 간에 데이터를 교환하기 위한 프로토콜입니다. 이 기술을 사용하기 위해서는 Swift에서 RxBluetoothKit 라이브러리를 사용할 수 있습니다. 이 블로그 포스트에서는 Swift RxBluetoothKit을 사용하여 Bluetooth GATT 서비스를 쓰는 방법에 대해 알아보겠습니다.

## RxBluetoothKit 소개

RxBluetoothKit은 Bluetooth Low Energy(BLE) 장치와 상호작용하기 위한 RxSwift 라이브러리를 사용하는 Swift용 Bluetooth 라이브러리입니다. 이 라이브러리를 사용하면 Bluetooth 장치와 통신하기 위해 Bluetooth개체를 직접 관리할 필요가 없으므로 편리하게 개발을 진행할 수 있습니다.

## Bluetooth GATT 서비스 쓰기

RxBluetoothKit을 사용하여 Bluetooth GATT(Service)를 쓰는 단계는 다음과 같습니다.

### 1. Bluetooth 중앙(central) 역할 설정

Bluetooth 중앙(central) 역할로 동작하기 위해 `centralManager`를 생성합니다. centralManager를 사용하여 Bluetooth 장치와 통신할 수 있습니다.

```swift
import RxBluetoothKit

let centralManager = CentralManager(queue: .main)
```

### 2. Peripheral 장치 스캔

Bluetooth 장치의 GATT 서비스를 찾으려면 주변(Peripheral) 장치를 스캔해야 합니다. `scanForPeripherals` 메서드를 사용하여 주변 장치를 스캔할 수 있습니다.

```swift
centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        // 주변(Peripheral) 장치를 찾았을 때 수행할 동작
        print("Found peripheral: \(scannedPeripheral)")
    })
```

### 3. 주변 장치 연결

스캔된 주변 장치를 선택하여 연결합니다. `connect` 메서드를 사용하여 주변 장치에 연결할 수 있습니다.

```swift
let targetPeripheral = ... // 연결할 주변 장치를 선택

centralManager.connect(targetPeripheral)
    .subscribe(...)
```

### 4. 주변 장치에서 GATT 서비스 찾기

연결된 주변 장치에서 GATT(Service)를 찾기 위해 `discoverServices` 메서드를 사용합니다.

```swift
centralManager
    .observeDisconnect(for: targetPeripheral)
    .take(1)
    .flatMap { _ in
        targetPeripheral.discoverServices([serviceUuid])
    }
    .subscribe(onNext: { discoveredServices in
        // GATT(Service)를 찾았을 때 수행할 동작
        print("Discovered services: \(discoveredServices)")
        // 쓰고자 하는 GATT(Service)에 대한 동작을 실행
    })
```

### 5. GATT 서비스에 쓰기

찾은 GATT(Service)에 데이터를 쓰기 위해서는 `writeValue` 메서드를 사용합니다.

```swift
let targetCharacteristic = ... // 쓰고자 하는 GATT 특성 선택
let dataToWrite = ... // 쓸 데이터 선택

centralManager
    .writeValue(dataToWrite, for: targetCharacteristic)
    .subscribe(...)
```

## 결론

Swift RxBluetoothKit을 사용하여 Bluetooth GATT(Service)를 쓰는 방법에 대해 간략히 알아보았습니다. RxBluetoothKit을 사용하면 BLE 기능을 쉽게 구현하고 Bluetooth 장치와의 통신을 간편하게 처리할 수 있습니다. 더 자세한 정보는 [RxBluetoothKit 공식 문서][1]를 참조해주세요.

[1]: https://github.com/Polidea/RxBluetoothKit