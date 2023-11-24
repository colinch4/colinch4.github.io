---
layout: post
title: "[swift] Bluetooth에 대한 Swift 퍼미션(Permission) 요청 방법."
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발할 때, 사용자의 Bluetooth를 사용하기 위해서는 Bluetooth 퍼미션이 필요합니다. 이 퍼미션을 요청하는 방법에 대해 알아보겠습니다.

## 1. Info.plist 파일 수정

Bluetooth 사용을 위해 Info.plist 파일에 `NSBluetoothAlwaysUsageDescription` 또는 `NSBluetoothPeripheralUsageDescription` 키를 추가해야 합니다. 이 키는 사용자에게 Bluetooth 퍼미션 요청 시 나타날 메시지를 정의합니다.

- `NSBluetoothAlwaysUsageDescription`: 항상 Bluetooth 기능을 사용하려는 경우
- `NSBluetoothPeripheralUsageDescription`: Bluetooth 전송 작업을 수행하려는 경우

아래는 예시입니다.

```xml
<key>NSBluetoothAlwaysUsageDescription</key>
<string>앱에서 Bluetooth 기능을 사용하려면 허용해주세요.</string>
```

## 2. CBPeripheralManager 객체 생성 및 요청

Bluetooth를 사용하기 위해 `CBPeripheralManager` 객체를 생성하고, 퍼미션을 요청해야 합니다. 아래는 Bluetooth 퍼미션 요청 예시입니다.

```swift
import CoreBluetooth

class BluetoothManager: NSObject, CBPeripheralManagerDelegate {
    private var peripheralManager: CBPeripheralManager!
    
    override init() {
        super.init()
        peripheralManager = CBPeripheralManager(delegate: self, queue: nil)
    }
    
    // Bluetooth 퍼미션 상태 체크
    func checkBluetoothPermission() {
        switch CBPeripheralManager.authorization {
        case .notDetermined:
            // 사용자에게 Bluetooth 퍼미션 요청
            peripheralManager?.startAdvertising(nil)
        case .restricted, .denied:
            // 퍼미션 거절됨
            print("Bluetooth 퍼미션 거절됨")
        case .allowedAlways, .allowedWhenInUse:
            // 퍼미션 허용됨
            print("Bluetooth 퍼미션 허용됨")
        @unknown default:
            // 다른 상태
            print("Bluetooth 퍼미션 상태 알 수 없음")
        }
    }
    
    // Bluetooth 퍼미션 변경 시 호출되는 메서드
    func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) {
        checkBluetoothPermission()
    }
}
```

위 예시 코드에서는 `CBPeripheralManagerDelegate`를 구현하여 Bluetooth 퍼미션 변경 시 호출되는 `peripheralManagerDidUpdateState(_:)` 메서드를 정의합니다. 이 메서드에서는 `checkBluetoothPermission()` 메서드를 호출하여 퍼미션 상태를 체크하고, 퍼미션에 따른 동작을 수행합니다.

## 3. Bluetooth 퍼미션 요청 결과 확인

Bluetooth 퍼미션 요청 결과는 `CBPeripheralManagerDelegate`의 `peripheralManagerDidUpdateState(_:)` 메서드에서 확인할 수 있습니다. 이 메서드에서 결과를 처리하여 원하는 동작을 수행하세요.

```swift
func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) {
    switch peripheral.state {
    case .poweredOn:
        // Bluetooth 퍼미션이 허용됨
        print("Bluetooth 퍼미션이 허용됨")
    case .poweredOff:
        // Bluetooth가 비활성화됨
        print("Bluetooth가 비활성화됨")
    case .resetting:
        // Bluetooth가 리셋 중임
        print("Bluetooth가 리셋 중임")
    case .unauthorized, .unsupported:
        // Bluetooth가 지원되지 않거나, 퍼미션이 거부됨
        print("Bluetooth가 지원되지 않거나, 퍼미션이 거부됨")
    case .unknown:
        // Bluetooth 상태 알 수 없음
        print("Bluetooth 상태 알 수 없음")
    default:
        break
    }
}
```

## 참고 자료

- [Apple Developer Documentation - Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)
- [애플 공식 퍼미션 가이드라인](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/requesting-permission/)

Bluetooth 퍼미션을 요청하는 방법은 위와 같습니다. 기기의 Bluetooth 상태에 따라 적절한 동작을 수행할 수 있도록 구현해보세요.