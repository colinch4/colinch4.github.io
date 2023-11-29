---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치 및 GATT 서비스의 UUID 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 장치 및 GATT(Generic Attribute Profile) 서비스의 UUID를 읽기 위해 Swift RxBluetoothKit을 사용하는 방법을 알아보겠습니다.

## 준비 사항

1. Swift 프로젝트가 준비되어 있어야 합니다.
2. RxSwift 및 RxBluetoothKit이 프로젝트에 설치되어 있어야 합니다. 만약 설치되어 있지 않다면 다음 명령어로 설치할 수 있습니다.

```
pod 'RxSwift', '~> 6.0'
pod 'RxBluetoothKit', '~> 5.0'
```

## 코드 구현

먼저, Bluetooth 장치 및 GATT 서비스의 UUID를 읽기 위해 다음과 같은 코드 구현을 시작할 수 있습니다.

```swift
import RxBluetoothKit
import RxSwift

// BluetoothManager 객체 생성
let manager = BluetoothManager(queue: .main)

// Bluetooth 장치 찾기
_ = manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scanResult in
        // 원하는 장치를 찾는다면 연결 시도
        if scanResult.peripheral.name == "MyBluetoothDevice" {
            _ = manager.connect(scanResult.peripheral)
                .flatMap { peripheral -> Observable<[Service]> in
                    // GATT 서비스 목록 조회
                    return peripheral.discoverServices(nil)
                }
                .subscribe(onNext: { services in
                    // 각 GATT 서비스의 UUID 읽기
                    for service in services {
                        print("Service UUID: \(service.uuid)")
                    }
                })
        }
    })
```

위의 코드는 다음과 같은 단계로 구성됩니다.

1. `BluetoothManager` 객체를 생성합니다.
2. `scanForPeripherals(withServices: nil)`로 Bluetooth 장치를 검색합니다.
3. `scanResult.peripheral.name`을 확인하여 원하는 Bluetooth 장치를 찾습니다.
4. 원하는 장치를 찾았다면, `connect(_:)`를 사용하여 장치에 연결합니다.
5. 연결된 장치에서 `discoverServices(nil)`로 GATT 서비스 목록을 조회합니다.
6. 조회된 각 서비스의 UUID를 출력합니다.

## 실행과 결과

위의 코드를 실행하면, Bluetooth 장치를 스캔하여 원하는 장치를 찾은 후, 해당 장치와 연결한 뒤, GATT 서비스 목록을 조회하고 각 서비스의 UUID를 출력합니다.

이와 같은 방법으로 Bluetooth 장치와 GATT 서비스의 UUID를 읽을 수 있습니다.

## 결론

Swift RxBluetoothKit을 사용하면 간단한 코드로 Bluetooth 장치와 GATT 서비스의 UUID를 읽을 수 있습니다. Bluetooth 관련 작업을 빠르고 효율적으로 처리할 수 있도록 도와주는 이 라이브러리를 적극 활용하시기 바랍니다.

## 참고 자료

- RxBluetoothKit 공식 문서: [https://github.com/Polidea/RxBluetoothKit](https://github.com/Polidea/RxBluetoothKit)
- Apple Developer Documentation: [https://developer.apple.com/documentation/corebluetooth](https://developer.apple.com/documentation/corebluetooth)