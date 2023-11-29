---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 서비스 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy(GATT) 서비스를 읽고 데이터를 처리하는 것은 iOS 애플리케이션에서 Bluetooth 기능을 구현하는 중요한 부분입니다. 이 문서에서는 Swift RxBluetoothKit을 사용하여 iOS 앱에서 Bluetooth Low Energy GATT 서비스를 읽는 방법을 설명합니다.

## RxBluetoothKit이란?

RxBluetoothKit은 Swift에서 Bluetooth Low Energy 기능을 사용하기 위한 라이브러리로, RxSwift와 함께 사용할 수 있습니다. RxBluetoothKit은 iOS, macOS 및 tvOS에서 Bluetooth 기능을 쉽게 구현할 수 있도록 돕습니다.

## 필수 사항

이 예제를 따라하기 위해 다음을 준비해야 합니다.

- Xcode 설치
- CocoaPods 또는 Swift Package Manager를 사용하여 RxBluetoothKit 라이브러리 추가

## GATT 서비스 읽기

1. 프로젝트에 RxBluetoothKit을 추가합니다. CocoaPods를 사용하는 경우, `Podfile`에 다음을 추가하고 터미널에서 `pod install` 명령을 실행합니다.

```swift
pod 'RxBluetoothKit'
```

2. Bluetooth 관련 권한을 추가합니다. Info.plist 파일에 다음 키를 추가합니다.

- **Privacy - Bluetooth Peripheral Usage Description**: 사용자에게 Bluetooth 액세스 권한에 대한 설명을 제공합니다.

3. RxBluetoothKit을 사용하여 GATT 서비스를 읽을 준비를 합니다. 다음과 같은 코드를 작성합니다.

```swift
import Foundation
import RxBluetoothKit
import RxSwift

func readGattService() {
    let bluetoothManager = BluetoothManager(queue: .main)
    let disposable = bluetoothManager.scanForPeripherals(withServices: nil)
        .take(1)
        .flatMap { $0.peripheral.establishConnection() }
        .flatMap { $0.discoverServices(nil) }
        .flatMap { Observable.from($0) }
        .flatMap { $0.discoverCharacteristics(nil) }
        .flatMap { Observable.from($0) }
        .filter { $0.uuid == CBUUID(string: "YOUR_SERVICE_UUID_HERE") }
        .flatMap { $0.readValue() }
        .subscribe(onNext: { characteristic in
            // 서비스 데이터 처리
            let value = characteristic.value
            // 읽은 데이터를 처리하는 로직을 작성합니다.
        }, onError: { error in
            // 에러 처리
        })

    // GATT 서비스 읽기 작업을 취소하거나 종료해야 할 때 사용합니다.
    disposable.dispose()
}

readGattService()
```

위의 코드에서 `YOUR_SERVICE_UUID_HERE` 부분을 실제 GATT 서비스의 UUID로 대체해야 합니다.

4. `readGattService()` 함수를 호출하여 GATT 서비스를 읽기 시작합니다.

5. 해당 GATT 서비스의 데이터를 처리하는 로직을 `onNext` 클로저 내에 구현합니다. 여기에서 값을 가져와 필요한 작업을 수행할 수 있습니다.

6. `onError` 클로저 내에서는 예외 상황에 대한 에러 처리 로직을 작성합니다.

7. GATT 서비스를 모두 읽거나 작업을 취소할 때에는 `disposable.dispose()`를 호출하여 작업을 정지합니다.

## 요약

iOS 앱에서 Bluetooth Low Energy GATT 서비스를 읽는 방법을 소개했습니다. 이를 위해 Swift RxBluetoothKit 라이브러리를 사용하여 Bluetooth 관련 작업을 수행하는 예시를 제시했습니다. RxBluetoothKit을 사용하면 Bluetooth 기능을 쉽게 구현할 수 있으며, 코드의 가독성과 유지 보수성을 향상시킬 수 있습니다.

## 참고 자료

- [RxBluetoothKit Github 페이지](https://github.com/Polidea/RxBluetoothKit)
- [Apple Developer Documentation - Core Bluetooth](https://developer.apple.com/documentation/corebluetooth)