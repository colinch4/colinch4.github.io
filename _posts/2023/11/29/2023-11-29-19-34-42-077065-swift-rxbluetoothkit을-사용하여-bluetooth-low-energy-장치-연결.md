---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치 연결"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력 무선 프로토콜로, 여러 디바이스 간의 데이터 통신을 지원합니다. Swift RxBluetoothKit은 Swift에서 BLE 장치를 조작하는 데 도움이 되는 라이브러리입니다. 이번 기사에서는 Swift RxBluetoothKit을 사용하여 BLE 장치를 연결하는 방법을 알아보겠습니다.

## RxBluetoothKit 설치

RxBluetoothKit은 CocoaPods을 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같이 라이브러리를 추가합니다.

```
pod 'RxBluetoothKit', '~> 4.0'
```

설치 후, 터미널에서 `pod install` 명령을 실행하여 라이브러리를 프로젝트에 추가합니다.

## BLE 장치 검색

BLE 장치를 검색하려면 `CentralManager`를 사용해야 합니다. 다음은 BLE 장치 검색을 위한 간단한 코드 예제입니다.

```swift
import RxBluetoothKit
import CoreBluetooth

let centralManager = CentralManager()

centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("발견된 장치: \(scannedPeripheral)")
    })
    .disposed(by: disposeBag)
```

`scanForPeripherals(withServices:)` 메서드를 사용하여 BLE 장치 검색을 시작합니다. 검색된 각 장치는 `scannedPeripheral`에 저장되며, 여기서는 단순히 콘솔에 출력합니다.

## BLE 장치 연결

검색된 장치 중 하나를 선택하여 연결하려면, `Peripheral` 객체를 사용해야 합니다. 다음은 BLE 장치를 연결하는 코드 예제입니다.

```swift
let peripheral: Peripheral = ... // 연결할 장치

centralManager.connect(peripheral)
    .subscribe(onNext: { connectedPeripheral in
        print("연결된 장치: \(connectedPeripheral)")
    }, onError: { error in
        print("연결 오류: \(error)")
    })
    .disposed(by: disposeBag)
```

`connect(_:)` 메서드를 사용하여 선택한 장치를 연결합니다. 연결이 성공하면, 연결된 `Peripheral` 객체가 `connectedPeripheral`로 전달됩니다. 연결 실패 시에는 `error`가 전달됩니다.

## 결론

Swift RxBluetoothKit을 사용하면 Swift 프로젝트에서 BLE 장치를 효과적으로 조작할 수 있습니다. 이번 기사에서는 BLE 장치 검색 및 연결에 대한 간단한 예제를 제공했습니다. 더 자세한 내용은 [RxBluetoothKit 공식 문서](https://github.com/Polidea/RxBluetoothKit)를 참고하시기 바랍니다.