---
layout: post
title: "[swift] Swift RxBluetoothKit과 CoreBluetooth의 차이점"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth를 사용하기 위해 Swift에서는 CoreBluetooth 프레임워크를 사용할 수 있습니다. 그러나 최근에는 RxSwift와 함께 사용할 수 있는 RxBluetoothKit이라는 새로운 라이브러리도 등장했습니다. 이번 포스트에서는 Swift의 RxBluetoothKit과 CoreBluetooth의 주요 차이점을 살펴보겠습니다.

## CoreBluetooth

CoreBluetooth는 iOS와 macOS에서 Bluetooth Low Energy(BLE) 기능을 사용하기 위한 Apple의 공식 프레임워크입니다. CoreBluetooth를 사용하면 Bluetooth 장치와의 연결 관리, 서비스 및 특성 검색, 데이터 읽기 및 쓰기 등을 수행할 수 있습니다. CoreBluetooth는 일반적으로 delegate 패턴을 사용하여 비동기적으로 이벤트를 처리합니다.

CoreBluetooth 사용 예시:

```swift
import CoreBluetooth

class BluetoothManager: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    
    var centralManager: CBCentralManager?
    var peripheral: CBPeripheral?
    
    override init() {
        super.init()
        
        centralManager = CBCentralManager(delegate: self, queue: nil)
    }
    
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        // Bluetooth 상태 변경 시 호출되는 메서드
    }
    
    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        // 페리프럴 발견 시 호출되는 메서드
    }
    
    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        // 페리프럴 연결 성공 시 호출되는 메서드
    }
    
    // ...
}
```

## RxBluetoothKit

RxBluetoothKit은 CoreBluetooth를 감싼 RxSwift 기반의 라이브러리입니다. 이를 사용하면 CoreBluetooth에서 제공되는 비동기 이벤트 처리 방식 대신에 Observable 및 Observable sequences와 같은 RxSwift의 장점을 활용할 수 있습니다. 이를 통해 더 간결하고 예측 가능한 Bluetooth 코드를 작성할 수 있습니다.

RxBluetoothKit 사용 예시:

```swift
import RxSwift
import RxCocoa
import RxBluetoothKit

class BluetoothManager {
    
    let bluetoothManager = BluetoothManager(queue: .main)
    
    func scanForPeripherals() {
        _ = bluetoothManager.scanForPeripherals(withServices: nil)
            .subscribe(onNext: { scanResult in
                // 스캔 결과 처리
            })
    }
    
    func connect(to peripheral: Peripheral) {
        _ = peripheral.establishConnection()
            .subscribe(onNext: { _ in
                // 연결 성공 처리
            })
    }
    
    // ...
}
```

RxBluetoothKit은 CoreBluetooth의 기능을 유지하면서 RxSwift의 강력함을 제공하는 장점이 있습니다. 또한 RxBluetoothKit은 CoreBluetooth와의 호환성을 보장하므로 필요에 따라 둘을 혼합해서 사용할 수도 있습니다.

## 결론

Swift에서 Bluetooth를 다루는 방법에는 CoreBluetooth와 RxBluetoothKit이 있습니다. CoreBluetooth는 Apple의 공식 프레임워크로 강력하고 안정적입니다. 하지만 비동기 이벤트 처리가 복잡할 수 있습니다. 반면에 RxBluetoothKit은 RxSwift를 기반으로 하여 CoreBluetooth의 기능을 감싸고 있으며, 보다 간결하고 예측 가능한 코드를 작성할 수 있습니다. 선택은 사용자의 필요에 따라 결정하는 것이 가장 중요합니다.

## 참고 자료

- [RxBluetoothKit GitHub Repository](https://github.com/Polidea/RxBluetoothKit)
- [CoreBluetooth Documentation](https://developer.apple.com/documentation/corebluetooth)