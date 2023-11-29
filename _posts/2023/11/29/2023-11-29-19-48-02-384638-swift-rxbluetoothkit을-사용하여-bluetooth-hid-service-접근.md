---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth HID Service 접근"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth HID (Human Interface Device) 서비스는 블루투스를 통해 키보드, 마우스, 게임 컨트롤러와 같은 인터페이스 장치와 연결할 수 있게 해주는 서비스입니다. 이번 블로그에서는 Swift와 RxBluetoothKit을 사용하여 Bluetooth HID 서비스에 어떻게 접근하는지에 대해 알아보겠습니다.

## 1. RxBluetoothKit 설치

RxBluetoothKit은 iOS에서 Bluetooth Low Energy (BLE) 기능을 사용하기 위한 라이브러리로, Swift에서 BLE 디바이스와 상호작용하는데 도움을 줍니다. RxBluetoothKit을 사용하기 위해 먼저 프로젝트에 RxSwift를 설치해야 합니다.

```swift
pod 'RxBluetoothKit'
```

## 2. Bluetooth 디바이스 스캔

Bluetooth HID 서비스에 접근하려면 먼저 기기를 스캔해야 합니다. 아래 코드를 사용하여 RxBluetoothKit을 사용하여 BLE 디바이스를 스캔하는 방법을 알아보겠습니다.

```swift
import RxBluetoothKit
import RxSwift

let disposeBag = DisposeBag()
let centralManager = CentralManager(queue: .main)

centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Scanned Peripheral: \(scannedPeripheral)")
    }, onError: { error in
        print("Error: \(error)")
    }).disposed(by: disposeBag)
```

위 코드에서 `centralManager.scanForPeripherals(withServices: nil)`은 모든 서비스를 가진 디바이스를 스캔합니다. 이 코드를 실행하면 주변에 있는 Bluetooth 디바이스의 목록이 출력됩니다.

## 3. Bluetooth HID 디바이스 연결

디바이스를 스캔한 후에는 Bluetooth HID 서비스를 가진 디바이스를 선택하여 연결해야 합니다. 아래 코드를 사용하여 RxBluetoothKit을 사용하여 디바이스를 연결하는 방법을 알아보겠습니다.

```swift
let peripheral = // 스캔한 디바이스 중에서 선택한 디바이스

centralManager.connect(peripheral)
    .flatMap { connectedPeripheral -> Observable<Peripheral> in
        // 연결이 성공했을 때 실행되는 코드
        print("Connected Peripheral: \(connectedPeripheral)")
        return connectedPeripheral.discoverServices([BluetoothService.hid])
    }
    .subscribe(onNext: { service in
        // HID 서비스를 찾은 후 실행되는 코드
        print("HID Service Found: \(service)")
    }, onError: { error in
        // 에러 발생 시 실행되는 코드
        print("Error: \(error)")
    }).disposed(by: disposeBag)
```

위 코드에서 `BluetoothService.hid`는 HID 서비스의 UUID입니다. 연결이 성공한 후에는 `discoverServices` 메서드를 호출하여 HID 서비스를 찾을 수 있습니다. HID 서비스를 찾은 후에는 해당 서비스를 이용하여 HID 디바이스와 상호작용할 수 있습니다.

## 결론

이제 Swift RxBluetoothKit을 사용하여 Bluetooth HID 서비스에 접근하는 방법을 알아보았습니다. RxBluetoothKit은 블루투스 기기와 상호작용하기 위한 강력하고 편리한 도구입니다. 다른 Bluetooth 서비스에 접근하는 방법에 대해서도 RxBluetoothKit 문서를 참조하세요.

참고 자료:
- [RxBluetoothKit GitHub repository](https://github.com/Polidea/RxBluetoothKit)
- [RxSwift GitHub repository](https://github.com/ReactiveX/RxSwift)