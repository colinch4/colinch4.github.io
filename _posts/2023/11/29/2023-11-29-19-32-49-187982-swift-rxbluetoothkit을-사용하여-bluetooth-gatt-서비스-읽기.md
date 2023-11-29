---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth GATT 서비스 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 통신은 많은 앱에서 사용되는 중요한 기능 중 하나입니다. Swift에서 Bluetooth GATT 서비스를 읽고 처리하는 방법을 배우기 위해 RxBluetoothKit을 사용해 보겠습니다.

## 1. RxBluetoothKit 설치하기

먼저 프로젝트에 RxBluetoothKit을 설치해야 합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 추가합니다:

```swift
pod 'RxBluetoothKit', '~> 5.0'
```

그런 다음 프로젝트 디렉토리에서 `pod install`을 실행하여 RxBluetoothKit을 설치합니다.

## 2. Bluetooth 서비스 스캔하기

Bluetooth 서비스를 읽으려면 우선 해당 서비스를 스캔해야 합니다. 다음과 같이 스캔을 시작합니다:

```swift
import RxBluetoothKit
import RxSwift

let centralManager = CentralManager()
let disposeBag = DisposeBag()

centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral)")
    })
    .disposed(by: disposeBag)
```

위의 코드에서 `scanForPeripherals` 함수는 모든 Bluetooth 장치를 검색하고 필터링하지 않는 것을 의미합니다. `withServices` 매개 변수에 원하는 서비스 UUID 배열을 전달하여 특정 서비스로 필터링할 수도 있습니다.

## 3. Bluetooth 서비스 읽기

서비스를 발견한 후, 해당 서비스의 특성(Characteristic)을 읽을 수 있습니다. 아래의 코드는 Bluetooth 서비스를 읽고, 그 서비스에 포함된 특성을 출력하는 방법을 보여줍니다.

```swift
import RxBluetoothKit
import RxSwift

let centralManager = CentralManager()
let disposeBag = DisposeBag()
let targetServiceUUID = CBUUID(string: "your_service_uuid")

centralManager.scanForPeripherals(withServices: nil)
    .take(1)
    .flatMap { scannedPeripheral in
        return scannedPeripheral.peripheral.establishConnection()
    }
    .flatMap { connectedPeripheral in
        return connectedPeripheral.discoverServices([targetServiceUUID])
    }
    .flatMap { discoveredServices -> Observable<Service> in
        guard let service = discoveredServices.first else {
            throw BluetoothError.serviceNotFound
        }
        return Observable.just(service)
    }
    .flatMap { service in
        return service.discoverCharacteristics(nil)
    }
    .subscribe(onNext: { characteristics in
        print("Discovered characteristics: \(characteristics)")
    })
    .disposed(by: disposeBag)
```

위의 코드는 다음과 같은 단계로 동작합니다:
- 퍼리페럴 스캔
- 스캔된 퍼리페럴과 연결
- 특정 서비스 검색
- 첫 번째 서비스 선택
- 서비스의 특성 검색

위의 코드는 보다 단순한 예시이며, 더 복잡한 Bluetooth 통신을 구현하려면 다양한 메서드와 Observable을 조합하여 사용해야 합니다.

## 4. 결론

이러한 방법을 사용하여 Swift에서 Bluetooth GATT 서비스를 읽을 수 있습니다. RxBluetoothKit을 사용하면 비동기적인 Bluetooth 통신을 간편하게 처리할 수 있습니다. 더 자세한 내용은 [RxBluetoothKit GitHub](https://github.com/Polidea/RxBluetoothKit)을 참조하세요.