---
layout: post
title: "[swift] Swift Core Bluetooth에서 BLE 서비스와 특성 사용하기"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

이번 블로그 포스트에서는 Swift Core Bluetooth 프레임워크를 사용하여 Bluetooth Low Energy(BLE) 서비스와 특성을 사용하는 방법에 대해 알아보겠습니다.

## 서비스와 특성

Bluetooth Low Energy(BLE)은 주변 기기와의 데이터 통신을 위한 프로토콜 스택입니다. BLE는 기기 간의 통신을 위해 서비스와 특성을 사용합니다.

- 서비스(service): 기기가 제공하는 기능 또는 동작을 나타내는 개념입니다.
- 특성(characteristic): 서비스 내에서 제공되는 세부 기능 또는 데이터로, 읽기, 쓰기, 알림 등의 동작을 할 수 있습니다.

## Core Bluetooth 프레임워크 사용하기

Swift에서 Core Bluetooth 프레임워크를 사용하려면, 먼저 CBCentralManager 객체를 생성해야 합니다. 이 객체는 주변 기기와의 연결 및 통신을 관리합니다.

```swift
import CoreBluetooth

class BluetoothManager: NSObject, CBCentralManagerDelegate {

    // CBCentralManager 객체 생성
    var centralManager: CBCentralManager!

    override init() {
        super.init()
        
        // CBCentralManager 객체 초기화
        centralManager = CBCentralManager(delegate: self, queue: DispatchQueue.main)
    }

    // CBCentralManagerDelegate 메서드 구현
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        // Bluetooth 상태 변경 시 호출되는 메서드
        if central.state == .poweredOn {
            // Bluetooth가 켜져 있으면 주변 기기 스캔 시작
            central.scanForPeripherals(withServices: nil, options: nil)
        }
    }

    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        // 주변 기기 발견 시 호출되는 메서드
        if peripheral.name == "MyDevice" {
            // 특정 기기를 발견한 경우 연결 시도
            central.connect(peripheral, options: nil)
        }
    }

    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        // 주변 기기와 연결되었을 때 호출되는 메서드
        peripheral.delegate = self
        peripheral.discoverServices(nil)
    }

}

extension BluetoothManager: CBPeripheralDelegate {

    func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
        // 주변 기기의 서비스를 발견한 경우 호출되는 메서드
        guard let services = peripheral.services else { return }

        for service in services {
            // 서비스별로 필요한 동작 수행
            if service.uuid == CBUUID(string: "MyServiceUUID") {
                peripheral.discoverCharacteristics(nil, for: service)
            }
        }
    }

    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
        // 주변 기기의 특성을 발견한 경우 호출되는 메서드
        guard let characteristics = service.characteristics else { return }

        for characteristic in characteristics {
            // 특성별로 필요한 동작 수행
            if characteristic.uuid == CBUUID(string: "MyCharacteristicUUID") {
                // 특성에 대한 동작 설정
            }
        }
    }

}
```

위 코드에서는 `BluetoothManager` 클래스가 CBCentralManagerDelegate와 CBPeripheralDelegate 프로토콜을 구현합니다. CBCentralManagerDelegate는 Bluetooth 상태 변경 및 주변 기기 발견과 연결에 사용되고, CBPeripheralDelegate는 주변 기기의 서비스와 특성을 발견하고 동작을 설정하기 위해 사용됩니다.

위 코드에서는 Bluetooth가 켜져 있을 때 주변 기기 발견 및 연결을 수행하고, 특정 서비스와 특성을 찾아 동작을 수행하도록 설정하였습니다.

## 결론

Core Bluetooth 프레임워크를 사용하여 Swift에서 Bluetooth Low Energy(BLE) 서비스와 특성을 사용할 수 있습니다. 이를 통해 주변 기기와의 통신을 간편하게 구현할 수 있습니다.

더 자세한 내용은 Apple의 [Core Bluetooth 프레임워크](https://developer.apple.com/documentation/corebluetooth) 문서를 참고하십시오.