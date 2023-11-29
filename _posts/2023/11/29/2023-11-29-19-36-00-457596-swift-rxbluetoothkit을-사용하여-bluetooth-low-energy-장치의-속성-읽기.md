---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치의 속성 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy(BLE)는 저전력 무선 기술로, 스마트 폰과 다양한 주변 장치 간에 데이터를 교환하는 데 사용됩니다. Swift RxBluetoothKit은 Swift에서 Bluetooth 기기와 상호 작용하기 위한 간편한 방법을 제공하는 라이브러리입니다. 이번 포스트에서는 Swift RxBluetoothKit을 사용하여 BLE 장치의 속성을 읽는 방법에 대해 알아보겠습니다.

## 1. RxBluetoothKit 설치

먼저, RxBluetoothKit을 설치해야 합니다. Swift Package Manager를 사용하는 경우, 프로젝트의 `Package.swift` 파일에 다음과 같은 의존성을 추가합니다:

```swift
dependencies: [
    .package(url: "https://github.com/Polidea/RxBluetoothKit.git", from: "3.4.0")
]
```

CocoaPods를 사용하는 경우, `Podfile`에 다음 라인을 추가한 후 `pod install` 명령을 실행합니다:

```ruby
pod 'RxBluetoothKit', '~> 3.4'
```

RxBluetoothKit을 통해 BLE 기능을 사용할 준비가 되었으니, 이제 속성을 읽어보겠습니다.

## 2. BLE 장치 속성 읽기

BLE 장치의 속성 읽기는 다음의 단계로 수행됩니다:

### 2.1. CentralManager 초기화

```swift
import RxBluetoothKit

let disposeBag = DisposeBag()

let centralManager = CentralManager(queue: .main)
```

### 2.2. BLE 장치 검색

```swift
centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral)")
    })
    .disposed(by: disposeBag)
```

위의 코드는 BLE 장치 검색을 시작하고, 검색된 각 장치에 대한 정보를 출력합니다.

### 2.3. 연결

```swift
let peripheralId = UUID(uuidString: "12345678-1234-1234-1234567890AB")!
let connectionTimeout = DispatchTimeInterval.seconds(5)

centralManager.connect(peripheralId, timeout: connectionTimeout)
    .subscribe(onNext: { peripheral in
        print("Connected to peripheral: \(peripheral)")
    }, onError: { error in
        print("Connection error: \(error)")
    })
    .disposed(by: disposeBag)
```

위의 코드는 specific한 peripheralId를 사용하여 BLE 장치에 연결합니다.

### 2.4. 속성 읽기

```swift
let characteristicUUID = CBUUID(string: "FFE1")
let timeout = DispatchTimeInterval.seconds(3)

peripheral.discoverServices(nil)
    .flatMap { services -> Observable<[Characteristic]> in
        let service = services.first!
        return service.discoverCharacteristics([characteristicUUID])
    }
    .flatMap { characteristics -> Observable<Characteristic> in
        let characteristic = characteristics.first!
        return characteristic.readValue().map { _ in characteristic }
    }
    .subscribe(onNext: { characteristic in
        print("Read characteristic value: \(characteristic)")
    }, onError: { error in
        print("Read characteristic error: \(error)")
    })
    .disposed(by: disposeBag)
```

위의 코드는 BLE 장치에서 특정한 characteristicUUID에 대한 속성 값을 읽어옵니다.

이제 위의 코드를 기반으로 자신의 BLE 장치에서 원하는 속성 값을 읽을 수 있습니다.

## 결론

Swift RxBluetoothKit은 BLE 기기와의 상호 작용을 편리하게 처리할 수 있는 강력한 도구입니다. 이번 포스트에서는 BLE 장치의 속성을 읽어오는 방법을 알아보았습니다. RxBluetoothKit의 다양한 기능을 활용하여 BLE 통신에 대한 더 깊은 이해를 개발하고, 스마트 폰과 주변 장치간의 강력한 연결을 구현할 수 있습니다.

참고자료:
- [RxBluetoothKit GitHub](https://github.com/Polidea/RxBluetoothKit)
- [Apple Developer Documentation - Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)