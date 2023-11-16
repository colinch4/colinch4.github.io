---
layout: post
title: "[swift] SwiftyJSON을 사용하여 JSON 데이터를 Bluetooth 형식으로 전송하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이 튜토리얼에서는 SwiftyJSON 라이브러리를 사용하여 Swift에서 Bluetooth를 통해 JSON 데이터를 전송하는 방법을 알아보겠습니다.

## SwiftyJSON이란?

SwiftyJSON은 JSON 데이터를 쉽게 다루기 위한 Swift 라이브러리입니다. SwiftyJSON을 사용하면 JSON 데이터를 손쉽게 파싱하고, 수정하고, 검색할 수 있습니다.

## SwiftyJSON 설치

SwiftyJSON을 사용하려면 먼저 프로젝트에 라이브러리를 설치해야 합니다. 다음은 Swift Package Manager를 사용하여 SwiftyJSON을 설치하는 방법입니다:

1. Xcode에서 프로젝트를 엽니다.
2. 프로젝트 네비게이터에서 프로젝트 파일을 선택합니다.
3. "Swift Packages" 탭을 선택하고 "+" 버튼을 클릭합니다.
4. 패키지 URL 입력란에 `https://github.com/SwiftyJSON/SwiftyJSON.git`을 입력하고 "Next"를 클릭합니다.
5. 원하는 버전에 체크하고 "Next"를 클릭합니다.
6. "Add Package"를 클릭합니다.

## Bluetooth 통신 설정

Bluetooth를 사용하여 기기 간 통신을 하려면 CoreBluetooth 프레임워크를 사용해야 합니다. 따라서 먼저 CoreBluetooth 프레임워크를 프로젝트에 추가해야 합니다.

1. Xcode에서 프로젝트 네비게이터에서 프로젝트 파일을 선택합니다.
2. "Project Target"을 선택한 후 "Build Phases" 탭을 클릭합니다.
3. "+" 버튼을 클릭하고 "Link Binary With Libraries"를 선택합니다.
4. "CoreBluetooth.framework"을 추가합니다.

## JSON 데이터 생성 및 전송

이제 SwiftyJSON과 CoreBluetooth를 사용하여 JSON 데이터를 생성하고 Bluetooth를 통해 전송하는 코드를 작성해보겠습니다.

```swift
import SwiftyJSON
import CoreBluetooth

// JSON 데이터 생성
let jsonDictionary = ["name": "John", "age": 30]
let jsonData = try? JSONSerialization.data(withJSONObject: jsonDictionary, options: .prettyPrinted)
let jsonString = String(data: jsonData!, encoding: .utf8)

// Bluetooth 관련 변수 설정
let serviceUUID = CBUUID(string: "YOUR_SERVICE_UUID")
let characteristicUUID = CBUUID(string: "YOUR_CHARACTERISTIC_UUID")
var centralManager: CBCentralManager?
var peripheral: CBPeripheral?
var characteristic: CBCharacteristic?

// Bluetooth 초기화
centralManager = CBCentralManager(delegate: self, queue: nil)

// Bluetooth 디바이스 검색
func centralManagerDidUpdateState(_ central: CBCentralManager) {
    if central.state == .poweredOn {
        centralManager?.scanForPeripherals(withServices: nil, options: nil)
    }
}

// Bluetooth 디바이스 연결
func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
    if peripheral.name == "YOUR_DEVICE_NAME" {
        self.peripheral = peripheral
        centralManager?.stopScan()
        centralManager?.connect(peripheral, options: nil)
    }
}

// Bluetooth 연결 완료
func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
    peripheral.delegate = self
    peripheral.discoverServices([serviceUUID])
}

// Bluetooth 서비스 찾기
func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
    if let services = peripheral.services {
        for service in services {
            if service.uuid == serviceUUID {
                peripheral.discoverCharacteristics(nil, for: service)
            }
        }
    }
}

// Bluetooth 특성 찾기
func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
    if let characteristics = service.characteristics {
        for characteristic in characteristics {
            if characteristic.uuid == characteristicUUID {
                self.characteristic = characteristic
                // JSON 데이터 전송
                let data = jsonString?.data(using: .utf8)
                peripheral.writeValue(data!, for: characteristic, type: .withResponse)
            }
        }
    }
}
```

위의 코드에서 "YOUR_SERVICE_UUID"와 "YOUR_CHARACTERISTIC_UUID"를 프로젝트에서 사용하는 실제 UUID 값으로 대체해야 합니다. 또한 "YOUR_DEVICE_NAME"은 JSON 데이터를 전송할 Bluetooth 디바이스의 이름으로 변경해야 합니다.

이제 JSON 데이터를 생성하고, Bluetooth를 통해 전송하는 코드가 준비되었습니다. 이 코드를 통해 Bluetooth를 사용하여 JSON 데이터를 전송할 수 있습니다.

## 결론

이번 튜토리얼에서는 SwiftyJSON 라이브러리를 사용하여 Swift에서 JSON 데이터를 Bluetooth 형식으로 전송하는 방법을 알아보았습니다. SwiftyJSON을 사용하면 JSON 데이터를 쉽게 다룰 수 있으며, CoreBluetooth 프레임워크를 통해 Bluetooth를 사용하여 기기 간 통신을 할 수 있습니다. 프로젝트에 이 코드를 적용하여 JSON 데이터를 Bluetooth로 전송해보세요!