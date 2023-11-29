---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 RSSI 값 얻기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 장치의 RSSI(Received Signal Strength Indicator) 값은 장치와의 신호 강도를 측정하는 데 사용됩니다. Swift에서는 RxBluetoothKit 라이브러리를 사용하여 Bluetooth 기능을 쉽게 구현할 수 있습니다. 이번 블로그 포스트에서는 Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 RSSI 값을 얻는 방법에 대해 알아보겠습니다.

## 필요한 라이브러리 설치

이 예제에서는 CocoaPods를 사용하여 RxBluetoothKit 라이브러리를 설치합니다. `Podfile`에 다음과 같이 RxBluetoothKit을 추가한 후 `pod install`을 실행합니다.

```ruby
pod 'RxBluetoothKit'
```

## Bluetooth 장치 검색

먼저 Bluetooth 장치 검색을 위해 `CentralManager`를 초기화합니다.

```swift
import RxBluetoothKit
import CoreBluetooth

let centralManager = CentralManager(queue: .main)
```

그런 다음 `CentralManager`의 `scanForPeripherals` 메서드를 사용하여 주변의 Bluetooth 장치를 검색합니다. 

```swift
centralManager.scanForPeripherals(withServiceUUIDs: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Found peripheral: \(scannedPeripheral)")
    })
    .disposed(by: disposeBag)
```

`scanForPeripherals`은 Observable을 반환하며, 이를 구독하여 주변의 Bluetooth 장치를 검색하고 각 장치를 처리할 수 있습니다.

## RSSI 값 얻기

Bluetooth 장치의 RSSI 값을 얻기 위해 장치를 찾은 후에는 각 장치의 `peripheralDidUpdateRSSI` 이벤트를 구독하여 RSSI 값을 받을 수 있습니다.

```swift
centralManager.scanForPeripherals(withServiceUUIDs: nil)
    .subscribe(onNext: { scannedPeripheral in
        scannedPeripheral.peripheral.observeRSSI()
            .subscribe(onNext: { rssi in
                print("RSSI value: \(rssi)")
            })
            .disposed(by: self.disposeBag)
    })
    .disposed(by: disposeBag)
```

각 장치의 `peripheral.observeRSSI()`를 호출하여 RSSI 값을 구독하고, 이벤트가 실행될 때마다 값을 출력합니다.

## 코드 전체 예제

```swift
import RxBluetoothKit
import CoreBluetooth

let centralManager = CentralManager(queue: .main)
let disposeBag = DisposeBag()

centralManager.scanForPeripherals(withServiceUUIDs: nil)
    .subscribe(onNext: { scannedPeripheral in
        scannedPeripheral.peripheral.observeRSSI()
            .subscribe(onNext: { rssi in
                print("RSSI value: \(rssi)")
            })
            .disposed(by: self.disposeBag)
    })
    .disposed(by: disposeBag)
```

## 결론

RxBluetoothKit을 사용하여 Bluetooth 장치의 RSSI 값을 얻는 방법에 대해 알아보았습니다. 이를 통해 Swift 코드에서 Bluetooth 기능을 손쉽게 구현할 수 있습니다. RxBluetoothKit의 기능을 활용하여 더 다양한 Bluetooth 기능을 구현할 수도 있습니다. 자세한 내용은 RxBluetoothKit 공식 문서를 참조하시기 바랍니다.

---

### 참고 자료

- [RxBluetoothKit GitHub 저장소](https://github.com/Polidea/RxBluetoothKit)