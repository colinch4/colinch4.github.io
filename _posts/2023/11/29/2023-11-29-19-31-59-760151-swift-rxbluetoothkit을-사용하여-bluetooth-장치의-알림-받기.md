---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 알림 받기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Swift RxBluetoothKit은 Bluetooth 장치와 상호 작용하고 데이터를 주고받을 수 있는 라이브러리입니다. 이 라이브러리를 사용하면 Swift로 Bluetooth 기능을 간편하게 구현할 수 있습니다. 이번 글에서는 Swift RxBluetoothKit을 사용하여 Bluetooth 장치로부터 알림을 받는 방법에 대해 알아보겠습니다.

## RxBluetoothKit 설정

RxBluetoothKit을 프로젝트에 추가하기 위해 먼저 CocoaPods을 사용하여 RxBluetoothKit을 설치해야 합니다. `Podfile`에 다음 내용을 추가하고, `pod install` 명령을 실행하여 RxBluetoothKit을 설치합니다.

```swift
pod 'RxBluetoothKit'
```

그리고, `import RxBluetoothKit`을 코드에서 사용할 파일 맨 위에 추가합니다.

## Bluetooth 기기 검색

Bluetooth 장치로부터 알림을 받기 위해 먼저 Bluetooth 장치를 검색해야 합니다. RxBluetoothKit에서는 `PeripheralScanner` 클래스를 사용하여 Bluetooth 기기를 검색할 수 있습니다. 아래는 Bluetooth 기기 검색 예제 코드입니다.

```swift
let manager = PeripheralManager()
manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { peripheral in
        print("Discovered peripheral: \(peripheral)")
    })
    .disposed(by: disposeBag)
```

위 코드는 `PeripheralScanner`의 `scanForPeripherals(withServices:)` 메서드를 사용하여 근처에 있는 모든 Bluetooth 장치를 스캔합니다. 스캔된 각 장치는 `onNext` 블록으로 전송되어 이곳에서 작업을 수행할 수 있습니다.

## 알림 받기

Bluetooth 장치로부터 알림을 받으려면 해당 장치에 연결한 후 알림을 등록해야 합니다. 아래는 알림 등록 및 알림을 받는 예제 코드입니다.

```swift
let manager = PeripheralManager()
manager.connect(peripheral)
    .flatMap { $0.discoverServices(nil) }
    .flatMap { Observable.from($0) }
    .flatMap { $0.discoverCharacteristics(nil) }
    .flatMap { Observable.from($0) }
    .flatMap { $0.observeValueUpdateAndSetNotification() }
    .subscribe(onNext: { characteristic in
        print("Received notification from characteristic: \(characteristic)")
    })
    .disposed(by: disposeBag)
```

위 코드는 `PeripheralManager`의 `connect(_:)` 메서드를 사용하여 Bluetooth 장치에 연결한 후, `discoverServices(_:)` 메서드를 사용하여 해당 장치의 서비스를 검색합니다. 그 다음, `discoverCharacteristics(_:)` 메서드를 사용하여 각 서비스의 특성을 검색하고, `observeValueUpdateAndSetNotification()` 메서드를 사용하여 특성의 알림을 등록합니다. 이후, 알림을 전달받는 블록에서 작업을 수행할 수 있습니다.

## 결론

Swift RxBluetoothKit을 사용하면 Bluetooth 장치로부터 알림을 쉽게 받아올 수 있습니다. RxBluetoothKit을 사용하여 Bluetooth 기능을 구현할 때 이러한 알림 기능을 활용할 수 있으며, 코드의 가독성과 유지 보수성을 향상시킬 수 있습니다. 더 자세한 내용은 [RxBluetoothKit GitHub 저장소](https://github.com/Polidea/RxBluetoothKit)를 참조하세요.