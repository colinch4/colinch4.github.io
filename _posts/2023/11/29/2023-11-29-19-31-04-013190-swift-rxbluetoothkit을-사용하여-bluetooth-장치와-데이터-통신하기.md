---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치와 데이터 통신하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth는 현재 많은 기기에서 사용되는 무선 통신 기술입니다. iOS 앱을 개발하다 보면 Bluetooth를 사용하여 다른 장치와 데이터를 주고받아야 할 때가 있습니다. 이런 경우에는 Swift RxBluetoothKit을 사용하여 간편하게 Bluetooth 장치와 데이터 통신을 할 수 있습니다.

RxBluetoothKit은 ReactiveX 프로그래밍 패러다임을 따르는 Bluetooth 라이브러리입니다. 이 라이브러리는 Bluetooth 장치와의 연결, 서비스 및 특성 탐색, 데이터 전송 등 다양한 기능을 제공합니다. 

## RxBluetoothKit 설치하기

RxBluetoothKit을 사용하기 위해서는 먼저 프로젝트에 해당 라이브러리를 추가해야 합니다. 

### CocoaPods를 사용하는 경우

```ruby
pod 'RxBluetoothKit'
```

### Carthage를 사용하는 경우

```
github "Polidea/RxBluetoothKit"
```

### Swift Package Manager를 사용하는 경우

먼저 프로젝트의 `Package.swift` 파일에 다음을 추가합니다:

```swift
dependencies: [
    .Package(url: "https://github.com/Polidea/RxBluetoothKit.git", majorVersion: 6)
]
```

그런 다음 터미널에서 다음 명령을 실행합니다:

```
swift build
```

빌드가 완료되면 RxBluetoothKit이 프로젝트에 추가됩니다.

## Bluetooth 장치 검색하기

Bluetooth 장치를 검색하려면 `CentralManager.scanForPeripherals` 메서드를 사용합니다. 다음은 장치 검색의 간단한 예시입니다:

```swift
import RxBluetoothKit

let manager = CentralManager()
let scanDisposable = manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral)")
    }, onDisposed: {
        print("Scanning disposed")
    })
```

위 코드는 Bluetooth 장치를 검색하기 시작하고, 장치를 발견할 때마다 로그를 출력합니다.

## Bluetooth 장치와 연결하기

Bluetooth 장치와 연결하려면 `Peripheral.connect` 메서드를 사용합니다. 다음은 장치와 연결하는 예시입니다:

```swift
import RxBluetoothKit

let manager = CentralManager()
let peripheralIdentifier: String = "장치 식별자"

let connectDisposable = manager.retrievePeripherals(withIdentifiers: [peripheralIdentifier])
    .subscribe(onNext: { peripherals in
        guard let peripheral = peripherals.first else { return }
        let connectionDisposable = manager.connect(peripheral)
            .subscribe(onNext: { connectedPeripheral in
                print("Connected to peripheral: \(connectedPeripheral)")
            }, onError: { error in
                print("Failed to connect to peripheral: \(error)")
            })
    })
```

위 코드에서는 먼저 `retrievePeripherals(withIdentifiers:)` 메서드를 사용하여 장치 식별자에 해당하는 Bluetooth 장치를 검색합니다. 그런 다음 `connect` 메서드를 사용하여 장치와 연결합니다. 장치와 연결이 성공하면 로그를 출력합니다.

## Bluetooth 데이터 전송하기

Bluetooth 장치와 데이터를 주고받으려면 `Peripheral.writeValue` 메서드를 사용합니다. 다음은 데이터 전송의 예시입니다:

```swift
import RxBluetoothKit

let manager = CentralManager()
let peripheralIdentifier: String = "장치 식별자"
let data: Data = "전송할 데이터".data(using: .utf8)!

let sendDataDisposable = manager.retrievePeripherals(withIdentifiers: [peripheralIdentifier])
    .subscribe(onNext: { peripherals in
        guard let peripheral = peripherals.first else { return }
        let connectionDisposable = manager.connect(peripheral)
            .subscribe(onNext: { connectedPeripheral in
                let writeDisposable = connectedPeripheral.writeValue(data, for: characteristic, type: .withResponse)
                    .subscribe(onNext: { _ in
                        print("Data sent successfully")
                    }, onError: { error in
                        print("Failed to send data: \(error)")
                    })
            })
    })
```

위 코드에서는 먼저 `retrievePeripherals(withIdentifiers:)` 메서드를 사용하여 장치 식별자에 해당하는 Bluetooth 장치를 검색합니다. 그런 다음 `connect` 메서드를 사용하여 장치와 연결하고, `writeValue` 메서드를 사용하여 데이터를 전송합니다. 데이터 전송이 성공하면 로그를 출력합니다.

## 결론

Swift RxBluetoothKit을 사용하면 Swift 언어로 쉽게 Bluetooth 장치와 데이터 통신을 할 수 있습니다. Bluetooth 장치 검색, 연결, 데이터 전송 등 다양한 기능을 제공하며 ReactiveX 프로그래밍 패러다임을 따르므로 비동기 처리가 편리합니다. 어플리케이션에서 Bluetooth와 데이터 통신을 해야하는 경우에는 Swift RxBluetoothKit을 고려해보세요.

## 참고 자료

- [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)
- [RxSwift GitHub 페이지](https://github.com/ReactiveX/RxSwift)