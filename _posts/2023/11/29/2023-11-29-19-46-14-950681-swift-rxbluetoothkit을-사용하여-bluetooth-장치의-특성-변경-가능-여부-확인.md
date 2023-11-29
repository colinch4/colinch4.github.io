---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 특성 변경 가능 여부 확인"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 장치의 특성을 변경할 수 있는지 여부를 확인하기 위해 Swift RxBluetoothKit 라이브러리를 사용할 수 있습니다. 이 라이브러리는 Swift에서 Bluetooth Low Energy(BLE) 기능을 사용할 수 있도록 도와줍니다.

## 1. RxBluetoothKit 설치

RxBluetoothKit을 사용하기 위해 먼저 프로젝트에 해당 라이브러리를 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음과 같이 추가합니다:

```ruby
pod 'RxBluetoothKit'
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다:

```shell
pod install
```

만약 Carthage를 사용하는 경우, Cartfile에 다음과 같이 추가합니다:

```ruby
github "Polidea/RxBluetoothKit"
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다:

```shell
carthage update --platform iOS
```

## 2. Bluetooth 특성 변경 가능 여부 확인

RxBluetoothKit을 사용하여 Bluetooth 장치의 특성을 변경할 수 있는지 여부를 확인하기 위해 다음 단계를 따릅니다:

### 2.1. CentralManager 생성

```swift
import RxBluetoothKit

let centralManager = CentralManager(queue: .main)
```

### 2.2. Bluetooth 장치 검색

```swift
let scanDisposable = centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        // Bluetooth 장치를 찾은 경우, 특성 변경 여부를 확인합니다
        self.checkCharacteristicPermissions(for: scannedPeripheral)
    }, onError: { error in
        // 에러 처리
    })
```

### 2.3. 특성 변경 가능 여부 확인

```swift
func checkCharacteristicPermissions(for peripheral: ScannedPeripheral) {
    let _ = peripheral.peripheral.connect()
        .flatMap { connectedPeripheral -> Single<[Service]> in
            return connectedPeripheral.discoverServices(nil)
        }
        .subscribe(onSuccess: { services in
            // 특성 변경 가능 여부 확인
            for service in services {
                for characteristic in service.characteristics {
                    if characteristic.properties.contains(.write) {
                        // 특성의 속성이 쓰기 가능한지 확인
                        print("Characteristic is writable")
                    } else {
                        print("Characteristic is not writable")
                    }
                }
            }
        }, onError: { error in
            // 에러 처리
        })
}
```

위의 코드는 Bluetooth 장치를 검색한 후, 각 장치에 대해 특성 변경 가능 여부를 확인하는 방법을 보여줍니다. `checkCharacteristicPermissions(for:)` 메소드는 Bluetooth 장치와 연결한 후, 연결된 장치의 서비스를 검색하고 각 서비스의 특성을 확인합니다. 특성의 `properties` 속성을 통해 특성이 쓰기 가능한지 여부를 확인할 수 있습니다.

이제 Swift RxBluetoothKit 라이브러리를 사용하여 Bluetooth 장치의 특성 변경 가능 여부를 확인할 수 있습니다. 자세한 내용은 [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)를 참조하세요.