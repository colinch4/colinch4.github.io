---
layout: post
title: "[swift] Swift Core Bluetooth와 블루투스 Low Energy (BLE)"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

블루투스 Low Energy (BLE)는 IoT 기기와 모바일 애플리케이션 간에 데이터를 교환하는 데 사용되는 표준이다. Swift 언어를 사용하여 iOS 애플리케이션에서 BLE를 구현할 수 있다. 이를 가능하게 하는 주요 프레임워크는 Swift Core Bluetooth이다.

Swift Core Bluetooth는 iOS 기기 간에 블루투스 연결을 설정하고 데이터를 주고받을 수 있는 기능을 제공한다. 이를 통해 iOS 애플리케이션은 BLE 기기와 상호작용할 수 있다. 

## Core Bluetooth 프레임워크 사용하기

Core Bluetooth를 사용하기 위해 먼저 `import CoreBluetooth` 문을 추가한다. 그런 다음 `CBCentralManager` 클래스를 사용하여 BLE 장치와 연결할 수 있다. `CBCentralManagerDelegate` 프로토콜을 준수하는 클래스에서 중앙 관리자 객체를 만들고 이를 초기화한다.

```swift
import CoreBluetooth

class MyBluetoothManager: NSObject, CBCentralManagerDelegate {
  var centralManager: CBCentralManager!
  
  override init() {
    super.init()
    
    centralManager = CBCentralManager(delegate: self, queue: nil)
  }
  
  func centralManagerDidUpdateState(_ central: CBCentralManager) {
    // 블루투스 장치 상태가 변경될 때 호출되는 메서드
    if central.state == .poweredOn {
      // 블루투스가 켜진 상태이면 스캔을 시작한다
      centralManager.scanForPeripherals(withServices: nil)
    } else {
      // 블루투스가 꺼진 상태이면 처리를 중단한다
      print("Bluetooth is turned off.")
    }
  }
}
```

위의 예시에서 `centralManagerDidUpdateState` 메서드는 블루투스 상태 변경에 대한 처리를 담당한다. `central.state` 속성을 통해 현재 블루투스 상태를 확인할 수 있다.

## 주변 장치 검색하기

주변 BLE 장치 검색을 시작하려면 `scanForPeripherals` 메서드를 사용한다. 이 메서드는 선택적으로 검색할 서비스 UUID를 인자로 받을 수 있는데, 서비스 UUID를 지정하면 해당 서비스를 가지고 있는 장치만 검색할 수 있다.

```swift
func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi: NSNumber) {
  // 주변 장치를 발견했을 때 호출되는 메서드
  print("Discovered peripheral:", peripheral)
}
```

위의 예시에서 `didDiscover` 메서드는 주변 장치를 발견했을 때 호출된다. 이 메서드에서 `peripheral` 객체를 사용하여 발견된 장치에 대한 정보를 얻을 수 있다.

## 연결하기

주변 장치를 선택하고 연결하려면 `connect` 메서드를 사용한다.

```swift
func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
  // 주변 장치에 연결되었을 때 호출되는 메서드
  print("Connected to peripheral:", peripheral)
}
```

위의 예시에서 `didConnect` 메서드는 주변 장치에 연결되었을 때 호출된다.

## 데이터 교환하기

연결된 주변 장치와 데이터를 주고받으려면 `CBPeripheralDelegate` 프로토콜을 준수하는 클래스에서 해당 장치의 특성과 서비스를 찾아야 한다.

```swift
class MyPeripheralManager: NSObject, CBPeripheralDelegate {
  var peripheral: CBPeripheral!
  
  func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
    // 주변 장치에 연결되었을 때 호출되는 메서드
    peripheral.delegate = self
    peripheral.discoverServices(nil)
  }
  
  func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
    // 주변 장치의 서비스를 발견했을 때 호출되는 메서드
    if let services = peripheral.services {
      for service in services {
        peripheral.discoverCharacteristics(nil, for: service)
      }
    }
  }
  
  func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
    // 주변 장치의 특성을 발견했을 때 호출되는 메서드
    if let characteristics = service.characteristics {
      for characteristic in characteristics {
        // 특성에 대한 작업을 수행한다
      }
    }
  }
}
```

위의 예시에서 `didDiscoverCharacteristicsFor` 메서드는 주변 장치의 특성을 발견했을 때 호출된다. 이 메서드에서 특성에 대한 작업을 수행할 수 있다.

## 참고 자료

- [Apple Developer Documentation - Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)
- [Ray Wenderlich - Bluetooth Low Energy (BLE) With Swift](https://www.raywenderlich.com/9537834-bluetooth-low-energy-ble-with-swift)
- [Hacking with Swift - Core Bluetooth tutorial for iOS: Read and Write](https://www.hackingwithswift.com/example-code/system/how-to-read-and-write-characters-from-a-ble-device-using-transferring-values)
- [Medium - Getting Started with CoreBluetooth with Swift](https://yoursunny.com/t/2017/CoreBluetooth)