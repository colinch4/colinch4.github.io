---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 서비스 검색"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 장거리 통신을 지원하는 무선 통신 기술로, 응용 프로그램에서 복잡한 Bluetooth GATT 서비스를 검색하고 관리하는 작업이 필요합니다. Swift RxBluetoothKit은 Swift 프로그래밍 언어용 RxSwift 라이브러리를 기반으로 한 BLE 라이브러리로, BLE 기기와의 통신을 쉽게 처리할 수 있도록 도와줍니다.

이번 블로그 포스트에서는 Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 서비스를 검색하는 방법에 대해 알아보겠습니다.

## GATT 서비스 검색
GATT (Generic Attribute Profile)는 BLE 기기간에 데이터를 교환할 수 있는 프로토콜입니다. BLE 기기는 하나 이상의 GATT 서비스를 제공하며, 각 서비스는 하나 이상의 특성 (Characteristics)을 포함합니다. 서비스와 특성은 UUID (Universally Unique Identifier)로 식별됩니다.

Swift RxBluetoothKit에서 GATT 서비스를 검색하려면 다음 단계를 따라야 합니다:

### 1. Central Manager 생성
```swift
let centralManager = CentralManager()
```

### 2. 중앙 매니저 상태 확인
```swift
centralManager.observeState()
    .startWith(centralManager.state)
    .filter { $0 == .poweredOn }
    .take(1)
    .flatMap { _ in centralManager.scanForPeripherals(withServices: nil) }
    .subscribe(onNext: { scannedPeripheral in
        // GATT 서비스 검색 작업 수행
    })
    .disposed(by: disposeBag)
```
Central Manager를 생성한 후, observeState() 메서드를 사용하여 중앙 매니저의 상태를 모니터링합니다. 상태가 poweredOn일 때, scanForPeripherals(withServices:) 메서드를 사용하여 BLE 기기 검색을 시작합니다. 검색된 기기를 onNext 블록에서 처리할 수 있습니다.

### 3. 기기 연결 및 GATT 서비스 검색
```swift
let peripheral = ... // 검색된 기기

centralManager.establishConnection(peripheral)
    .flatMap { $0.discoverServices(nil) }
    .subscribe(onNext: { discoveredServices in
        for service in discoveredServices {
            // 검색된 서비스 정보 활용
        }
    })
    .disposed(by: disposeBag)
```
establishConnection(_:) 메서드를 사용하여 검색된 기기와 연결을 설정한 후, discoverServices 메서드를 사용하여 GATT 서비스를 검색합니다. 검색된 서비스를 onNext 블록에서 처리할 수 있습니다.

## 요약
Swift RxBluetoothKit은 Swift 프로그래밍 언어의 BLE 개발을 쉽게 할 수 있게 해주는 강력한 도구입니다. 이번 포스트에서는 Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 서비스를 검색하는 방법에 대해 알아보았습니다. GATT 서비스 검색은 중앙 매니저 생성, 상태 확인, 기기 연결 및 서비스 검색 단계로 이루어져 있습니다. 위의 예제 코드를 참고하여 BLE 개발을 시작해보세요.

## 참고 자료
- [RxBluetoothKit 공식 문서](https://github.com/Polidea/RxBluetoothKit)