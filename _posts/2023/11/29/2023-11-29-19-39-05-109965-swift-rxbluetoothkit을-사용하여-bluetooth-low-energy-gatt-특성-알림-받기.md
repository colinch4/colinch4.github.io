---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 특성 알림 받기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력 블루투스 기반의 무선 통신 기술로, 작은 전력 소비, 짧은 전송 거리 등의 특징을 가지고 있습니다. BLE는 GATT (Generic Attribute Profile)를 사용하여 장치 간 데이터를 교환합니다.

이 가이드에서는 Swift와 RxBluetoothKit을 사용하여 BLE 프로토콜을 통해 GATT 특성 알림을 받는 방법을 알아보겠습니다.

## 1. RxBluetoothKit 설치하기

먼저 프로젝트에 RxBluetoothKit을 설치해야 합니다. CocoaPods를 사용하는 경우, `Podfile`에 다음 라인을 추가하고 `pod install` 명령어를 실행합니다.

```swift
pod 'RxBluetoothKit'
```

## 2. Bluetooth 관리자 생성하기

Bluetooth 관리자는 BLE 기능을 관리하고 장치를 스캔하며 연결을 설정하는 데 사용됩니다. 아래 코드를 사용하여 Bluetooth 관리자를 생성합니다.

```swift
import RxBluetoothKit

let disposeBag = DisposeBag()
let bluetoothManager = BluetoothManager(queue: .main)
```

## 3. 장치 스캔하기

GATT 서비스의 특성 알림을 받기 전에 원하는 장치를 스캔해야 합니다. 아래 코드를 사용하여 장치를 스캔합니다.

```swift
let scanDisposable = bluetoothManager.scanForPeripherals(withServiceUUIDs: nil)
    .subscribe(onNext: { scannedPeripheral in
        // 스캔된 장치 처리
        // 필요한 서비스 UUID를 사용하여 필터링할 수도 있습니다.
    }, onError: { error in
        // 에러 처리
    })

scanDisposable.disposed(by: disposeBag)
```

## 4. 연결 설정하기

원하는 장치를 스캔한 후에는 연결을 설정해야 합니다. 아래 코드를 사용하여 원하는 장치에 연결합니다.

```swift
let connectDisposable = scannedPeripheral.connect()
    .subscribe(onNext: { peripheral in
        // 연결 성공 후 처리
        // 연결된 peripheral을 사용하여 다른 작업을 수행할 수 있습니다.
    }, onError: { error in
        // 연결 실패 시 처리
    })

connectDisposable.disposed(by: disposeBag)
```

## 5. GATT 특성 알림 설정하기

원하는 장치와 연결되면 GATT 특성 알림을 설정할 수 있습니다. 아래 코드를 사용하여 특성 알림을 받을 특성을 설정합니다.

```swift
let characteristicDisposable = connectedPeripheral.discoverServices([serviceUUID])
    .flatMap { services -> Single<Characteristic> in
        return connectedPeripheral.discoverCharacteristics([characteristicUUID], for: services[0])
    }
    .flatMap { characteristics -> Single<Characteristic> in
        return characteristics[0].observeValueUpdateAndSetNotification()
    }
    .subscribe(onNext: { characteristic in
        // 특성 업데이트 처리
    }, onError: { error in
        // 알림 설정 실패 시 처리
    })

characteristicDisposable.disposed(by: disposeBag)
```

이제 BLE 장치의 GATT 특성 알림을 성공적으로 받을 수 있습니다.

> 이 가이드는 RxBluetoothKit에 대한 기본적인 사용 방법을 보여주기 위한 것입니다. 자세한 내용은 [RxBluetoothKit GitHub 저장소](https://github.com/Polidea/RxBluetoothKit)를 참조하십시오.

이제 Bluetooth Low Energy GATT 특성 알림을 받기 위해 Swift RxBluetoothKit을 사용하는 방법을 알게 되었습니다. 코드를 사용하여 BLE 장치와의 통신을 처리할 수 있습니다. 이를 기반으로 BLE를 활용한 다양한 응용프로그램을 개발해 보세요.