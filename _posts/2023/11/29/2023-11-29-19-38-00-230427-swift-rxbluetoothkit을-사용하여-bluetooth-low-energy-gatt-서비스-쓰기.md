---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 서비스 쓰기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력으로 동작하는 무선 통신 기술이며, 다양한 환경에서 사용됩니다. RxBluetoothKit은 Swift에서 BLE 기능을 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이번 글에서는 Swift RxBluetoothKit을 사용하여 BLE GATT 서비스를 쓰는 방법을 알아보겠습니다.

## 1. RxBluetoothKit 설치

먼저 프로젝트에 RxBluetoothKit을 설치해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같이 추가하고 `pod install` 명령을 실행합니다.

```swift
pod 'RxBluetoothKit', '~> 5.0'
```

## 2. GATT 서비스 쓰기

GATT(Generic Attribute Profile)는 BLE 장치 간 데이터를 교환하는 프로토콜입니다. GATT 서비스는 하나 이상의 특성(Characteristic)을 포함할 수 있습니다. 특성은 데이터를 읽고 쓰는 데 사용됩니다.

```swift
import RxBluetoothKit
import CoreBluetooth

let manager = BluetoothManager(queue: .main)
let peripheralIdentifier = UUID(uuidString: "YOUR_PERIPHERAL_IDENTIFIER")!

manager.scanForPeripherals(withServices: nil)
    .filter { $0.peripheral.identifier == peripheralIdentifier }
    .take(1)
    .flatMap { $0.peripheral.connect() }
    .flatMap { $0.discoverServices([CBUUID(string: "YOUR_SERVICE_UUID")]) }
    .flatMap { Observable.from($0) }
    .flatMap { $0.discoverCharacteristics([CBUUID(string: "YOUR_CHARACTERISTIC_UUID")]) }
    .flatMap { Observable.from($0) }
    .flatMap { characteristic -> Observable<Characteristic> in
        let data = Data("Your data to write".utf8)
        return characteristic.writeValue(data)
            .flatMap { _ in characteristic.monitorValueUpdateAndSetNotification(true) }
            .map { _ in characteristic }
    }
    .subscribe(
        onNext: { characteristic in
            print("Successfully wrote data to characteristic: \(characteristic)")
        },
        onError: { error in
            print("Error writing data to characteristic: \(error)")
        }
    )
```

위 예제는 RxBluetoothKit을 사용하여 BLE 장치를 검색하고, 연결하고, GATT 서비스와 특성을 찾은 다음 데이터를 쓰는 과정을 보여줍니다. 주요 단계는 다음과 같습니다:

1. BluetoothManager를 생성합니다.
2. `scanForPeripherals(withServices:)`를 사용하여 BLE 장치를 검색합니다.
3. 필터링된 장치를 선택하여 연결합니다.
4. `discoverServices()`를 사용하여 GATT 서비스를 검색합니다.
5. `discoverCharacteristics()`를 사용하여 특성을 찾습니다.
6. `writeValue()`를 사용하여 데이터를 쓰고, `monitorValueUpdateAndSetNotification(true)`를 호출하여 알림을 설정합니다.
7. 성공적으로 데이터를 쓴 경우 결과를 출력합니다.

## 3. 추가 자료

- [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)
- [CoreBluetooth 프레임워크 공식 문서](https://developer.apple.com/documentation/corebluetooth)

위 예제 코드는 RxBluetoothKit 5.0 버전을 기준으로 작성되었습니다. 최신 버전에 맞추어 사용하는 것을 권장합니다.