---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth GATT 특성 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift 프로그래밍 언어와 RxBluetoothKit 라이브러리를 사용하여 Bluetooth GATT 특성을 읽는 방법에 대해 알아보겠습니다.

## 준비하기

먼저 RxBluetoothKit을 프로젝트에 추가해야 합니다. 이를 위해 CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 추가합니다:

```ruby
platform :ios, '10.0'
use_frameworks!

target 'YourProjectName' do
    pod 'RxBluetoothKit'
end
```

그리고 터미널에서 프로젝트 폴더로 이동하여 다음 명령을 실행합니다:

```
$ pod install
```

이제 RxBluetoothKit을 사용할 준비가 되었습니다.

## Bluetooth 디바이스 연결

먼저 Bluetooth 디바이스에 연결해야 합니다. RxBluetoothKit을 사용하여 디바이스를 검색하고 연결하는 방법에 대한 예제 코드는 다음과 같습니다:

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let centralManager = CentralManager(queue: .main)
let peripheral = /* 검색된 Bluetooth 디바이스 */

centralManager.connect(peripheral)
    .subscribe(onSuccess: { peripheral in
        print("디바이스에 성공적으로 연결되었습니다.")
    }, onError: { error in
        print("디바이스 연결에 실패했습니다: \(error.localizedDescription)")
    })
    .disposed(by: disposeBag)
```

RxBluetoothKit의 CentralManager를 사용하여 Bluetooth 디바이스를 검색하고 연결합니다. `peripheral`은 검색된 디바이스 객체입니다.

## GATT 특성 읽기

디바이스에 연결한 후에는 GATT 특성을 읽을 수 있습니다. RxBluetoothKit을 사용하여 특성을 읽는 방법에 대한 예제 코드는 다음과 같습니다:

```swift
import RxSwift
import RxBluetoothKit

let disposeBag = DisposeBag()

let peripheral = /* 연결된 Bluetooth 디바이스 */
let serviceUUID = CBUUID(string: "YOUR_SERVICE_UUID")
let characteristicUUID = CBUUID(string: "YOUR_CHARACTERISTIC_UUID")

peripheral.discoverServices([serviceUUID])
    .flatMap { services -> Observable<Peripheral> in
        return peripheral.discoverCharacteristics([characteristicUUID], for: services[0])
    }
    .flatMap { characteristics -> Observable<Characteristic> in
        return characteristics[0].readValue()
    }
    .subscribe(onNext: { characteristic in
        let value = characteristic.value ?? Data()
        print("특성 값: \(value)")
    }, onError: { error in
        print("특성 읽기에 실패했습니다: \(error.localizedDescription)")
    })
    .disposed(by: disposeBag)
```

위 코드에서 `serviceUUID`와 `characteristicUUID`를 읽고 싶은 GATT 특성의 UUID로 변경해야 합니다. `peripheral`은 연결된 디바이스 객체입니다.

위 코드는 먼저 연결된 디바이스에서 해당 서비스와 특성을 검색한 후에, 첫 번째 특성의 값을 읽습니다. `characteristic.value` 에서 특성의 값을 가져와서 출력합니다.

이렇게 Swift와 RxBluetoothKit을 사용하여 Bluetooth GATT 특성을 읽을 수 있습니다.

## 결론

이번 글에서는 Swift RxBluetoothKit 라이브러리를 사용하여 Bluetooth GATT 특성을 읽는 방법에 대해 알아보았습니다. 먼저 RxBluetoothKit을 프로젝트에 추가하고, Bluetooth 디바이스에 연결한 후에 GATT 특성을 읽을 수 있음을 살펴보았습니다. 이를 활용하여 Bluetooth 기능을 구현할 때 도움이 되기를 바랍니다.

## 참고 자료

- [RxBluetoothKit - GitHub](https://github.com/Polidea/RxBluetoothKit)
- [Bluetooth 개발 가이드](https://developer.apple.com/bluetooth/)