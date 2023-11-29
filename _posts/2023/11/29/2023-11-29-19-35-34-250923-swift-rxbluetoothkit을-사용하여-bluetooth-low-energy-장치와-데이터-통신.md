---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치와 데이터 통신"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력 장치 간의 통신에 사용되는 기술로, 주변 장치 간에 데이터를 교환하기 위한 표준 프로토콜입니다. iOS 애플리케이션에서 BLE 장치와 통신하기 위해 RxBluetoothKit 라이브러리를 사용할 수 있습니다. 이 라이브러리는 Swift에서 BLE 기능을 쉽게 사용할 수 있도록 도와줍니다.

## RxBluetoothKit 설치 및 설정

RxBluetoothKit을 사용하기 위해 먼저 Swift 프로젝트에 라이브러리를 추가해야 합니다. Cocoapods를 사용하고 있다면 Podfile에 다음 줄을 추가합니다.

```ruby
pod 'RxBluetoothKit'
```

그리고 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## BLE 장치 스캔

이제 RxBluetoothKit을 사용하여 BLE 장치를 스캔하는 방법에 대해 알아보겠습니다. 먼저 `CentralManager` 객체를 생성해야 합니다.

```swift
import RxBluetoothKit

let centralManager = CentralManager()
```

그런 다음 `scanForPeripherals` 메서드를 사용하여 BLE 장치를 스캔할 수 있습니다.

```swift
centralManager.scanForPeripherals(withServices: nil)
   .subscribe(onNext: { scannedPeripheral in
       // 스캔된 장치 처리 로직을 작성합니다.
   })
   .disposed(by: disposeBag)
```

위의 코드에서 `withServices` 매개변수는 스캔할 장치의 서비스 UUID를 지정하는 데 사용됩니다. `nil`로 설정하면 모든 장치를 스캔합니다. 스캔된 각 장치는 `scannedPeripheral`으로 전달됩니다.

## BLE 장치 연결

BLE 장치를 스캔한 후에는 연결을 설정하여 데이터 통신을 수행할 수 있습니다. 연결을 설정하려면 `Peripheral` 인스턴스가 필요합니다. 이를 위해 `CentralManager`의 `connect` 메서드를 사용합니다.

```swift
centralManager.connect(scannedPeripheral)
    .subscribe(onNext: { peripheral in
        // 연결된 장치 처리 로직을 작성합니다.
    }, onError: { error in
        // 연결 에러 처리 로직을 작성합니다.
    })
    .disposed(by: disposeBag)
```

위의 코드에서 `scannedPeripheral`은 이전 단계에서 스캔된 장치입니다. 연결된 장치는 `peripheral`로 전달됩니다. 연결 도중에 에러가 발생하면 `onError` 블록이 호출됩니다.

## 데이터 통신

BLE 장치와의 연결이 설정되면 데이터를 수신하고 전송할 수 있습니다. 데이터는 `Peripheral` 인스턴스를 통해 전달됩니다.

```swift
peripheral.observeValueUpdateAndSetNotification(characteristic)
    .subscribe(onNext: { characteristic in
        // 데이터 수신 처리 로직을 작성합니다.
    })
    .disposed(by: disposeBag)
```

위의 코드에서 `characteristic`는 특정 서비스의 특성을 나타내는 객체입니다. 데이터를 전송하기 위해서는 `writeValue(_:for:withoutResponse:)` 메서드를 사용합니다.

```swift
let data = Data() // 전송할 데이터
peripheral.writeValue(data, for: characteristic, withoutResponse: true)
   .subscribe(onNext: {
       // 데이터 전송 완료 처리 로직을 작성합니다.
   })
   .disposed(by: disposeBag)
```

위의 코드에서 `withoutResponse` 매개변수를 `true`로 설정하면 데이터 전송 후 응답을 받지 않습니다.

## 결론

이제 Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치와 데이터 통신하는 방법에 대해 알아보았습니다. RxBluetoothKit은 Swift에서 BLE 기능을 쉽게 사용할 수 있도록 도와주는 강력한 라이브러리입니다. BLE 기반 애플리케이션을 개발할 때 유용하게 활용할 수 있습니다.

더 자세한 정보를 원한다면, [RxBluetoothKit GitHub 저장소](https://github.com/Polidea/RxBluetoothKit)를 참조하세요.