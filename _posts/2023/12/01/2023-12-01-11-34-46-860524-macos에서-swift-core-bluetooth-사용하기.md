---
layout: post
title: "[swift] macOS에서 Swift Core Bluetooth 사용하기"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

macOS에서는 Swift Core Bluetooth를 사용하여 Bluetooth 기능을 활용할 수 있습니다. Swift Core Bluetooth는 iOS 및 macOS 기기 간의 Bluetooth 통신을 위한 프레임워크입니다. 이를 이용하여 기기 간 데이터 전송, 주변 장치 탐색 및 연결 등의 작업을 수행할 수 있습니다.

## 1. 프로젝트 설정

먼저 Xcode에서 Swift Core Bluetooth를 사용하기 위해 프로젝트 세팅을 해야 합니다. 다음은 프로젝트 설정의 주요 내용입니다.

1. Xcode에서 프로젝트를 엽니다.
2. Target 설정에서 `Capabilities` 탭으로 이동합니다.
3. `Background Modes`를 활성화하고 `Uses Bluetooth LE accessories`를 선택합니다.

## 2. CBCentralManager 초기화

Swift Core Bluetooth를 사용하려면 `CBCentralManager` 인스턴스를 초기화해야 합니다. 이 인스턴스를 사용하여 Bluetooth 장치를 탐색하고 연결할 수 있습니다. 다음은 `CBCentralManager`의 초기화 방법입니다.

```swift
import CoreBluetooth

let centralManager = CBCentralManager(delegate: self, queue: DispatchQueue.main)
```

## 3. CBCentralManagerDelegate 메서드 구현

`CBCentralManagerDelegate` 프로토콜을 구현하여 Bluetooth 이벤트에 대응할 수 있습니다. 예를 들어, 주변 장치가 발견되었을 때, 연결이 성공했을 때 등의 이벤트를 처리할 수 있습니다.

```swift
func centralManagerDidUpdateState(_ central: CBCentralManager) {
    switch central.state {
    case .poweredOn:
        // Bluetooth가 켜진 상태
    case .poweredOff:
        // Bluetooth가 꺼진 상태
    default:
        break
    }
}

func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
    // 발견된 주변 장치 처리
}

func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
    // 주변 장치 연결 성공 처리
}
```

## 4. 주변 장치 탐색 및 연결

`CBCentralManager`를 사용하여 주변 장치를 탐색하고 연결할 수 있습니다. 다음은 주변 장치를 탐색하는 예제입니다.

```swift
centralManager.scanForPeripherals(withServices: nil, options: nil)
```

주변 장치를 다음과 같은 방법으로 연결할 수 있습니다.

```swift
centralManager.connect(peripheral, options: nil)
```

## 5. 데이터 전송

주변 장치와 연결된 후에는 데이터를 전송할 수 있습니다. `CBPeripheral`을 사용하여 데이터를 읽고 쓸 수 있습니다. 다음은 데이터 전송의 예제입니다.

```swift
let data = Data("Hello, Bluetooth".utf8)
peripheral.writeValue(data, for: characteristic, type: .withResponse)
```

위의 예제에서 `data`는 전송할 데이터, `characteristic`는 데이터를 쓸 특성을 나타냅니다.

## 마무리

위에서는 macOS에서 Swift Core Bluetooth를 사용하는 방법에 대해 간략히 살펴보았습니다. Bluetooth를 이용한 데이터 통신을 구현하려면 `CBCentralManager`와 `CBPeripheral`를 적절하게 활용해야 합니다. 더 자세한 내용을 알고 싶다면 [Apple Developer Documentation](https://developer.apple.com/documentation/corebluetooth)을 참고해 주세요.