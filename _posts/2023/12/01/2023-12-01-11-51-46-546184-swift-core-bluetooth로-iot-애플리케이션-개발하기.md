---
layout: post
title: "[swift] Swift Core Bluetooth로 IoT 애플리케이션 개발하기"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

이미지: ![Swift Core Bluetooth](https://example.com/swift-core-bluetooth.png)

IoT(Internet of Things) 애플리케이션은 현재 많은 관심을 받고 있습니다. IoT 기기들을 제어하거나 데이터를 수집하고 분석하기 위해서는 효율적으로 블루투스 연결을 관리해야 합니다. 이러한 요구에 대응하기 위해 Swift에서는 Core Bluetooth 프레임워크를 제공하고 있습니다.

Core Bluetooth는 iOS, macOS 및 watchOS에서 블루투스 Low Energy(BLE) 장치와 통신하기 위한 네이티브 프레임워크입니다. BLE는 전력 소모가 낮고 효율적인 블루투스 통신 프로토콜로, 주로 센서 기기나 웨어러블 디바이스 등에 사용됩니다.

이제 Swift Core Bluetooth를 사용하여 IoT 애플리케이션을 개발하는 방법에 대해 알아보겠습니다.

## 1. 블루투스 디바이스 검색하기

Core Bluetooth를 사용하여 블루투스 디바이스를 검색하려면 `CBCentralManager` 객체를 생성하고 해당 객체의 `scanForPeripherals(withServices:options:)` 메서드를 호출합니다. `withServices` 매개변수를 사용하여 원하는 서비스 UUID 배열을 지정할 수 있습니다.

```swift
import CoreBluetooth

class BluetoothManager: NSObject, CBCentralManagerDelegate {
    private var centralManager: CBCentralManager!

    override init() {
        super.init()
        centralManager = CBCentralManager(delegate: self, queue: nil)
    }

    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == .poweredOn {
            central.scanForPeripherals(withServices: nil, options: nil)
        }
    }

    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        // 디바이스를 찾았을 때의 동작 코드 작성
    }
}

let bluetoothManager = BluetoothManager()
```

위의 코드에서 `centralManagerDidUpdateState(_:)` 메서드는 블루투스 상태가 .poweredOn 상태로 변경될 때 호출되고, `centralManager(_:didDiscover:advertisementData:rssi:)` 메서드는 디바이스가 검색되었을 때 호출됩니다. `advertisementData` 매개변수를 사용하여 광고 정보를 확인할 수 있습니다.

## 2. 디바이스 연결 및 통신하기

디바이스를 검색한 후에는 해당 디바이스와 연결을 수행하고 데이터를 주고받을 수 있습니다. 디바이스 연결은 `CBCentralManager` 객체의 `connect(_:options:)` 메서드를 사용하여 수행됩니다. 

```swift
import CoreBluetooth

class BluetoothManager: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    // ...

    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        if peripheral.name == "IoT Device" {
            centralManager.connect(peripheral, options: nil)
        }
    }

    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        peripheral.delegate = self
        peripheral.discoverServices(nil)
    }

    func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
        guard let services = peripheral.services else { return }

        for service in services {
            peripheral.discoverCharacteristics(nil, for: service)
        }
    }

    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
        guard let characteristics = service.characteristics else { return }

        for characteristic in characteristics {
            if characteristic.uuid == CBUUID(string: "0000") {
                peripheral.readValue(for: characteristic)
            }
        }
    }

    func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error: Error?) {
        guard let value = characteristic.value else { return }

        // 데이터 수신 후의 동작 코드 작성
    }
}

let bluetoothManager = BluetoothManager()
```

위의 코드에서 `centralManager(_:didDiscover:)` 메서드에서 연결할 디바이스를 찾았을 때 `connect(_:options:)` 메서드를 호출하여 연결을 시도합니다. `centralManager(_:didConnect:)` 메서드에서 연결이 성공하면 `peripheral.discoverServices(nil)`를 호출하여 디바이스의 서비스를 찾습니다. 그리고 `peripheral(_:didDiscoverCharacteristicsFor:error:)` 메서드에서 해당 서비스의 특성을 찾아 특성 값을 읽습니다.

## 3. 데이터 전송하기

데이터를 전송하기 위해서는 연결된 디바이스의 특성에 값을 쓰는 작업이 필요합니다.

```swift
import CoreBluetooth

class BluetoothManager: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    // ...
    
    func sendData(_ data: Data) {
        guard let characteristic = characteristic else { return }

        peripheral.writeValue(data, for: characteristic, type: .withoutResponse)
    }
}

let bluetoothManager = BluetoothManager()
bluetoothManager.sendData(Data("Hello, IoT!".utf8))
```

위의 코드에서 `sendData(_:)` 메서드를 호출하여 데이터를 전송합니다. `writeValue(_:for:type:)` 메서드의 `type` 매개변수를 `.withoutResponse`로 설정하면 데이터 전송 후 디바이스로부터 응답을 기다리지 않습니다.

## 마무리

이제 Swift Core Bluetooth를 이용하여 IoT 애플리케이션을 개발하는 방법을 알아보았습니다. Core Bluetooth 프레임워크를 사용하면 블루투스 기능을 효율적으로 활용하여 IoT 기기와의 통신을 구현할 수 있습니다.

더 자세한 내용은 [Apple Developer Documentation](https://developer.apple.com/documentation/corebluetooth)을 참조해주세요.