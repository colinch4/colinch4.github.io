---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Battery Service 접근"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Battery 서비스는 BLE 장치의 배터리 수준 정보를 제공하는 데 사용됩니다. 이 게시물에서는 Swift 언어와 RxBluetoothKit을 사용하여 Bluetooth Battery 서비스에 접근하는 방법을 살펴보겠습니다.

## 1. RxBluetoothKit 설치

RxBluetoothKit은 Swift에서 BLE 통신을 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 아래와 같이 Podfile에 RxBluetoothKit을 추가하여 설치할 수 있습니다.

```swift
platform :ios, '10.0'
use_frameworks!

target 'YourProjectName' do
  pod 'RxBluetoothKit'
end
```

터미널에서 `pod install` 명령을 실행하여 RxBluetoothKit을 설치합니다.

## 2. Bluetooth Manager 초기화

```swift
import RxBluetoothKit

let manager = CentralManager(queue: .main)
```

Bluetooth Manager를 초기화합니다.

## 3. Bluetooth 장치 검색

```swift
manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Found peripheral: \(scannedPeripheral.peripheral)")
    })
    .disposed(by: disposeBag)
```

위의 코드를 사용하여 Bluetooth 장치를 검색합니다. 스캔 결과로 검색된 각 장치에 대한 정보를 받을 수 있습니다.

## 4. Bluetooth Battery 서비스 접근

```swift
manager.connect(scannedPeripheral.peripheral)
    .flatMap { $0.discoverServices([BatteryService.uuid]) }
    .subscribe(onNext: { discoveredServices in
        for service in discoveredServices {
            print("Discovered service: \(service)")
            
            if service.uuid == BatteryService.uuid {
                manager.monitorCharacteristic(for: service.characteristics.first!)
                    .subscribe(onNext: { characteristic in
                        print("Battery level: \(characteristic.value?.first) %")
                    })
                    .disposed(by: disposeBag)
            }
        }
        
    })
    .disposed(by: disposeBag)
```

위의 코드를 사용하여 Bluetooth 장치에 연결하고 Battery 서비스를 찾습니다. Battery 서비스를 찾았을 경우, 해당 서비스에 대한 Characteristics를 찾습니다. 최초로 발견된 Characteristic를 모니터링하여 배터리 수준을 확인할 수 있습니다.

## 결론

위의 단계를 따라가면 Swift와 RxBluetoothKit을 사용하여 Bluetooth Battery 서비스에 접근할 수 있습니다. Bluetooth Battery 서비스에는 BLE 장치의 배터리 수준 정보가 포함되어 있으므로, 이를 활용하여 BLE 통신 애플리케이션을 개발할 수 있습니다.

참고: https://github.com/Polidea/RxBluetoothKit