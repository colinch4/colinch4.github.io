---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치의 알림 받기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

이 글에서는 Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy(BLE) 장치의 알림을 받는 방법에 대해 알아보겠습니다.

## 목차
1. [소개](#소개)
2. [RxBluetoothKit 설치](#RxBluetoothKit-설치)
3. [BLE 장치 스캔](#BLE-장치-스캔)
4. [BLE 디바이스 연결](#BLE-디바이스-연결)
5. [알림 필터링 및 구독](#알림-필터링-및-구독)

## 소개
Swift RxBluetoothKit은 블루투스 장치와 통신할 수 있는 라이브러리입니다. 이 라이브러리를 사용하면 BLE 장치와의 상호작용에 대한 강력한 기능을 쉽게 구현할 수 있습니다. 

## RxBluetoothKit 설치
RxBluetoothKit은 Swift Package Manager를 통해 설치할 수 있습니다. 아래의 명령어를 사용하여 프로젝트에 RxBluetoothKit을 추가합니다.

```swift
dependencies: [
    .package(url: "https://github.com/Polidea/RxBluetoothKit.git", .upToNextMajor(from: "4.2.0"))
]
```

## BLE 장치 스캔
먼저, BLE 장치를 스캔하여 사용 가능한 장치 목록을 가져와야 합니다. 아래의 코드는 RxBluetoothKit을 사용하여 BLE 장치를 스캔하는 예시입니다.

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let manager = CentralManager()
manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral.peripheral.identifier)")
    })
    .disposed(by: disposeBag)
```

## BLE 디바이스 연결
스캔된 BLE 장치 목록에서 특정 장치에 연결하려면 `connect` 메서드를 사용합니다. 아래의 코드는 특정 BLE 장치에 연결하는 예시입니다.

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let manager = CentralManager()
let targetPeripheralIdentifier = UUID(uuidString: "YourPeripheralIdentifier")!

manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        if scannedPeripheral.peripheral.identifier == targetPeripheralIdentifier {
            manager.stopScan()
            manager.connect(scannedPeripheral)
                .subscribe(onNext: { connectedPeripheral in
                    print("Connected to peripheral: \(connectedPeripheral.peripheral.identifier)")
                })
                .disposed(by: disposeBag)
        }
    })
    .disposed(by: disposeBag)
```

## 알림 필터링 및 구독
BLE 장치에서 알림을 수신하려면 해당 서비스 및 특성에 대한 알림을 활성화해야 합니다. 아래의 코드는 특정 서비스 및 특성에서 알림을 수신하는 예시입니다.

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let manager = CentralManager()
let targetPeripheralIdentifier = UUID(uuidString: "YourPeripheralIdentifier")!
let targetServiceUUID = CBUUID(string: "YourServiceUUID")
let targetCharacteristicUUID = CBUUID(string: "YourCharacteristicUUID")

manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        if scannedPeripheral.peripheral.identifier == targetPeripheralIdentifier {
            manager.stopScan()
            manager.connect(scannedPeripheral)
                .flatMap { $0.discoverServices([targetServiceUUID]) }
                .flatMap { $0[0].discoverCharacteristics([targetCharacteristicUUID]) }
                .flatMap { $0[0].setNotifyValue(true) }
                .subscribe(onNext: { characteristic in
                    print("Received notification from characteristic: \(characteristic.uuid)")
                })
                .disposed(by: disposeBag)
        }
    })
    .disposed(by: disposeBag)
```

위의 코드에서 `YourPeripheralIdentifier`, `YourServiceUUID` 및 `YourCharacteristicUUID`를 실제 값으로 대체해야 합니다.

## 결론
이렇게 Swift RxBluetoothKit을 사용하여 BLE 장치의 알림을 받는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 BLE 장치와의 상호작용을 쉽게 구현할 수 있습니다. 위의 예시 코드를 기반으로 애플리케이션에 맞게 장치와의 상호작용을 구현해보세요.

## 참고 자료
- [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)
- [RxSwift GitHub 페이지](https://github.com/ReactiveX/RxSwift)