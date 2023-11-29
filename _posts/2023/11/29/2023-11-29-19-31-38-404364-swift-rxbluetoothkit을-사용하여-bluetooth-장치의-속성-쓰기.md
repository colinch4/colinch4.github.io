---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 속성 쓰기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 장치의 속성을 쓰기 위해 Swift에서 RxBluetoothKit 라이브러리를 사용할 수 있습니다. RxBluetoothKit는 RxSwift를 기반으로 한 Bluetooth Low Energy(BLE) 통신을 쉽게 처리할 수 있게 해주는 라이브러리입니다.

## RxBluetoothKit 설치하기

RxBluetoothKit을 사용하기 위해 먼저 Cocoapods나 Swift Package Manager(SPM)을 통해 라이브러리를 설치해야 합니다. 

1. Cocoapods를 사용하는 경우:

```ruby
pod 'RxBluetoothKit'
```

2. SPM을 사용하는 경우:

```swift
dependencies: [
    .package(url: "https://github.com/Polidea/RxBluetoothKit.git", from: "4.0.0")
]
```

설치가 완료되면 프로젝트에 RxBluetoothKit를 import 해줍니다.

```swift
import RxBluetoothKit
```

## Bluetooth 장치의 속성 쓰기

1. Bluetooth 장치를 찾습니다.

```swift
let centralManager = CentralManager()
let peripheral = centralManager.scanForPeripherals(withServices: nil)
    .filter { $0.peripheral.name == "MyDevice" }
    .take(1)
    .subscribe(onNext: { scannedPeripheral in
        // Bluetooth 장치 찾음
        self.connectToPeripheral(scannedPeripheral)
    })
```

2. Bluetooth 장치에 연결합니다.

```swift
func connectToPeripheral(_ peripheral: ScannedPeripheral) {
    centralManager.connect(to: peripheral)
        .subscribe(onNext: { connectedPeripheral in
            // Bluetooth 장치에 연결됨
            self.writeCharacteristic(connectedPeripheral)
        })
}
```

3. 연결된 Bluetooth 장치에 속성을 씁니다.

```swift
func writeCharacteristic(_ peripheral: Peripheral) {
    let writeValue: [UInt8] = [0x01, 0x02, 0x03] // 속성에 쓸 데이터
    let characteristicUUID = CBUUID(string: "YourCharacteristicUUID")
    
    peripheral.writeValue(Data(writeValue), for: characteristicUUID, type: .withResponse)
        .subscribe(onNext: { _ in
            // 속성 쓰기 완료
            print("속성 쓰기 완료")
        })
}
```

위의 예시에서는 RxBluetoothKit를 사용하여 Bluetooth 장치의 속성을 쓰는 방법을 보여줬습니다. 실제로는 더 다양한 기능을 활용할 수 있으며, 필요에 따라 속성을 읽고 알림을 받는 등 다양한 작업을 수행할 수 있습니다.

더 자세한 내용은 [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)를 참고하시기 바랍니다.