---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth GATT 서비스 검색하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth GATT 서비스는 주변의 Bluetooth 장치와 통신하기 위한 프로토콜과 데이터 형식을 정의합니다. Swift RxBluetoothKit은 iOS와 macOS에서 Bluetooth 연결 및 통신을 위한 라이브러리입니다. 이 블로그 게시물에서는 Swift RxBluetoothKit을 사용하여 Bluetooth GATT 서비스를 검색하는 방법에 대해 알아보겠습니다.

## RxBluetoothKit 설치하기

RxBluetoothKit은 Swift Package Manager를 통해 설치할 수 있습니다. 프로젝트 파일에서 `dependencies` 섹션에 다음을 추가하십시오.

```
dependencies: [
    .package(url: "https://github.com/Polidea/RxBluetoothKit.git", .upToNextMajor(from: "2.13.0"))
]
```

그런 다음 터미널에서 `swift package update` 명령을 실행하여 라이브러리를 다운로드 및 설치합니다.

## Bluetooth 매니저 인스턴스 생성하기

Bluetooth 기능을 사용하기 위해 Bluetooth 매니저 인스턴스를 생성해야합니다. 다음 코드를 사용하여 Bluetooth 매니저 인스턴스를 만듭니다.

```swift
import RxBluetoothKit
import RxSwift

let centralManager = CentralManager(queue: .main)
```

## Bluetooth 서비스 검색하기

Bluetooth 서비스를 검색하려면 다음과 같은 단계를 따르십시오.

1. Discovery 트리거 수신기를 만듭니다.

```swift
let discoveryTrigger = centralManager.observeState()
    .startWith(centralManager.state)
    .filter { $0 == .poweredOn }
```

2. Discovery 트리거 수신기에서 서비스 검색을 시작합니다.

```swift
discoveryTrigger
    .flatMap { _ in return centralManager.scanForPeripherals(withServices: nil) }
    .subscribe(onNext: { scannedPeripheral in
        // 검색된 페리페럴로 작업 수행
        print("Found peripheral: \(scannedPeripheral)")
    }, onError: { error in
        // 에러 처리
        print("Error scanning peripherals: \(error.localizedDescription)")
    })
    .disposed(by: disposeBag)
```

위 코드에서는 `scanForPeripherals` 함수를 사용하여 검색 대상 서비스가 `nil`로 설정된 상태로 페리페럴을 검색합니다. 검색된 각 페리페럴은 `onNext` 클로저에서 처리됩니다.

3. 필요한 GATT 서비스를 검색합니다.

```swift
discoveryTrigger
    .flatMap { _ in return centralManager.scanForPeripherals(withServices: nil) }
    .flatMap { scannedPeripheral in
        return scannedPeripheral.establishConnection()
            .flatMap { $0.discoverServices([serviceUUID]) }
    }
    .subscribe(onNext: { discoveredService in
        // 검색된 GATT 서비스로 작업 수행
        print("Found service: \(discoveredService.uuid)")
    }, onError: { error in
        // 에러 처리
        print("Error discovering services: \(error.localizedDescription)")
    })
    .disposed(by: disposeBag)
```

위 코드에서는 `discoverServices` 함수를 사용하여 페리페럴에 대한 연결을 설정한 후 검색 대상 서비스를 제공하여 GATT 서비스를 검색합니다.

## 요약

이 블로그 게시물에서는 Swift RxBluetoothKit을 사용하여 Bluetooth GATT 서비스를 검색하는 방법을 알아보았습니다. Bluetooth 매니저를 생성하고, 검색을 시작하고, 필요한 GATT 서비스를 검색하여 작업을 수행하는 방법을 살펴보았습니다. RxBluetoothKit 문서를 참조하여 더 자세한 정보를 알아볼 수 있습니다.

## 참고 자료

- RxBluetoothKit 공식 GitHub 저장소: [https://github.com/Polidea/RxBluetoothKit](https://github.com/Polidea/RxBluetoothKit)
- Swift RxBluetoothKit 문서: [https://rxbluetoothkit.com/](https://rxbluetoothkit.com/)