---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치의 속성 쓰기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy(BLE)는 저전력 블루투스 기술로, 주변 장치와의 통신에 사용됩니다. Swift RxBluetoothKit은 Swift에서 BLE 디바이스와 상호 작용하기위한 강력한 라이브러리입니다.

이번 블로그 포스트에서는 Swift RxBluetoothKit을 사용하여 BLE 장치의 속성을 쓰는 방법을 알아보겠습니다.

## 1. RxBluetoothKit 설치

먼저, RxBluetoothKit을 프로젝트에 설치해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음 줄을 추가합니다:

```ruby
pod 'RxBluetoothKit'
```

그런 다음 터미널에서 `pod install` 명령어를 실행하여 RxBluetoothKit을 설치합니다.

## 2. BLE 장치 연결

먼저, BLE 장치와 연결해야 합니다. 다음 예제 코드를 사용하여 BLE 장치에 연결합니다:

```swift
import RxSwift
import RxBluetoothKit

// BLE 매니저 생성
let disposeBag = DisposeBag()
let centralManager = CentralManager()

// 장치 검색
centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral)")
        
        // 필요한 장치를 찾으면 연결 시도
        if scannedPeripheral.peripheral.name == "MyDevice" {
            centralManager.connect(scannedPeripheral.peripheral)
                .subscribe(onNext: { connectedPeripheral in
                    print("Connected to peripheral: \(connectedPeripheral)")
                })
                .disposed(by: disposeBag)
        }
    })
    .disposed(by: disposeBag)
```

위 코드에서 `scanForPeripherals` 함수는 주변에 있는 모든 장치를 검색하고, `connect` 함수는 특정 장치와 연결합니다.

## 3. 속성 쓰기

BLE 장치의 특정 속성을 쓰기 위해서는 `writeValue` 함수를 사용해야 합니다. 다음은 속성 쓰기의 예제 코드입니다:

```swift
let characteristicUUID = CBUUID(string: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX") // 속성의 UUID
let writeData = Data(bytes: [0x01, 0x02, 0x03]) // 쓰고자 하는 데이터

connectedPeripheral.discoverServices(nil)
    .subscribe(onNext: { discoveredServices in
        for service in discoveredServices {
            service.discoverCharacteristics(nil)
                .subscribe(onNext: { characteristics in
                    for characteristic in characteristics {
                        if characteristic.uuid == characteristicUUID {
                            characteristic.writeValue(writeData, type: .withResponse)
                                .subscribe(onNext: { _ in
                                    print("Value written to characteristic successfully")
                                })
                                .disposed(by: disposeBag)
                        }
                    }
                })
                .disposed(by: disposeBag)
        }
    })
    .disposed(by: disposeBag)
```

위 코드에서 `discoverServices` 함수는 연결된 장치의 서비스를 검색하고, `discoverCharacteristics` 함수는 특정 서비스의 속성을 검색합니다. 그리고 `writeValue` 함수를 사용하여 속성에 데이터를 씁니다.

## 결론

이번 포스트에서는 Swift RxBluetoothKit을 사용하여 BLE 장치의 속성을 쓰는 방법을 알아보았습니다. RxBluetoothKit은 BLE 장치와의 상호 작용을 쉽게 할 수 있도록 도와주는 강력한 라이브러리입니다.

더 많은 정보를 얻으려면 RxBluetoothKit의 공식 문서를 참조하십시오:

[RxBluetoothKit 공식 문서](https://github.com/Polidea/RxBluetoothKit)

Happy coding!