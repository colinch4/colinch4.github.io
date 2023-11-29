---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치 연결 및 연결 상태 모니터링"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 장치 연결 및 연결 상태 모니터링은 iOS 애플리케이션에서 유용한 기능 중 하나입니다. Swift RxBluetoothKit은 Bluetooth Low Energy(BLE) 기능을 사용하여 Bluetooth 장치와의 통신을 간편하게 관리할 수 있는 라이브러리입니다.

이 튜토리얼에서는 Swift RxBluetoothKit을 사용하여 Bluetooth 장치를 연결하고, 연결 상태를 모니터링하는 방법을 살펴보겠습니다.

## 1. 프로젝트 설정

먼저, 프로젝트에 Swift RxBluetoothKit을 추가해야 합니다. 이를 위해 [Swift Package Manager](https://swift.org/package-manager/)를 사용하는 것이 가장 간단합니다. 

1. Xcode에서 프로젝트를 엽니다.
2. 프로젝트 탐색기에서 프로젝트 이름을 선택한 후, `Swift Packages` 탭을 선택합니다.
3. `+` 버튼을 클릭하여 패키지를 추가합니다.
4. 패키지 URL 입력란에 `https://github.com/Polidea/RxBluetoothKit.git`을 입력하고, `Next`를 클릭합니다.
5. `Version` 메뉴에서 원하는 버전을 선택하고, `Next`를 클릭합니다.
6. `Add to Target`을 확인하고, `Finish`를 클릭하여 패키지를 추가합니다.

## 2. Bluetooth 장치 검색

Bluetooth 장치를 검색하기 위해 `CentralManager` 클래스를 사용합니다. 다음 코드는 Bluetooth 장치를 검색하는 예제입니다.

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let centralManager = CentralManager(queue: .main)
let scanDisposable = centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral.peripheral.name ?? "")")
    })

// 검색을 멈추려면 다음과 같이 dispose()를 호출합니다.
// scanDisposable.dispose()
```

위 코드에서 `scanForPeripherals` 메서드를 호출하여 Bluetooth 장치를 검색합니다. 이 메서드는 `Observable`로 Bluetooth 장치를 방출하며, `subscribe`를 사용하여 방출된 장치를 처리합니다.

## 3. Bluetooth 장치 연결

Bluetooth 장치를 연결하기 위해 `Peripheral` 클래스를 사용합니다. 다음 코드는 Bluetooth 장치를 연결하는 예제입니다.

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let peripheral: Peripheral = ... // 연결할 Bluetooth 장치
let centralManager = CentralManager(queue: .main)

centralManager.connect(peripheral)
    .subscribe(onNext: { connectedPeripheral in
        print("Connected to peripheral: \(connectedPeripheral.peripheral.name ?? "")")
    })
    .disposed(by: disposeBag)
```

위 코드에서 `connect` 메서드를 호출하여 Bluetooth 장치에 연결합니다. 이 메서드는 연결된 `Peripheral` 객체를 방출하며, `subscribe`를 사용하여 연결 이벤트를 처리합니다.

## 4. 연결 상태 모니터링

Bluetooth 장치의 연결 상태를 모니터링하기 위해 `Peripheral` 객체의 `observeConnection()` 메서드를 사용합니다. 다음 코드는 Bluetooth 장치의 연결 상태를 모니터링하는 예제입니다.

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let peripheral: Peripheral = ... // 연결된 Bluetooth 장치
let centralManager = CentralManager(queue: .main)

peripheral.observeConnection()
    .subscribe(onNext: { connectionEvent in
        switch connectionEvent {
        case .connecting:
            print("Connecting to peripheral: \(peripheral.peripheral.name ?? "")")
        case .connected:
            print("Connected to peripheral: \(peripheral.peripheral.name ?? "")")
        case .disconnecting:
            print("Disconnecting from peripheral: \(peripheral.peripheral.name ?? "")")
        case .disconnected:
            print("Disconnected from peripheral: \(peripheral.peripheral.name ?? "")")
        }
    })
    .disposed(by: disposeBag)
```

위 코드에서 `observeConnection` 메서드를 호출하여 Bluetooth 장치의 연결 상태를 구독합니다. 이 메서드는 `Observable`로 연결 상태 이벤트를 방출하며, `subscribe`를 사용하여 이벤트를 처리합니다.

## 결론

이제 Swift RxBluetoothKit을 사용하여 Bluetooth 장치를 연결하고, 연결 상태를 모니터링하는 방법에 대해 알아보았습니다. Swift RxBluetoothKit은 다양한 기능을 제공하고 있으며, Bluetooth 기반 애플리케이션 개발에 유용하게 사용될 수 있습니다.

더 자세한 내용은 [Swift RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)를 참조하시기 바랍니다.