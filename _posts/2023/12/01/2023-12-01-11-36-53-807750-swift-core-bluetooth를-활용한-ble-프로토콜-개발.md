---
layout: post
title: "[swift] Swift Core Bluetooth를 활용한 BLE 프로토콜 개발"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

## 소개
Bluetooth Low Energy (BLE)는 휴대폰, 태블릿 등의 디바이스와 저전력으로 통신할 수 있는 무선 통신 프로토콜입니다. Swift에서는 Core Bluetooth 프레임워크를 사용하여 BLE 통신을 구현할 수 있습니다. 이번 글에서는 Swift Core Bluetooth를 사용하여 BLE 프로토콜을 개발하는 방법을 알아보겠습니다.

## Core Bluetooth 프레임워크 소개
Core Bluetooth 프레임워크는 iOS나 macOS 앱에서 Bluetooth 및 BLE 장치와 상호작용하기 위한 기능을 제공합니다. 이 프레임워크를 사용하면 BLE 장치 검색, 연결, 데이터 교환 등 다양한 작업을 수행할 수 있습니다.

## BLE 프로토콜 개발 단계
BLE 프로토콜을 개발하기 위해서는 몇 가지 단계를 거칠 필요가 있습니다.

1. BLE 장치 검색: Core Bluetooth를 사용하여 주변에 있는 BLE 기기들을 검색합니다.
2. 장치 연결: 검색된 기기 중에서 연결할 기기를 선택하여 연결합니다.
3. 서비스 발견: 연결된 기기에서 사용 가능한 서비스를 검색합니다.
4. 특성 검색: 서비스 내에서 사용 가능한 특성을 검색합니다.
5. 데이터 교환: 특성을 통해 데이터를 읽거나 쓰거나 알림을 받을 수 있습니다.

## Swift 코드 예제
다음은 Swift Core Bluetooth를 사용하여 BLE 프로토콜을 개발하는 간단한 예제 코드입니다.

```swift
import CoreBluetooth

class BLEManager: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    var centralManager: CBCentralManager?
    var peripheral: CBPeripheral?
    
    override init() {
        super.init()
        
        centralManager = CBCentralManager(delegate: self, queue: nil)
    }
    
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == .poweredOn {
            // BLE 장치 검색
            central.scanForPeripherals(withServices: nil, options: nil)
        } else {
            print("Bluetooth not available.")
        }
    }
    
    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        // 찾은 장치에 연결
        self.peripheral = peripheral
        self.peripheral?.delegate = self
        centralManager?.connect(peripheral, options: nil)
    }
    
    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        // 연결 성공 시 서비스 검색
        peripheral.discoverServices(nil)
    }
    
    func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
        // 찾은 서비스 내의 특성 검색
        for service in peripheral.services ?? [] {
            peripheral.discoverCharacteristics(nil, for: service)
        }
    }
    
    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
        // 특성을 통해 데이터 교환
        for characteristic in service.characteristics ?? [] {
            // 데이터 읽기
            peripheral.readValue(for: characteristic)
            // 데이터 쓰기
            peripheral.writeValue(data, for: characteristic, type: .withoutResponse)
            // 알림 받기
            peripheral.setNotifyValue(true, for: characteristic)
        }
    }
}
```

위의 코드에서는 `BLEManager` 클래스를 만들어 BLE 통신을 관리합니다. `CBCentralManagerDelegate`를 구현하여 BLE 상태 업데이트와 검색된 BLE 장치를 처리하고, `CBPeripheralDelegate`를 구현하여 연결된 기기의 서비스와 특성을 검색하고 데이터를 교환합니다.

## 결론
Swift Core Bluetooth를 사용하면 간단하게 BLE 프로토콜을 개발할 수 있습니다. BLE 장치 검색부터 데이터 교환까지 다양한 작업을 쉽게 처리할 수 있으며, BLE 통신이 필요한 앱 개발에 유용하게 사용될 수 있습니다.

## 참고 자료
- [Apple Developer Documentation - Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)
- [Ray Wenderlich - Getting Started with Core Bluetooth](https://www.raywenderlich.com/231-core-bluetooth-tutorial-for-ios-heart-rate-monitor)