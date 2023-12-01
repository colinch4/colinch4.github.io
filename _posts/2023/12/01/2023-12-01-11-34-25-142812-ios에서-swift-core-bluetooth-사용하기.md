---
layout: post
title: "[swift] iOS에서 Swift Core Bluetooth 사용하기"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발할 때 Bluetooth 통신을 사용해 외부 디바이스와 통신해야 할 때가 있습니다. 이러한 경우 Swift Core Bluetooth 프레임워크를 사용하여 쉽게 Bluetooth 통신을 구현할 수 있습니다.

## 1. 프로젝트 설정

먼저 Xcode에서 새로운 iOS 프로젝트를 생성합니다. 프로젝트를 생성한 후, 'Build Phases' 탭으로 이동하여 'Link Binary With Libraries' 섹션에서 'CoreBluetooth.framework'를 추가합니다.

## 2. Bluetooth 관련 권한 설정

Info.plist 파일을 열고 다음 권한을 설정합니다:

- `NSBluetoothAlwaysUsageDescription` : 앱이 Bluetooth를 항상 사용한다는 메시지
- `NSBluetoothPeripheralUsageDescription` : 앱이 Bluetooth 페리프럴을 사용한다는 메시지

## 3. Core Bluetooth 클래스 사용하기

Core Bluetooth 클래스는 `CBCentralManager`와 `CBPeripheral`을 기반으로합니다.

### 3.1. Central Manager 생성

`CBCentralManager` 인스턴스를 생성해야 합니다. 아래와 같은 코드를 사용하여 생성할 수 있습니다.

```swift
import CoreBluetooth

// Central Manager 생성
var centralManager: CBCentralManager!

override func viewDidLoad() {
    super.viewDidLoad()
    
    centralManager = CBCentralManager(delegate: self, queue: nil)
}
```

### 3.2. Delegate 설정

`CBCentralManagerDelegate`를 준수하기 위해 ViewController 클래스에 다음 코드를 추가합니다.

```swift
class ViewController: UIViewController, CBCentralManagerDelegate {
```

또한, `centralManagerDidUpdateState` 메서드를 구현하여 Bluetooth 상태를 확인할 수 있습니다.

```swift
func centralManagerDidUpdateState(_ central: CBCentralManager) {
    switch central.state {
    case .poweredOn:
        print("Bluetooth가 켜져있습니다.")
    case .poweredOff:
        print("Bluetooth가 꺼져 있습니다.")
    default:
        break
    }
}
```

### 3.3. Peripheral 스캔

외부 디바이스를 찾기 위해 주변 디바이스로 스캔해야 합니다. 다음 코드를 사용하여 주변 디바이스를 스캔할 수 있습니다.

```swift
centralManager.scanForPeripherals(withServices: nil, options: nil)
```

### 3.4. Peripheral 연결

디바이스를 찾은 후, 해당 디바이스에 연결하는 방법은 다음과 같습니다.

```swift
func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
    // 디바이스 연결
    centralManager.stopScan() // 스캔 중지
    centralManager.connect(peripheral, options: nil)
}
```

### 3.5. 서비스 및 특성 검색

연결된 디바이스에서 사용 가능한 서비스 및 특성을 검색하는 방법은 다음과 같습니다.

```swift
func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
    peripheral.delegate = self
    peripheral.discoverServices(nil)
}
```

### 3.6. 데이터 통신

서비스 및 특성을 검색한 후, 데이터를 읽거나 쓸 수 있습니다.

```swift
func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
    if let characteristics = service.characteristics {
        for characteristic in characteristics {
            // 특성에 데이터 쓰기
            // characteristic.value = Data("Hello".utf8)
            // peripheral.writeValue(characteristic.value!, for: characteristic, type: .withResponse)
            
            // 특성에서 데이터 읽기
            peripheral.readValue(for: characteristic)
        }
    }
}
```

## 결론

이제 iOS에서 Swift Core Bluetooth를 사용하여 외부 디바이스와의 Bluetooth 통신을 구현하는 방법을 알아보았습니다. Bluetooth 관련 권한 설정과 Core Bluetooth 클래스의 사용 방법을 이해하면, 간단하게 Bluetooth 통신 기능을 추가할 수 있습니다. 

더 자세한 내용은 [Apple의 Core Bluetooth 프레임워크 문서](https://developer.apple.com/documentation/corebluetooth)를 참조하세요.